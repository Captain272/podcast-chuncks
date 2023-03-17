from pydub import AudioSegment
import re

text = '''Timestamps
00:00:00 Water
00:03:33 Tool Deliberate Cold Exposure, Immersion & Showers Mood & Fat Loss
00:15:26 Sponsors: LMNT, Thesis, HVMN, Momentous
00:19:27 Water: Physical Properties & Chemistry
00:26:32 Bonds & Water Phases, “Structured Water”
00:34:07 Body, Cells & Water
00:36:22 Sponsor: AG1 (Athletic Greens)
00:37:37 Water as a Solvent, Temperature & On the phone. I’ll respond soon.
00:41:49 Water Transport in Cells, Aquaporin Channels
00:49:46 Alkaline/pH Water; Temperature, pH & Water Transport
00:55:14 Water Cellular Function, Reactive Oxygen Species (ROS) & Antioxidants
01:01:20 Sponsor: InsideTracker
01:02:38 Tool: Baseline Hydration
01:11:35 Tool: Hydration & Exercise, Galpin Equation
01:15:40 Tool: Hydration, Sauna, Humidity & Sweat; Thirst, Caffeine
01:19:15 Hydration; Cognitive & Physical Performance
01:23:53 Tool: Water Filtration; Nighttime Urination
01:29:35 Tap Water Tests, Disinfection Byproducts (DBPs), Fluoride & Thyroid Health
01:37:18 Tool: Water Filters
01:44:18 Tool: Resting Tap Water & Sediment
01:48:13 Tool: “Hard Water”; Magnesium, Calcium & Cardiovascular Health
01:53:40 Water Temperature
01:56:42 Water Types: Distilled, Reverse Osmosis, Hydrogen-Enriched
02:03:26 Hydrogen-Enriched Water, Magnesium, Optimize Hydration
02:11:13 Tool: Molecular Hydrogen Tablets, Water pH
02:14:05 Structured Water
02:16:39 Tool: Water Pipes, Faucet Filter
02:19:42 Zero-Cost Support, Spotify & Apple Reviews, YouTube Feedback, Sponsors, Momentous, Social Media, Neural Network Newsletter'''


# define the path of your audio file
audio_path = 'path/to/your/audio/file.mp3'

# define the list of timestamps where you want to split the audio


def time_to_milliseconds(time_str):
    # split the time string into hour, minute, and second components
    hours, minutes, seconds = map(int, time_str.split(':'))

    # calculate the total number of milliseconds
    total_ms = ((hours * 60 + minutes) * 60 + seconds) * 1000

    return total_ms


timestamps = []  # in milliseconds



pattern = re.compile(r'\b\d{2}:\d{2}:\d{2}\b')

# find all the timestamps in the text and store them in a list
# stamps = pattern.findall(text)
stamps=['00:00:00', '00:03:33', '00:15:26', '00:19:27', '00:26:32', '00:36:22', '00:41:49', '00:49:46', '00:55:14', '01:01:20', '01:02:38', '01:11:35', '01:15:40', '01:19:15', '01:23:53', '01:29:35', '01:37:18', '01:44:18', '01:48:13', '01:53:40', '01:56:42', '02:03:26', '02:11:13', '02:14:05', '02:16:39', '02:19:42']


for i in stamps:
    timestamp.append(time_to_milliseconds(i))



# create an AudioSegment object from the audio file
audio = AudioSegment.from_file(audio_path)

# iterate over the timestamps and split the audio at each timestamp
for i, timestamp in enumerate(timestamps):
    if i == 0:
        # for the first segment, start at 0 seconds
        start = 0
    else:
        # for subsequent segments, start at the end of the previous segment
        start = timestamps[i-1]
    
    end = timestamp
    # extract the segment between start and end
    segment = audio[start:end]

    # define the path and filename for the new segment
    output_path = f'path/to/output/segment{i+1}.mp3'

    # export the segment to a new file
    segment.export(output_path, format='mp3')
