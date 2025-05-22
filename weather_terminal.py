def render_ascii_weather(destination, weather_data):
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table

    console = Console()
    console.rule(f"[bold cyan]Weather Report: {destination}")

    for day in weather_data:
        date = day.get("date", "Unknown Date")
        console.print(f"[bold magenta]{date}[/bold magenta]")
        
        parts = ["morning", "noon", "evening", "night"]
        for part in parts:
            part_data = day.get(part, {})
            desc = part_data.get("description", "")
            temp = part_data.get("temp", "")
            wind = part_data.get("wind", "")
            rain = part_data.get("rain", "")
            icon = get_ascii_icon(desc)

            block = f"""
{icon}
{desc}
🌡️ {temp}°C
💨 {wind}
🌧️ {rain}
"""
            console.print(Panel(block, title=part.capitalize(), expand=False))

def get_ascii_icon(description):
    # Very simplified
    if "cloud" in description.lower():
        return "     .--.\n  .-(    ).\n (___.__)__)"
    elif "rain" in description.lower():
        return "     .--.\n  .-(    ).\n (___.__)__) 💧💧"
    elif "sun" in description.lower():
        return "    \\   /  \n     .-.   \n  ― (   ) ―\n     `-’   \n    /   \\  "
    elif "fog" in description.lower():
        return " _ - _ - _ -\n_ - _ - _ -"
    else:
        return "(?)"
