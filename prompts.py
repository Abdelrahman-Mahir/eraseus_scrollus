from bs4 import BeautifulSoup
import random

# Sample HTML content (replace with your HTML content)
html_content = """
<ol>

<li style="font-weight: 400;"><span style="font-weight: 400;">You wake up one morning to find out that you get to move to any planet of your choosing.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Your wife is a droid.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Every day, you get one hour to revisit any moment from your life. What do you pick?</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Gravity no longer exists.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">You are chosen to go on the first ever recreational space journey.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">After people die, their spirits can be brought back from death but at the cost of one random human life. Is it worth it?</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Everyone in the world has the ability to read thoughts. Except for one person.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">You have to power to build one separate planet. How do you build it? Who gets to live there?</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">What team do you gather to fight the largest alien and terrorist threat on Earth?</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">The world is dying. In order to save it, you’ve been commanded to sacrifice yourself to an invading alien group.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">You are the first person able to breathe in outer space.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">A rare form of cancer is the newest superbug. With a team of scientists, you all must find a cure before the population is wiped out.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Human beings begin to find themselves growing extra limbs as global warming amps up.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">It turns out humans have been the aliens all along.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">You are in charge of a secretive government agency that aligns people’s fates. Their livelihood is entirely up to you and what you want to do with it.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Technology becomes illegal.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">All plant life on the planet is wiped out, except for in Florida.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">You are one of the mechanics on the first ever self-flying airplane.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Walking through the woods one day, you come across a small animal that has the ability to instantaneously clone itself.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Your whole family has fought in the space military, but you’ve decided to no longer take part in it.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">In an alternate universe where global warming has ruined the planet, you’ve spent your entire life living in an airplane on autopilot.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">You’re a 15-year-old in the middle of a zombie apocalypse. However, a cure has been found that not only rids the infected person of the virus before they turn but prevents it altogether. Only one problem… Your parents are anti-vaxxers. (@writing.prompt.s)</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Nasa engineers monitor the curiosity rover’s actions. All seems normal until the robot suddenly changes its course. The scientists attempt to correct it over and over until they suddenly receive a transmission from the rover: “Will Save Oppy” (@writing.prompt.s)</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">What if a nuclear submarine was ordered to launch their nuclear arsenal onto the world? (Screencraft)</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">What if the world we live in is actually a computer simulation? (Screencraft)</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">What if the past and present timelines began to merge? (Screencraft)</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">What if your stepfather or stepmother is actually your future self? (Screencraft)</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">What if the sun began to die? (Screencraft)</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">What if the universe as we know it is actually someone’s imagination? (Screencraft)</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Everyone on earth begins to experience universal amnesia.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">The year is 2200. What does the world look like to you?</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">In the future, we no longer require water, air, or food. We are a super efficient team of robots.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">What do you think happens when the grid goes down?</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Describe your perfect utopian world.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Your penpal lives on the opposite side of the universe.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Aliens who only communicate with sign language invade. To avoid war, our governments must engage a vastly marginalized portion of the human population: the hearing-impaired. (The Write Practice)</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">A rogue planet with strange properties collides with our sun, and after it’s all over, worldwide temperature falls forty degrees. Write from the perspective of a someone trying to keep his tropical fruit trees alive. (The Write Practice)</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Ever read about the world’s loneliest whale? Write a story in which he’s actually the survivor of an aquatic alien species which crashed here eons ago, and he’s trying very hard to learn the “local” whale language so he can fit in. Write from his perspective the first time he makes contact. (The Write Practice)</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">An alien planet starts receiving bizarre audio transmissions from another world (spoiler: they’re from Earth). What does it mean? Are they under attack? Some think so…until classic rock ‘n’ roll hits the airwaves, and these aliens discover dancing. Write from the perspective of the teenaged alien who first figures it out. (The Write Practice)</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Take anything we find normal today (shopping malls, infomercials, products to remove facial hair, etc.) and write a story from the perspective of an archeologist five thousand years in the future who just unearthed this stuff, has NO idea what any of it was for, and has to give a speech in an hour explaining the historical/religious/sociological significance. (The Write Practice)</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">House cats are aliens who have succeeded in their plan to rule the world. Discuss.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">A high schooler from fifteen hundred years in our future is assigned a one-page writing project on a twenty-first century person’s life based entirely on TV commercials. Write the beginning of the essay. (The Write Practice)</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Time travel works, but only once in a person’s life. Write from the perspective of someone who chooses to go back in time, knowing they can never return. Where do they go and why? (The Write Practice)</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">So yeah, ancient Egypt really was “all that” after all, and the pyramids turn out to be fully functional spaceships (the limestone was to preserve the electronics hidden inside). Write from the perspective of the tourist who accidentally turns one on. (The Write Practice) </span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Ten years from now, scientists figure out how to stop human aging and extend life indefinitely—but every time someone qualifies for that boost, someone else has to die to keep the surplus population in check. Oh, it’s all very humane; one’s descendants get a huge paycheck. Write from the perspective of someone who just got a letter in the mail saying they’re the one who has to die. (The Write Practice) </span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">In the future, neural implants translate music into physical pleasure, and earphones (“jacking in”) are now the drug of choice. Write either from the perspective of a music addict, OR the Sonforce agent (sonance + enforcer) who has the job of cracking down. (The Write Practice) </span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">It’s the year 5000. Our planet was wrecked in the great Crisis of 3500, and remaining human civilization survives only in a half dozen giant domed cities. There are two unbreakable rules: strict adherence to Life Quality (recycling doesn’t even begin to cover these laws), and a complete ban on reproduction (only the “worthy” are permitted to create new humans). Write from the perspective of a young woman who just discovered she’s been chosen to reproduce—but she has no interest in being a mother. (The Write Practice) </span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">In the nineteenth century, there’s a thriving trade in stolen archeological artifacts. Write a story from the perspective of an annoyed, minimum-wage employee whose job is traveling back in time to obtain otherwise unobtainable artifacts, then has to bring them back to the present (the 1800s, that is) and artificially age them before they will sell. (The Write Practice) </span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Steampunk! Write a story from the perspective of a hot air balloon operator who caters to folks who like a little thrill… which means she spends half her time in the air shooting down pterodactyls before the paying customers get TOO scared. (The Write Practice) </span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Creation myth! Write from the perspective of a crazy scientist in the year 28,000 who, determined to discover how the universe began, rigs up a malfunctioning time machine, goes to the “beginning” of the universe, and ends up being the reason for the Big Bang. (Logic? Causal effect? Pfft. Hush, it’s time-travel, and that was never logical.) (The Write Practice) </span></li>

</ol>
"""

# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')
list_element = soup.find('ol')
list_items = list_element.find_all('li')

prompts_list = []
# Print the list items
for item in list_items:
    prompts_list.append(item.text)


class PromptGenerator():
    def __init__(self):
        self.prompts_list = prompts_list

    def get_prompt(self):
        return random.choice(self.prompts_list)







