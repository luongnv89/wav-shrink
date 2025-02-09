import argparse
import os
from waveshrink import wav_shrink

def main():
    parser = argparse.ArgumentParser(
        description="Convert a WAV file or all WAV files in a directory to a smaller compressed format (MP3, OGG)."
    )
    parser.add_argument(
        "input",
        type=str,
        nargs="?",
        help="Path to a WAV file (if converting a single file).",
    )
    parser.add_argument(
        "-d",
        "--directory",
        type=str,
        help="Path to a directory containing WAV files (convert all WAV files in the folder).",
    )
    parser.add_argument(
        "-f",
        "--format",
        type=str,
        choices=["mp3", "ogg"],
        default="mp3",
        help="Output format (default: mp3).",
    )
    parser.add_argument(
        "-b",
        "--bitrate",
        type=str,
        default="64k",
        help="Bitrate for the output file (default: 64k).",
    )
    parser.add_argument(
        "-k",
        "--keep",
        action="store_true",
        help="Keep original WAV files after conversion (default: delete).",
    )

    args = parser.parse_args()

    if args.directory:
        # Convert all WAV files in the directory
        if not os.path.isdir(args.directory):
            print(f"❌ Error: Directory not found: {args.directory}")
            parser.print_help()
            return

        wav_files = [f for f in os.listdir(args.directory) if f.endswith(".wav")]
        if not wav_files:
            print("⚠️ No WAV files found in the directory.")
            return

        print(f"📂 Found {len(wav_files)} WAV files in {args.directory}. Converting...")

        for wav_file in wav_files:
            input_path = os.path.join(args.directory, wav_file)
            wav_shrink(input_path, args.format, args.bitrate, args.keep)

    elif args.input:
        # Convert a single file
        if not os.path.isfile(args.input):
            print(f"❌ Error: File not found: {args.input}")
            parser.print_help()
            return

        wav_shrink(args.input, args.format, args.bitrate, args.keep)

    else:
        print("❌ Error: You must specify either a WAV file or a directory containing WAV files.")
        parser.print_help()


if __name__ == "__main__":
    main()