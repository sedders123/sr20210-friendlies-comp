#!/usr/bin/python

import argparse
import json
import random
import sys

parser = argparse.ArgumentParser()
parser.add_argument('match_number', type=int)
parser.add_argument('tla1')
parser.add_argument('tla2')
parser.add_argument(
    '--output',
    type=argparse.FileType(mode='w'),
    default=sys.stdout,
)
args = parser.parse_args()

result = {
    "match_number": args.match_number,
    "arena_id": "Simulator",
    "teams": {
        args.tla1: {
            "zone": 0
        },
        args.tla2: {
            "zone": 1
        }
    },
    "duration": 5,
    "recording_config": {
        "resolution": {
            "width": 1920,
            "height": 1080
        },
        "quality": 100
    },
    "arena_zones": {
        "other": {
            "territory_claims": [
                {
                    "zone": 0,
                    "station_code": "OX",
                    "time": 5.04
                }
                if random.choice((True, False))
                else {
                    "zone": 1,
                    "station_code": "SN",
                    "time": 5.04
                }
            ],
            "game_style": "end_state"
        }
    }
}

json.dump(result, args.output, indent=4)
