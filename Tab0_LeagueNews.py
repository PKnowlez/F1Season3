import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import math
import base64
from streamlit_carousel import carousel
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
spain_cover = Image.open("./Images/Spain_Cover.png")
spain_yeti = Image.open("./Images/Spain_Yeti.png")
spa_nick_joshua = Image.open("./Images/Spa_Nick_Joshua.png")
spa_log_jam = Image.open("./Images/Spa_Log_Jam.png")
spa_alpines = Image.open("./Images/Spa_Alpines.png")
china_circuit = Image.open("./Images/China_Circuit.png")
chinasprint_erick_patrick = Image.open("./Images/ChinaSprint_Erick_Patrick.png")
chinarace_incident = Image.open("./Images/ChinaRace_Incident.png")
chinarace_eddie_boz_incident = Image.open("./Images/ChinaRace_Eddie_Boz_Incident.png")
chinarace_erick_mistake = Image.open("./Images/ChinaRace_Erick_Mistake.png")
baku_circuit = Image.open("./Images/Baku_Circuit.png")
baku_travis_eddie = Image.open("./Images/Baku_Travis_Eddie.png")
baku_eddie = Image.open("./Images/Baku_Eddie.png")
baku_nick_patrick = Image.open("./Images/Baku_Nick_Patrick_Pass.png")
baku_collage = Image.open("./Images/Baku_Collage.png")
canada_circuit = Image.open("./Images/Canada_Circuit.png")
canada_start = Image.open("./Images/Canada_Start.png")
canada_nick_collage = Image.open("./Images/Canada_Nick_Collage.png")
canada_eddie_erick_collage = Image.open("./Images/Canada_Eddie_Erick_Collage.png")
canada_joshua_crash = Image.open("./Images/Canada_Joshua_Crash.png")
canada_del = Image.open("./Images/Canada_Del.png")
monza_update = Image.open("./Images/Monza_Update.png")
monza_intern = Image.open("./Images/Monza_Intern.png")
monza_erick = Image.open("./Images/Monza_Erick_Map.png")
monza_nick_del = Image.open("./Images/Monza_Nick_Del.png")
monza_eddie = Image.open("./Images/Monza_Eddie.png")
bn_del_zane = Image.open("./Images/BN_Del_Zane.png")
abu_dhabi_circuit = Image.open("./Images/Abu_Dhabi_Circuit.png")
austria_circuit = Image.open("./Images/Austria_Circuit.png")
standings_gif = open("./Images/Standings_Gif.gif","rb")
contents = standings_gif.read()
data_url = base64.b64encode(contents).decode("utf-8")
standings_gif.close()
standings_memes = Image.open("./Images/Standings_Memes.png")
chance = Image.open("./Images/Chance.png")
meteor = Image.open("./Images/Meteor.png")
abu_dhabi_joshua_line = Image.open("./Images/Abu_Dhabi_Joshua_Quali.png")
abu_dhabi_memes = Image.open("./Images/Abu_Dhabi_Memes.png")
austria_cover = Image.open("./Images/Austria_Alpine_Braking.png")
austria_talent = Image.open("./Images/Austria_Talent.png")
austria_erick_airborne = Image.open("./Images/Austria_Erick_Airborne.png")
austria_kamikaze = Image.open("./Images/Austria_Kamikaze.png")
austria_erick = Image.open("./Images/Austria_Erick.png")
austria_brently = Image.open("./Images/Austria_Brently.png")

