#!/bin/bash
#
# This script generates audio samples in WAV format,
# with various sample rates, channels, and sampling bits.
#
# Prerequisite:
# Bash
# mediainfo
# ffmpeg
#

function die() {
  local msg=$1
  echo $msg
  exit 1
}

master_track=master.wav
ffmpeg -y -f lavfi -i sine=frequency=1000:sample_rate=192000:duration=50 -c:a pcm_s32le -ac 8 $master_track || die "Failed to generate master track"

sample_rates="32000 44100 48000 96000 192000"
channel_counts="2 4 6 8"
sample_bits="16 24 32"

for ch in $channel_counts
do
  for rate in $sample_rates
  do
    for bits in $sample_bits
    do
      # proper naming of the output files
      rate_name=`awk "BEGIN{print $rate/1000}"`
      output="${ch}ch_${rate_name}k_${bits}bit.wav"

      echo "Generate audio sample $output"
      ffmpeg -y -i $master_track -ar $rate -ac $ch -c:a "pcm_s${bits}le" $output || die "Failed to generate $output"

      # verify with mediainfo
      mi_ch=`mediainfo $output| egrep 'Channel.*channel' | awk '{print $3}'`
      mi_rate=`mediainfo $output| egrep 'Sampling rate' | awk '{print $4}' | awk '{print $0/1}'`
      mi_bits=`mediainfo $output| egrep 'Bit depth' | awk '{print $4}'`

      if [[ $mi_ch != $ch ]]; then
        die "Channel count $mi_ch not correct, should be $ch"
      fi
      if [[ $mi_rate != $rate_name ]]; then
        die "Sampleing rate ${mi_rate}kHz not correct, should be $ch" 
      fi
      if [[ $mi_bits != $bits ]]; then
        die "Sample bits $mi_bits not correct, should be $bits" 
      fi
    done
  done
done

rm -f $master_track
