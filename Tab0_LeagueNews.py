import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import math
from PIL import Image

# Images
trophy = Image.open("./Images/Trophy.png")
silverstone0 = Image.open("./Images/Silverstone_Start.png")
silverstone1 = Image.open("./Images/Silverstone_Final_Turn.png")
silverstone2 = Image.open("./Images/Silverstone_PK_Zane.png")
australia_circuit = Image.open("./Images/Australia_Circuit.png")
australia1 = Image.open("./Images/Australia_Start.png")
australia2 = Image.open("./Images/Australia_Collage.png")
australia3 = Image.open("./Images/Australia_Side_Shot.png")
spa_circuit = Image.open("./Images/Spa_Circuit.png")
spa_collage = Image.open("./Images/Spa_Race_Week_Collage2.png")
postponed = Image.open("./Images/Postponed.png")
spain_circuit = Image.open("./Images/Spain_Circuit.png")

def Tab0():
    #region Race Week Spa & Spain
    st.subheader('Race Week - Spa & Spain')
    st.markdown('''
                Motorsports fans are in for a treat. The league is kicking off the New Year with a double feature: Spa Part 2 Electric Boogaloo followed by high speed thrills in Barcelona Spain. As the perils of Spa have been covered in a previous post, this will focus on Spain and its high speed twists and turns. Track limits, tire wear, and plenty of places for aggressive overtakes should all combine for an unpredictable event. 
                ''')
    st.image(spain_circuit)
    st.markdown('''
                Once the lights go out the drivers will have a long straight to draft, bump, and position themselves for the first pair of corners. Both are wide enough to allow for drivers to go two or even three wide for the brave. The third corner will require incredible courage for the drivers to be wheel to wheel throughout, but during the first lap who knows what might happen. Sector 2 will help queue up the drivers for the circuit’s back straight. If everyone’s wings, wheels, and side pods are still intact, the drivers will need to test the track limits on their way to the final corner at full tilt. With two DRS straights, there will be plenty of room for conventional overtaking. However, with sweeping high speed and medium speed corners, the circuit will allow for harrowing battles throughout each lap. 
                ''')
    st.markdown('''
                The drivers will need to respect the track limits both for penalty's sake as well as the heavy amount of gravel that lines the high speed portions of the circuit. Penalties, crashes, and yellow or red flags all could lead to some incredible shifts in the standings. Drivers will also have to battle through the fatigue of the day’s double header. Which they did not have to contend with the last time out in Spain. That outing provided a close race between McLaren’s defending champion Nick and the then Mercedes driver, now Ferrari driver, Erick with the other Ferrari brother, then Aston Martin driver, Zane rounding out the podium. Three of the league’s drivers DNS and two of the AI DNF. Spain should provide plenty of exciting racing for every driver who makes it to the starting line.
                ''')
    st.markdown('''
                <p style="color:lightgray;">Saturday 12/29/2024 - Patrick Knowles</p>
                ''',
                unsafe_allow_html=True,)
    st.divider()
    #endregion

    #region Spa Update
    st.subheader('Spa Update')
    st.image(postponed)
    st.markdown('''
                The league’s battle at Spa has been postponed until 1/1/2025 or later. Something about some driver ditching to party in Mexico and a few drivers unable to connect to EA's crappy servers. However this did allow some of the drivers to run some laps in Saudi Arabia as a mid-season practice session. The FIA will be working to finalize the upcoming schedule for the remainder of the season as rumor has it there will be a week or two of double headers. The league takes a short break as we head into this holiday season to allow drivers to recuperate and spend time with loved ones.
                ''')
    st.markdown('''
                <p style="color:lightgray;">Saturday 12/22/2024 - Patrick Knowles</p>
                ''',
                unsafe_allow_html=True,)
    st.divider()
    #endregion

    #region Race Week Spa
    st.subheader('Race Week - Spa')
    st.markdown('''
                The league heads out for a Spa day this week. However, this one probably won’t be all that relaxing. With the Constructor’s and Driver’s championships heating up, Spa will prove to be a place where everyone has the opportunity to make up ground. Historically known as a track favorable for overtaking, Spa’s sacred pavement is also known for being one of the most treacherous high-speed circuits on the calendar. Nestled deep in the Ardennes forest, Spa is riddled with corners, straights, and stories that have filled the racing history books.
                ''')
    st.image(spa_circuit)
    st.markdown('''
                Famous early corners like La Source and Raidillon’s Eau Rogue will provide exhilarating braking and high-speed moments. Followed by the twisting turns of Le Combes, Pouhon, and Campus among others, the drivers are sure to provide incredible wheel-to-wheel action. Finally drivers will have the opportunity for late sends or strategic tailgating going into the chicane before the start-finish straight.
                ''')
    st.image(spa_collage)
    st.markdown('''
                Previously when the league navigated a day at Spa, McLaren’s Nick took home the win. He finished just seconds before the then Mercedes driver, now Aston Martin driver Del. While Ferrari’s Erick rounded out the podium. Current league leader, and Alpine driver, Joshua was unable to start the race along with three other drivers. In fact, Joshua has not run a race at Spa in the last two seasons, and reigning champion Nick has not lost at Spa in recent memory. Ferrari’s pairing of Erick and Zane have also had historically good races, with Erick boasting a second and third place finish, and Zane placing fourth on his last two outings. With the addition of last week’s regulation changes and the thrilling nature of the Circuit of Spa-Francorchamps, this week is aimed at being another piece of absolute cinema. Hopefully none of the drivers end up just a few tire marbles short of a win.
                ''')
    st.markdown('''
                <p style="color:lightgray;">Saturday 12/14/2024 - Patrick Knowles</p>
                ''',
                unsafe_allow_html=True,)
    st.divider()
    #endregion

    #region Australia Recap
    st.subheader('Australia Recap: A Rumble Down Under')
    st.markdown('''
                tldr; Australia did not disappoint. Safety cars, front wings destroyed, questionable restarts, engines blown, drivers fuming, DNFs, a DNS, and a new race winner. 
                '''+'''
                With race hype at an all time high the drivers jumped into discord and silently sat waiting for the race to begin. Nerves were frayed, but when the lights went green in qualifying the drivers took to the streets of Albert Park without much trouble. The Red Bull pairing failed to make it out of Q1 and Alpine’s #2 driver Eddie totaled his car beyond repair, making it impossible for him to set a lap time during Q2. The final results of Q3 saw Alpine’s Joshua take home another pole position, with McLaren’s Nick, Aston Martin’s Del, and VCARB’s Patrick completing the first two rows. The Ferrari pairing occupied the third row and McLaren’s Travis and VCARB’s Brently rounded out the top eight on the fourth row of the grid. The rest of the field found themselves starting near the back, which to some strategists was the right move to ensure their drivers survived the first corner.
                ''')
    st.image(australia1)
    st.markdown('''
                When the five lights went out, the drivers quickly proceeded down the straight into Turn 1 where the top few drivers made it through fairly clean. However, Zane’s Ferrari was caught up in an incident on his way through Turn 2. This ended up proving to be a detrimental loss for Zane early in the race. Erick was able to make up a place into fourth passing Del and avoiding contact through the first few corners. 
                '''+'''
                As the race continued Alpine’s dominant driver Joshua took an early lead but was unable to break free from McLaren’s top contender Nick. As the front of the pack continued, Erick miraculously avoided contact with both Patrick and Nick in Turn 3 as he found himself in the gravel. This maneuver would have normally left him high and dry, but an early VSC and safety car allowed Erick to get right back into the groove. 
                ''')
    st.image(australia2)
    st.markdown('''
                Track limits were heavily enforced across the field as drivers tested the race director’s new regulations. Prior to the start of the race the league was informed that, due to sloppiness and abuse of the rules by Alpine’s Joshua at Silverstone, any corner cutting would be strictly recorded and penalties would be awarded for drivers who broke the rules three or more times throughout the race. For most these penalties were minor and did not end up changing the outcome of the race. However in the post race driver’s meeting there was a minor uproar that the regulations were too strict. Only time will tell if these regulations will remain or if the race director will renege their stance.
                '''+'''
                With just nine laps to go a late safety car bunched up the drivers and allowed some to take advantage of a less impactful pitstop. With Joshua still in first, Nick tailing him, and Erick following in third, the queue of cars cautiously took the final few corners of Lap 22 waiting for Joshua to throttle up. Waiting on bated breath, Nick and Erick pounced as Joshua launched only to find Joshua jump off the throttle for a short moment causing a multitude of front wings to be damaged. Regardless, no penalties were called and the drivers mustered what they could with their damaged vehicles. A tight battle ensued up front which ultimately saw McLaren’s Nick take home his first win of the season with Alpine’s Joshua right behind. 
                ''')
    st.image(australia3)
    st.markdown('''
                Rounding out the podium was Ferrari's Erick, who moved up from 5th to 3rd. Just behind him the two VCARB drivers had their best team finish of the season with Patrick finishing 4th, and driver of the day Brently moving up from 8th to 5th. Del was unable to fully recover from the early setbacks and ended in 11th with McLaren’s Travis just behind in 12th, and Alpine’s 7th place wunderkind Eddie falling all the way back to 13th. Rounding out our finishers today was Ferrari’s Zane in 15th. For Red Bull, this will be a qualifying and race to take notes from and improve upon as both drivers ended up unable to cross the finish line. Aston Martin again ran with just a single driver today as Gary was sadly watching the Knicks fall to the Hawks.
                '''+'''
                After all the engines were turned off and points totalled, battles for rank in both the World Driver’s and Constructor’s Championships have begun to heat up. McLaren begins to close the gap to Alpine and leap frogs Ferrari into second. In the Driver’s Championship, we saw both of the VCARB drivers overtake Ferrari’s Zane, but the leaders Joshua, Nick, and Erick remain the same. Next our drivers take to the Belgian forest in Spa where they will test their mettle against the highspeed Eau Rouge and longest track on the calendar.
                ''')
    st.markdown('''
                <p style="color:lightgray;">Thursday 12/11/2024 - Patrick Knowles with credit Erick & Nick</p>
                ''',
                unsafe_allow_html=True,)
    st.divider()
    #endregion

    #region Race Week Australia
    st.subheader('Race Week - Australia')
    st.markdown('''
                This week the drivers will be “defying gravity” while racing upside down in Melbourne. The real question is whether or not the league continues to let Alpine and Joshua cook? Or maybe more fittingly, will the league let Joshua put another shrimp on the barbie? Only the streets of Albert Park will be able to answer these questions.
                '''+'''
                Albert Park Circuit provides the first street circuit of the year, which without a doubt is set to create some sparks. With the first heavy braking Turn 1 of the calendar, the start of this race will likely turn into an abbreviated game of Survivor. From there the drivers will be challenged by tight walls coming out of Turn 2 and Turn 5 as they queue up into the highspeed Sector 2. Sector 3’s heavy braking zones will provide tantalizing opportunities for the drivers to throw dummies, lick it and send it, and hopefully keep all the carbon fiber on their cars
                ''')
    st.image(australia_circuit)
    st.markdown('''
                The league took a short pause from running down under last season. Which means the most recent winner here is current Ferrari driver and previous Mercedes driver Erick, who took home a commanding win with a lead of 18 seconds over McLaren’s Nick. Rounding out the podium was  retired Mercedes driver turned steward Marcus. If Silverstone’s race is any evidence of how close the drivers plan to race this week, we will certainly see an exciting race in the capital of Victoria. With nearly no room for run off, mistakes will be magnified, and incidents are sure to become heated.
                '''+'''
                <p style="color:lightgray;">Saturday 12/7/2024 - Patrick Knowles</p>
                ''',
                unsafe_allow_html=True,
                )
    st.divider()
    #endregion

    #region Silverstone Recap
    st.subheader('Silverstone Recap: “007 You Only Win Twice”')
    st.image(silverstone0)
    st.markdown('''
                Another week, another race. The sun mercifully shone down on the British Isles and provided the perfect weather for an eventful race. Reigning WDC Nick, and Alpine’s top driver Joshua, battled it out for 26 laps straight. Joshua took the win after a little bit of questionable contact and a helpful dose of backmarker blocking. This is Alpine and Joshua’s second win of the season. Alpine also had some 007 magic from their second seat, Eddie, who had 0 intention of racing, 0 practice, and placed 7th. Coincidentally this was also his second time placing 7th this season. Let’s see if this pattern continues for the French outfit.
                ''')
    st.image(silverstone1)
    st.markdown('''
                The podium was rounded out by Ferrari ace, Erick, who raced a lonely set of laps around the hallowed airfield. Ferrari’s other driver Zane battled with VCARB’s Patrick in a tightly contested tango where the drivers had opposite tire strategies (softs to mediums and mediums to softs respectively). However, in the end, a bit of contact left Zane just out of reach on the final lap.
                ''')
    st.image(silverstone2)
    st.markdown('''
                Further down the field the two Red Bull drivers Yeti and Boz sparred for the entire race, ending in 6th and 11th after a late error by Boz. Which allowed VCARB’s Brently to make up a place after a muddled start, and end in 8th. Finally, rounding out our grid this week were the Aston Martins with Gary finishing in 19th and Del MIA for this week’s bout.
                '''+'''
                Alpine’s Joshua takes an early strong lead in the WDC with his back-to-back wins. His efforts, along with Jr.'s, have propelled the team into the lead for the WCC as well. As it stands today Alpine leads the way, followed by Ferrari and McLaren who are separated by mere points. The WDC currently stands with Joshua, Nick, and Zane in the top three with Erick just one point behind his Ferrari teammate in 4th. See you all down under where the league takes to the converted streets of Albert Park.
                ''')
    st.markdown('''
                <p style="color:lightgray;">Wednesday 12/4/2024 - Patrick Knowles with credit Eddie & Nick</p>
                ''',
                unsafe_allow_html=True,)
    st.divider()
    #endregion

    #region Race Week Silverstone
    st.subheader('Race Week - Silverstone')
    st.markdown('''
                Rise and shine gamers, its race week! This week The Alternative will take to the famed and hallowed pavement of Silverstone. With a week off for the Thanksgiving holiday, the drivers should not be worried about meeting the minimum weight limit at the end of the race. With the season still young, all drivers are still hopeful they can make a meaningful impact on both championship races.
                '''+'''
                Additionally, the league’s president, Mr. Erick Tavera, is proud to unveil the crown jewel of this year’s competition, the champion’s trophy. Derived from F1’s cancelled COTA trophies, The Alternative’s World Driver’s Champion and Constructor’s Champions will receive a commemorative trophy marking their achievement from throughout the season. The Pirelli tire the champion stands upon has each of this season’s tracks encircling the perimeter of the tire. The races won by each driver or constructor will be highlighted in gold. Additionally, the bottom of the base will include the driver’s and constructor’s records and accomplishments from throughout the season.
                ''')
    st.image(trophy)
    st.markdown('''
                <p style="color:lightgray;">Sunday 12/1/2024 - Patrick Knowles</p>
                ''',
                unsafe_allow_html=True,)
    st.divider()
    #endregion

    #region Suzuka Recap
    st.subheader('Suzuka & Pre-Season Recap')
    st.markdown('''
                With a lovely pre-season in Miami complete where 8 of the league's 12 drivers and all 6 constructors took to the streets around Hard Rock Stadium, the lights went out in Suzuka to an aborted start. With a multiple car incident that sent the whole grid into turmoil,the race director determined it was best to have a full restart. One of our top qualifiers, VCARB's Patrick, fell back two positions at the start and near the end of the first lap attempted to make up those positions going into the Hitachi Astemo Chicane. This maneuver failed and ended with a slow down into the chicane allowing many of our drivers to make up spots against the AI and other drivers. The remainder of the race saw only a few spins, beachings, and other minor mishaps that affected a few of the final standings. Big winners from this race include VCARB's Brentuar as well as Aston Martin's Del. Alpine's Joshua took home the win and the fastest lap with McLaren's reigning champion Nick coming in second and Del rounding out the podium.
                ''' + '''
                With the results final, Alpine takes an early lead in the Constructors’ Championship. Alpine's Joshua is also leading the Driver's Championship. Reigning champion Nick finds himself in second place in the Driver's Championship with his team, McLaren, also slotting into second overall in the Constructors’ Championship. Ferrari, Aston Martin, VCARB, and Red Bull respectively make up the rest of the Constructors’ Championship standings.
                '''+'''
                <p style="color:lightgray;">Thursday 11/21/2024 - Patrick Knowles</p>
                ''',
                unsafe_allow_html=True,)
    #endregion