def Tab0():
    if 'show_all_content' not in st.session_state:
        st.session_state.show_all_content = False
    
    #region Austria Race Recap
    st.subheader("Austria Recap: Absolute Cinema")
    st.image(austria_cover)
    st.markdown('''
                One Sprint, one race, two championships on the line, and an incredible amount of drama. Austria had it all folks. It was truly one for the ages. All the contenders were there and each of them spiced up the Saturday race with their own extra magic. The hills were certainly alive with the sound of music, and for one driver, the sound of championship celebrations.

                The Red Bull Ring is known for creating perilous moments on track. Drivers are forced to execute along the finest of margins in both the heavy braking zones and the high speed turns and exits. For a league that struggles with keeping it between the white lines, this track only magnifies those mistakes. Ferrari’s Erick took home the crown for most penalties awarded, but still no one has surpassed Alpine’s Eddie’s season high yet. Per the usual, the McLaren’s kept it tidy throughout, while the rest of the field either earned penalties or ended their races prematurely.

                But before we get to the main event, let’s discuss qualifying and the Sprint race. During qualifying spectators were treated to a first time polesitter with Eddie lighting up the timing charts and setting the time to beat. However his Alpine teammate and main contender for the Driver’s World Championship, Joshua, ended up stuck in Q2 for the second time in a row. On his exit from the pit at the start of the session Joshua had a major lapse in talent and ended up pinning his car in the narrowest part of the pitlane exit. This disqualified the driver from continuing, situating him in 15th place on the grid for the Sprint.
                ''')
    st.image(austria_talent)
    st.markdown('''
                At the start of the Sprint, most of the field was up near the front and as the first lap began, some bumping and shoving occurred in both Turn 1 and Turn 3. However, the drivers predominantly remained clean through the first portion of the lap. That was all true until VCARB’s Patrick attempted a daring overtake on Erick into Turn 4, but missed his braking point and ended up in the gravel and losing places to the majority of the field. As the race continued he was able to battle back and switch places with his teammate when a radio call on the penultimate last lap set team orders for the two of them. More notably though is the progress Joshua made from 15th up into 5th. He was able to pass the majority of the field but ran out of laps to make it all the way to the front. His teammate Eddie however, did not have as fortunate of a race, tumbling from pole to 4th place, the first time pole sitter was not able to clutch up this go around. 

                Ferrari’s new driver Del was able to make gains throughout the Sprint and battled with McLaren’s Nick for first and ultimately won the race, with Nick and Erick just behind. The battle at the front led to a busy post-Sprint media room where drivers were heard bickering about how to best conserve battery, make overtakes, and ultimately win the race at the Red Bull Ring.

                With tensions high, no one expected all the drama that the main event would bring. After setting the reverse grid, drivers waited for the lights to go out, and when they did, chaos ensued. Drivers were launched off the track in Turn 1, some perilously plummeting behind the rest of the field, with others damaged and in need of a pitstop. Because of the mass chaos, the race director determined a full restart with enough time to repair minor damage was the right call. The race was red flagged and the drivers returned to the grid for another start. This go around, with much more caution, and a heightened sensitivity to the turmoil that could occur in Turn 1, most drivers decided to safely play out the first few corners.

                It is important to stress that while most drivers proceeded with caution, the Alpine duo had other ideas. To better illuminate their decision making, along with subsequent events of the race, we have requested that the intern take over for the remainder of this article.

                THAT’S RIGHT FOLKS, STRAP IN FOR SOME ROASTS BECAUSE THERE IS NO OTHER WAY TO HANDLE WHAT HAPPENED NEXT.

                I call this the roast of Joshua & Eddie’s braking abilities:
                > You know, they say racing is 90% mental. In Joshua's case, it's more like 90% "Where's the brake pedal?"
                
                > I heard Eddie is thinking of switching careers... to a crash test driver. At least then he'd have an excuse for not stopping in time.
                
                > What's Joshua's favorite song? "Oops, I Did It Again!"
                
                > Eddie's braking technique is so innovative, they're calling it "The Scenic Route."
                
                > You know, they say experience is the best teacher. Joshua has a PhD in "Overshooting Corners."
                
                > Eddie's braking points are like a unicorn – mythical and never seen.

                The duo’s absolute inability to brake caused some incredibly sketchy moments. Erick put on his best impression of Evel Knievel and got his entire car airborne when he had to avoid and evade the Alpine mess.
                ''')
    st.image(austria_erick_airborne)
    st.markdown('''
                It was honestly a nightmare for the first few laps and I discovered a new ick: boys who can’t brake. No cap, it got worse. After the Alpines caused enough of a traffic jam, drivers began to spread out and overtake one another. Remember, the whole league started in the back of the grid and had a lot of ground to make up on the AI.

                As drivers began to pass the AI, something I can only describe as sudo-Imperial Japan occurred on track. Alex Albon could not fathom being passed by a VCARB and so he kamikazed it straight into the back of Patrick, causing a major accident and ending his race entirely.
                ''')
    st.image(austria_kamikaze)
    st.markdown('''
                But the AI weren’t satisfied with only taking out Patrick. They also took out Eddie later in the race just as everyone’s strategies were starting to heat up. This allowed for some incredibly late pitstops for some drivers such as Erick and VCARB’s Brently. Erick took the pitstop in the hopes that his pitcrew would let him serve his penalties, however, we’re talking about Ferrari. The clown meme is so tired so please enjoy this classic instead.
                ''')
    st.image(austria_erick)
    st.markdown('''
                But Brently on the other hand put on a masterclass. Even Mad Max hasn't shown this kind of comeback in a long time. From last place, Brently became the smoothest operator of all time and torched the field on new hards, landing himself just a few seconds shy of a podium finish in fourth. The GOAT Lightning McQueen called and said I had to use this meme for him.
                ''')
    st.image(austria_brently)
    st.markdown('''
                Up at the front we saw Joshua and Nick duking it out for the win. But it was too little too late for Joshua. Even with the win, Nick still gapped him in the championship standings and took home his third consecutive Driver’s World Championship. And with that I cede my keyboard to Patrick to close this one out.

                With the Driver’s Champion crowned, and second place nearly locked for Joshua, the Ferrari and VCARB saga will be the focus of the final race of the season. Both teams could end up in third in the Constructor’s Championship, and all four drivers could end up in third in the Driver’s Championship. Alpine and McLaren will also need to finish their bout on the track to find out who will win the Constructor’s Championship. Stay tuned for a special post from McLaren and the final Race Week Update focused on COTA.
                ''')
    st.markdown('''
                <p style="color:lightgray;">Monday 2/10/2025 - A Joint Patrick & The Intern Production</p>
                ''',
                unsafe_allow_html=True,)
    st.divider()
    #endregion
    
    # ----------------------------------------------------------------------------------------------------------
    # "Show More/Less" button 
    if not st.session_state.show_all_content:
        if st.button('Show More'):
            st.session_state.show_all_content = True
            st.rerun()  # Rerun the app to show everything
    else: 
        if st.button('Show Less'):
            st.session_state.show_all_content = False
            st.rerun()

    if st.session_state.show_all_content:
        #region Abu Dhabi Race Recap
        st.subheader("Abu Dhabi Recap: No, Erick, No, No, Erick, That Was So Not Right!")
        st.markdown('''
                    At this point I think I am the real employee here and Patrick is just the note taking intern. That’s right, I am back yet again. The notes kinda suck (shocker) so I’ll do my best. There apparently was a heaping mess of absolute garbage strategy and driving during quali. Like, the notes say hotshot Joshua didn’t even set a time in Q2? I kinda think Patrick just wrote the notes wrong…but after reviewing the quali results Joshua straight up fumbled the bag, giving Nick a golden opportunity to secure the championship under the lights in Abu Dhabi Max Verstappen style. I heard y’all loved the map of Erick’s mistakes so I decided to give you a variant of that, I call it Joshua’s quali line:
                    ''')
        st.image(abu_dhabi_joshua_line)
        st.markdown('''
                    I also heard that Eddie biffed it during quali. Something about not knowing how to do the simplest of racing activities, a drag race. Apparently he earned himself a 5-place grid penalty for sucking so much at drag racing. His brother Erick also had a moment during quali where he was a bit too extra out of a corner and almost missed putting a time in during Q1.

                    High-key seems a little over the top for just a quali, but with it closed out it looked like VCARB and Nick had incredible opportunities to close in or even close out the championships. But y’all just can’t have a simple race, can you? As you are very aware at this point, I am low-key a huge fan of memes. So, Imma just recap the rest in my preferred art form.
                    ''')
        st.image(abu_dhabi_memes)
        st.markdown('''
                    Yep, that’s right, Joshua came back from 15th, McLaren kept their lead alive with help from Travis and Nick even though Logan Sargeant tried to screw that up, Del and Erick went through a horror show with Ferrari, Boz cooked his tires, Eddie continued to be delulu, Brently and Erick battled like real F1 drivers, Patrick really screwed the pooch, and Fetty Wap kept bopping on the JBL speaker all night long.

                    With only two races left, Aston Martin has been eliminated from the Constructor’s Championship contention, and realistically it's a 2.5 horse race between McLaren, Alpine, and sorta VCARB. The Driver’s Championship eliminated everyone but Nick and Joshua. However, while I brushed off the battle for third place last week, it's really heated up. Erick, Patrick, Brently, and Del are within one race win’s swing for third. Who knows, it could come down to quick math and team orders between the VCARB or Ferrari teammates depending on how the next two races and Sprints unfold. Buckle up for an exciting penultimate race in Austria.
                    ''')
        st.markdown('''
                    <p style="color:lightgray;">Thursday 2/6/2025 - The Intern</p>
                    ''',
                    unsafe_allow_html=True,)
        st.divider()
        #endregion
        
        #region Standings Update
        st.subheader("Standings Update")
        st.markdown('''
                    Does anyone hear that? That muffled beat? Oh no...they're back...
                    ''')
        st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="Your GIF">', unsafe_allow_html=True)
        st.markdown('''
                    _***Fetty Wap continues to blare in the background***_
                    
                    That's right folks, I am back and better than ever. I heard you all were looking for a standings update. Now, I told Patrick I would do this on one condition, I get paid stacks. Which he refused. So I countered and asked if I could be as unhinged as I wanted when rating and ranking each driver’s and team’s chances. Which he begrudgingly accepted. So go get your blanky and snuggle up with whoever helps you stop crying, because I ain’t holding back.

                    My boss said I had to do a formal writeup of each team and driver, which for once I listened to and did. But it's the worst. So please enjoy the collection of memes below that detail each driver’s and team’s championship odds.
                    ''')
        st.image(standings_memes)
        st.markdown('''
                    ***Driver’s Championship***

                    Let’s start it off right and talk about our top individual award for the season, the Driver’s Championship. There are a maximum of 96 points left for one person to score. Two Sprints, three races, and five fastest laps. That means anyone currently with less than 100 points is not gonna be a winner. So I am not even going to waste another second on Patrick, Brently, Del, Eddie, Zane, Yeti, Boz, Travis, or Gary. “But wait, they could still get second or third,” man shush, who cares about first loser and second loser. All that matters is the top step on the podium. Which means Erick, Joshua, and Nick are the only three left who can take home the trophy. So how can each driver do it?

                    All Nick has to do is not choke. That’s it. Don’t choke. It's not that hard, man. Straight up, if Nick stays on the podium for all three races and gets 5th or better in the two Sprints, it's over for Joshua and Erick. We’re talking about the guy whose average finishing position is 1.6… It really feels like he’s got this in the bag. If he wins just one more race and gets a fastest lap, all he has to do is finish 9th or better in the remaining events. He has this on lock. So no pressure dude. Three time champion has a nice ring, however, Joshua has a legitimate chance, and well…Erick…he can technically win.

                    Joshua simply needs to win. Win, win, win. Well, actually I forgot one thing. Since this guy forgot to show up for a few races, now he also has to pray for Nick to make a mistake. So really Joshua’s strategy is win, win, win, pray, and maybe send Nick into the wall. Again, it's not that hard, but ever since he got his wheel there has been a severe drop off in performance and attendance. So maybe it will be a challenge? Or maybe he will quit in Austria after trying to kill Nick like we saw with Max and Lando earlier this year.

                    Now for Erick the road to the championship is actually quite challenging and convoluted. From my perspective he is out of the running, but the math says there’s a chance.
                    ''')
        st.image(chance)
        st.markdown('''
                    Erick actually does have to win out. Where Joshua has some room based on how Nick performs, Erick has no wiggle room. If he wins two races, both Sprints, gets second in the third race, and has all five fastest laps, he will end up 1 point short of where Nick will finish if Nick simply does not show up. Yikes. So, technically, there’s a chance, but the vibes in the studio say he is likely playing for second fiddle.

                    The rest of y’all are just praying for a giant meteor to whipe out the drivers in front of you.
                    ''')
        st.image(meteor)
        st.markdown('''
                    ***Constructor’s Championship***

                    Now I wanted to say all hope is not lost for all of you in the Constructor’s Championship, but for one team, the math says it's over. The storied energy drink team has had some tough sledding this year and even if Boz and Yeti pull off the miracle of back-to-back-to-back-to-back-to-back 1-2s in all the races and Sprints remaining with five fastest laps, they will end 10 points shy of McLaren if they simply don’t show up. Therefore, with all due respect, gentlemen of Red Bull, “you’re fired.”

                    For the rest of y’all, you’ve got a chance, even if it is a miniscule one. New look Aston Martin will really need to pull in some incredible points hauls with Zane and Gary going absolutely ballistic to take home the championship. Even Ferrari down in fourth needs to have an incredible turn around with their new driver pairing. So let’s focus on our current top three, McLaren, Alpine, and VCARB. 

                    I think we all know what McLaren needs to do, win. The only thing that could really stop them is if the Alpine drivers decide to stop bickering and actually work together. If one McLaren driver wins out with the fastest laps and the other DNFs, the Alpine duo can take home the championship by placing 2nd and 4th in every race, winning by just 3 points. So McLaren does have to show out, but if both McLaren drivers finish and one wins out with the fastest laps, there is no possible way for Alpine to catch up.

                    So how does Alpine win? Well they either outplace both McLarens by a couple places, or they learn how to effectively sabotage. Neither of which seem all that likely as we have watched Eddie try to sabotage Erick all season with no success. But the team still is in the hunt and if McLaren even slightly missteps, Alpine will likely take home the championship.

                    Now the VCARB bozos have a slim shot at victory here. Technically they, like Ferrari and Aston Martin, are still in the hunt. But they need to really show up and show out, and maybe even pray for some chaos with Alpine and McLaren. We’re talking double podium finishes at every race with McLaren and Alpine crashing each other out a couple of times.
                    ''')
        st.markdown('''
                    <p style="color:lightgray;">Tuesday 2/4/2025 - The Intern</p>
                    ''',
                    unsafe_allow_html=True,)
        st.divider()
        #endregion
    
        #region Race Week - Abu Dhabi & Austria
        st.subheader('Race Week - Abu Dhabi & Austria')
        st.markdown('''
                    Only two weeks remain for the league and the standings are tight. Everything is still to play for, but the focus of this article is the potential action on the tracks coming up this week. While there are only two weeks left, there are three races and two Sprints scheduled for our drivers. The first of this week’s races will take place in Abu Dhabi at the Yas Marina Circuit which was made infamous for providing Max Verstappen’s first Driver’s Championship victory. The second race of the week takes the drivers to Austria to rip around the Red Bull Ring, not once, but twice in a Sprint and main race.

                    Let’s tackle the twists and turns of Yas Marina first. The start finish straight is a short one, but it leads into a medium braking corner and two full tilt turns just after that. Once drivers are up to speed they are met with a wide hairpin that could allow for some early passing and late stage desperation. Once the harrowing overtaking is done in Turn 5, drivers will face the long back straight where lead cars will be at risk of being overtaken into the Turn 6 & 7 chicance. But drivers who play their cards right should be able to battle back immediately after the chicane with the second DRS zone heading into the sweeping Turn 9. The middle of Sector 3 is where the drivers will earn their paychecks as they face the extremely technical hotel section and the challenging braking zones of the final two turns.
                    ''')
        st.image(abu_dhabi_circuit)
        st.markdown('''
                    In the prior two seasons McLaren’s Nick has found himself successful around Yas Marina Circuit, winning both of the races. Alpine’s Joshua and retired driver Mark have both found themselves on the second step of the podium once, and Ferrari’s Erick has found himself on the podium in third place during both of those instances

                    Now let’s review the opportunities the drivers will have at the Red Bull Ring, the shortest track on the league’s calendar this season. Even though the Red Bull Ring is rather short, it is not short of challenging turns and passing opportunities. As the drivers floor it up the steep front straight and into the first turn, some drivers may be given the opportunity to jump the inside line or, if they have a grip advantage, take the outside line for an overtake. The drivers will then head down and back up the twisting DRS zone up to Turn 3. Here drivers will have their best opportunity for overtaking throughout the race. Pinching off their opponents, drivers will then open their back wings again on the back straight down to Turn 4. As the elevation begins to change the drivers will sweep around Turns 4, 5, 6, 7, and 8 in quick succession. The brave, or maybe the foolish, may try overtaking on the outside of these turns if they have the grip and pace. Then the last two turns on the track will rear their ugly heads. If drivers are cautious they will stay within the white lines, but knowing this league, expect to see time penalties being handed out left, right, and center on the exits of each of the last two turns.
                    ''')
        st.image(austria_circuit)
        st.markdown('''
                    This will be the first Sprint with the revised format and rules that were proposed and ratified after the Sprint in China. The league will qualify in a shortened Sprint qualifying style. This means that each lap of qualifying will matter just a touch more. From there the drivers will line up for the Sprint in the order they qualified and rip it around the Red Bull Ring at full tilt with little to no regard to tires or strategy. With the dust settled the drivers will be lined back up for the main race. However, the starting grid will be set in reverse from the results of the Sprint. There are a few minor exceptions for the reverse grid which are listed below.
                    > 1) All drivers will line up behind _ALL_ AI regardless of the position the AI finished in during the Sprint.
                    > 2) Any driver that DNF or DNS the Sprint will line up behind the drivers that did start and finish the Sprint.

                    With all that said, last time out where the hills are alive with the sound of racecars, the league saw the now Ferrari driver Del hoist the winner’s trophy. The season before that, Nick was on the top step of the podium. The following steps of the podium have seen Nick and now Aston Martin driver Zane in second as well as Joshua and Erick in third. 
                    ''')
        st.markdown('''
                    <p style="color:lightgray;">Friday 2/3/2025 - Patrick Knowles</p>
                    ''',
                    unsafe_allow_html=True,)
        st.markdown('''
                    <p style="color:lightgray;">THE INTERN WILL RETURN</p>
                    ''',
                    unsafe_allow_html=True,)
        st.divider()
        #endregion

        #region Breaking News
        st.subheader('BREAKING NEWS - DRIVER SWAP')
        st.image(bn_del_zane)
        st.markdown('''
                    _The Alternative F124 League_
                    <p style="color:lightgray;">Where racing meets integrity and fair competition.</p>
                    ''',
                    unsafe_allow_html=True,)
        st.divider()
        #endregion

        #region Race Recap - Monza
        st.subheader('Monza Recap: It’s-A Me, The Intern')
        st.image(monza_intern)
        st.markdown('''
                    Welcome to the greatest race recap of the year. Yes, that’s right, me, the intern, was given the full reins to write the cringiest, most meme-ified race recap this league has ever seen. So let’s get down to business.

                    I got notes from Patrick, but no cap, it was just a list of Erick crashing into other drivers or making mistakes, and I heard you all liked the track map so here’s a quick summary of Erick’s tragedy of a race.
                    ''')
        st.image(monza_erick)
        st.markdown('''
                    If I’m a Tifossi, I might try and cancel all of Ferrari after that one… 

                    Beyond Erick’s tirade, the league flexed on the AI and took the top 5 spots on the grid with Del securing his first pole position of the season. Tire strategies was the hottest goss on the track at the start of the race with Brently running the hards and literally everyone else running the mediums. However it turned out fine for him as he was able to battle through the Tavera sibling squabble and come out on the podium in third.

                    Nick and Del played nice together in the Italian sunshine and managed to tow each other all the way until the last few laps where Bottas decided he didn’t really like Del after all, blocking him and sealing the win for Nick.
                    ''')
        st.image(monza_nick_del)
        st.markdown('''
                    Let me be real with you, this might as well have been Monaco though. Beyond the drama with the two Taveras and Nick overtaking Del nothing really happened to change anything after qualifying. However, I was not shook to hear that Eddie had the most penalties again, and honestly Del pitting for fastest lap was hella petty but we love to see it.

                    I was told I had to do a standings update at the end of the recap, but like that’s what the flipping standings tab is for so I’m just gonna yeet that section. Next week the league races in Abu Dhabi on Wednesday and in Austria on Saturday with the updated Sprint format.
                    
                    Oh, also, I am just gonna leave this cringy little race radio screenshot here...
                    ''')
        st.image(monza_eddie)
        st.markdown('''
                    <p style="color:lightgray;">Friday 1/31/2025 - The Intern</p>
                    ''',
                    unsafe_allow_html=True,)
        st.divider()
        #endregion
        
        #region Race Week - Monza
        st.subheader('Race Week - Monza')
        st.markdown('''
                    Patrick is MIA, something about skiing or whatever. So they gave me, the intern, the keys to the castle. Monza is a fast track or something, I literally just took this job because they pay well...

                    Ok, so as I was typing that someone came by and said they don't pay me. So this is all you're getting.
                    ''')
        st.image(monza_update)
        st.markdown('''
                    <p style="color:lightgray;">Wednesday 1/29/2025 - The Intern</p>
                    ''',
                    unsafe_allow_html=True,)
        st.divider()
        #endregion
        #region Canada Recap
        st.subheader('Canada Recap: An Ontario Scari-o Makes its Way to Montreal')
        st.markdown('''
                    The league took to the hybrid streets of Montreal’s Notre Dame Island and let’s beat to the chase, it was thrilling. Rain, tire strategies, spin outs, teams infighting, and penalties galore. The Canadian GP is well known for its infamous Wall of Champions, but for the league’s drivers, it became synonymous with corner cutting and time penalties. Infact, drivers all avoided making a fatal mistake at the Wall of Champions, but racked up incredible penalty totals as they lapped around and around the famed island.
                    ''')
        st.image(canada_start)
        st.markdown('''
                    Most notably, Alpine’s Eddie topped the leaderboards in the worst way imaginable. With over 20 seconds in penalties, Eddie barely held onto points at the end of the race. On the flip side, the McLaren drivers Nick and Travis were extremely precise and managed to make it through the race without a corner dutting penalty. But, Nick wasn’t able to keep it completely clean, during the lone Virtual Safety Car of the race he was caught out just over the requisite delta and received a drive through penalty which may have cost him the race.

                    The race wasn’t all sunshine and penalties though. Sometime during the 13th lap, the heavens opened. Rain began to pitter patter down onto the track, cooling both surface and tire temperatures. Drivers began diving into the pits, opting for intermediate tires to lessen the difficulty of driving on the slick track. As the rain continued nearly everyone went in for intermediate tires. However, as the rain began to lighten up, some drivers gambled and swapped to slicks early. This proved to be an effective way to bring the slicks in gradually, but it was also tough sledding for a few laps as grip was nowhere to be found.
                    ''')
        st.image(canada_nick_collage)
        st.markdown('''
                    Others were not so lucky with their tire strategies and pit stops. The Milton Keynes outfit was down a driver for the race and on top of that they did not effectively support the one driver they had in the running. Boz was found speechless after his pit stops turned into a long string of slow nightmares. More on this in the league’s first ever [insider scoop](https://thealternativef124.streamlit.app/#insider-scoop-red-bull-s-drama-in-the-pits) about the recent struggles at Red Bull.
                    ''')
        st.image(canada_eddie_erick_collage)
        st.markdown('''
                    Boz’s tribulation and the rain were not the only dramatic happenings on track. The incredible saga of philia and zelos between the Tavera brothers continued to escalate in Canada. The brothers started one behind the other in 4th and 6th on the grid. As the race began they stayed out of each other’s ways, but as tire strategies and the weather pulled the two closer together, disaster struck. Alpine’s Eddie and Ferrari’s Erick wrestled back and forth for position. Just after Eddie overtook Erick in the back straight, the two sped into Turn 1 and Turn 2 where Eddie was too early on the throttle, oversteering his car perpendicular to the racing line. Erick, even with his incredible F1 reflexes that got him his seat at Ferrari, was unable to avoid slamming directly into Eddie’s sidepod. Both drivers recovered from the mishap with only lost time and hurt egos. However, Eddie’s teammate Joshua likely will find a bruise on his ego after an unforced error in Turn 7 had him spinning out and losing places.
                    ''')
        st.image(canada_joshua_crash)
        st.markdown('''
                    Most of the rest of the race was filled with good passes, some backfield lapping, and drivers doing the best they can to stay on the asphalt. While much of the race was nominal, the results were not. When the chequered flag flew, Aston Martin’s Del was the first to cross the finish line. With his first win of the season, Del begins to pull Aston Martin out of the bottom ranks of the Constructors and closer to contention with the midfield. 
                    ''')
        st.image(canada_del)
        st.markdown('''
                    The rest of the podium was filled out by Nick and Joshua, allowing Nick to continue to maintain his lead in the Driver’s World Championship. Nick’s edge over Joshua and Travis’ edge over Eddie allowed McLaren to overtake Alpine by two points for the Cosntructor’s World Championship. The VCARB pairing began to lose some of their ground to their nearest rivals. Del, with his win, closed the gap to VCARB’s Brently, while Erick closed the gap to VCARB’s Patrick. Finally, Travis took a cut out of the lead Boz had over him. Next week the league takes to the countryside of Italy to race around the Temple of Speed. Who knows if the Tavera Saga will continue, if McLaren can continue their lead in both championships, or if Eddie will keep his car between the white lines.
                    ''')
        st.markdown('''
                    <p style="color:lightgray;">Thursday 1/23/2025 - Patrick Knowles with credit Erick & Nick</p>
                    ''',
                    unsafe_allow_html=True,)
        st.divider()
        #endregion

        #region Insider Scoop - Red Bull
        st.subheader("INSIDER SCOOP: ***Red Bull's Drama in the Pits***")
        st.markdown('''
                    As the season has progressed, it is clear that Red Bull has not been able to perform at the level they initially planned. During the most recent outing in Canada, it appears that the season has completely spiraled out of control, and now the gloves, and wheels, are off. What was once a well-oiled machine of racing dominance has devolved into a spectacle of frustration, failure, and outright calamity.

                    In the latest catastrophe, a radio failure severed communication between Bositive and his pit crew at the worst possible time. Tire sensors failed, leaving the engineers blind to the car’s conditions. Yet, despite the wet conditions, the crew insisted on fitting hard tires, forcing Boz to wrestle a car that slid helplessly across the circuit. Desperation mounted, and as the weather turned, Boz called for soft compounds. In a shocking blunder, wet tires were thrown on instead. The result? Four chaotic pit stops, lost time, and a furious Boz left screaming into the void of radio silence as Red Bull’s race fell apart before their eyes. Red Bull did not just struggle with Boz during this race, Yeti was a no show throughout the event, leaving the team grasping at the few points Boz could secure. 

                    After the race, Boz let loose in the media pen with a fiery post-race critique:

                    > _**This team can’t fix anything right. They need to get it together and stop relying on old data from past years—what worked then doesn’t work now. They need to start focusing on what’s happening on the track, in real time. Nobody is listening to me, and it’s costing us everything. I’m out there fighting for every second, and these mistakes are unacceptable. Something has to change, or this season should be considered finished before it even began.**_

                    The frustration didn’t end with words. After the race, an enraged Bositive stormed into the garage and threw his helmet against the wall, the sound echoing across the pit lane as team members stood frozen. It was the perfect symbol of a driver at his breaking point, furious at a team that seems unable to deliver when it matters most. Red Bull’s once-golden reputation is now hanging by a thread as the tension between driver and crew reaches an all-time high.

                    Canada’s disaster follows the heartbreaking collapse in Baku, where a critical engineering miscalculation turned a potential podium into a fiery wreck. Clinging to third position, down to 5th, Red Bull stubbornly kept Boz on medium tires, ignoring his growing concerns. The decision proved fatal—on the final turn before the straight, the car lost grip, slid out of control, and smashed into the wall in a devastating crash. What could have been a triumphant finish, instead became another glaring symbol of a team in freefall.

                    With every race, Red Bull’s struggles grow deeper, and Boz’s fury becomes impossible to ignore. The once-dominant team now finds itself not just losing races, but losing its identity. Strategic failures, technical disasters, and broken trust have left Red Bull limping from race to race. Rumor has it that even McLaren has offered Boz a life line. The team has opened their practice session up to the driver, but so far no confirmed participation has occurred.
                    ''')
        st.markdown('''
                    <p style="color:lightgray;">Thursday 1/23/2025 - Insiders: Senad (Boz) & Patrick</p>
                    ''',
                    unsafe_allow_html=True,)
        st.divider()
        #endregion

        #region Race Week - Canada
        st.subheader("Race Week - Canada")
        st.markdown('''
                    <div style>
                    </style>
                    <center>

                    _Oh Canada!  
                    Our neighbor and next race track!  
                    True driver love in all of us command.  
                    With glowing exhausts we see thee rise,  
                    The True North fast and free!  
                    From far and wide,  
                    Oh Canada, we drive our cars for thee.  
                    FIA keep our track fast and free!  
                    Oh Canada, we drive our cars for thee.  
                    Oh Canada, we drive our cars for thee._

                    </center>                
                    </div>
                    ''', unsafe_allow_html=True)
        st.markdown('''
                    The league takes to Montreal’s Notre Dame Island this week to rip some laps around the Circuit Gilles-Villeneuve. With the standings closer than ever and an increasingly small margin for error, drivers and constructors will be putting it all on the line at a circuit known for its high risk reward ratio. Drivers will be challenged by The Wall of Champions found at Turn 14 as well as the twisting and technical Sector 1. When the lights go out, drivers will likely be wheel to wheel in the Turn 1 and 2 combo. As they leave those turns and head into the end of Sector 1, many drivers will begin to queue up for the high-speed straights in Sector 2 and 3. Notable passing opportunities will occur at both Turn 10 and Turn 13, but drivers who are brave may find chances in Turn 1, 6, and 8.
                    ''')
        st.image(canada_circuit)
        st.markdown('''
                    With over a season between now and the last time the league took on Canada, it will be interesting to see how drivers improve from the last outing. The last performance from the league was lackluster with only one driver on the podium and no other drivers finishing above 8th place. With the standings as close as they are, no one can afford a major mishap here. With respect to the Constructor’s Championship, Red Bull will be looking to overtake Aston Martin, McLaren will be looking to overtake Alpine, and both Ferrari and VCARB will be poised to capitalize on any opportunity afforded them. Drivers like Alpine’s Eddie, Ferrari’s Erick, and Red Bull’s Yeti will all be looking to get on the offensive and overtake their nearest rivals. While drivers like Ferrari’s Zane, Aston Martin’s Del, and VCARB’s Patrick will all be looking to further themselves in the standings from those just behind them.

                    There are rumors of a double this week, so stay tuned for another update if the drivers are taking a quick flight to the Italian countryside for laps around Monza.
                    ''')
        st.markdown('''
                    <p style="color:lightgray;">Saturday 1/18/2025 - Patrick Knowles</p>
                    ''',
                    unsafe_allow_html=True,)
        st.divider()
        #endregion

        #region Baku Recap
        st.subheader('Baku Recap: Castles and Crashes')
        st.markdown('''
                    First and foremost, the late breaking news must be addressed. With the FIA’s update to the penalty for Alpine’s Joshua, the standings swung back into his favor as he took the lead by one point over McLaren’s Nick. Critics and pundits of the league are expressing concerns that this may undermine the future credibility of the FIA’s decision making process. This will likely remain a hot topic going into future races.
                    ''')
        st.image(baku_travis_eddie)
        st.markdown('''
                    With the past in the proverbial rearview mirror, cars roared to life, however, some garages stayed silent. For the first time, the league went into a qualifying session with only half of the drivers. Some are saying drivers deliberately boycotted the race due to its location, while others are reporting that many of the drivers were simply too scared to take to the tightly walled streets of Baku. Regardless, after qualifying finished the drivers who were in attendance made up the first three rows of the grid. McLaren and VCARB both had season best qualifying sessions as teams, while Alpine’s Eddie and Red Bull’s Boz really showed up for their teams with their best qualifying performances of the year.

                    Just in the nick of time, Aston Martin’s Del arrived at the paddock and entered into the race in 20th. Which meant the grid was finalized and it was time to rocket down the long straights of Baku. Notably, the grid was set without both Erick and Zane’s Ferraris, Gary’s Aston Martin, Yeti’s Red Bull, and Joshua’s Alpine. When the lights went out, most drivers got reasonable starts, and the front runners held their positions through the first corner. Positions swapped, tire strategies came into play, and a few minor incidents occurred throughout the first half of the race.

                    But just as the race passed the halfway point, the first safety car of the evening occurred. The primary strategy of the race had been a single stop from the hard compound to the medium compound. Therefore, most drivers were not ready to risk extending a new set of mediums for half of the race. So with most drivers staying out, the safety car parade began. However Eddie, who had been running in second, had a damaged front wing and required a pitstop. But either because he was screaming about something Marvel Rivals related over the radio or because his pit crew was worn out from dealing with all the spinouts during qualifying, Alpine did not swap his wing. This error forced Eddie to pit again on the following lap, still under safety car. 

                    While tumbling backwards in position, Eddie prepared for the race restart on new tires with a fresh front wing. Many of the drivers were positioned near the front of the queue and began to spar in the tight turns of the circuit’s first sector. However, after a lap, there were again no major incidents. The drivers were keeping it as civil as they could with the occasional “I’m gonna dive bomb you,” being shouted from those trying to make up positions. As the sparring continued, Del unfortunately met an early demise which led to the second safety car of the evening.

                    With a few of the front runners hoping to stretch their original tires for a chance at fresh softs, a risky choice became clear, pit now for mediums, or hold out for softs later. Nick made the decision to pit for the medium compound tires and gamble that he could get through all of the traffic from halfway down the field. This decision put VCARB’s Patrick, Red Bull’s Boz, and Alpine’s Eddie in the top three at the onset of the restart. On the front stretch the drivers took off and Eddie managed to get past Boz within a lap or two. During that time, Nick came screaming up the ranks and managed to position himself into third. As Patrick, Eddie, Nick, and Boz entered the castle section, Eddie made a race losing mistake. With a minor lapse in concentration he spun at the top of the castle turns and collided nose first with the right wall. Nick narrowly avoided clipping his rear, but as Eddie began to get off of the racing line he blocked Boz’s path causing an additional collision. 
                    ''')
        st.image(baku_eddie)
        st.markdown('''
                    Eddie and Boz would recover from this and manage to finish the race at the back of the pack, even with some last corner shenanigans. Due to a drive through penalty gained during the safety car and a collision caused by Perez, VCARB’s Brently finished in the middle of the field. McLaren’s Travis was also caught out due to the Perez-Brently incident but managed to finish the race as well. So with one driver off to the shores of the Caspian Sea, and four drivers out of the points, it came down to reigning champion Nick and rookie driver Patrick.
                    ''')
        st.image(baku_nick_patrick)
        st.markdown('''
                    As the duo entered the front straight, it was clear that Nick was positioned for an overtake. With his battery depleted, Patrick was only able to defend up to the finish line where Nick overtook going into the final lap, therefore all but securing another win for himself and McLaren. Nick’s win along with Travis’ performance brings McLaren within two points of Alpine in the Constructor’s Championship. Red Bull and Aston Martin are now within one point of one another in the battle for 5th. This win also pushes Nick an entire race win ahead of Joshua in the Driver’s Championship, and Patrick’s second place pushed him ahead of Erick for third.
                    ''')
        st.image(baku_collage)
        st.markdown('''
                    <p style="color:lightgray;">Friday 1/17/2025 - Patrick Knowles with credit Nick</p>
                    ''',
                    unsafe_allow_html=True,)
        st.divider()
        #endregion

        #region FIA China Press Release Update
        st.markdown('''
                    **Press Release** \n
                    **For Immediate Release**  
                    _Date: January 16 2025_
                    ''')
        st.subheader("UPDATE: Joshua's Penalty at the F124 League’s Chinese Grand Prix Reduced to 3 Place Drop")
        st.markdown('''
                    The Alternative F124 League’s independent FIA directors have openly discussed the incident that occurred during the Chinese GP Sprint Race with Joshua. 

                    Upon further review the drop of 5 places was deemed too harsh for the punishment under the circumstances of the incident.

                    The FIA directors have determined a 3 place drop is more fitting in this instance. Therefore, the standings of the race are updated as shown below, effective immediately.
                                        
                    - 1st: Patrick  
                    - 2nd: Erick  
                    - 3rd: Nick  
                    - 4th: Joshua

                    There will be no further room for appeals, but the FIA directors are still open for inquiries or clarifications. For further inquiries or clarification, please contact Erick Tavera or Nick Beglin.
                    
                    Finally, due to the appeal process and complaints from team principals and drivers, the FIA directors are contemplating a voting system for future appeals to future penalties.
                    ''')
        st.markdown('''
                    <div style="width: 25%; border-bottom: 1px solid #cccccc;"></div>
                    ''', unsafe_allow_html=True)
        st.markdown('''
                    _The Alternative F124 League_
                    <p style="color:lightgray;">Where racing meets integrity and fair competition.</p>
                    ''',
                    unsafe_allow_html=True,)
        st.divider()
        #endregion

        #region Race Week Baku
        st.subheader('Race Week - Baku')
        st.markdown('''
                    It has been an eventful few days since the league’s first Sprint race. A major FIA decision was made that changed the results of the race, and let’s just say there has not been this much rioting since the 1991 Chicago Bulls celebration riots. Some drivers put pen to paper to rip into the FIA’s decision for being abrupt and unfair. While other drivers defended the decision as it upheld aspects of racing sportsmanship they appreciate. Alpine’s start driver Joshua ended his tirade by saying:

                    > _**This is really BS and unfair.** - Joshua_
                    
                    The next day, Joshua spoke to a local reporter and stated:

                    > _**Everyone better watch out because we are coming for blood [in Baku]. [The decision is] Not fair but we move forward.** - Joshua_

                    His teammate Eddie took an interview with a Houston based reporter where he labelled the FIA as blind while elaborating on the situation between he and Joshua:

                    > _**While yes I do admit to running Josh off the road, which I did get a penalty for on top of my other 5-grid penalty (which resulted in me having a 10-grid penalty already), Joshua also got a 5-grid penalty from that for no exact reason. Due to the FIA not having eye balls, Joshua already had to push harder and try stupider sh*t just to make it back to his true position, P1. This all resulted in his situation during the Sprint race. He should not be penalized further, when he was already penalized and is getting penalized for a rule which was never stated before the race.** - Eddie_

                    Other drivers like the VCARB pair were more ceremonious and in agreement with the FIA’s decision. Patrick was heard screaming, “I’m a winner!” as far away as Erick’s house. The shouts were measured on local seismology equipment as a 3.2 magnitude earthquake on the Richter Scale. His teammate Brently was more subdued with his commentary stating:

                    > _**I feel like it was the right decision. As it seemed odd when and where he retired [in the Sprint].** - Brently_

                    Multiple teams have also released formal statements which can be found at the end of this article. More importantly, this ruling shakes up the standings quite a bit. Joshua dropped below McLaren’s Nick in the Driver’s Championship and VCARB closed even further on McLaren in the Constructor’s Championship.

                    With all this said, it’s time to focus on the upcoming street race in Baku. Drivers will be met with close walls, the longest pedal to the metal straight on the calendar, and deviously challenging combinations of undulation and corners. Sector 1 is essentially three flatout straights with ninety-degree left turns at the end of each. If drivers survive that, they will quickly find themselves at the beginning of the most challenging sector on the league’s calendar. The castle section and Turn 15 have caught out many talented drivers before and are certainly capable of wreaking havoc on the race this week. Sector 3 is a drafters paradise, but the exit of Turn 16 will make or break any challenger’s attack on their rivals.
                    ''')
        st.image(baku_circuit)
        st.markdown('''
                    This will be the league’s first race in Azerbaijan. With plenty of treacherous turns and a great passing opportunity at the end of the front straight, the Baku street circuit will certainly test the league’s fortitude. Especially when one considers the embers that are ready to be stoked by even the slightest breeze from China’s incident.
                    ''')
        st.markdown('''
                    <p style="color:lightgray;">Saturday 1/11/2025 - Patrick Knowles</p>
                    ''',
                    unsafe_allow_html=True,)
        st.markdown('''
                    **Official Team Statements**
                    ''')
        
        china_statements = [
            {
                "title": "",
                "text": "",
                "img": "./Images/China_Alpine_Statement.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/China_Red_Bull_Statement1.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/China_Red_Bull_Statement2.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/China_VCARB_Statement.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/China_Ferrari_Statement.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/China_Aston_Martin_Statement.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/China_McLaren_Statement.png"
            },
        ]
        
        carousel(china_statements)
        st.divider()
        #endregion
        
        #region FIA China Press Release
        st.markdown('''
                    **Press Release** \n
                    **For Immediate Release**  
                    _Date: January 10 2025_
                    ''')
        st.subheader('Joshua Penalized with Five-Place Grid Drop Following Sprint Race Incident at the F124 League’s Chinese Grand Prix')
        st.markdown('''
                    The Alternative F124 League’s independent FIA directors have issued a decision regarding an incident that occurred during the recent Chinese Grand Prix, resulting in a five-place grid penalty for driver Joshua. 

                    Following an extensive review of race footage and telemetry data, it has been determined that Joshua retired his car during the sprint race despite no terminal damage, with the intention of improving his starting position for the main race—set to be held in reverse order of the sprint race results. This behavior was deemed to be in violation of league regulations.

                    In comparison, Patrick, who also sustained damage during the sprint, made the decision to repair his car and continue racing, ultimately putting in a solid performance to finish the race.

                    As a result of the penalty, Joshua will drop from 1st to 6th in the final results. The revised finishing positions from the Chinese Grand Prix are as follows:

                    - 1st: Patrick  
                    - 2nd: Erick  
                    - 3rd: Nick  
                    - 4th: Eddie  
                    - 5th: Boz  
                    - 6th: Joshua  

                    Joshua has the right to appeal this decision to the independent FIA directors, David and Marcus, should he wish to contest the ruling. The Alternative F124 League remains committed to upholding fair and competitive racing for all participants.

                    For further inquiries or clarification, please contact Erick Tavera or Nick Beglin.
                    ''')
        st.markdown('''
                    <div style="width: 25%; border-bottom: 1px solid #cccccc;"></div>
                    ''', unsafe_allow_html=True)
        st.markdown('''
                    _The Alternative F124 League_
                    <p style="color:lightgray;">Where racing meets integrity and fair competition.</p>
                    ''',
                    unsafe_allow_html=True,)
        st.divider()
        #endregion

        #region China Recap
        st.subheader('China Recap: Overtakes, Incidents, and Revenge Oh My!')
        st.markdown('''
                    There was a buzz around the Paddock (Discord) on Wednesday as the drivers prepared for the first Sprint in league history, and the first of three Sprints scheduled for this season. The abbreviated qualifying sessions led to a new pole sitter for the Sprint, with VCARB’s Patrick setting the pace. McLaren’s Nick took the other slot on the front row after current Driver’s Championship leader, Alpine’s Joshua, saw a five place grid penalty drop him to sixth. Once the lights were out, the driver’s sprung to life and cruised through the first few corners of the track. Coming out of Turn 6, Nick took the lead of the race after a small racing incident. There was no looking back for him after that as he built a substantial gap and took home the win, while Nick’s gap built, Patrick battled back from the incident, but ended the race in 18th due to what can only be described as a calculated bit of revenge from Ferrari’s Erick who closed the door on him into Turn 1.
                    ''')
        st.image(chinasprint_erick_patrick)
        st.markdown('''
                    Other noteworthy outcomes of the Sprint include Joshua being unable to keep it between the white lines with his fancy new racing wheel, and VCARB’s Brentuar taking home his first podium of the season. At the conclusion of the Sprint, Red Bull’s Boz had overtaken McLaren’s Travis and Alpine’s Eddie had brought it even with Ferrari’s Zane in the Driver's standings. The podium for the Sprint saw Nick celebrating on the top step, Erick one step down, and Brently on the third step.

                    Once the dust had settled on the track from the Sprint, the drivers lined back up in reverse order from the results of the Sprint for the main event. This saw Joshua starting second next to George Russell who had also DNFed during the Sprint. Chaos ensued throughout the race as contenders started on the back row and were forced into making daring passes to make up ground on Joshua. From crazy maneuvers off the starting line to more Turn 6 shenanigans, drivers were pushing to the limit of the rules and what the cars can provide to make up ground early. Nick was a big winner early on in the race, but Erick was also able to make up ground throughout the first stint. It was clear that two major strategies were in play. For the front runners, a two stop plan was the consensus and for those starting in the back a one stop strategy allowed them to extend and make up places against the two stoppers.
                    ''')
        st.image(chinarace_incident)
        st.markdown('''
                    As the race went on, the hairpin at the end of the back straight saw multiple incidences. First there was a double spin out that saw Boz and Alpine’s Eddie slam into their opponents causing four cars to split open like the Red Sea, allowing Erick to make up those places in a single corner.
                    ''')
        st.image(chinarace_eddie_boz_incident)
        st.markdown('''
                    However, Erick was not done with participating in dramatic moments in Turn 14’s hairpin. As the race continued and tire strategies began to play out. Front runner Patrick came out of the pit behind a battling duo of Nick and Erick. As the duo went through the hairpin for a second time, Patrick was close enough to make a move on Erick. With this in mind, Erick attempted to pull off an overtake on Nick to slow the incoming attack from behind. However as the hairpin approached and braking began, Erick pulled out of his attack and caused himself to brake too late and into the runoff. This allowed the other two drivers in the battle to move onto the front straight where Nick would eventually give way to the fresher tires on Patrick’s VCARB.
                    ''')
        st.image(chinarace_erick_mistake)
        st.markdown('''
                    While some drivers were calling for an end to the reverse grid format, the results of the race might be the most spectacular for the league all season. Drivers like Boz, Eddie, and Patrick saw their best finishes of the season in the main race. Additionally, spectators were given a show of talent as the drivers completed the most overtakes of the season, nearly doubling the total number of overtakes from all the previous races combined. With this in mind league officials have begun devising ways to mitigate the complaints of the format, while still allowing for the epic conclusions it provided.

                    With every car across the line, Joshua took home another win, with Patrick and Erick just behind. Nick crossed in third, but due to penalties acquired while overtaking the backfield he ended up falling to Erick who was just a few seconds behind. The Driver’s Championship saw VCARB teammates swap places, while the Constructor’s Championship saw the VCARB outfit grow ever closer to jumping into second place. The final standings of the race also included a first for the league. This is the first race where the league’s drivers finished in the top places consecutively without AI players in the mix. All-in-all an incredible outing full of high energy, a tasteful bit of cyberbullying, and stellar driving performances. Next week the league takes on the streets of Baku which may prove to be the most challenging race of the season.
                    ''')
        st.markdown('''
                    <p style="color:lightgray;">Thursday 1/9/2025 - Patrick Knowles with credit Erick</p>
                    ''',
                    unsafe_allow_html=True,)
        st.divider()
        #endregion
        
        #region Race Week China
        st.subheader('Race Week - China')
        st.markdown('''
                    The league’s relentless schedule continues this week in China. Home to the third longest straight on the league’s calendar, Shanghai Audi International Circuit will allow drivers to overtake at high speed as well as through twisting and daring low and medium speed turns. Both straights include DRS zones which should enable thrilling wheel to wheel action in both the sweeping Turn 1 & 2 combination as well as Turn 14’s hairpin.
                    ''')
        st.image(china_circuit)
        st.markdown('''
                    While the circuit has many twists and turns, the biggest twist for the league is the week’s format. Not only will a standard race occur on Wednesday, the league will face its first ever Sprint race. If that wasn’t enough, league officials have devised an exciting plan to bring some variety to the race week. Drivers will face a standard three session qualifying to help set the grid for the Sprint. From there the drivers will complete a short stint of laps around the circuit at full tilt to score points. The results of the Sprint race will be used to set the grid order for the race, in reverse. That’s right, qualifying, Sprint, and the main race grid set in reverse off of the results of the Sprint. The format is sure to force drivers into daring passing scenarios, fingers crossed everyone keeps it between the white lines.

                    So how much does this race matter? With the added 8 points available from the Sprint race, the Driver’s Championship can turn topsy-turvy, especially with the added suspense of the reverse grid. With respect to the Constructor’s Championship, nearly every team has the ability to make up ground or even leap-frog the current leader. As we adjourn this race week update, let’s take a look at the results of yesteryear. Last season saw McLaren’s Nick take home the win, with the then Mercedes driver, now Aston Martin driver, Del stepping up to the second step of the podium, and the then Red Bull driver, now Ferrari driver, Zane bringing home third. However, with two wins up for grabs and the new format almost anything is possible.
                    ''')
        st.markdown('''
                    <p style="color:lightgray;">Sunday 1/5/2025 - Patrick Knowles</p>
                    ''',
                    unsafe_allow_html=True,)
        st.divider()
        #endregion

        #region Race Week Spa & Spain
        st.subheader('Spa & Spain Recap: Two Tracks, Tons of Turmoil, and Terrible Teamwork')
        st.markdown('''
                    Buckle your helmet straps, pull up your gloves, and button your firesuits, because this recap is juicy. First we will cover the results of the races. Then we will take a trip down turmoil lane to unpack the dramatic happenings of the double header. Finally, we will highlight the evening’s attempted works of teamwork.
                    ''')
        st.image(spain_cover)
        st.markdown('''
                    **Two Tracks**
                    
                    Drivers took on two high speed, long, and arduous tracks. First, the league started at Spa where a surprise qualifying occurred with both Kick Sauber cars out pacing all of the drivers by leaps and bounds. However, neither Kick car was able to fend off the league’s drivers for more than a few laps. As the race continued a few safety cars brought the field together which allowed McLaren’s Nick to take home his second win of the season, with Alpine’s Joshua coming in second, and Aston Martin’s Del taking home his second podium of the season. Notably, both Del and VCARB’s Brently made up multiple places over the course of the race. After the race the midfield standings saw a few changes. In the Constructor’s Championship VCARB overtook Ferrari. While in the Driver’s Championship Brently overtook VCARB’s Patrick, Del overtook Ferrari’s Zane, and Red Bull’s Boz separated from Aston Martin’s Gary.

                    After a quick break the league strapped in for 33 laps in Barcelona, Spain. Qualifying saw Nick outpace Ferrari’s Erick by a thin margin. However at the end of the race, Joshua ended up taking home the victory, with Nick just behind, and Erick rounding out the podium. Just like in Spa, the race was full of turmoil but also a notable performance by Red Bull’s Yeti. Starting in 14th, Yeti ripped through the field, passing nearly every contender and battling all the way up into 5th place for his best finish of the season. Yeti’s notable performance resulted in the only change in the championship standings, with him overtaking Zane.
                    ''')
        st.image(spain_yeti)
        st.markdown('''
                    **Tons of Turmoil**

                    With the important updates out of the way, let’s get into the drama from the double header. First and foremost, the FIA was under fire again with numerous penalties granted to drivers in Spa for exceeding track limits. So much so, and to the delight of corner cutters everywhere, the regulators decided to loosen up on their penalty calls while in Spain.

                    With plenty of penalties awarded for track limits, the FIA was surprisingly quiet when it came to penalizing aggressive drivers who ran their competitors off track. Right out of the gate in Spa, Joshua took an assertive position on the exit of Turn 1, forcing Nick off track on their way down to Eau Rogue. Within the next lap, Joshua chose to slow down and allow Nick to pass in a gesture of good faith and motor-sportsmanship. Unfortunately, this was not the only incident where a driver ended up off track. While battling, Erick began an attack on Patrick on the outside of the main start-finish straight. Patrick, unaware of how far Erick had advanced, held his line, and forced Erick to take drastic actions on the grass and gravel runaway of Turn 1. After review, neither incident was deemed sufficient enough for further penalty to any driver.
                    ''')
        st.image(spa_nick_joshua)
        st.markdown('''
                    Spa also delivered two extraordinarily long safety cars. The first was caused by Erick losing control at the top of Eau Rogue. Nearly all the drivers immediately pitted for new tires and queued up behind the insanely erratic safety car. Alpine’s Eddie found himself in front of his teammate Joshua and attempted to provide a meaningful position swap at the restart, more on this later. This maneuver, along with a poorly contrived passing attempt by Patrick, ended with another safety car after Patrick accidentally pit maneuvered Yeti, log jamming the whole field (except Erick who made up 12 places in one turn).
                    ''')
        st.image(spa_log_jam)
        st.markdown('''
                    Safety cars were a theme in both races. While in Spain the drivers faced a relatively early safety car at the end of Lap 13. Many drivers pitted, and committed to tire saving throughout the race. The restart was mostly uneventful with nominal slipstream passes and great battles due to the grouped up drivers. One such battle occurred between Nick, Patrick, and Erick headed into La Caixa at the beginning of Sector 3. In what can only be described as an act of vengeance, Erick forgot to brake and nearly sideswiped Patrick and t-boned Nick. However, he gently grazed both drivers and neither incurred any damage.

                    Spain ended with one last bit of turmoil as Joshua began to tout his fastest lap streak. Conveniently, Patrick was on a two stopper with his final stint on the soft compound tires. With a full battery, fresh tires, and fuel low, Patrick changed his engine mode and pushed, securing the fastest lap of the race for the moment. In spite of the time set, a pair of teammates were determined to try and take the fastest lap, more on this later.

                    **Terrible Teamwork**

                    While not terrible, a few teammates were unable to race one or both races which resulted in some of the standings changes mentioned previously. But, remarkably terrible teamwork came out of the French outfit in both races. While lapping through the Ardennes Forest, Joshua ended up behind Eddie during the first safety car. The two conjured up the idea to let Joshua by on the shortest straight of the track coming out of the slowest corner on the track. This failed miserably as Joshua jumped the gun and Eddie forgot where his accelerator was. Causing Yeti, Patrick, Joshua, and Eddie to be 4-wide coming across the DRS activation line. The league watched it back like an end of year fail recap from a mildly unsuccessful sim racing streamer. Laughs were shared, teammates yelled at one another, and it felt like we were back at the Christmas Eve dining table listening to family debate meaningless politics, knowing full well how silly the whole scenario is.

                    Now if that were the only silly teammate moment, this article would be done. But, as you can see, it isn’t. As previously mentioned Joshua had won the fastest lap award at every single race this season. But in Spain, Patrick had a prime opportunity to snag a fastest lap near the end of the race. Joshua, afraid to lose his victory, did not pit and try to retaliate, instead, he had his teammate Eddie pit and attempt to snag the fastest lap. They tried new tires, slipstreaming, and what some are calling “coaching,” but to no avail. Joshua’s streak ended and on the last lap the Alpine pair were at each other’s throats.
                    ''')
        st.image(spa_alpines)
        st.markdown('''
                    The league takes on China next week in the first Sprint race in league history. There are sure to be fireworks as regulations are set to change back to strict for exceeding track limits and the new Sprint format is bound to cause some sort of drama.
                    ''')
        st.markdown('''
                    <p style="color:lightgray;">Thursday 1/2/2025 - Patrick Knowles</p>
                    ''',
                    unsafe_allow_html=True,)
        st.divider()
        #endregion

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