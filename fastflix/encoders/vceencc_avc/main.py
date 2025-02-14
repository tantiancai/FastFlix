#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Chris Griffith"

from pathlib import Path

import pkg_resources

name = "AVC (VCEEncC)"

video_extension = "mkv"
video_dimension_divisor = 1
icon = str(Path(pkg_resources.resource_filename(__name__, f"../../data/encoders/icon_vceencc.png")).resolve())

enable_subtitles = True
enable_audio = True
enable_attachments = False

# Taken from VCEEncC64.exe --check-encoders
audio_formats = [
    "aac",
    "ac3",
    "ac3_fixed",
    "adpcm_adx",
    "adpcm_ima_apm",
    "adpcm_ima_qt",
    "adpcm_ima_ssi",
    "adpcm_ima_wav",
    "adpcm_ms",
    "adpcm_swf",
    "adpcm_yamaha",
    "alac",
    "aptx",
    "aptx_hd",
    "comfortnoise",
    "dca",
    "eac3",
    "flac",
    "g722",
    "g723_1",
    "g726",
    "g726le",
    "libmp3lame",
    "libopus",
    "libspeex",
    "libtwolame",
    "libvorbis",
    "libwavpack",
    "mlp",
    "mp2",
    "mp2fixed",
    "nellymoser",
    "opus",
    "pcm_alaw",
    "pcm_dvd",
    "pcm_f32be",
    "pcm_f32le",
    "pcm_f64be",
    "pcm_f64le",
    "pcm_mulaw",
    "pcm_s16be",
    "pcm_s16be_planar",
    "pcm_s16le",
    "pcm_s16le_planar",
    "pcm_s24be",
    "pcm_s24daud",
    "pcm_s24le",
    "pcm_s24le_planar",
    "pcm_s32be",
    "pcm_s32le",
    "pcm_s32le_planar",
    "pcm_s64be",
    "pcm_s64le",
    "pcm_s8",
    "pcm_s8_planar",
    "pcm_u16be",
    "pcm_u16le",
    "pcm_u24be",
    "pcm_u24le",
    "pcm_u32be",
    "pcm_u32le",
    "pcm_u8",
    "pcm_vidc",
    "real_144",
    "roq_dpcm",
    "s302m",
    "sbc",
    "sonic",
    "sonicls",
    "truehd",
    "tta",
    "vorbis",
    "wavpack",
    "wmav1",
    "wmav2",
]

from fastflix.encoders.vceencc_avc.command_builder import build
from fastflix.encoders.vceencc_avc.settings_panel import VCEENCCAVC as settings_panel
