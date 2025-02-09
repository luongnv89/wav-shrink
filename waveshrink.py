import os
from pydub import AudioSegment
from rich.progress import Progress, BarColumn, TextColumn
from rich.console import Console

console = Console()

def wav_shrink(input_file, output_format="mp3", bitrate="64k", keep_original=False):
    """
    Converts a WAV file to a compressed format (MP3, OGG, etc.) with a real progress bar.

    Args:
        input_file (str): Path to the input WAV file.
        output_format (str): Target format (e.g., "mp3", "ogg").
        bitrate (str): Bitrate for compression (e.g., "64k", "128k").
        keep_original (bool): If False, delete the original WAV file after conversion.

    Returns:
        str: Path to the converted file.
    """
    if not os.path.exists(input_file):
        console.print(f"[red]Error:[/red] File not found: {input_file}")
        return None

    output_file = os.path.splitext(input_file)[0] + f".{output_format}"

    console.print(
        f"\n🎵 Converting [cyan]{input_file}[/cyan] → [green]{output_file}[/green] at [yellow]{bitrate}[/yellow] bitrate"
    )

    # Load the WAV file
    audio = AudioSegment.from_wav(input_file)

    # Get total duration (in ms) to use as progress reference
    total_duration = len(audio)  # milliseconds

    # Progress bar setup
    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        console=console,
    ) as progress:
        task = progress.add_task("Processing...", total=total_duration)

        # Convert in chunks to track progress
        chunk_size = 1000  # Process in 1-second chunks
        chunks = [audio[i : i + chunk_size] for i in range(0, total_duration, chunk_size)]

        combined = AudioSegment.empty()
        for i, chunk in enumerate(chunks):
            combined += chunk
            progress.update(task, advance=len(chunk))  # Update based on processed duration

        # Export compressed file
        combined.export(output_file, format=output_format, bitrate=bitrate)

    if not keep_original:
        try:
            os.remove(input_file)
            console.print(f"[dim]Deleted original file: {input_file}[/dim]")
        except OSError as e:
            console.print(f"[yellow]Warning:[/yellow] Could not delete original file: {e}")

    console.print(
        f"[bold green]✅ Conversion complete![/bold green] Saved as: {output_file}"
    )

    return output_file