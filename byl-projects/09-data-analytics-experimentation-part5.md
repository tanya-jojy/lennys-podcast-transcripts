# BYL Brain: Data, Analytics & Experimentation (Part 5)
_Auto-generated from Lenny's Podcast Transcripts Archive_
_Last updated: 2026-02-23 00:40 UTC_
_This is part 5 of a multi-part project file._

---

## FULL TRANSCRIPTS

---

## An inside look at how CNN builds product | Upasna Gautam
**Guest:** Upasna Gautam  
**Published:** 2023-02-23  
**YouTube:** https://www.youtube.com/watch?v=gRiCzfFEd7c  
**Tags:** growth, onboarding, okrs, roadmap, analytics, conversion, leadership, management, vision, persona  

# An inside look at how CNN builds product | Upasna Gautam

## Transcript

Upasna Gautam (00:00):
It happens all the time, right? That is the nature of breaking news. I mean, you have to be ready to pivot at the drop of a hat. I had a big working session planned with my users to do research with them, or do user testing, and breaking news breaks, and it takes so much time and effort to gather a team of editors across the globe to do a user testing session. And when breaking news happens, they have to prioritize that over everything. So what do you do in that situation? You can be frustrated, absolutely it's frustrating. But we always have to have the ability to A, pivot of course, but also have backup and buffers in those types of scenarios.
Lenny (00:45):
Welcome to Lenny's Podcast, where I interview world-class product leaders and growth experts to learn from their hard-won experiences building and growing today's most successful products. Today my guest is Upasna Gautam. Upasna is a product manager at CNN, where she leads the team responsible for the content management system that journalists use to write and publish their stories. She's also on the frontlines of elevating the discipline of product management within newsrooms through her work at the News Product Alliance. She's also a longtime meditation and mindfulness teacher, which as we discuss ends up being pretty damn handy working at a place like CNN. We dig into how the product team operates within CNN, how they collaborate with journalists for breaking news, dress rehearsals, and also some simple tricks to build your own mindfulness in your day-to-day work as a PM.
(01:31):
Enjoy this episode with Upasna Gautam after a short word from our wonderful sponsors. This episode is brought to you by Amplitude. If you're setting up your analytics stack but not using Amplitude, what are you doing? Anyone can sell you analytics, while Amplitude unlocks the power of your product and guides you every step of the way. Get the right data, ask the right questions, get the right answers, and make growth happen. To get started with Amplitude for free, visit Amplitude.com. Amplitude, power to your products. Today's episode is brought to you by OneSchema, the embeddable CSV importer for SaaS. Customers always seem to want to give you their data in the messiest possible CSV file, and building a spreadsheet importer becomes a never-ending sink for your engineering and support resources.
(02:19):
You keep adding features to your spreadsheet importer, the customers keep running into issues, six months later you're fixing yet another date conversion etch case bug. Most tools aren't built for handling messy data, but OneSchema is. Companies like Scale AI and Pave are using OneSchema to make it fast and easy to launch delightful spreadsheet import experiences, from embeddable CSV import to importing CSVs from an SFTP folder on a recurring basis. Spreadsheet import is such an awful experience in so many products. Customers get frustrated by useless messages like, "Error online 53," and never end up getting started with your product. OneSchema intelligently corrects messy data so that your customers don't have to spend hours in Excel just to get started with your product. For listeners of this podcast, OneSchema's offering a $1,000 discount. Learn more at OneSchema.co/lenny. Upasna, welcome to the podcast.
Upasna Gautam (03:15):
Thank you Lenny, I'm so excited to be here.
Lenny (03:18):
As you probably know, I'm on this kind of quest to understand how different companies build product, especially companies that are kind of outside the Silicon Valley, just like standard tech scene. And I've always wondered what it was like to build product at a company like CNN, which is very different from where most, I don't know, tech PMs work. And so I'm really excited to have you on and to give us a little glimpse into what it's like to build product at CNN.
Upasna Gautam (03:42):
Awesome, I'm very excited to share as well.
Lenny (03:44):
So I was doing a little research on you before this chat, and I noticed that you've been teaching and studying meditation and mindfulness for, I don't know, maybe a decade? And I imagine that comes in handy at a company like CNN, which also I imagine is quite hectic at times with breaking news all the time. And so here's my question, what have you learned or brought from that practice to your ability to lead and ability to just like keep your team calm and focused during I imagine many hectic moments?
Upasna Gautam (04:16):
Love that question, and working in product in news is a very [inaudible 00:04:22]. We hear a lot about having the skills to thrive in ambiguity in order to be a successful product manager, but to be a successful product manager in news you have to be able to thrive in chaos. And equanimity is the most important skill I've developed I think across my entire life, and it's due to all of those years of practicing mindfulness and meditation. And equanimity is one of my favorite words, it means mental calmness, composure, evenness of temper, especially in crazy, stressful situations. It's the ability to remain un-rattled in like the highest of highs and the lowest of lows. And if you think about it in the dynamic of a workplace or human interaction, it's really the ability to pause before reacting.
(05:11):
And reactivity is the root cause of so many of our workplace woes and product management frustrations, and when you're able to pause before reacting you can start to undo and break a lot of those negative patterns in your brain. And in news, and especially the world's biggest breaking news organization, you can cut through that chaos with equanimity because it also really gives you this outsized advantage in everything from stakeholder management, team morale, to the way you're able to translate user feedback, to product development philosophy. And the thing is is you're always going to hear things and feedback that you don't like, and opinions that you don't like, and you're going to get frustrated. That's product management, that's life.
(05:59):
But real power to me comes from equanimity, and that comes from managing your emotional reactions, and not trying to control others. So I think when you're able to cultivate that level of self-awareness for yourself, you're able to chart a clear path forward for your team and serve as a compass in the chaos.
Lenny (06:22):
Is there a story or an example that comes to mind where things were just like, "Oh shit," and you were able to tap into that skill that you built to stay calm and focused, or even just like help your team stay focused?
Upasna Gautam (06:33):
I mean, it happens all the time right? That is the nature of breaking news. I mean, you have to be ready to pivot at the drop of a hat. And so I think more than just like the big, chaotic moments in those daily interactions when there's chaos, I think that's when it really shows its power and helps me navigate those day-to-day interactions when I had a big working session planned with my users to do research with them, or do user testing, and breaking news breaks, and it takes so much time and effort to gather a team of editors across the globe to do a user testing session. And when breaking news happens, they have to prioritize that over everything. So what do you do in that situation? You can be frustrated, absolutely it's frustrating. But you always have to have the ability to, A, pivot of course, but also have backup and buffers in those types of scenario. So any time we're planning we build in buffers for all of that chaos that's happening on a daily basis.
Lenny (07:41):
Wow, that's cool. Is that a real thing that happened? You were like, in a big meeting with all the researchers and then something went off the rails in the world?
Upasna Gautam (07:47):
Oh yeah, absolutely. Happens all the time.
Lenny (07:49):
I don't know how much you can go into all this, but what is it that you would do in that case, like as a product team? What are they looking for you to do at that moment?
Upasna Gautam (07:56):
For us it's not really anything we have to do. It is more so, "Okay, well our goal at this session was to get user testing done, or user feedback from that user testing session with our editors. And so, what do we do? Okay, well good thing we had a backup planned, right?" We don't actually have to go into that scenario, but since our editors and our journalists are customers we're there to serve their needs, but they're not here to serve our needs. They have a whole another job that they have to do. And so we have to have the ability to adapt and accommodate to those really chaotic schedules across global time zones. And so that happens again like, it's not like once in a while, it's a very regular thing that we have to be aware of and also account for.
Lenny (08:46):
Okay, again, it's like the journalists are the ones in the meeting that like, "Oh, they have to go write about the stuff uncovered."
Upasna Gautam (08:50):
Totally.
Lenny (08:51):
I see, that makes sense. You said that you built in some buffer time to kind of account for these things. Is there like a systematic way of doing that, or is it just broadly, "Let's add buffer time"? Is there like a rule of thumb you think about there?
Upasna Gautam (09:02):
It depends on the scope of the work we're doing at that time. So one of my main responsibilities is to rebuild our content management system, which also involves onboarding our editors and journalists to it off of our legacy platform and onto our new one. So when we're thinking about onboarding especially the teams, our onboarding cycle's very long. It involves training, testing, lots of dialogue and feedback. And then only do we actually test, and then we onboard. And so it is a long cycle, and it's longer than it maybe seems like it needs to be because we have to build in those buffers. Sometimes that buffer is a day or two, and sometimes it's a week or a month. And sometimes when we think we need a buffer, we get it done in a day and we quickly move onto the next phase.
(09:53):
And so I think that quick decision-making in those times is super-important, because you have to be able to assess the situation as it stands. And so I think mindfulness is so important too in practices like this, because being able to objectively see the scenario for what it is, make a quick decision and move on to the next phase is something we have to analyze every single day.
Lenny (10:16):
Makes me think a little bit about a lot of CEOs are very busy and pulled into a lot of things, and so you have to kind of account for their schedule. And it sounds like you have many, many people that you work with that have crazy schedules.
Upasna Gautam (10:29):
Yes.
Lenny (10:30):
I wanted to dig a little bit deeper into how you, your team works with the news team. It's such a unique way of working, most product teams don't have a whole set of journalists that they have to work with as stakeholders. So I'm curious specifically, say a journalist has like, "Hey, I'd love to build a special immersive experience for this story," or, "I need some special feature to help support this work that I'm doing." How does that work? Do they come to you, and, "Okay, here's a roadmap [inaudible 00:10:57] maybe in the quarter [inaudible 00:10:59]." Imagine it's like, "I need this next week." How do you work with the journalist team, basically, on product?
Upasna Gautam (11:04):
Yep. This is pretty much the foundation of all of my work. We talk to our editorial staff every single day, and after a lot of observation and learning I implemented a system to manage that kind of intake with four different touch points or events. So we have weekly demo days, working sessions, breaking news dress rehearsals, and office hours. So with weekly demo days, I facilitate those with my product design lead and my tech lead. And we use that as an open form of communication to deep dive into features that exist on our platform, also to preview or give a sneak peek of new features to come, and kind of recreate their workflows and do a show and tell. Again, we wanted to open that up as a forum to not just our editorial partners but also anyone across the business who is interested in learning about the product and which is our platform.
(12:00):
And it was also a great way to kind of evangelize the product too. Coming off of a legacy system after several years onto a brand-new one is a big change at a place like CNN, and so we definitely tried to make sure that smart repetition in different ways is top priority. So, weekly demo days is one. Working sessions are interesting. I use the term working session because it's a combination of several things. This is a really critical part of our onboarding process where we gather breakout groups of our journalists and editors to work with us to recreate their workflows in the new platform. This allows us to address any friction or issues of course that are occurring in their workflows. But also we're able to gather a lot of awesome feedback from them in those sessions.
(12:54):
We used to call them user testing sessions, but decided to move away from that and just call them working sessions so they're more collaborative. And again, it's a really critical part of our onboarding process. We usually do three to six of them depending on the size of the group before the team is actually onboarded for two hours per session. So they're like deep dives into their specific workflows, so as you can imagine the way the politics team programs content is wildly different than the way the entertainment team does, or the way that the health team does, and very different than the way that the CNN homepage even interacts. So all of those are separate teams we have to work with when it comes to getting feedback. So in addition to that, we also do I mentioned breaking news dress rehearsals.
(13:44):
And you can imagine this is exactly what it sounds like. We create a script and do a simulation of a breaking news scenario to stress test our platform, because all breaking news scenarios are definitely not the same either. So this gives us a lot of great feedback in that short amount of time at the speed of breaking news. And then last but not least, we have office hours which I just started last year, and that's also probably what you can imagine, open blocks of time where me and my product design partner and my tech lead are just there to answer questions, help people troubleshoot any friction they might be experiencing in their workflow, get their feedback. We just wanted to open up another line of communications, so we do those right now once a week. Sometimes they go up to two times a week if we're in a really vigorous onboarding phase.
(14:33):
After those conversations and sessions and events happen, you know it's our job to translate their needs into the functions that we, A, either maybe already have that we can optimize, B, we build anew, or we tell them it's not viable. And the good thing is that because they've been along for the ride with us throughout the product discovery process we've earned their trust and respect. So that when we tell them something like it's not viable, they usually get it.
Lenny (15:07):
Man, I have so much questions about just working with journalists. I feel like pushing back on a journalist is probably extra hard versus other types of stakeholders.
Upasna Gautam (15:14):
It is.
Lenny (15:15):
Can we zoom out a little bit, and you talked about what you work on at CNN, which is the content management system and things around that. Can you just talk about whatever you can share, just like what does the product team look like at CNN, how many PMs are there, how's like the product work structured and where do you fit in there?
Upasna Gautam (15:31):
Yes. I mentioned earlier my team sits on CNN Digital, and I think when most people think of CNN of course you think of TV and linear programming. I have nothing to do with that, CNN Digital is digital, and it's made up of several teams that are structured around a lot of different product areas. It includes everything from the content management platforms that I work on, to data infrastructure, to personalization, to video experience, which includes like the products of video editor, and the video player, to podcasts, there's a lot. So each of those are product teams. And so we also split out... The way CNN is split out into CNN Digital is because there's a separate core content platform that powers broadcast and linear TV.
(16:21):
And the one that I work on powers CNN Digital. So on my team, the core platform team, our stakeholders and our customers, like I mentioned, are journalists and are editors. Which presents a really unique dynamic, and it's one that I love. We have direct access to our customers at all times of day, for better or for worse, and they're embedded into our product development process. And each of those teams under CNN Digital is kind of like a squad, very similar to how it is at other larger tech companies. We have PMs, we have engineers, designers, and delivery managers embedded in those squads. And since my team is a core platform team, our main responsibility is to A, build our newer, faster, more flexible content management platform to replace our legacy one, and B, onboard our entire editorial staff to it.
(17:19):
And so even more specifically my role is focused on rebuilding the tooling and the editorial experience of that platform, as well as doing the actual onboarding of our journalists. So we work cross-functionally because our team kind of is the umbrella over a lot of different teams, so we truly work cross-functionally to make sure that we're serving our journalists with the tools that they need to do their job in the most efficient way possible.
Lenny (17:48):
What would surprise people most about how product is built at CNN?
Upasna Gautam (17:54):
I think the most surprising thing may actually be that there's just so many different types of products that we build. Like I said, I think when most people think of CNN you see TV, and you think of Anderson Cooper, and all of the things that are very publicly visible. Most of our product work and product teams all sit behind the scenes, and so I think just that in itself, like the sheer size of that is surprising to a lot of people. So I mentioned like all of the different teams, product teams that are based off of function, content management platforms, infrastructure, personalization, video, podcasts, linear TV. And I think that in itself, like the sheer size of it, we're not the size of Google by any means. But at the same time we have the expertise and the depth and breadth of a lot of those larger tech companies.
Lenny (18:52):
I'm curious about the day-to-day operational work of how you build product at CNN. So our first question here is just, you use like OKRs, and OKRs with like key objectives, and outcomes, and 70% of a goal is success.
Upasna Gautam (19:06):
Yeah, absolutely, we do. We've used OKRs for a long time, and they've served as an anchor for my team over the last three years. I can't go into specifics on like what our OKRs are, but I did kind of cover the two main parts of it, which is rebuilding our content management platform and onboarding our users to it. So again, it's a long game at CNN when you're working on a core platform to replace a legacy one. And so we break those OKRs down of course even further into, we look two to three years out and build goals based off of that. Then we break them down by quarter and month, and then out of that for my team and what I do I need to, for my own sake and my team's sake, break those down by the week. And when we're in rapid development phases, we're planning on a daily basis.
Lenny (20:01):
How about in terms of just planning broadly? How far out does the product team at CNN plan in detail, like have an actual roadmap? And is that standardized across teams, or can each team kind of do their own approach?
Upasna Gautam (20:13):
It's a combination of both. So we have one that is an over-arching roadmap that tracks to like our company OKRs and our product organization OKRs. And then from there I mentioned we have our squads, product teams, and we have OKRs on those as well track up to the larger, broader ones. And so once we get down to that level though, there is flexibility and we have autonomy to tackle those how we want. Which is really great, because the scope of work across our different product teams is drastically different. Working on core platform, like I do, versus working on video experience, versus podcasts. I mean, it's apples and oranges. And so it's really awesome that we have the flexibility to kind of make it work for us, while also having these larger goals that we know that, "Okay, this is what we need to work towards."
(21:12):
And I mean, like the saying we always hear in product, of, "Stay firm on the goal, but flexible on the process." And we've definitely been able to use that and leverage that in the way that we track against our goals.
Lenny (21:27):
Something else that a lot of people are always curious about is product review meetings and design review meetings. You talked about a couple of these meetings that you have, but do you have standard product review meetings where folks get together and just review stuff and progress? And if so, how do they work? Like who runs them, who comes to them, how do you make decisions, things like that?
Upasna Gautam (21:46):
We have multiple variations of those. Some are standing ceremonies of course, and some are ad-hoc. Again, it's really based on the work we're doing in whatever phase we're in. But when it comes to product review, and product discovery or design review meetings, in addition to my design lead I've made it a point to bring in my tech lead and engineers along for this product discovery ride, and that's definitely been a game-changer as well. When our engineers are able to understand our journalists' needs at the same level as we are, they're able to define the how to do it with so much greater clarity and precision. And so my tech lead is embedded also in our product discovery process, he joins our user testing sessions, and our design jams, and our editorial conversation planning sessions.
(22:37):
And it's helped him and the rest of our tech and engineering team become experts on the why are we doing this and what are we working towards, to better determine technical feasibility. And he's done an amazing job of also passing that knowledge down to the rest of our engineers on our team, so it's really like this mentality of getting that important feedback from our journalists, understanding their pain points and then sharing and teaching it across the team. And I think the key takeaway on that is it's so important to think of your engineers as partners and not just resources. And when they are embedded into the process right upfront, it makes the whole process in general more efficient.
Lenny (23:21):
So it sounds like that was maybe an evolution of the way the team works, as engineering has been looped into a lot of this early stuff more recently?
Upasna Gautam (23:30):
Totally, yeah. Recently-
Lenny (23:33):
Cool.
Upasna Gautam (23:33):
... meaning, I mean... Again, long game right? Because it's been a couple of years.
Lenny (23:39):
Got it. Going in a slightly different direction, I'm curious if there's any fun or unique traditions or rituals that the CNN product team has. These are always fun to hear about.
Upasna Gautam (23:51):
I'll be very honest, we are not one of the cool teams. The politics team and the breaking news teams have all these cool rituals and fun things that they do.
Lenny (24:02):
What kind of stuff do they do?
Upasna Gautam (24:03):
It's different also because they're usually in-person in the newsroom and I work remotely, and so... And actually most of my team works remotely. And so they have their rituals, but I will say one of the things that we started to do is... So onboarding teams has been a big goal of ours, and that we've slowly checked off the list over 2022. And any time we successfully onboard a team or launch a new feature, it's not anything crazy or fun, like there's only so much you can do when you work remotely. But we definitely make it a point to celebrate, and it's been hard to figure out ways to keep team morale up when you're all-remote. And it started with... We knew we needed to start doing something when we would have a big launch, and it was so anticlimactic.
(24:51):
And we literally hit publish and onboard onto like a politics page, and we were like, "Oh, okay, so I guess that's it." So one thing we started doing is sending like these gift boxes of like random tchotchkes and stuff that mean things to us from the whole year, and it's like just cheap little gag gifts and stuff that we send to each other. I have random stuff all over my desk, I don't even know if I can share some of it. So we try to make it a point to at least share and celebrate, and then when we're in-person we do too. But again, being remote, there's definitely a challenge there.
Lenny (25:32):
Are you ever able to get like a cameo from an Anderson Cooper, or someone else on-air to thank the teams? That feels like a cool feature potentially.
Upasna Gautam (25:41):
So one of my key stakeholders, she leads the video team at CNN, and she is a... We've had some discussions about doing a sizzler reel for our content management platform, since we're onboarding people and building new features. And there have been discussions with her about getting a celebrity to come and promote the product for us, so working on it.
Lenny (26:07):
Yeah, it feels like a missed opportunity, you've got so much talent around.
Upasna Gautam (26:11):
Totally.
Lenny (26:12):
This episode is brought to you by Vanta, helping you streamline your security compliance to accelerate growth. If your business stores any data in the cloud, then you've likely been asked or you're going to be asked about your SOC 2 compliance. SOC 2 is a way to prove your company's taking proper security measures to protect customer data, and builds trust with customers and partners, especially those with serious security requirements. Also if you want to sell to the enterprise, proving security is essential. SOC 2 can either open the door for bigger and better deals, or it can put your business on hold. If you don't have a SOC 2, there's a good chance you won't even get a seat at the table.
(26:52):
But getting a SOC to your port can be a huge burden, especially for startups. It's time-consuming, tedious, and expensive. Enter, Vanta. Over 3,000 fast-growing companies use Vanta to automate up to 90% of the work involved with SOC 2. Vanta can get you ready for security audits in weeks instead of months, less than a third of the time that it usually takes. For a limited time, Lenny's Podcast listeners get $1,000 off Vanta. Just go to Vanta.com/lenny, that's V-A-N-T-A.com/lenny to learn more and to claim your discount. Get started today. Coming back a little bit to the way y'all built product, I'm curious how you balance new product work and new features versus maintenance and bugs. Do you have kind of a... Is there like a philosophy at CNN of how much goes to bugs, maintenance versus new stuff, or is it per team and just, how do y'all think about that?
Upasna Gautam (27:45):
It's certainly team-specific, because again, the scope of work across teams really varies. But since my team's product is an entire platform, it's my job to ensure we're still clear on our goals because like I said, they may change on a week-by-week basis. One sprint might be high-priority feature development, in another sprint maybe we're focused on medium-priority optimizations and bug fixes. But we know that any time there's a critical incident in production, it also takes critical priority over everything else. So it's a balancing and juggling act that relies heavily on intuitive decision-making. But I will say we're also really fortunate to have a global, 24/7 editorial support team that we work really closely with.
(28:35):
So they are the ones who handle, troubleshoot, escalate incidents up to the relevant teams. There are a lot of layers to that protocol when a critical incident occurs. And so our editorial support team is that first layer of support, whereas my team might be the second or third depending on the level of severity and who it gets escalated to. So there's definitely a lot of processes in place, we're not always that first line of defense, which is actually... It alleviates a lot of stress, to know that we have an entire team around the clock globally dedicated just to that.
Lenny (29:12):
When you're talking about these incidents and moments it makes me wonder, is there a memory of just like a wild time of something happened in the news, or just like, "Oh man, we've got to get on top of this thing"? Is there like a memory that you think of like, "Wow, that was crazy"?
Upasna Gautam (29:26):
It's funny but also crazy and amazing, is... So our new content management platform, we've been building it for a while and stress testing it for a while. And politics and election season at CNN is Superbowl like times a hundred. And so we have to be all hands on deck, like all layers of support intact. And so we have also a lot of layers of fallback in case something happened, right? Like there's layers and layers of infrastructure fallback if CNN.com goes down, or another service goes down. And so it actually did happen a couple of years ago in the 2020 election, and one of the fallbacks at that time, because we were not...
(30:14):
We're still on our current content management platform, but we had our new one as we're building it as one of the levels of fall. And if X, Y, Z fails, then it goes to our current platform, and it did. And so that's actually happened, where our new platform saved the day even though it wasn't fully ready. But that just goes to show we think about that kind of stuff like in granular detail, when we think about everything that could possibly go wrong. Because it has happened, and it will happen, and it does go wrong. So that was kind of cool, it was validation to know that the platform we have is really stable, and strong, and secure, that it was a fallback for the election.
Lenny (31:03):
Okay, and it must have felt good, it feels like a promotion material right there that your work-in-progress system saved the day.
Upasna Gautam (31:10):
Yeah, I agree.
Lenny (31:12):
You talked about how you have like these breaking news dress rehearsals. I just noted that, and I thought it would be cool to just revisit that briefly. Like, how does that work? You just get the team together, and like, "Here's a news story that just broke. What do we do?" Like, how does that work?
Upasna Gautam (31:27):
It is scripted, right. So we can only get so close to the real thing. But one thing we do is we script everything, like the teams and the players that we need involved in it, what the incident is. And it usually starts when breaking news occurs with an email, the news-gathering team sends an email to our writers and our producers. And then from there it goes out all the places it needs to go. There's a video that needs to be created, there's an article that needs to be written. Again, the TV side I have no insight into, it's like a foreign land to me. But as far as the digital scope goes, there's a lot of work that has to be done. Even things like photo and imagery, we have a whole team dedicated just to selecting photos.
(32:11):
The photo desk is very involved with that process. And so that is all scripted out, and so we say, "Okay, here's the news, here's how it's going to break," and then we run it. And so we use interpersonal communication tools at work of course, email, and we run the whole thing from the minute the email is sent to... And of course since we're testing the platform with this breaking news dress rehearsal, to the minute you hit publish on that page. And there's a lot of stuff that goes on in there, and it all happens in the span of minutes. And so while that is happening, while that dress rehearsal is happening, we have our engineers and our editorial support team on hand as well. So they're observing what's happening while it's usually me and one of our editorial stakeholders and leads facilitating the actual rehearsal part.
(33:02):
And you know, getting user feedback on, "Okay, did something break, did everything work as it was supposed to work?" And also allows us to understand like how far we can go with stress testing different features on our system. So each one is different, but it's a crazy amount of stuff and information you can gather in such a short span of time. Because if it cannot serve the needs of breaking news, then it's useless. So it's a lot of work that goes into it for this three-minute event.
Lenny (33:35):
That is cool. It feels like just a cool tactic you could use anywhere, and that's a good segue to the next question I had, is just having built product at CNN and seeing how the product team works, what is it that you think you'll take with you to future product teams and future companies if you ever move on to anything else?
Upasna Gautam (33:53):
So I of course can't speak for the entire scene and product team, but I can speak for myself and my specific team. In order to stay competitive in our modern news landscape, building this content management platform and the technology behind it has taught us how to enable rapid development and integration of new features and workflows. And we've been able to quickly test hypotheses while reducing risk, and again, time is of the essence when it comes to breaking news. And when you layer that with a very complex content management technology, there's a lot of moving parts. And we've been able to do that successfully, and it's pretty amazing. And because of that we've developed, I think, this unique skill of high agency under high pressure.
(34:49):
And I really think that that skill or combination of skills is our superpower, and that is something you can take anywhere, that is something that is an asset to any product development team.
Lenny (35:03):
Let's circle back to our original topic about mindfulness and meditation. Other than just living through it and either becoming a meditation expert or having worked at a company like CNN that has a lot of this, is there any, I don't know, tactic you could share, something that someone could take tomorrow and be like, "Okay, I'm going to get better at dealing with crazy, unexpected events," based on the experience you've had?
Upasna Gautam (35:25):
Two parts to this. So one, I would be remiss as a meditation educator if I didn't say that there is no substitution for meditation. So just do it, it takes a long time, and it's a lifelong work-in-progress. But the good thing is that it also... Like the more you do it and consistently you do it, it compounds over time. Okay, if you think of any job description for a product manager it's mostly the same core stuff. You need to be able to lead a team without having authority, you need to have great communication skills, you need to be able to bribe in ambiguity, you need to be able to work with a lot of different people on the technical side and business side, all of the stuff that we hear all the time right?
[NEW_PARAGRAPH]But how do you actually become better at those things? Like, there's only so much you can gain from reading a book. To me it's either A, you've got to go do it, and B, meditation has helped so much because of the clarity of mind and clarity of thinking you're able to cultivate because of it, especially when it comes to communication. And this comes back to another tactic I think. So meditation is one, you can't get around it. It's a very, very powerful tool, I will die on that hill. But thinking about workplace tactics, communication is so essential. When I started at CNN it was a very new chapter for me, it's my first official product management role after working a decade in tech, in data and search infrastructure.
(36:57):
And it was really scary to make that change so far into my career. But when I asked my boss why he took such a big chance on me he said, "It's because of your communication skills and relationship-building skills, and that I've seen you in a room where engineers listen to you and what you have to say, and you listen to them." And he was like, "That in itself is really, really hard to teach." And I was like, "Okay, yeah, I can do that." So when I think about what communication means I also attach that to mindfulness. Like mindful communication is so critical for successful product management, no matter what type of product environment you're in. And it means being like deeply aware of the conversation you're having.
(37:43):
And when I'm having this conversation with you, I'm only having this conversation with you. When I'm talking to my design lead, I'm only talking to my design lead. When one of my journalists is venting because this feature is not working the way we told them it was going to, I am shutting my mouth and I'm listening to them vent, and then I'm extracting what the root cause of the problem is. And I think the takeaway and the tactic is that goes back to exactly what we talked about in the beginning is the ability to pause before reacting is the key to mindful communication and being a successful product manager. I think a lot of times we are taught to have all the answers, or we're expected to have all of the answers.
(38:27):
And people assume we have all of the answers so it's a really frustrating, sometimes, place to be in. But, if you listen and you know where to go to get the answers, that in itself is like a tremendous place to be. So I think the power of meditation, being able to pause before reacting lets you do things like conversate in the language of the listener. So when I'm talking to my journalists I'm not using technical terms or like content management technology terms. They have a whole different vocabulary that they use, they have shortcuts that they have lingo for in our content management system. They call things nicknames, and so you have to speak many different languages as a product manager. And if there's one thing that learning and teaching mindfulness has strengthened, it is that communication, yes, it's very important.
(39:24):
How do you become an effective communicator? I think a lot of times we think of speaking articulately first and foremost, or we think about writing well, which those two are really, really important things. But those can't be effective for us as product leaders if we're not listening, so I think listening and being able to converse in the language of the listener is the utmost importance. And how do you do that in your day-to-day? It's like, okay, if you're having a conversation with your customer are you actually listening to what they say, or are you going in with your own assumptions? Because maybe you're a user of the product. And it was very interesting, because I actually started writing freelance for CNN this past year.
(40:12):
And I was like, "Oh, okay, I'm a user now." And no I'm not, I'm not going to say that it helped me understand their pain points so much more and where they're coming from in a whole different light. But again, I am merely a proxy, I'm not actually the user. What they do is still drastically different. And so when having those customer interactions and stakeholder interactions, the priority should be to listen. And I think that is one of the most important things I've learned, and it's also helped build trust and respect between a previously fragmented structure where product and editorial didn't talk to each other, and now we're a unified partnership.
Lenny (41:00):
Oh, I love that. I love the reminder that a lot of communication is incredibly important for product managers, and so much of it is not actually you talking, it's you being really good at listening, and that makes you a better communicator. I imagine some people listening to this are going to be like, "Yeah, meditation, I should be doing that." What's like one thing someone could do to move forward on the path to starting to meditate? Is there a resource to recommend, a tip of just starting to do something there?
Upasna Gautam (41:27):
Totally. I think when people think of meditation, you immediately think of sitting on a mediation cushion like a monk for an hour. And that doesn't have to be true, especially if you're just starting. And there's also of course social media has commercialized what meditation is a lot as well. But at its core, all it is is being deeply aware of the present moment. So I always tell people who are for example like really busy moms who have no time in the morning for an hour-long meditation is, "Okay, take something in your day that you do every single day. You brush your teeth every morning, right? Okay, take brushing your teeth. Can you brush your teeth and just brush your teeth? And when you're brushing your teeth you are engaging all of your senses, and being fully present and aware of how it feels, how it smells, how it sounds."
(42:27):
That's two, three minutes of your day. That's meditation, and I think it's an amazing way and an easy way... Oh, sorry, not easy. Simple, not easy way, always, to think about what meditation actually is. Is like, instead of like having to uproot your whole life and the way you live to bring meditation in, think about what you already do every day and how you can just be more present, like fully present. And that's one of the core examples I give, is start with brushing your teeth and just brush your teeth. There's an old app I've been using for a long time if you're into that, I stopped using it recently but it's still amazing. It's called Insight Timer, the free version is amazing. It started as like a single-frame app probably about 10 years ago, and it's turned into this...
(43:18):
They've done amazing things with that product. So that's what I recommend, but again, you don't... I think, again, when people have a vision of meditation in their mind they're like, "Well I need these tools, and I need these resources, and I need these things, and I need knowledge." You don't need anything, you need five minutes and yourself, and that's it.
Lenny (43:37):
Amazing. I imagine many people listening to this coming into thinking, "I'm going to learn about CNN and how they build product," and then get a free meditation lesson. What a bonus, that was awesome. I'm going to be brushing my teeth very mindfully today-
Upasna Gautam (43:49):
Love it.
Lenny (43:49):
... my takeaway.
Upasna Gautam (43:50):
Love it.
Lenny (43:52):
Final question, around something that I know is important to you, that is basically there's this growing shift of product thinking in the news industry at large. And I know that's something that you're passionate about and something you're trying to create, is just to kind of move the media industry and the news industry toward more product thinking. So I'd love for you to just talk about what you're doing there, what's happening there, and then maybe if there's anything people could do to help in that effort.
Upasna Gautam (44:16):
Compared to the rest of product management as a discipline and the tech industry, product management in news is still in its, I will say infancy. And that's just because it hasn't been an integrated role for as long as it has been in big tech. But it is starting to become more and more not just prominent now, but people are realizing the value and power of it because especially in smaller newsrooms... I mean, CNN, places like The New York Times, The Washington Post, we have great, embedded, strong product teams. But that is not the case for the majority of newsrooms across the country and the world. Newsrooms are strapped for resources, they are strapped in all resources, including financial resources.
(45:07):
And so first, bringing in product and tech talent is expensive, and that in itself has forced editorial staff and journalists to take on other jobs that they never signed up for. And so they've had to learn how to do things product management, and engineering, and coding hacks, because there was nobody else to do it. And so it's interesting because a lot of times when you talk to editors and journalists, they're doing so many other things other than just their reporting of the news, right? They've had to take on other roles because of those restraints in the newsroom. And so there was a group established and a community established during the pandemic called the News Product Alliance. And there was like a realization occurring all at the same time that, "Wow, there's a lot of us doing this work.
[NEW_PARAGRAPH]"Like, what do we call it? Is this product management?" And it was, it's product management at so many different levels. And so the News Product Alliance was formed during the pandemic in 2020 I believe by several media and news executives, who had been there and have seen people in their newsrooms do that. And the goal of it is to increase the awareness and education of product thinking and product management in newsrooms, while also increasing the diversity of thought and the diversity of people in those positions as well. And making the resources more readily available, especially for those smaller newsrooms that don't have the money to hire tech talent. And that in itself has...
(46:56):
So that group, the News Product Alliance, has grown dramatically in the past three years since I've been a part of it, since the beginning. And we regularly produce the resources that are catered... Product management resources that are catered to working in a newsroom, because it is different, it is very unique. But there are of course frameworks and processes that are still relevant, right? Like editors who have been cobbling together how to make this thing that they want, but hey, maybe this PRD framework will help you, just to keep it on track. So these very simple, like rudimentary types of things have helped them so much. And so last year we kicked off a mentorship network in which we had about 400 people apply.
(47:46):
We accepted 150 mentees from across the world, and matched them with 50 mentors from different newsrooms across the world in leadership positions. And each mentee defined a goal that they wanted to work on, and all of course having to do with product management. And some of them were creating a product management role for themselves in the newsroom. Some of it was creating a product management practice, maybe they were given the title of product manager and said, "Okay, you can hire a couple of people." But it was all on them, and they had no idea what to do, right? And so some of it, it's across the board, and it's amazing to see people doing this from scratch who never in a million years thought they'd walk into it.
(48:32):
You know, they're not coming from big tech, they don't have startup backgrounds. They had journalism degrees from around the world, and they're learning how to do product, and build... Not just learning how to do it, they're building product practices, they're actually building and developing products and features, and they're creating more leaders in this space as well, and across their newsrooms to empower each other. So it's been really amazing to see, and it's the most valuable professional organization I've been a part of just because it is so niche that talking about product management is always fun. But when you talk about it at a level that specific, it becomes even more valuable.
Lenny (49:16):
That is some really impactful product work. Where can people find that if they want to maybe participate, maybe apply if you're doing another cohort in the future?
Upasna Gautam (49:24):
Go to Newsproduct.org, there is a very active Slack group with a couple thousand people in it, a very active and popular job board as well. And you just have to submit an application on the website... A form, sorry, on the website to join the Slack, and ten you'll get an invitation to join the Slack. And then you'll have all of the resources at your fingertips, it's very low barrier to entry, and we want everyone and everyone who is interested in the intersection of news and product to be a part of it. And the cool thing about it is like I mentioned, it's a global network. We have people from the biggest newsrooms across the world, to all of the regional ones, to even big tech, one of my fellow board members was doing news at Twitter.
(50:10):
One was working on the Google News Initiative. So it's a really, really awesome group of people, and everyone is so hungry and passionate about sharing and paying it forward.
Lenny (50:23):
We'll put a link to this in the show notes. One last question, and what kind of people are you looking for? Who should apply, if they're listening?
Upasna Gautam (50:29):
If you are interested in working in news and have a product background, or the inverse of that, if you work in news and you're interested in breaking into product. So either side of the coin or any combination of that, news media, product technology, even... We have a lot of audience development, and analytics, and data science folks in there too. It's just an amazing community for knowledge sharing in tech and news, so there will be a fit for you somewhere, or to learn something, or at the very least to meet other really amazing people.
Lenny (51:07):
Well, with that we've reached our very exciting lightning round. I've got five questions for you, and are you ready?
Upasna Gautam (51:14):
I'm ready.
Lenny (51:16):
All right. What are two or three books that you recommend most to other people, or that you've recommended most?
Upasna Gautam (51:21):
One, Mindfulness in Plain English. Two, How To Win Friends and Influence People. I have to attribute a lot of my communication skills to my dad forcing me to read that book when I was like 10 years old, and-
Lenny (51:36):
Wow, 10 years old. Intense.
Upasna Gautam (51:39):
He was an engineer, and they were in their very beginning phases of introducing... Well, at that time there was no product, but product-type stuff into his engineering practice. And so he had to read the book and was like, "You need to read this book." So I never forgot about it. And then the third one is actually, it's not a book, but it's an article that I think is still very powerful and relevant to this day. It's The New Product Development Game, published by Harvard Business Review in 1986. And it looks at a really different approach, one that I resonate a lot with because it's a lot along the lines of how we work at CNN, around rapid development, and time and flexibility being like key anchors of successful product development. So, I threw that in there as well.
Lenny (52:29):
Favorite recent movie or TV show? And it can't be White Lotus.
Upasna Gautam (52:32):
Okay, I haven't even seen that show.
Lenny (52:34):
Okay, great. That's come up so many times, we've got to not allow it anymore.
Upasna Gautam (52:38):
TV show is a toss up between The Mandalorian and Ted Lasso. I know it's not very new, but I don't watch tons and tons of TV, and I usually find like the few that I latch onto, and then I get obsessed with, and then I've got to take a break for a while. So, those are my last two obsessions. Movie is Everything Everywhere All At Once, the last amazing one that really, really struck a chord with me.
Lenny (53:02):
If you like Mandalorian check out Andor, it's incredible.
Upasna Gautam (53:05):
Oh yeah, it's good too.
Lenny (53:06):
It's like the best Star Wars thing. Okay, you've seen it. Okay, great, you're on it.
Upasna Gautam (53:09):
I still love Mandalorian more, I do like that one too.
Lenny (53:11):
Wow.
Upasna Gautam (53:12):
My husband is obsessed.
Lenny (53:15):
Okay, okay. Wow, contrarian. Favorite interview question that you like to ask candidates?
Upasna Gautam (53:21):
What's something that would not exist without your initiative?
Lenny (53:28):
Mm-hmm. And what do you look for in an answer that's a sign that this is someone you may want to hire?
Upasna Gautam (53:31):
The whole point of the question is like, do you have and can you exhibit high agency? And especially again, working in news it's so important. And so there's not like a specific answer, I think the ability to actually define something specific and tangible in itself is a really, really, really good sign. I think a lot of people definitely get startled by that question sometimes, because it requires you to kind of have to know what it is that you put on the table, right? So yeah, it's different every single time. But if they can define something out of that question, it's usually a positive sign.
Lenny (54:15):
Cool, thanks for sharing that additional detail. Next question, what's something relatively minor you've changed in your product development process at CNN or on your team specifically that's had a tremendous impact on your ability to execute?
Upasna Gautam (54:29):
Bridging the gap between product and editorial, that mutual trust and respect has had an outsized impact on our success as a high-performing team.
Lenny (54:38):
Sadly not something other people can use, but that's cool to know. Then we'll have to hire some journalists now, I think, to take advantage of that learning.
Upasna Gautam (54:46):
I can add onto that to make it relevant for others-
Lenny (54:50):
Sure.
Upasna Gautam (54:50):
... which is, it just goes back to, there's no substitute for having those direct conversations with your customers and your users. And it's like, when you understand that the assumptions you make are not one to one, or ever going to be one to one with their actual feedback. And developing that line of communication with your users and your customers is of utmost importance, I think that in itself is the key takeaway. It's like, how do you bridge the gap between collecting that feedback, having those conversations. Like, how far are you from your users, how frequently are you having conversations, how consistently are you having conversations? And I always think the more frequently and the more consistently, and earlier on in the process that you're having those conversations, the better.
Lenny (55:44):
Final question, maybe you already answered this. What's the most crazy or most memorable story from working at CNN?
Upasna Gautam (55:51):
Every election season is absolutely crazy in the best way possible. It's incredible to see our democracy in action, and watch history unfold. And while that's happening, using the platform you had a direct hand in building, and it's never lost on me that my work impacts the world every single day. And on the crazy, frustrating, stressful days, that is what serves as my anchor.
Lenny (56:19):
Awesome. Plus, this was amazing, I learned how to brush my teeth more mindfully, about elections, downtime, Trump, all these things. Final two questions, where can folks find you online if they want to reach out and learn more, and how can listeners be useful to you?
Upasna Gautam (56:34):
It's very easy to find me. Online I'm pretty active on Twitter and Instagram. I recently became an amateur content creator, so I share lots of stuff here and there on social. So any social platform... Well not any, only on Twitter, LinkedIn and Instagram. So any of those three is good, and I always love to hear feedback on stuff that resonated and made sense, and the stuff that there are further questions on. Always love having conversations around that. So yeah, DMs are always open.
Lenny (57:10):
I know we'll link to this in the show notes, but just, what's your handle on these networks?
Upasna Gautam (57:12):
It's my first and last name, very creative. I thought about it all by myself.
Lenny (57:16):
Awesome. And then I don't know if you answered the second question, how can listeners be useful to you?
Upasna Gautam (57:21):
It's the feedback, right? Like I love to hear what you found valuable, what helped you, what's a tactic that you took away and employed that helped you, things that made sense, things that didn't make sense, what you'd like to hear more about, any specific topic that would be valuable to do a deeper dive on. All of those things are very valuable to me.
Lenny (57:42):
Amazing. Again, thank you for being here, and adios.
Upasna Gautam (57:46):
Thank you.
Lenny (57:49):
Thank you so much for listening. If you found this valuable you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also please consider giving us a rating or leaving a review, as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at Lennyspodcast.com. See you in the next episode.

---

## An inside look at how Miro builds product | Varun Parmar (CPO of Miro)
**Guest:** Varun Parmar  
**Published:** 2023-04-20  
**YouTube:** https://www.youtube.com/watch?v=furNg4njlsg  
**Tags:** growth, acquisition, metrics, okrs, roadmap, analytics, funnel, pricing, hiring, culture  

# An inside look at how Miro builds product | Varun Parmar (CPO of Miro)

## Transcript

Varun Parmar (00:00:00):
Every single day, every single time somebody is pushing your code to production and you're releasing a feature or an enhancement, you are making the product better or you're making the product worse, but the products never remain same. So with every release that your competitor is making and every release that you're making, you are either making chess points, moves against them, positive points, or you're going negative. I think that framework, it actually drives an insane amount of clarity in terms of what you're doing and what the impact is going to be.

Lenny (00:00:33):
Welcome to Lenny's Podcast, where I interview world-class product leaders and growth experts to learn from their hard-won experiences building and growing today's most successful products. Today my guest is Varun Parmar. Varun is chief product Officer at Miro, and prior to Miro, he was senior vice president and chief product officer at Box. As I share with Varun at the start of our chat, I've always been really curious about the product culture at Miro, partly because everyone I've ever met from Miro has been super interesting and super smart, and partly because they've been able to grow as a business and a product in an incredibly competitive market.

(00:01:07):
In our conversation, we get really deep into the product values and principles at Miro, their product development process, how Varun approaches competitive threats, how a bimonthly company-wide product demo ritual led to saving months of engineering work on a feature, plus insights into how Miro got started, how they grow today, and what their product team has learned about working with a large sales org. Varun is amazing, I learned a lot, and I hope you find it as interesting as I did. With that, I bring you Varun Parmar after a short word from our sponsors.

(00:01:39):
Today's episode is brought to you by Miro, an online collaborative whiteboard that's designed specifically for teams like yours. I have a quick request. Head on over to my Miro board at miro.com/lenny and let me know which guests you'd want me to have on this year. I've already gotten a bunch of great suggestions, which you'll see when you go there, so just keep it coming. While you're on the Miro board, I encourage you to play around with the tool. It's a great shared space to capture ideas, get feedback, and collaborate with your colleagues on anything that you're working on. For example, with Miro, you can plan out next quarter's entire product strategy. You can start by brainstorming, using sticky notes, live reactions, a voting tool, even an estimation app to scope out your team's sprints. Then your whole distributed team can come together around wire frames, draw ideas with a pen tool, and then put full mocks right into the Miro board.

(00:02:29):
With one of Miro's ready-made templates, you can go from discovery and research to product roadmaps to customer journey flows to final mocks, all in Miro. Head on over to miro.com/lenny to leave your suggestions. That's M-I-R-O.com/lenny. This episode is brought to you by Braintrust, where the world's most innovative companies go to find talent fast so that they can innovate faster. Let's be honest, it's a lot of work to build a company and if you want to stay ahead of the game, you need to be able to hire the right talent quickly and confidently. Braintrust is the first decentralized talent network where you can find, hire and manage high quality contractors in engineering, design and product for a fraction of the cost of agencies. Braintrust charges a flat rate of only 10%, unlike agency fees of up to 70%, so you can make your budget go four times further.

(00:03:22):
Plus they're the only network that takes 0% of what the talent makes, so they're able to attract and retain the world's best tech talent. Take it from DoorDash, Airbnb, Plaid, and hundreds of other high growth startups that have shaved their hiring process from months to weeks at less than a quarter of the cost by hiring through Braintrust network of 20,000 high quality vetted candidates ready to work. Whether you're looking to fill in gaps, upskill your staff or build a team for that dream project that finally got funded, contact Braintrust and you'll get matched with three candidates in just 48 hours. Visit useBraintrust.com/lenny or find them in my show notes for today's episode. That's usebraintrust.com/lenny for when you need talent yesterday. Varun, welcome to the podcast.

Varun Parmar (00:04:10):
Thank you, Lenny. So excited to be here. Thanks for having me.

Lenny (00:04:13):
I'm really excited to have you here. I've been looking forward to having a chance to dig into Miro's product culture and the way Miro works for a while. We've actually had a few guests, ex-Miro... Mironeers, is that what you call yourselves?

Varun Parmar (00:04:25):
Yes, Mironeers.

Lenny (00:04:27):
Okay. Mironeers. So we had Elena Verna on the podcast, who's amazing, and Barbara who I think worked in marketing and everyone I've always met from Miro has been just really smart and really interesting and it just feels like you guys have a really interesting product culture that I haven't felt like has been shared a lot, and so I have a bunch of stuff I want to dig into there. One question I have at the bat, you guys have a really interesting history and specifically the way your company's structured, which is that you're collocated in Amsterdam and San Francisco. First of all, is that correct?

Varun Parmar (00:05:00):
The company is a global company, so we've got 12 different hubs. We have multiple offices in US, four different offices, and then multiple hubs in Europe as well, and presence in AsiaPac as well. I think by now we have a global footprint, yeah.

Lenny (00:05:17):
Got it. A question I wanted to ask off the bat is just how has that cross-cultural approach to product teams impacted the way that you guys built product and the way the company operates?

Varun Parmar (00:05:30):
The one thing that's really interesting, Lenny, around the way Miro is set up is that our product organization is actually based in Europe and our go-to-market organization is worldwide. Our product management team, our designers, our engineers are located across three different hubs in Europe. What that sort of leads to is a couple of practices that we have as part of our culture. The first one is practicing empathy to gain insights. It's not just practicing empathy in terms of customers and figuring out what customer pain points and problems we can solve, but given our distributed nature in terms of having a global footprint and a lot of our go to market teams, folks in sales and marketing and customer success are in different continents or geographies, we have to make sure that we actually practice that internally. When we are interacting with folks, let's say in San Francisco, and those folks are out there meeting some of our large customers and stuff, how do we, in the product organization, understand their perspective, and bring that perspective into how we design, prioritize and build products? I think that's one thing that's unique.

(00:06:43):
I would say the other thing that's less to do with the location, but I think is sort of the core cultural value or philosophy that Andre, who's the founder and CEO has instilled in all of us, is practicing teamwork, how do we actually come together as a team, and bring down the silos that might exist across functions? I'll talk a little bit around how we are structured in the product organization so that it's a cross-functional perspective we bring to everything that we're doing because we believe the best work happens when we bring different diverse perspectives to the problem and then co-create the outcome that the customer is looking for.

Lenny (00:07:20):
I want to pull on these threads actually real quick. You talked about this value of empathy and the importance of having empathy across... because you guys are located in different locations and have different cultures, and also this idea of teamwork. What's something that you've done that helps you do that, either build empathy and maintain empathy across teams or make sure that people work in teams and not like, "Hey, there's this other team over there doing something else"?

Varun Parmar (00:07:45):
One of the most powerful things that I've seen work is the questions that you ask, the questions that you ask when you're going through product review or you are going to sit down and talk to someone and trying to understand why did they prioritize something over the other and was it something that was done through interactions they've had with folks internally or externally? I think it's the set of questions to ask in terms of how did they get to where they are today and was it informed by understanding of the insights that collectively the organization has? Was it informed by their understanding of where the market is evolving, where the competition is going.

(00:08:31):
Was it informed through the series of insights they have, either through inbound feedback that's coming through our different channels where customers are giving feedback or some outbound interactions that they've had? I think just trying to double click and getting to the details in terms of what insight led them to recommend certain things or make a left turn or a right turn is where I think is the most powerful way to make sure that those things are informed through practicing empathy internally and externally.

Lenny (00:08:59):
Got it. There's this kind of cultural value of just assuming good intention and asking questions to understand where someone came from. I don't know if you'll have something off the top of your head, but is there a story or an example of that comes to mind where that was done well or not done well, I don't know, in something you recently were building?

Varun Parmar (00:09:16):
Maybe there are certain things, for example, anytime we're trying to build a new experience, one of the approach we want to take is very quickly validate that our original hypothesis, is that sound or not. We are big fans of the Design Sprint framework, what Jake Knapp has done I think is really amazing. In a short five-day window, you can get a small set of people to quickly mock up a concept, convert it into some sort of a prototype and then go out there and get some sort of a validation. Oftentimes when we are working on some of these new things, we have our product teams that are focused on zero to one initiatives, run this five-day initiative, and at the end of it we say, "Oh, this is great. Who did you get insight from?" There's a capability that we recently released, it's called Miro Talktrack, which essentially allows you to asynchronously do asynchronous collaboration by recording audio video on top of a Miro board.

(00:10:16):
We had two fundamental choices we could make. One, we could go down the path of what everyone's doing where you could do a screen recording and then spit out a series of videos, like pixels being captured. Or what we did was we actually went down a different path and the path that we went down was we basically synchronized the movement of the board. Let's say Lenny's presenting a board, some template he's created in terms of best practices for PMs, but he wants to have some sort of a talk track on top of it, an audio video feed. What we are doing is we're actually capturing the movement of the board that Lenny's going through along with the video talk track that's on top. The reason why we did that was because we had an insight that came through some of our interviews.

(00:10:56):
What our users want to do is they want to use Miro for collaboration. While communication is an important aspect of how teams come together, where we believe our sweet spot is that we want people to use Miro for collaboration. By making sure that they could actually use a video recording and while the video recording is playing, they could add in a sticky note, they could add in a comment, they could actually give a reaction. We were able to develop this insight by practicing empathy as part of the Design Sprint framework when we went and started to show our original concept and we walled and built on top of that.

Lenny (00:11:31):
That is a really cool story. That came out of this Sprint framework, these five-day sprint approach.

Varun Parmar (00:11:36):
Yes, that's right. Yeah.

Lenny (00:11:37):
That is cool. I got to have that guy on this podcast. Jake Knapp, you said, right?

Varun Parmar (00:11:41):
Yes, yes, yes. I can text him right now and I can make the introductions, yes.

Lenny (00:11:45):
Let's pull him right into this podcast live, tell us how the Sprint process works. That is awesome. This connects a little bit to another question I wanted to ask around the top is, you guys are in a really competitive space and it feels like Miro was very early in online collaborative whiteboarding space and then I think during COVID it just became huge, with the remote work exploding. Like, "Holy shit, everyone needs this immediately." Over the years, many companies have come into the space that you are all in and it feels like Miro continues to do extremely well. I remember when Figma launched FigJam, there was a lot of just like, "Miro's dead. Figma's getting into the space, they're juggernaut, game over." Clearly that's not been the case and it just feels like, I don't know what it is internally that you all do that continues to allow you to compete and continue to innovate in the space. I'm curious just like is there something to how Miro approaches competition and also just, I don't know, the way they approach these sorts of challenges that is unique or interesting that you can share?

Varun Parmar (00:12:45):
If you look at the mission for Miro, we empower teams to create the next big thing and our focus is to enable teams that are innovating, and generally innovation happens at the intersection of a bunch of cross-functional folks coming together. Like we discussed, folks in product management or design or engineering or analytics or product marketing or research. What we find, Lenny, is that there are a lot of tools out there and those tools are generally sort of focused on a particular persona and maybe they're trying to solve the needs of a designer and a designer has a workflow that they're trying to do and they're using a specific tool and they sit at the adjacency of extending that core use case. The fundamental value that Miro provides is that we enable teams. I think what's unique about our product, and we can talk about the capabilities and roadmaps and use cases that we are investing in and we already have as part of the product, is that we take a team-centric lens.

(00:13:50):
So we're not saying, "Hey, we're building a tool that just works for designers," or "Hey, we're building a tool that just works for engineers." Because we fundamentally believe that innovation happens when cross-functional teams come together. When you look at the problem through that lens, you realize that you have to actually architect your solution. You have to think about the use cases and you have to go and prioritize certain experiences that are different and our customers see value in that, right? I think that's probably one sort of big macro aspect of how we think about our capabilities and products and why our customers think of us differently. I'd say that's say one point.

(00:14:27):
I think the second thing is Miro is actually used obviously by teams that are creating these innovative products and we actually have broad applicability across industries and verticals. While some tools might be hyper-focused on digital experiences and Miro's has great offerings there in terms of core capabilities, what we find is that Miro is used equally by companies in manufacturing, by companies in healthcare, by companies in architecture and engineering and construction functions, by companies that are in aerospace, governmental agencies and medical agencies and so on and so forth. I think the platform is actually much more agnostic in terms of its capabilities and what we offer that actually makes it more accessible and appealing to organizations that want to go beyond just digital experiences.

(00:15:26):
Then I would say finally there are capabilities that are available very, very uniquely to Miro that are valued by our users. That again is a big reason people come to Miro. For example, if Lenny's trying to conduct a big workshop with a bunch of product folks and he wants to facilitate that workshop and wants to have certain folks focus on one part of the board and while others focus on the other part, then there are some advanced capabilities that enable certain use cases like workshops. Or if you want to use Miro for some team rituals or from some agile practices, there are core set of capabilities that you could use the product for that are missing in some of the other capabilities. I would say a combination of all of those three things continue to drive differentiation. I would say on top of that, we are a big fan of our community and we believe that community love is what drives us. That's the fuel that keeps us going every single day.

Lenny (00:16:31):
Awesome. Just to summarize and I was taking notes as you're chatting, just thinking about what allows you all to continue to do well in the market, considering all the competition constantly coming at you. One, as you mentioned, just there's kind of like a innate multi-functional architecture which is hard for someone to copy if they weren't built from that without the start. Two, it sounds like you are focusing on a wide spectrum of personas and it's not just tech employees basically. Also, just there's specific features that end up being really important that maybe people have a hard time building and then this last piece of the community. Awesome.

Varun Parmar (00:17:08):
Yep.

Lenny (00:17:09):
Let's dig into the product team a little bit and understand how you all build product and structure product team. How many PMs are there at Miro? Then just broadly, how many employees, just to give people a set of, little bit of context?

Varun Parmar (00:17:20):
Give or take about 1,800 employees at Miro globally across all of the 12 hubs, and specifically in terms of the number of product managers, there are over 450 PMs in the team.

Lenny (00:17:34):
Then how's the product team structured? Is it like outcome oriented? Is it product area oriented? Is it user persona oriented? Is it something else? How do you think about the structure of the product team?

Varun Parmar (00:17:46):
Yeah, so I would say it's maybe a hybrid structure that we have, but the foundation of the team setup is around persona. We have what we refer to as streams, some companies refer to as domains, but essentially it's a set of individuals that are focused on solving the problems for a key persona. Just to give you an example, we have a stream that's focused on enterprise, and in enterprise we are looking at the IT admin persona, we're looking at the security persona or the compliance persona. There are a set of folks who are creating a roadmap and innovating for that audience. There's another stream which is called platform where we are going after the developer install base, folks that want to use Miro as a platform and build apps that they can actually make available either on the marketplace for everyone to use or they could be developers that are inside of a large organization and they're trying to integrate Miro with their specific use cases and workflows and business systems. That's another sort of stream that's focused on that, and there are a couple of other streams like that.

(00:18:53):
Then finally there are some just horizontal sort of streams, if you will. We have a big focus given that we are a PLG-led company around growth and self-serve business. We've got a stream that's actually focused on our core internal infrastructure. We've got a stream that's actually focused on data science that's doing all of the magic that we started to release in terms of Miro AI, et cetera, et cetera. I would say it's a combination of those. At the heart of it is we are focused on personas and we are sort of aligning people around solving problems and creating value for that persona.

Lenny (00:19:24):
That is really interesting. One of the downsides of a persona-based approach I imagine is that features keep getting added that solve that user's pain points. What have you learned about keeping the product consistent and having a holistic perspective on the experience? How do you address Those challenges?

Varun Parmar (00:19:43):
Architecturally, there are two sort of things that we have done that allow us to not pigeonhole ourselves into that specific way of working. I completely agree with you, you could lead to that. The first one is actually when we think about the product org, we call our org, it's called AMPED, A-M-P-E-D. This is actually going back to our earlier point, Lenny, we had around what's unique about the product culture, what's unique about Miro, and we talked about teams coming together, removing barriers or silos cross-functionally. AMPED stands for analytics, marketing, product, engineering and design. And everything that we do in the product org, when we say the product org, we actually don't meet product managers. We actually don't mean product managers, designers and engineers. What we mean by product org in Miro is this AMPED function. By having this cross-functional representation where product marketing team is deeply, deeply embedded inside of each of these streams, what we do is that we have different perspectives that come in where they say, "Oh, wait a second, did you think about the end user experience?"

(00:20:49):
If you think about the end user experience, you know have someone on the team that says, "Wait a second, did you actually think about the enterprise requirements or what's needed in the largest corporation?" I think the unique setup of bringing these cross-functional folks allows us to sort of course correct. The second thing is the ways of working that we have. We have these product reviews that happen. We generally classify anything that we are doing in terms of its complexity around a small, medium or high complexity, and anything that's being worked on is actually being shared with the entire organization. If it's something that's small to medium, it's actually shared with the entire product org. In fact, if you are non-product, you can actually subscribe to that Slack channel as well. Everybody sees what the product org is working on, everybody sees what the core hypothesis is, "What is the solution for that, what is the proposed design for it, how are we thinking about the capabilities?"

(00:21:49):
Then anything that's big actually goes through a formal process like a product review where there's a meeting and a bunch of us are in there and it's up to us, including the product leaders, to basically make sure that we are connecting the dots in terms of having a much more holistic perspective. I would say lastly, as Miro has sort of scaled the spectrum of companies all the way from a team that might have two or three people and might be taking out their credit card and using Miro for their own team all the way to a large corporation that might have 50,000, 80,000 employees, all of them are using Miro. We've come to realize that at some point the deep enterprise requirements need to be encapsulated in a set of requirements or best practices and we need to make sure that those get democratized across all of the feature teams.

(00:22:36):
When I'm thinking about building a new feature, I have a checklist in front of me where I can say, "Here are the 10 things that I need to think of that I need to incorporate early on in my thinking in the architecture, in the definition of the process, so that it doesn't come downstream." I would say that's an area where we're still working on and more recently we put more focus and energy and there's a product manager who's now leading that particular charter.

Lenny (00:22:57):
I love all these details. This AMPED structure, I love that. There's analytics, you said product marketing, analyst marketing and then product engineering design. It's rare that you see marketing as a part of teams, as a leadership, kind of part of the leadership group. Do you have a sense of what impact adding that had on the team or where that came from? Or is that just historically been something Miro has prioritized, marketing and product marketing?

Varun Parmar (00:23:25):
This was done before I got here and I wish I could take credit for it, but I can't. I think this was the result of an observation, which is quite similar to what you're saying, which is while we might be developing a lot of the features and PMs or thinking bottoms-up in terms of what we are building, we might find that what we have built might not be able to capture the imagination of what we originally thought it would. A big part of that is how are you going to think about positioning, how are you going to think about competitive differentiation? How are you going to package it up so that the sellers that are out there are able to position it in a way that the customer, in this case the buyer, might be an IT professional, might a line business leader, can basically see the full vision of where we are going? I think by having product marketing as part of AMPED, we now bring that unique perspective that may be missing in certain teams.

(00:24:24):
PMs are more acting as product owners or more focused on core problem and solution but not thinking about positioning, because that's so important, especially when you're thinking about a market that we are increasingly in that there is competition there. That's one of the first things we started off with and that's top of mind for you as well, is that everything that we are doing has to be looked through that lens. One of the core philosophies that I have, Lenny, is that the success of a company is a direct relation of what the competition allows you to do. I feel like not many people talk about that, but in many cases in my professional career, and I've been at it for close to 24, 25 years, is that every single instance when I looked at a company accelerated their growth or there was a deceleration of growth, it was a direct relation to what the competition allowed you to do. Obviously, you have to do everything that you should be doing, but competition is the biggest variable that allows you to figure that out.

Lenny (00:25:24):
I want to hear more about your core product philosophies, but let me dig into the one you just shared. What you find is that the way you grow or stop growing is often a direct result of your competition. Is there an example of that that comes to mind? I'm guessing maybe Box versus Dropbox is an experience you had there, or if not, what's an example of that that you've experienced, to make it a little more concrete even?

Varun Parmar (00:25:50):
For those of us who've been in the collaboration space, and I've been doing collaboration and productivity apps for over 20 years, over two decades, at some point, you have companies like Microsoft that get really attracted to a space and you can see the trajectory of a business that's growing at a certain clip and then all of a sudden there's a competitive product that enters that has the might of distribution and the might of pricing, and that's just a direct example. I think I've seen that multiple times, first at Adobe where I was part of the document cloud business, clearly saw that at Box as well.

(00:26:27):
I think you can, in general, sort of look at every single category and you can say that there was a category leader and they were growing at a certain clip or a certain pace and all of a sudden there were a bunch of entrants that get in and what happens to your growth rate? It's all dependent on how strong is the competitor in terms of providing a good enough solution? That's one. The second is how strong is the competition in terms of their distribution outreach? Then the third thing is how strong is the competition in terms of the pricing and packaging?

Lenny (00:26:55):
I really like this discussion, especially because often the advice is, "Don't worry about the competition, just focus on the customer, it's going to be fine." Which what you're saying is that's not right, and I agree. What do you do with that in mind? How does that impact the way you build product or strategy? Is there some you could share that maybe tactically someone could leverage to how they're approaching their product strategy?

Varun Parmar (00:27:18):
It depends on who the competition is and what is their unfair advantage here. We talked about one specific competitor and I have a lot of respect for them, by the way, and I learn a lot from them every single day in terms of how they make bets and how they enter markets and stuff. At some point I'm going to write a book on them, I feel.

Lenny (00:27:35):
Ooh. We'll have to come back to talk about that.

Varun Parmar (00:27:38):
That's right, yeah. I think it sort of comes down to how do you think about your unique place relative to all of these players, and in your customer's mind are they able to clearly understand what is the unique value that you deliver relative to everything else? Part of that is the unique capabilities you provide. Part of that is how you're packaging those unique capabilities to them, and making sure that they in their mind can see how you coexist in this overall sort of tech ecosystem that they might be investing in, to enable their employees or to enable them to operate. So I think it's sort of looking at that from that lens, yeah.

Lenny (00:28:26):
Got it. So what I'm hearing is be very clear about your differentiator and continue to invest there and then make sure your positioning is clear around why you're... just identifying, "Here's why we're different and we're not just a better or worse version of this thing" or "Here's why we're different" and making sure that's really clear.

Varun Parmar (00:28:43):
Exactly. I think the other thing I would say, there's another core philosophy I have, which is products either get better over a period of time or they get worse. Products never remain the same. I think you can take that philosophy to a bunch of things in life, but I'm going to take the lens of products, which is my core philosophy is every single day, every single time somebody is pushing your code to production and you're releasing a feature or an enhancement, you are making the product better or you're making the product worse, but the products never remain same. The lens for this, Lenny, is actually from a customer's perspective, from the end user perspective. The thing is that if you are a player where there's no one else in the market, that's one thing, so that's great. Kudos to you for actually identifying a blue ocean strategy and sort of executing to that. But most markets, most products, actually have either direct or indirect competitors that are available.

(00:29:40):
From the customer's mind, you're doing something, the competitor is doing something, so in their mind they're looking at these products and they're looking at these companies and they're saying, "Which is better versus not?" So with every release that your competitor is making and every release that you're making, you're either making chess points, moves against them, positive points, or you're going negative. I think that framework, if you have in mind, it actually drives an insane amount of clarity in terms of what you're doing and what the impact is going to be. Because every single move that you're making, the customer has that sort of in their mind, if not explicitly, implicitly that they're actually comparing these things. I think it brings a level of focus in terms of where you need to invest and why you need to invest and why this is going to make those decisions.

(00:30:28):
I think it allows at least for product leaders to make some high quality decisions around the bets that they're making and how they're going to play out in terms of eventual once the dust settles and the market at large is going to say, "I'm going to standardize on something and now I feel I need to go get it for everyone." Or "This is the tool that I want to use for this particular use case." That all of these decisions that you are making ladder up to that final sort of play that you have to do in terms of the market consolidation that eventually happens.

Lenny (00:30:59):
This is so interesting. Essentially what you're saying is that you find that being very close to and understanding the competition really well is really essential, versus this kind of the other end of the spectrum almost from just like, "Don't worry about the competition, don't pay attention." I like this point, metaphor of just like, "Are we moving ahead or further behind?" Is that where you operationalize that to track that? Then also just how do you not over-obsess with, "Let's just catch up, get more features," that kind of thing? How do you find that balance?

Varun Parmar (00:31:28):
I'll be honest, I don't think we've figured it out. We haven't cracked the nut in terms of how to operationalize this, but I know you are way smarter than me on some of these things, so maybe we can-

Lenny (00:31:39):
Unlikely.

Varun Parmar (00:31:39):
... partner on this and come up with something.

Lenny (00:31:43):
All right, that'll be something we work on. Any other product philosophies that you want to share? That was awesome.

Varun Parmar (00:31:52):
This is all sort of related to it. It's like a string of pearls. I think there's maybe one more pearl we can actually thread into the needle right here.

Lenny (00:31:59):
Let's do it.

Varun Parmar (00:32:00):
Which is we talked about how do you ladder this up and stuff, and then the question is, okay, how do you know that everything that you're doing, is that in the right direction or not? Should you move slow and be much more mindful about the things that you're doing or should you move fast and make certain bets and then decide certain things and stuff? I think there are two views that are out there. My personal perspective on this is that what you want to do is that you want to be the first one to hit the brick wall. This is particularly true when you are in a market that is competitive. The reason for that is that if you consider yourself as an innovation-centric company and you believe that you are building experiences that fundamentally don't exist anywhere else and you're sort of paving the way for the rest of the folks to basically get inspired with how you are building these experiences, speed is the single biggest determinant, in my experience, in terms of who ends up being more successful versus not.

(00:33:14):
I don't know, maybe this is a little bit controversial where people say, Go slow to actually go fast." I think I have a lot of respect for that and there's certain areas you should do that, but when you are trying to figure out new experiences and stuff and you don't know if it's going to resonate or not, speed is something that you should accelerate for the organization. I think Frank Slootman talks about this a lot in his book and how can you accelerate? I think for me from a product perspective, the fundamental concept is can you be the first one to hit the brick wall where you have the learning faster than anyone else in the market so that you can decide, "Oh my god, the path that I was going was not the right path. I need to do 10 degrees west or I need to do 30 degrees east." I think as long as you're one or two or three steps ahead of everyone else in terms of uncovering or discovering those insights, then I think you can continue to be ahead of the pack in terms of building your product in business.

Lenny (00:34:21):
You're talking about urgency. I've never met a founder or a product leader who doesn't want their team to move faster. They're always encouraging their team, "How do we move faster?" I'm curious if there's something you've learned tactically about helping your team move more quickly. You mentioned Frank Slootman's book. Amp It Up is what it's called, by the way, in case folks want to check it out and he's big on just like creating a sense of urgency, constant urgency, and we'll link to that and share notes. But yeah, what have you found helps create urgency and generally helps your teams move faster other than just like, "Move faster, everyone"?

Varun Parmar (00:34:52):
My fundamental belief here, Lenny, is that every product manager... I can talk to product managers because there is reason certain ones, someone wants to be a product manager, because in my view it's one of the most thankless jobs, like you get to do a lot of [inaudible 00:35:10] and it's like, "Why you have to do this?" But it attracts a certain personality and that personality is driven by challenge and that personality wants to prove that they can solve this challenge and do something amazing. I think fundamentally the product persona actually wants to move fast. I think the reason why in some cases we are not able to move fast is because of roadblocks that we run into and those roadblocks can manifest themselves into technical challenges, they can manifest them in cells of organizational challenges, they could be priority challenges and so on and so forth.

(00:35:52):
My fundamental approach to solving that is to ensure that the product leads who are working on these capabilities can instantly raise their hand and call out that there are challenges that they are running into. Then the job of the leadership team, the product management team, is to essentially go and quickly resolve those issues. I think if you are able to resolve those issues, then what it does is it actually starts a virtuous cycle where you can actually start to see those wins. Once you see those wins, you actually create that courage to do more things. Maybe because you've seen how that specific roadblock was solved and you have a pattern matching that you've developed now, you can solve a lot of those things on your own and it's the next level of challenge that you now going to raise your hand.

(00:36:41):
What that does is it starts to build this organizational competency in terms of how you can figure out what to build. We all find these people in our organizations where there's someone somehow is able to do certain things in one-tenth the time that it would take a normal person. It's not that they are 10 times faster, it's just that in my observation that they've figured out which part of the core base they should build in versus not, who should be part of their team and who should not be, how they need to define that from a scope perspective, what does success look like, and it's the architecture of bringing all of these things together that actually brings that magic formula line in terms of "Hey, we are able to deliver faster."

Lenny (00:37:19):
I really like this topic. What I'm hearing is one of the biggest roots of slowdown in a company and product development is blockers not being unblocked, and I always feel the same thing. I feel like a PM's number one job is to unblock their team because their job is basically make the most out of their team that they're marshaling towards some outcome. The way you do that is just figure out what's slowing them down. You just talked about this idea of a PM raises their hand to leadership, "Hey, we're blocked by this thing." Is there a process you've come up with there that helps you do that, it's connected to-

Varun Parmar (00:37:51):
Yeah, I would say we are trying to sort of systematically ingrain this in the culture of the organization. We have a motto in the product org, it's very simple, single sentence, deliver customer value faster with high quality. That's it. Everything that we do, and when I say everything, everything, Lenny, from performance and reward system and measurements, everything is based on this one single statement and it has three attributes. The first one is deliver customer value, and we believe customer value is only delivered when customers use it. Anytime as a PM at Miro, when you ship something, we are looking at, "Well, what was the metric you were going to move and how much did it move?" We have some original targets that we can go back to. That's the first aspect of what we're doing, deliver customer value.

(00:38:35):
The second one is move faster, and there are certain cycle times that we are measuring across the organization. From the time you came up with the idea to the time that you actually pitched a solution to the time you actually shipped it, to the time we actually moved the metric, it's information that has been collected and is being made available to the organization. You can say, "Hey, if it was a small, medium or large, what's the average? What's the medium, what's the variance?" And you can say, "Hey, looking at this data, what can be improved?" That's on the faster aspect of it. Then the last one is around high quality, which is we want to build best in class collaboration experiences, so we are always getting inspired by what we find in applications and experiences that we see around us and we are saying, "Hey, when it comes to designing, sharing flows, we believe that these are the three apps that have best in class sharing flows when it comes to designing some synchronous capabilities like this. These are the best in class apps that we should look at."

(00:39:31):
We are always trying to make sure that we are benchmarking ourselves against that and we have our design team. On a regular basis, like when we ship stuff on a monthly basis, our design leadership team does a triage of everything that got shipped into high quality or not high quality. It's just like a binary function, and we're doing that and we're saying, "Hey, the reason why we believe it's not high quality is because A, B, C, D, E and we're making it available to other designers so they can actually start to build that telemetry in terms of some things are more subjective." But you can start to see some patent matching and say like, "Hey, this is what great looks like."

Lenny (00:40:06):
This episode is brought to you by Linear. Let's be honest, the issue tracker that you're using today isn't very helpful. Why is it that always seems to be working against you instead of working for you? Why does it feel like such a chore to use? Well, Linear is different. It's incredibly fast, beautifully designed, and it comes with powerful workflows that streamline your entire product development process, from issue tracking all the way to managing product roadmaps. Linear's designed for the way modern software teams work. What users love about linear are the powerful keyboard shortcuts, efficient GitHub integrations, cycles that actually create progress, and built-in project updates that keep everyone in sync. In short, it just works. Linear is the default tool of choice among startups and it powers a wide range of large established companies such as Vercel, Retool and Cash App. See for yourself why product teams describe using linear as magical. Visit linear.app/lenny to try Linear for free with your team and get 25% off when you upgrade. That's linear.app/lenny.

(00:41:15):
Okay, so every month or so the design team looks at everything that's shipped and puts things into a bucket. Either this is... It's like a binary thing, high quality or not high quality.

Varun Parmar (00:41:24):
Yes.

Lenny (00:41:24):
Wow, that is so cool. Then, one, what do they do with that? Do they send it out to the product team? Then two, is this just like FYI or is it like, "We need to fix all these low quality things going back"? Or is it more just like, "For the future, please be aware these are not high quality"?

Varun Parmar (00:41:39):
Yeah, so it's actually both. Generally what happens is that the design leadership team is doing this and there's one particular design leader who's the designated person to make sure that this is happening on a regular basis. Right now the way we're using it is that we are actually using it to calibrate and align around the design leadership around what we mean by high quality. Because it's one of those things, it's like if you've never seen colors and I ask you, "Lenny, describe pink and compare that to red," and if you haven't seen colors, how do you describe colors? You can't. But if I show you and I say, "Lenny, these are three examples of what pink is and these are three examples of red is," then you're like, "Oh, I get pink and I get red." There are certain things that you just like when you write it's very, very hard to describe it, but if you show specific examples, it's very clear, "Oh, I get it. I get how pink is different than red." But if I try to describe it, it's going to be very hard.

(00:42:35):
So we got into these endless conversations at some point about a year ago where we were saying, "We need high quality, we need high quality." And people are like, "Let's just go and define this thing." We had a bunch of our leaders go and write documents, really long documents in terms of what are the attributes and how do we define those attributes and how do we measure those attributes and how do we enable people to do that? It felt like it's a good thing because we are trying to codify it, but it also felt like it was a very heavy way of solving that problem. Then we just came up with this approach, which is like, "What's great versus not great" and just start classifying it. As you know, it's like modern AI systems are classification systems and we [inaudible 00:43:12]-

Lenny (00:43:12):
Yeah, I was going to say, sounds like reinforcement learning approach here.

Varun Parmar (00:43:14):
Exactly.

Lenny (00:43:14):
Defining cost.

Varun Parmar (00:43:15):
That's right. That's right. I think it's worked decently well. I would say with most things we need to operationalize it and we need to make sure that now we are democratizing it and everybody has access to it and so on and so forth. But I think it's been a good start and now we are sharing this more openly with others in the org.

Lenny (00:43:37):
When I said that, I imagined you... From the outside, you have a very unique culture and approach your product. That's a great example of that. I've never heard of a process like this. What I'm hearing is essentially you're trying to build the muscle within the organization of what is quality. It's like this continued heuristic of, "Okay, I get it." So PMs on the team start to understand in their head what that means.

Varun Parmar (00:43:56):
Right.

Lenny (00:43:57):
Super cool. You also talked about, in the middle part of that sentence, of moving faster and that you track and measure that somehow. Can you talk more about that? Because that's something every product team is always trying to understand. "How do we know if we're going faster, if we're going as fast as we could?" How do you actually do that? How do you measure these things?

Varun Parmar (00:44:13):
The core philosophy there is velocity is more like the game of golf where you're just playing against yourself. It's not like if Lenny and Varun are out at the golf course, it doesn't matter. I'm not competing against you, I'm just competing against myself because that's the only... I'm going to just hit the ball, so it's like how much better can we get? I think our core philosophies around that and what we're trying to do is that on all the product teams, the feature teams that we have, we're just collecting all the information and we are making it available to everyone so that they can actually see what the cycle times are. What we are interested in is from the time that you have an insight, from the time you believe "I can do something unique for my user, for my persona," how long does it take for you to actually deliver that value?

(00:45:04):
We have a product process that we follow, which starts with a P-strat, which is a strategy, and then we go into P0, which is definition of the problem, then we go into P1, which is definition of the solution, and then we go into P2, which is once the solution is shipped, are we hitting the metrics that we originally had defined upfront before we decided to work on this. You have all of these stage gates and then we basically classify everything that we are doing in small, medium, large. You can go in and you can say, "Hey, I thought this was a small thing," and small thing is something you can get it done in less than a month, and so on and so forth. There are 50 other product teams that are shipping these features, and what's the average, what's the variance, what's the median?

(00:45:48):
"Oh, wait a second, actually it seems like I took way more time in the problem definition stage. Let me actually try to go talk to this other product team that actually did it much faster," or "Oh, I actually did it really, really fast, and the reason why I did it fast was because of this. Let me go share this out with the broader team." Usually the product ops function, we call it product excellence internal, sort of product excellence function, is recording some of these things. I would say getting reliable data, and then because we have some things that are going through meetings and there are some things that are going through Slack, we could do better on some of those dimensions, but all of this data is available and we provided it openly and folks can benchmark themselves against that.

Lenny (00:46:34):
So cool. Okay, so you have this P-strat, you called it, document which is kind an initial concept and then it's interesting you use the P0, P1, which is often for bugs, but it's cool that you use it for defining your products. So P-strat is just an idea pitch. P0 is a spec, basically, like a one-pager for the product, and then P1 and P2 are basically getting to "Here's the actual product we're building." And you basically track time per step and map it to, "Here's how large this project should be." Over time you track per person, it sounds like, just like are you matching the benchmarks of how long a small project should take across each step?

Varun Parmar (00:47:13):
Yeah, exactly.

Lenny (00:47:14):
Wow, that is extremely cool. Whatever templates you can share, these things that we can include in the show notes would be awesome.

Varun Parmar (00:47:21):
Yes.

Lenny (00:47:22):
Because people are always looking for just like, "Ah, I want do some of this stuff." If they can just plug and play, the more, the merrier.

Varun Parmar (00:47:28):
Yes.

Lenny (00:47:29):
Shifting a little bit, it sounds like you guys are doing Scrum in some form. Can you just talk about just broadly the product development process? How long you or your sprints, how long do you plan for in the future, in detail specifically just like high level, how does the product development process work?

Varun Parmar (00:47:43):
There are certain things that I learned at Box and that inspired some things that we do at Miro, and there are certain things that we've evolved. One of the things that we've instituted is our roadmap process, so that's sort of the first thing around how the different teams are looking at the things that they're going to work on. We have a rolling six month roadmap, it seems large, but we've got, like I mentioned, a number of enterprise customers. If I've learned one thing that large enterprises is asking for a roadmap review. That tends to be my favorite meeting of sitting down with the enterprise leaders and walking through what we are working on. What we've done is we've tried to architect something which actually allows our customers to get what they're looking for, but at the same time does not remove the agility that is so important for us to deliver value faster.

(00:48:41):
What we do is we have a rolling six month roadmap that gets updated every three months and the first three months of that roadmap, we have a 80% position level, which means that 80% of the things that we claim to be on the roadmap will get done. That's the target. For the next three months, because it's six months, so the first three months is 80%, the next three months is 50%, so we have a much lower level of resolution in the next three months after that. What that allows the product teams to do is actually have flexibility, which is based on what the customers are asking for and based on what the competitive moves are, based on some technology breakthroughs that happen around large language models, they can pivot and they can pivot and move towards that and they won't get penalized either by the customer or internally in terms of doing that. That's what we do and that's all at on the backdrop of an annual strategy that we publish.

(00:49:34):
Every year we publish a strategy white paper that it gets published internally available to every single Mironeer across all functions that clearly articulates the key bets that we want to make. Why do we want to make those bets? What is the expected outcome and how does that ladder up into the overall business outcomes that we are trying to drive from an OKR perspective as well as the overall business strategy that we have. So people take that product strategy, white paper or artifact, and then against that they're building their roadmaps which get updated every three months. Then inside of the teams, we enable teams to be quite autonomous in terms of some of the rituals that they're doing. We want them to obviously embrace best practices. We've got a team of agile coaches that share best practices or are available to help if there's certain specific needs that teams have.

(00:50:31):
Then I think on top of that, there are certain key, I would say, rituals that we do that maybe are unique. For example, we have something called as Miro Connect, which happens every other Friday. Every other Friday, for example, in our Amsterdam office, you can go in there and at 4:00 in the afternoon, 4:00 to 7:00 or 8:00, and sometimes it goes really late, you've got a bunch of product teams sitting around tables and it feels like, "Oh, it's like a pitch or something." And people are coming in, they're having a good time, you've got a drink in your hand, there's maybe some light music playing in the background and you're going from table to table and you have teams that are actually showing all the amazing work that... If done right, it happens once in a while, but if done right, it's magical in terms of the outcomes that you can get.

(00:51:20):
I'll tell you, there was a team that actually was presenting at our Berlin hub and they were saying, "We're working on this feature, and there's an engineer who walks over to that desk and says, 'What are you working on?'" The team describes it, "Oh, we are trying to do something like this." And this engineer had actually worked on that particular problem in their prior life, literally they had implemented this. So he says, "So how are you going to implement this?" And the team, the engineer that's sitting there, says, "This is the approach I'm going to take and it's going to take me three months." He's like, "Oh, would you mind if I go and help you with this?" They're like, "Sure, more the merrier. Go ahead." So this person puts down their beer and says, "Okay, I'm having a good time. Let me just head back to my home." And in the next three or four hours goes and codes the entire thing, makes a poll request.

(00:52:10):
Next day in the morning one of the engineers from this core team that was exhibiting at Miro Connect looks at the poll request, reviews the code and says, "Yes, something that would have taken three months for this core team because they didn't have the expertise literally got done in three hours because there was another engineer that ran into them and said, "I know how this is done. I can actually help you here," and went ahead and did the right thing. We are trying to create these magic moments. It happens once in a while, but we have one success story and I like to tell that in every opportunity that I get. But that's another sort of unique thing that we've done in terms of book-ending things around how we operate here.

Lenny (00:52:50):
That story is like a dream for any PM. Just imagine saving months of work with one conversation. I imagine people were like, "How do we replicate this often?" I love that. With these meetings, just to understand, if their team is in Berlin, let's say, there's a screen there in front of a table and they're talking through a screen, like a video conference?

Varun Parmar (00:53:12):
Yeah. I mean, right now what we've figured out is that it is really hard to do these events over audio-video conferencing and stuff. So generally what happens is that you have an audio-video bridge that's playing, but mostly it's people walking up to the respective teams and then having a live conversation. That's usually how these things are operated. Yeah.

Lenny (00:53:34):
Got it. Okay, so you have six month rolling roadmaps. You have a yearly vision strategy for the company, two week sprints. Is there also a quarterly OKR sort of process or is it-

Varun Parmar (00:53:34):
Yeah.

Lenny (00:53:48):
... those or not? There is, okay.

Varun Parmar (00:53:48):
There is, yeah.

Lenny (00:53:49):
Can you just talk a little bit about how that works?

Varun Parmar (00:53:51):
Yes, yes, yes. At Miro, we practice OKRs and it starts off at the company level, and then those company level OKRs are taken by the AMPED organization. Like we describe, it's the AMPED organization, and then we break it up and I would say we have refined it over the period of time, the two years that I've been at Miro. Early on we were doing OKRs on a quarterly basis, and I would say more recently we've actually evolved to six month KRs. What we found was that six month was the right cadence in terms of giving enough time for teams to basically push forward in executing these KRS and minimizing the "overhead" of doing replan every single quarter. We found that it was much more effective and efficient for the entire organization to do it on a six-month basis. However, we are doing traction on a monthly basis. So every four weeks, as AMPED, we are looking at our KRS for the AMPED organization on a monthly basis doing traction. However, the planning, the targets, are done on a six-month basis.

Lenny (00:55:06):
I love how OKRs could just be anything, could be every six months, could have objectives, could have key results. It's just such a term that just applies to anything that people do with goals, basically.

Varun Parmar (00:55:17):
That's true.

Lenny (00:55:18):
And it works. It's great.

Varun Parmar (00:55:19):
That is so true.

Lenny (00:55:21):
Again, if there's any templates that your team could share of the way you do that stuff, that would be amazing, and we'll include that in the show notes.

Varun Parmar (00:55:27):
Yeah, absolutely. Because I think, as you would expect, we run Miro on Miro, so there's a lot of things that we could share as templates in terms of how we are running things on Miro, not just as OKRs, but in terms of product reviews. We have ways of how we are doing asynchronous reviews combined with synchronous reviews and there's this blended experiences that we have, and so we can definitely share out with the community how we do some of these things.

Lenny (00:55:55):
Awesome. That's a great segue to another question I was going to ask is just what other tools, what's in the stack of the product team's workflow? So Miro, obviously. Maybe talk about what use Miro for, but then what else is in there? What do you use for task management, bug tracking, things like that? Design?

Varun Parmar (00:56:12):
Starting from the bottom-up infrastructure view, so all of our tickets are handled in Jira and we are using some of the newer capabilities in Jira in terms of coming up with roadmaps and coming up with the priorities and stuff. On top of that, all of the specs generally get recorded in Confluence. Having said that, we're actually a big fan of tools like Google Docs as well as Coda that allows us to track our KRs in a pretty effective way. On top of that, obviously we use Miro a lot, I would say for a lot of our things, especially on the product and design side of the team. Generally all of our insights get captured inside of Miro board, so when we are going and conducting user experience interviews and stuff, we will record those and then those recordings get added to a Miro board, so Miro access the content hub or a team hub for a particular project.

(00:57:20):
Once you capture all of those insights, then generally all of the brainstorming and team ideation happens on the Miro board as well, so Miro's actually also used as a tool to facilitate meetings and workshops. Once all of that is synthesized into a set of recommendations and outcomes, so when we go into these product reviews that we were talking about, Lenny, the same Miro board then gets manifested into a set of presentations, so we use Miro for presentations. We've actually made some really amazing updates in terms of our capabilities there and if folks haven't checked them out, I would strongly encourage them. There's a capability called Showtime that basically abstracts out the UI and lets people focus on the content, but do it in a way that it's interactive so everyone that's on the call can have reactions, can share their comments and leave comments while the presentation is happening without actually disrupting any of the flow for the user, so we use that a lot for presentations as well.

(00:58:15):
I would say more recently what we've started to do is that we've started to move some of our synchronous meetings into asynchro view. I talked about this Talktrack feature that we have, and a lot of teams, what they would do is that they would actually send you five minute, 10 minute Talktrack in advance and it's just a link to a Miro board, you click on it and then you just sit back and relax. Then you have this magical experience where you're sitting back and the Miro board is automatically moving because Lenny was recording it like that. Then you have the video play and then you can pause it anytime, you can add in your comments and stuff so that the next time when you meet, instead of actually providing context to everyone, those synchronous sessions are lot more deliberate and focused on driving outcomes or achieving consensus, so people are just focusing on the comments that were added as part of a async product review so that when they meet synchronously they can use that. Miro boards are used for that as well.

(00:59:06):
I would say now a lot of our dashboarding shows up in Miro boards now. We recently released data visualization capabilities around most popular VI tools. At Miro we use Google Looker a lot, so a lot of our dashboards are in Looker, and what you would typically find is that our analyst team and product teams will just grab a link to a Looker dashboard, put it on a Miro board, and it unfolds into a full visualization. Unlike a screen grab, you never have to go update it because right there on the Miro board, it's always updated and you can refresh that, so you basically have this experience where Miro acts as that single source of truth for a lot of the teams across the entire journey of product development where a single Miro board is meeting the needs of multiple use cases there.

Lenny (00:59:51):
Then for the road-mapping, is that in Miro, each team's roadmap, or do you use something like Jira?

Varun Parmar (00:59:57):
Yeah, so I think we've got a couple of tools for road-mapping, and our observation is that while those tools are great for the unique needs that they're solving, we haven't found a universal solution for road-mapping. So there are some teams that use Miro for road-mapping and they would use the Kanban widget in Miro for that. What are they working on? What's coming next? What's in the backlog? But I would say it is a problem that is not completely solved in terms of how do we actually bring these artifacts together at scale.

(01:00:27):
What we are starting to see, and this is actually a unique use case of Miro, is that we actually enable our entire field organization using Talktracks. What happens is that we have our entire roadmap published out as a Miro board for enablement purposes, so that that's a artifact that is approved to be shown to a customer. What you will see is that you'll see five or six recordings in there, and the leader for enterprise has done a five-minute recording on everything they're working on. The leader for platform has done that. The leader for end user experience has done that. The person who's driving some of our AI experience has done that. So you can go in and you can just click on that video and you can meet your needs by using Miro and this capability that we have.

Lenny (01:01:09):
That's awesome. It sounds like each team can basically choose the tools they want to use. There's no standardized, everyone needs to use Jira or Miro for their roadmap. I like that. I like how teams do that often. Maybe one last question around the product org, and then I want to shift a little bit to growth and how Miro grows and things you have learned about growing. Question I always try to get to is how do you think about balancing new bets and innovation with maintenance and just general incremental work? Do you have some sort of philosophy as a product leader broadly, and then maybe at Miro specifically, of just how to balance investments in these two buckets and maybe three buckets, bugs, incremental work, and then just big bet? How do you think about that?

Varun Parmar (01:01:55):
We have some rule of thumbs in terms of how we want to allocate our investments across these buckets. I would say a lot of it, Lenny, actually depends on the state of the team. There are certain teams that have more tech debt than others. There are certain teams that are actually working on some really big zero to one features than other teams, and so I think there is a variance. The standard deviation actually is dependent on which part of the spectrum that you're in, which is are you a team that we believe needs to create the next generation experience on the platform and hence we have to prioritize innovative work or are you the team that's actually so critical to actually meeting our objective around better board performance or any of the other things that we believe are important and hence we need to invest in those critical areas?

(01:02:41):
But I would say in general innovation versus not, varies on a spectrum of anywhere from 60 to 80%. I would say about 20 to 40% of the available capacity at any given time is either getting allocated to architectural initiatives. There's a technology roadmap that our CTO is driving that we believe is extremely important as the platform scales, and now as we have over 50 million people on the platform, so we continuously have to invest in making sure that the platform can scale. There are certain teams that probably have 40 to 50% of their allocation towards that because they're a critical part of the component. There are other teams that are maybe more end user focused and are more UI focused where that allocation is lower. But I think general rule of thumb is 20% is always a given, but it can go as high as 40 to 50%.

Lenny (01:03:30):
On bigger bets and longer-term thinking?

Varun Parmar (01:03:33):
Yeah, 20 to 40% goes on the technology-related initiatives and maintenance and stuff.

Lenny (01:03:38):
Oh, got it. Infrastructure, maintenance, making sure everything's there. Got it.

Varun Parmar (01:03:44):
[inaudible 01:03:44] Exactly, yeah.

Lenny (01:03:44):
Then what about just big, long-term bets that you're not expecting to pay off anytime soon? Do you have a heuristic of just what percentage of, say, total resources you put there?

Varun Parmar (01:03:53):
You've probably seen this, the framework of three horizon, it's quite popular in McKinsey and Harvard [inaudible 01:04:01] school and so on and so forth, is horizon one business, which is the thing that's delivering food on the table. Generally there's about a 70% allocation of resources that we have, give or take. Then there is horizon two, which is an adjacent thing. With the next 12 to 36 months we believe it's material. Usually that tends to be around 20% of the allocation. Then there's horizon three, which is three years out, three to five years, next generation things, and that's about 10% of the ratio. So it's like 70/20/10 across horizon one, two, and three.

Lenny (01:04:30):
Awesome. Any other thoughts along the lines of just how you think about product before we shift? I only have a few questions around the growth story of Miro and what you've learned about growing.

Varun Parmar (01:04:41):
In terms of product leadership and what we believe is the way we want product leaders to be developed and I think it's more of a people philosophy. We have our product leadership which constitutes of all of the folks who are running all of these streams, and I always tell them that you have two personas that you have to think about. Everyone who's on the product leadership team is a product leadership team member. The fundamental thing that you have to do is drive accountability. The number one thing that a product leader on the product leadership team needs to do is drive accountability with others in the product leadership team. The other persona that they have is that they are a stream leader. They're actually responsible for delivering value for the respective persona and respective customers and stuff. So when you put on the persona hat of a stream leader, which is different than the persona or of a product leader, your number one metric, the number one goal that you have, is drive improvement.

(01:05:42):
When you go back and you work with your team, always have the lens are you improving things and whatever you want to improve, but you always have to ask yourself, "Today compared to yesterday, tomorrow compared to today, have I improved things? That's the yardstick you should think about. When you go sit in the product leadership team every Monday afternoon at 1:00 in the afternoon when we meet together, your number one goal is actually to drive accountability around this and are you making sure that we as leaders in the organization are doing the right thing for the company?" I think that's a philosophical construct that I always remind people in terms of what they should be doing. As an example, tomorrow we have calibrations, we have our annual review cycle happening in the company.

Lenny (01:05:42):
Good times. Always a blast.

Varun Parmar (01:06:23):
Yes, exactly, always fun and so critical as a leader, because it sets the tone for everything that you're going to do. In my opening remarks, the only thing I'm going to remind everyone in the room is that "Your number one goal here is to be a product leader and accountability is what you have to write. That's it. Just hold each other as accountable, including myself in terms of making sure that as we go in, that's the key thing." I think once people understand the duality of how they need to operate across those two specific goals, it actually leads to really high-performing teams and teams that actually are able to create somewhat of a magic if they are open and there is trust that has been built in the team.

Lenny (01:07:07):
When you say accountability, what does that look like? Is it pointing out, "Hey, you didn't achieve this thing we were trying to achieve" or "You didn't do a great job leading this meeting"? Is it just direct feedback often or is there some other way you see that manifested, and what do you like to see?

Varun Parmar (01:07:24):
Yeah, I think it's basically practicing feedback in a very open and constructive way and focusing on what is important for the business and not shying away from having some of those observations and conversations, not shying away from them. But it's all in the lens of what is the right thing to do for the business, and if you feel that that one or more members of the leadership team are not living up to what needs to be done, then just voicing it. It's not like you're complaining or anything, it's just like, "I have this perspective. Is this the right perspective or not?" Because actually it ties very well with the overall cultural values that we have.

(01:08:02):
If you do things with the lens that you are being empathetic, then you pose it as a question as opposed to a statement. I think that's one of the things that we practice a lot at Miro is that I believe that I am seeing there are certain things that are happening that it could be just me that I'm not seeing the other things. "But what is it? Can you help me understand? Can you help me figure out that why certain things are happening? Because I might just be missing the perspective." But because you bring it up, and that's part of practicing accountability in an empathetic way, it actually gets the entire team in the right mindset in terms of how they operate.

Lenny (01:08:39):
Has anyone given you some sort of direct feedback recently or pointed out something you didn't do well that held you accountable that you can share?

Varun Parmar (01:08:47):
All the time. Yeah, all the time. When we do our offsites, this is actually a fun thing, is that every offsite that I do with my leadership team, usually there is a one to two hour session where it is feedback to Varun, and I actually do it openly. I will have about eight to 10 people in the room and I will force people to be very honest and I want to show my vulnerabilities to everyone, that I am not perfect and I have lots of areas to improve. Every time people do it, it's interesting that they open up in very amazing ways and I think I love it because it helps me become better. It helps me identify my blind spots. But what it does is, because I do it in an open way, it brings a lot of trust. It brings trust that I do it openly and I'm an open book and they can share whatever they want, not just with me but openly in front of everyone.

Lenny (01:09:43):
Are you willing to share one thing they suggested that they pointed out that they wish you did differently or better?

Varun Parmar (01:09:48):
Yeah, I think in general, finding time with me tends to be a bit of a hard thing, and generally there's always this feedback, which is need more time, maybe more responsiveness over email or Slack or something like that. That's an area that I'm constantly working on and improving, so yeah.

Lenny (01:10:11):
That feels like a cop out. That doesn't feel too painful to hear. I'm like, "Yeah, yeah, I know. I don't have a lot of time. I'm sorry." But I get it, and that comes back to your point about blockers and how important it's to unblock teams because that leads to a lot faster progress.

Varun Parmar (01:10:26):
That's true, that's true.

Lenny (01:10:28):
Okay, so let me shift a little bit to Miro's growth and I only have a few questions here. I know it's getting late on your side so I don't want to keep you too long.

Varun Parmar (01:10:34):
Sure.

Lenny (01:10:35):
The first is something I'm on this constant quest to understand how companies got their first users, and I haven't actually heard the story of how Miro got its first thousand users or customers. I know you weren't there in the early days, but you happen to know how Miro initially grew and got their first thousand users and customers?

Varun Parmar (01:10:53):
I think the fundamental thing there is that we always had user first approach and reaching out to certain communities that were relevant to what was a key part of lighting the fire, if you will, the proverbial way people start to talk about the product. Given the collaborative nature of the product, some of the early adopters invited people who were also early adopters and the flywheel started to work. I've heard that we did a fair amount of content marketing and listing the product on sites like Capterra sort of helped. There was some early investments in terms of SEO and organic growth, so there was a focus there, which was the main source of driving traffic. The top of the funnel came through that.

(01:11:43):
The product teams were very intensely focused on building vital loops as a key mechanism of driving growth, once the traffic came in. Every interaction that actually introduced barrier, they looked at it and they looked at the data and they said, "Let's reduce this barrier. Let's remove this thing so that the product could be effectively embraced." It was an evolution over a period of time. There was also the fact that early on in the journey, some of the features were presented on a trial basis and then later on the model was evolved from a trial basis, time limited to a premium model that further accelerated the growth for the business. I would say those were some of the approaches that were taken to get to the first thousand users or so.

Lenny (01:12:34):
You talked about how Miro grows, where it has this magical loop of "I use Miro to for myself, then I share it with my team in whatever way I'm using it." They're like, "Oh, Miro, this is cool." Then they start using it and then they share it with people that they want to work with, and it creates this loop of growth." I imagine that's how Miro mostly grew initially and continues to grow. Is there anything surprising or unintuitive about how Miro grows that is beyond that? I imagine sales is a part of it and we can talk about that, but is there anything else that is interesting that is worth mentioning?

Varun Parmar (01:13:07):
No, I think that's the key of the growth. I think there are specific use cases where they are uniquely sort of geared towards inviting a lot of new people. For example, Miro is loved as a workshopping tool, and so generally one person is using Miro, but they invite 10, 15, 20, 50, 200, 300 people to that workshop. There are specific use cases where people get introduced to the product and then go and sign up for it and then start to use it for that use case or other use cases. I think the other accelerant in all of this is the templates that we have, in particular the role that Miroverse plays in all of this.

(01:13:49):
Just to give you an example here, there was a template which was created around FIFA World Cup, so there was a FIFA World Cup diagram. Cornelius, he's the founder and managing director of a Canadian strategic service design consultancy firm. He created this Miroverse template and it had over 100,000 views and about 15,000 copies were made of the single template. Given the popularity of all of this, it actually got indexed by Google. When you went in the search, you actually saw the Miroverse FIFA template show up when you were trying to search for FIFA World Cup, and that was another sort of acquisition channel top of funnel that actually drew a lot of users to it. So I think I would say the Miroverse is also a key accelerant to this.

Lenny (01:14:45):
If you had to think about the pie chart of how Miro grows, what percentage roughly would you say is word of mouth, organic, versus what you just described, which is essentially a CO versus sales, outbound sales? How do you think about that? Is there a way to model that simply?

Varun Parmar (01:15:02):
Without getting into specific numbers and stuff, I would say fundamentally Miro is a product-led growth company and product channels are one of the highest contributors for growth of users. As the business has evolved to serve the needs of some of the largest corporations in the world, the enterprise segment and the enterprise persona when they're trying to provision Miro for tens of thousands of users who then go conduct hundreds of thousands of workshops on Miro that invite millions of users on the platform, is a key part of the flywheel that we are seeing. I would say product channels are probably very strong and increasingly enterprise is a key part of that acceleration.

Lenny (01:15:53):
A great segue to our final question, which is the idea that you started a product growth, sounds like clearly it's a big part of growth today, but as every product growth company does eventually you have a large sales team, I imagine, what have you learned as a product leader working with sales, especially at a product growth company about how to make that relationship work and have a product work effectively with a sales org?

Varun Parmar (01:16:15):
There are a few learnings and I would say maybe this is one area where we are working on how we could be doing better in terms of bringing ourselves closer to our high-touch and bringing high-touch closer to self-serve, in terms of how we operate overall. It's a lot of hard work, I would say first of all, basically, to bring both of these organizations together and you have to be very deliberate around the points of intersection and you have to make sure that these organizations don't consider themselves as competition. It's one product, one company, just two channels of how we are serving our customers. There's some things that we've done which is have the product marketing team that basically works across both of these functions and make sure that they are bridging what we are hearing from the sales organization in terms of what directly customers need on the enterprise side, and then what do we need on the self-serve side.

(01:17:23):
There's a full process in terms of how the handoff happens across the maturity of the account. It can start as a self-serve, it drives adoption, and once there's adoption, there's a hand raiser that happens and then there's a sales rep that gets engaged and you go through the qualification process and then you have an opportunity to expand the account. We've over the years sort of architected and built the entire funnel and what the process is, and that's also sort of a key part of how all of this operates. But like I said, I think there are a few areas where we could further streamline how we operate and think of it as one single unit.

Lenny (01:18:05):
I imagine that is true for every company out there.

Varun Parmar (01:18:07):
Yes.

Lenny (01:18:09):
One maybe final question before we get to our very exciting lightning round. What are some features that people could look forward to that are coming with Miro?

Varun Parmar (01:18:19):
We recently, about a month ago, announced Miro AI, the backdrop of all the amazing work that's happening around generative AI and large language models and stuff. I think it was really, really exciting to see all of the community enthusiasm around the use cases that we launch. So we're going to be taking it across the finish line and doing a general availability in the coming weeks and months. I think that's one big thing and we'll be adding more capabilities there. Just today we actually announced a bunch of really deep enhancements and updates around how Miro can be used for team rituals and agile practices. Now you can actually do retrospectives in Miro where you can have a private mode where while Lenny's typing his feedback during retrospective, nobody else can see it and then one click you can reveal it. I just saw some of the results of the feedback and it was rated as the number one feature people saw.

(01:19:14):
There's also some deeper integrations in terms of bringing an entire program board from Jira to start to do dependency mapping inside of Miro in a fun and collaborative way, to use this dependency mapping along with program board to start to do program increment planning, which is essentially scrum of scrums or big room planning that's happening. There's some really amazing capabilities that we've added there, which is on the backdrop of some of the updates we've made in terms of estimation of sprint story points and so on and so forth. Now there's a whole plethora of capabilities and apps that are available as part of the platform that allow you to have your entire team conduct your team rituals in Miro and you can automate certain things, you can streamline things, you can do certain things in async and then do the rest in synchronous ways, so I think that's been a big update as well.

Lenny (01:20:12):
Amazing. With that, we've reached our very exciting lightning round. I've got six questions for you. Are you ready?

Varun Parmar (01:20:19):
Yes.

Lenny (01:20:20):
All right, let's do it. What are two or three books that you have recommended most to other people?

Varun Parmar (01:20:26):
One is, I love this, When Breath Becomes Air by Paul Kalanithi. It's one of those really emotional books that at the end of it, you might have tears in your eyes, but really, really amazing. We talked about Frank Slootman's Amp It Up, and then Satya Nadella's Hit Refresh. I think philosophically some of the things that we talked about today are inspirations that I found in some of these books.

Lenny (01:20:49):
What's a recent favorite movie or TV show?

Varun Parmar (01:20:52):
Ted Lasso. I don't know if it's a recent one or not, but something-

Lenny (01:20:55):
It's a new season.

Varun Parmar (01:20:57):
Yeah, I've enjoyed a lot. I think it's a very positive and uplifting message. I think the performance is huge. It's humorous, the characters are well-developed, so I think overall it's a treat, at least for, me to watch.

Lenny (01:21:13):
What's a favorite interview question you like to ask?

Varun Parmar (01:21:16):
I actually ask a math problem. For those of you who interviewed with me, I have this math problem, which is based on how Adobe created its first Creative Suite bundle. I was actually part of the team that came up with the pricing and packaging for the first Creative Suite post-acquisition of Macromedia. It's a math problem that allows you very quickly to figure out people in terms of their problem-solving skills. Usually I give that problem to people. I've given it to, I don't know, 700, 800 people, so I now have a very, very well established standard distribution of how long it takes for people, where do they get stuck and where they've gotten stuck, for those people I've hired, what evidence do I have in terms of using that as a framework in terms of them being able to solve things? So that's my favorite question.

Lenny (01:22:08):
So you're saying you've mapped back people that have done a certain way on the problem with their success and you've kind of found that it's a good signal of their performance?

Varun Parmar (01:22:17):
Yes. Not directly, but yes, correlation and stuff.

Lenny (01:22:21):
That's amazing. That's one of the biggest problems with interviewing. You think you're asking all these amazing questions and it's such a good signal, you have no idea. No one goes back and is like, "Oh, this person sucked. This person didn't... " That's really cool to get that much data on that one question. Two more questions for you. What's something relatively minor that you've changed in how you do product development that has had a tremendous impact on your team's ability to execute?

Varun Parmar (01:22:44):
We talked about some of that, sort of removing the roadblocks. I think having this motto of great customer value faster with high quality, just the simplicity of that and it's actually part of our evaluation rubric, it's part of how we measure ourselves and stuff. So I think just coming up with these simple concepts that you can rally the organization around, and I think it's still a work in progress, but something that I believe is leading to positive outcomes.

Lenny (01:23:07):
Final question. What's your favorite Miro template?

Varun Parmar (01:23:10):
It's the FIFA World Cup actually. I am so fascinated with what was done. Yeah, it's the latest one, but I think there's a bunch of them in terms of retros as well, and I think... like your template as well.

Lenny (01:23:21):
Amazing. We will link to all of those. Varun, this was amazing. Everything I expected and more, your team is as interesting and unique as I thought, and I am excited for people to learn from you and we're going to share a lot of links alongside this episode in the show notes. Two final questions, where can folks find you online if they want to reach out and learn more, and how can listeners be useful to you?

Varun Parmar (01:23:43):
Thank you, Lenny. It was a lot of fun. I enjoyed our interaction. You folks can find me online on LinkedIn. I think that's probably the best way to connect with me. I think in terms of one or two things I can ask everyone is that, one is if you are an existing Miro user and you use the product for something interesting, I highly encourage you to contribute it as a template as part of Miroverse. There's a lot of folks who use that and we would love for you to contribute there. The second thing is, I know a lot of product development teams, PMs and designers are big fans of you, Lenny, so those are also the users that use Miro. If there's anything we could do to make the product better, if there's things that you feel like we can expand the platform into, we would love to hear from you and just reach out to me directly over LinkedIn, direct message or connect with me there and yeah, and let us know. We're here to serve.

Lenny (01:24:40):
Amazing. Varun, thank you again for being here.

Varun Parmar (01:24:43):
Thanks, Lenny. Awesome.

Lenny (01:24:45):
Bye everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcast, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review, as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

---

## An inside look at Mixpanel’s product journey | Vijay Iyengar
**Guest:** Vijay  
**Published:** 2023-01-26  
**YouTube:** https://www.youtube.com/watch?v=t-2oXtZrlEc  
**Tags:** growth, retention, onboarding, churn, metrics, okrs, roadmap, prioritization, analytics, funnel  

# An inside look at Mixpanel’s product journey | Vijay Iyengar

## Transcript

Vijay Iyengar (00:00):
The issue for us at the time was that we took people away from the investment in our core product to go do those other things. We moved people, right? And so the trap there is that you leave yourself right for disruption in your core because someone else can out invests you in that core. And so if you are the leader in some core product, our takeaway here is you should continue to out invests everyone else in that core and then invest the profits that come out of that core into the next venture. Invest profits and not people, or venture capital, which is maybe net present value of profits or something to that effect. But don't take people away from the core to go to these other things because then you end up distracted.
Lenny (00:40):
Welcome to Lenny's Podcast where I interview world class product leaders and growth experts to help you get better at the craft of building and growing products. Today my guest is Vijay Iyengar. Vijay is currently head of product at Mixpanel. He actually has a very similar career trajectory to myself where he started as an eng intern at Amazon. Then he was an engineer for a while at Uber, then he became an eng manager at Mixpanel. But then he shifted from an ENG manager to director of product, and now head of product at Mixpanel. You don't often see people moving from an leadership role straight to director of product, so it was really interesting to hear what he took from his eng experience and brought into his approach to product leadership. But we spent the bulk of our time talking about what he's learned from the journey that Mixpanel has been on, where they started with a simple product, then scaled to a number of different products, solving many problems for customers, and then made the hard decision to scale back to just a single core focused analytics product.
(01:33):
We talk about why they made that choice, what they learned about when it makes sense to expand a new product and when you probably shouldn't, and how they approach that organizationally. We also talk about how Mixpanel builds product, how they think about products philosophy, how they prioritize, and also what you're probably doing wrong in how you set up your analytics for your own product. With that, I bring you Vijay Iyengar after a short word from our wonderful sponsors.
(01:56):
This episode is brought to you by Pando, the always on employee performance platform. How much do you love the performance review process? Yeah, it's time consuming subjective bias, and there's rarely any transparency. With the rapid shift to distributed work, it's a struggle to create the structure and transparency that you want to help your employees have the highest impact and growth in their careers. Pando is disrupting the old paradigm of performance management, including a continuous employee-centric approach so employees stay engaged, see their progression in real time, and know exactly when and how they can level up. With Pando, managers can leverage competency-based frameworks to effectively coach and develop their teams and align on consistent growth standards, resulting in higher quality feedback and higher performing teams. Visit pando.com/lenny for more info and get a special discount when you sign up and reference this podcast. That's pando.com/lenny.
(02:54):
This episode is brought to you by Notion. If you haven't heard of Notion, where have you been? I use Notion to coordinate this very podcast, including my content calendar, my sponsors, and prepping guests for launch of each episode. Notion is an all-in-one team collaboration tool that combines note-taking, document sharing, wikis, project management, and much more into one space that's simple, powerful and beautifully designed. And not only does it allow you to be more efficient in your work life, but you can easily transition to using it in your personal life, which is another feature that truly sets Notion apart. The other day, I started a home project and immediately opened up notion to help me organize it all. Learn more and get started for free at notion.com/lennyspod. Take the first step towards an organized happy team today, again at notion.com/lennyspod. Vijay, welcome to the podcast.
Vijay Iyengar (03:52):
Thank you, Lenny. Great to be here. Huge fan of the pod, and so glad I can contribute.
Lenny (03:57):
I definitely want to talk about Mixpanel's journey both as a product team and a product. But before we get there, as an engineer, you were in a longtime engineer and then you became a product leader, is there anything you had to unlearn as an engineer in the way you thought about leadership and product and business?
Vijay Iyengar (04:13):
One of the things after you've been in engineering for a while is that develop this tendency to immediately respond with no to new ideas. And I think from the engineering perspective, this is because you spend a lot of your time building and maintaining ideas that maybe are half thought out or didn't really go anywhere, and you just feel like the full brunt of the maintenance cost of that. And so you build up the scar tissue and this immune response to say no to new ideas, and it's a hard no, like no, we're definitely not going to do it. And I think I had to unlearn that moving into product because you get a lot of ideas coming from a lot more places in the organization, and ideas are fragile in their agency and it's a hard no can really kill a whole direction that you could potentially go.
(04:55):
They could be very high reach and high impact. So, one thing that I've found is the best way to get to a no, if you ultimately need to get there, is to try to make it work. Start trying to make yes work and document how you've tried to make yes work. And do that earnestly, not as an exercise of just an alternative that you're considering. Try to do it sincerely and get to know after trying to make yes work. And so that's one thing I've been trying to just apply my engineer problem solving brain to do that instead of thinking about how it might not work and saying no.
Lenny (05:25):
Is that something that you recommend engineers work on looking back? I know as a PM, it's like, oh, I love when engineers say yes. This is awesome. I'm going to actually help everyone learn to say yes. But as an engineer, obviously that's a challenge often. What do you recommend to folks that are engineers currently that maybe want to improve on this or shift in how they think about saying yes, saying no when they're asked about something new?
Vijay Iyengar (05:48):
I think some of the best engineers that I've worked with actually already do this, but [inaudible 00:05:53] they're able to balance both in their head. So, ultimately this balancing act, you just want on-call, you were woken up three times at 3:00 AM due to various bad ideas, and the next morning you wake up and then stand up, it's like, "Hey, can we do this new thing?" You kind of have to have that empathy and do that. So yeah, I think the exercise is just take 10 minutes to consider the idea and just sincerely consider how might we make it work. And if at the end of those 10 minutes, it's like futile and there's no path, it's fine to say no. And it's a good instinct to say no, actually in a lot of cases. But yeah, I would recommend that to engineers. I think it would've been better in my career, for sure, if I had learned that sooner.
Lenny (06:26):
I want to spend some time on the Mixpanel product journey. It's been an interesting rollercoaster. I think the company's been around for how many years? Since 2010? 2009?
Vijay Iyengar (06:34):
20009, yeah.
Lenny (06:35):
So, I know it started as kind of a very simple product analytics product back in the day. And then as you do with ambitious companies, you look for more problems to solve. You look for more problems to solve from your customers. So as I understand it, you guys added a lot more products to the suite of Mixpanel products. And then I know that there are some challenges with scaling that, and maybe the products didn't stick as much as you're hoping. And what I understand is recently, you moved back to just the single core analytics product. And so I'd love to just hear that journey of what that process was like, what you learned as a product leader and as a company about scaling, expanding, trying to solve a lot of problems, and then coming back to one core straightforward problem.
Vijay Iyengar (07:15):
Mixpanel started in 2009 as provide product analytics to EPD teams. And I think early on, it saw a lot of success because it built this in-house database called Arb, which stands for arbitrary segmentation. And that was necessary because events data, which is the fuel for product analytics, is few orders of magnitude larger than most other types of data that people collect, and so you need a specialized approach to deal with it. And so that I think spurred the first wave of explosive growth, because product analytics was a really burning problem at the time. People were shipping mobile apps like crazy and they needed a solution that could scale, and that was kind of a durable mode for Mixpanel for a while. And I think because we had this SDK that was installed in so many apps and we had this really scalable event collection and analytic interface, it was just natural to expand into a few adjacencies that would leverage those same technologies.
(08:04):
So, the first one was messaging, being able to send targeted messages to users, which is something that's fairly natural, you might want to do, especially if you have an SDK already installed. Yeah. The other aspect that we've added into was data infrastructure and trying to be the single source of truth of data in companies. And what ended up happening was that by 2018, we had this big churn problem. We had something like 40% churn, revenue churn, our core product. And when we dug into, it wasn't that people were churning because they didn't need product analytics anymore. They had the need. They were just churning to competition because we were just not up to the market in terms of the features we had in our core. And when we dug into why that was, it was just that we had a 50% engineering team that was building products across three domains, product analytics, messaging, and data engineering stuff.
(08:52):
Our engineering team was just spread too thin to address all of those core gaps in functionality. And so we made a really hard call at the time. We said the hard no to those two other categories and decided to focus our entire engineering team on closing the gap on product analytics and innovating there. And from a process standpoint, how we operationalize this was we threw away all our planning and all the execution and that we work that we'd planned to do so far, and we did something very simple. We took all the churn reasons that our customer success and sales teams had been painstakingly collecting for years, grouped them by category, which was roughly product features we needed to build, sorted descending by ARR, took the top 10 things and made that our roadmap, just give every engineer direct access to customers and give them a bucket to go work on, which I think goes against about a million product best practices out there of just doing that.
(09:41):
But I think given the context at the time, we needed to optimize for speed, and speed comes when you have extreme clarity on what you want to do and focus. And so we really just optimize for speed in that time. And so in that first year we moved really quickly and we shipped something like a hundred features in that year and closed a lot of gaps. Again, these are all vanity metrics. Measuring number of features doesn't mean anything.
Lenny (10:04):
And what year was this by the way?
Vijay Iyengar (10:06):
This is 2018 to 2019.
Lenny (10:09):
Got it.
Vijay Iyengar (10:09):
Yeah. So, we moved really fast shipping all these features and instantly saw the improvements to win rate and to retention. But one of the cracks that started to emerge was we neglected the holistic design of our product at the time, right? And if you're shipping features that quick leads, you don't have time to stop and think, where does this go, and how does this fit into our overall system architecture? And what started to happen was that we were hitting diminishing returns with some of these features. And not considering the holistic design and consistency meant the reach of every feature was low. You had to rebuild it for every part of the product that we were in. And so at the time we made... We spun up the second stream that was very design led. And I think this was also coincided around the time we adopted Figma, and it's a really broad design at seat at the table of the company, and we just set up this goal to make design one of our key differentiators.
(10:53):
So, this design driven initiative was really about how can we think about the system architecture of our product? What are the key building blocks of Mixpanel? Where do they need to fit? How few of them can we have, which is a really important step? And then how will users discover them and how do they relate to each other? But I think this realization was born out of the fact that so many great products win or lose based on their architecture. I think Notion, for example, that pages in blocks architecture is so strong, and you can hang so many features off of those core building blocks in a way that has such high impact on region and discovery of those features.
(11:26):
So anyway, we did that in parallel with the.... And continued that grind on core jabs. And so the end result of that phase, which is from 2018 to maybe late 2021, 2022, was our retention went from about 60% to 90%, and our NPS went from 16 to 50. So I think, yeah, there's a lot in there to unpack, but refocusing on the core really helped us achieve those results.
Lenny (11:52):
Got it. Yeah. I have a lot of questions about this. So interesting. So, that phase that you went through where you sorted things by potential ARR, was that the phase of expanding to multiple products or that was post we're going to focus on analytics and go all in there?
Vijay Iyengar (12:06):
Oh, that was post focusing on analytics.
Lenny (12:08):
Okay.
Vijay Iyengar (12:08):
Yeah. Yeah.
Lenny (12:09):
And you're saying that you had a stream of just builds all the features that were lacking that are causing customers to churn, and in parallel, there was a track of let's build this product, such that it all connects and works together well and it's really well thought through long term?
Vijay Iyengar (12:24):
The first thing, I might have made it seem like it was just the buckets were features. We did take the step of turning them into problems and being clear, exposing engineers directly to the customers that had those problems and then invent a solution to solve them. So I mean, loosely there were features involved, but a lot of them were kind of core problems we needed to solve.
Lenny (12:40):
That first approach is so interesting. It's kind of like, yes, we will make more money if we focus on these features. To your point, it ends up being just a bunch of features and products that kind of maybe don't synergize. Looking back, was that a good idea to approach it that way, at least for a while?
Vijay Iyengar (12:54):
It highly depends on your context. In a very competitive context where there are just table stakes features that customers need and that it's been validated by the market, you need to optimize for speed more so than anything else. But it is an approach that outlives it's usefulness pretty fast, and we've put that approach behind us relatively quickly after that phase. And I would actually say that design driven phase was the next phase, where it was, okay, we're not bleeding on the table stakes anymore, but we want to make a holistic product that has high reach, high impact on the features and is actually usable. And so that was I think a follow-on phase that's necessary. Obviously, depending on your particular circumstances and competitive dynamics, you can sequence them differently, but I think it was the right call to just... Sort of the on-call thing again where when you're in trouble, you got to get out of trouble. You can't mow your lawn while your house is on fire. You kind of put out the fire and then deal with everything else.
Lenny (13:47):
Yeah.
Vijay Iyengar (13:47):
So, that's kind of the approach we took.
Lenny (13:49):
What's an example of a feature or product that you launched within that first track? And then what's an example of something that came out of the designer led approach, if anything comes to mind?
Vijay Iyengar (14:00):
I think out of the first track, oh man, there's so many that were just core. We didn't have a good cohorts product at the time, just being able to create behavioral cohorts users and create them from any report that we built, right? And I think that, I mean it's just table stakes and analytics to be able to do that. So, that was one of the first things we built, and it was fairly obvious. There's a lot of other things in more advanced types of funnel analytics and a flows and visualization that was really interactive. I think on the design-led phase, the biggest thing I think was visualization consistency and making our charts interactive in a consistent way across our entire product. And so there's two things that enabled. One was that every time we added a new visualization or a new enhancement to a visualization or how something is sorted in one report, it just instantly applied everywhere.
(14:46):
So, just the reach was multiplied for everything we added. And the other thing is it just made the product more accessible, let us add dark mode. So, it made our visualizations really stunning and really easy to see what the takeaways were. And then every new visualization we added inherited all those benefits.
Lenny (14:59):
I'm trying to think about being at a company that goes through this phase of, "Hey, we're just going to build a bunch of stuff that we know we need." And it feels like hearing it, it's like, "Oh yeah, and then we're just going to make it all look great and connect and work well." I imagine that wasn't planned, and I imagine that wasn't easy to get people to maybe slow down on just building more products and features or push it in a direction where it's all going to make sense. Can you talk at all about what that process was, how hard it was to shift from we're just going to knock through all this checklist of things to let's just bigger, let's slow down, let's spend a lot of time designing?
Vijay Iyengar (15:35):
It was definitely more messy internally than I described it. One of the key junctures was when we had this really talented design team and we were putting them on these very tactical projects that was, frankly, that was very engineering led, right? And design would often come in at the end and be asked like, "Hey, can you just make this look nice and put some pixels on it?" And it's just such a waste of your design team to have them do that. But at the same time, the pace was so high that they didn't have time to come up for air and do anything else. And so there's actually this moment where I was an engineering manager at part of this.
(16:05):
And had a meeting with our BM and our head of design at the time, and we said, "Hey, we can actually do the next three months of projects about any design," which was a kind of controversial thing to say, "but we're doing this so that you can take three months with a set of designers and go think about the system architecture of the product, and we'll wait for that to be done before we do any architectural things that might impact the architecture." And I think that gave designers a bit of breathing room to go do that, just separating them for a bit from the tactical fire. Because what was happening instead was we would get towards the end of the project, bring design in, and they would use each project as an opportunity to squeeze in like, oh, and we can simplify here. And that's just a classic way to blow up scope at the end of the project because there wasn't a dedicated space for design led projects.
(16:48):
And I think that that was kind of a key friction point that we ultimately had to decouple for a bit, and then regroup and say, "Okay, now we'll look what's our strategy," and just take on projects purely for the sake of improving consistency, reach depth of our UX.
Lenny (17:02):
Also, looking back, the process you went through adding a bunch of products to solve more customer problems, something every founder and product team thinks about, when should we add new product lines? When should we expand beyond the core? I'm curious what you take away as a lesson and what you'd advise other founders and companies when it comes to when is the time to expand and think about a new product and a third product and a fourth product?
Vijay Iyengar (17:28):
I don't know if there's a hard and fast rule here. I can just maybe say what made sense and didn't make sense in our context. The issue for us at the time was that we took people away from the investment in our core product to go do those other things. We moved people, right? And so the trap there is that you leave yourself ripe for disruption in your core because someone else can out invest you in that core. And so if you, you're the leader in some core product, our takeaway here is you should continue to out invest everyone else in that core, and then invest the profits that come out of that core into the next venture. Invest profits and not people, or venture capital, which is maybe net present value of profits or something to that effect. But don't take people away from the core to go to these other things because then you end up distracted.
(18:10):
And the other aspect of that is that those secondary products we took on were in categories of their own. And it's really tempting and you'll often get dragged into accidentally entering another category, and then you'll end up building these bolt-on products that are the best in their category, right? And the adjacent categories for analytics are CDPs or message targeting or feature flagging or something, but there's not that many people that need the sixth best CDP or the eighth best feature flagging or the 10th best message targeting tool. And it ends up being, in aggregate will contribute five to 10% to your revenue, won't seriously accelerate your growth rate, and then takes engineers away from the core product. And so those were the circumstances that we were.
(18:50):
And I think if you're seeing churn to your competitor on your core product and you're not best in class on any of the other ones, then maybe it's time to reevaluate. And then the last thing I'll say there is that it's also 10x more painful than you think to cut mild successes than anything else, and just organizationally painful. And there's teams that have whole roadmaps, and it's a really painful experience, so you have to think really hard before you kick those off.
Lenny (19:18):
That is really, really insightful advice, makes me think about if you bundle good enough solutions, there needs to be kind of this anchored tenant that I will not give this thing up and I'll use the third best version of something else, if you have it. But if you're not that valuable and important, you're not going to convince people to use something because they're competing against the best in every category.
Vijay Iyengar (19:39):
Exactly. Yeah.
Lenny (19:40):
That is really interesting. I've been doing this kind of series on how different companies approach building product and I have a few questions I'd love to ask around the product development process and Mixpanel.
Vijay Iyengar (19:50):
Sure.
Lenny (19:51):
The first is just like, how do you plan? How do you plan? I know it evolves, but just how do you plan currently? How long are your planning cycles? How far ahead do you plan in detail? Do you use OKRs? Maybe let's start there, those three kind of sub-questions.
Vijay Iyengar (20:04):
We have these unsolved problems and analytics that we're going after. For us that’s like, people always want more power, more simplicity, better data trust, faster onboarding, better collaboration, better price performance. And so we largely organize our teams around those problems and those missions. One quick aside there is that some of those problems have attention with each other. Power and simplicity, there's a trade off there, right? And we want one team to own both, so that they're kind of forced to confront that tension and beat that trade off. And so that's kind of how we think about generally our product team, is these cross-functional EPD teams, each of which that's focused on solving these long-lived paired problems for customers [inaudible 00:20:41] our core analysis team focused on that power, simplicity, trade off problem. In terms of planning, the way it works is that we plan on a six month time horizon. And I can talk about our most recent planning cycle actually, because we're just completing it.
Lenny (20:53):
Yeah, let's do it.
Vijay Iyengar (20:54):
Yeah, basically it started out with this strategy memo that our leadership team wrote that basically just conveys this is where we want to go as a company in the next year, and here's how the product team can contribute most of that and just established these key pillars. We shared that with the teams, and they took that and also combined that with all the quantitative and qualitative context they're constantly consuming about the problem they're working on and our customers, and ideated and developed the series of bets for the next six months, which I think are some extent similar to OKRs, where ABET... The anatomy of ABET is that it's problem we want to solve, our hypothesis on the solution, and then some plan to win, some plan to actually get there and a way to measure that you got there.
(21:32):
And I think one of the unique things that we did relative to other companies that do planning is... I think it usually is sort of this W process of there's the strategy memo, and then teams generate bets and there's a review, and then they go back and I iterate and then they finalize. And we kind of collapsed the middle part of the W where myself and our head of design actually spend time with each of the teams actually ideating on the bets and participating in the solution discovery process, going into the jam sessions and adding fig must keys ourselves with ideas and thoughts on things, which we did because we aren't a huge product team, and we are not going to do 50 things and a half. We're going to do maybe 10 to 12 things.
(22:12):
And so that's enough that we don't... We can do something that doesn't scale if that enables high bandwidth communication between us and the teams. And it ends up being more messy and unstructured ABET in that phase because we're in there contributing ideas as well. But by the end of it, I think the team leaves feeling both more competent in their bets because there's more thought that's gone into it, and then more aligned top to bottom line why we made certain decisions. And so I think that that's one thing that's different. And then we conclude that process with the roadshow where we presented the rest of the company, and then get their feedback as well.
Lenny (22:41):
How long is this process generally?
Vijay Iyengar (22:43):
The teams did pre-work for a couple of weeks, like two weeks in December, and then we did a two week sort of sprint on solutioning and ideation in January, the first two weeks of January.
Lenny (22:53):
Awesome. And what's the end result of planning for each team? Did they deliver a document with, here's our strategy, here's the big bets, here's a roadmap? Is there a template you pass around? How do you get to a thing that people share and present and comment on?
Vijay Iyengar (23:10):
Yeah, I think there's basically three artifacts that are kind of linked to each other. So, the first is we use Notion, and so we have a database in notion called bets, which is where each page in the database is [inaudible 00:23:22]. And that has a template, yeah. So, it's kind of roughly what I described with a few more sections of what problem we're solving? What's the evidence of demand? What's the region impact of this problem? How do we know we're successful? And then what's the key driving hypothesis behind the solution? And then a rough line. And then that's tied with a presentation that's kind of like a tight summary of that that has one slide per bet, and then is also tied with more of an execution focused, how do we sequence and staff this thing and eliminate dependencies, which the engineering team contributes to. So, I think those are the three artifacts that are linked together.
Lenny (23:54):
This episode is brought to you by lemon.io. You achieved product market fit, you're able to activate, engage and retain your customers, but you don't have the engineers that you need to move as fast as you want to because it's hard to find great engineers quickly, especially if you're trying to protect your burden rate. Meet lemon.io. Lemon.io will quickly match you with skilled senior developers where all vetted results oriented and ready to help you grow, and all that At competitive rates. Startups choose lemon.io because they offer only handpicked developers with three or more years of experience in strong proven portfolios. Only 1% of candidates to apply get in, so you can be sure that they offer you only high quality talent. And if something ever goes wrong, lemon.io offers you a swift replacement so that you're kind of hiring with a warranty. To learn more, just go to lemon.io/lenny and find your perfect developer or tech team in 48 hours or less.
(24:51):
And if you start the process now, you can claim a special discount exclusively for Lenny's Podcast listeners, 15% off your first four weeks of working with your new software developer. Grow faster With an extra pair of hands, visit lemon.io/lenny.
(25:08):
I know you have some insights on prioritization and some strong opinions on how to prioritize. Can you talk a bit about that and how you advise your product teams to prioritize?
Vijay Iyengar (25:17):
One really common framework in prioritization is RICE, reach, impact, confidence, effort. And I think it's simple and fairly robust, which is generally good qualities of a framework. But one of the traps with RICE that we observed is that the C and E, the confidence and effort tends to cause you to prematurely deprioritize potentially high reach, high impact bets, really innovative things. And we encountered this on one of our teams early last year were we just RICE'd everything, all the ideas, and a lot of the high reach, high impact things ended up at the bottom because confidence and effort were just so murky for them, as they should be typically for high reach, high impact ideas.
(25:55):
And so one exercise that we push our teams on is just ignore the C and E for a little longer than it's comfortable, and just sit with those high reach, high impact ideas with engineers and designers in the room committed to actually trying to solve them. Give it a fair shot. And you'll often find if you spend a week on that set of ideas, you can get pretty far in understanding the confidence and the effort. You can probably find a higher confident lower effort way to do them. Then add the C and E back in, and then RICE as usual. And the goal is to end up with a reasonable mix of innovative bets, incremental bets, and then ones that are technical debt or product debt that you need to address.
Lenny (26:31):
I usually just cut out the C myself. I find that it's not that powerful. Do you do this in a Google Sheet? Do you use this in Notion? How do you actually recommend teams do this prioritization, or just eyeball it?
Vijay Iyengar (26:43):
I'm not super opinionated on the exact tools that teams use. I think this is a team local exercise typically, but most teams use Notion and just simple tables or databases in Notion-
Lenny (26:51):
Sweet.
Vijay Iyengar (26:52):
... work fine for this. I think the other thing on prioritization that's always tricky is estimation. And every engineer will value you estimates are all lies, and if you say it'll take eight weeks, it'll take eight months. But I think the core problem with estimation is you're asked to estimate things before what the thing is, and it's just a strange output to be expected to produce. And one approach that I found really interesting is from this book called Shape Up by Basecamp, which this idea of appetite overestimates, where instead of making the estimate an output of planning, you make the time box or an appetite the input, and you say, "We want to solve X problem and we're willing to invest six weeks solving that problem."
(27:31):
The obvious question there is how do you pick that time window? It just seems arbitrary. And so the base camp people suggest just pick six weeks for everything, and they're really austere about if you can't scope hammer something down to six weeks, you're doing it wrong, which I think is... It can work and has a lot of benefits if you creates a rhythm in your company, but one approach I found that works better is pick a reasonable sounding appetite and just explore the two to three options around it. Pick six weeks, and then say, "What would we do differently if we only had four weeks or eight weeks?" And you'll kind of naturally find the efficient frontier of cost and impact, and then align on that. And the important thing is that you check in after that time period and say, "Is there any new information that's just we should continue? Did we uncover the biggest risks, and are we just on the long tail of things?" And actually be honest with yourself about that. I think that's important regardless of what framework you use.
Lenny (28:23):
I really like that. So, is that how you actually operate, you create a time box, we have four weeks for this project, whatever we get done, we ship whatever we don't, we push out?
Vijay Iyengar (28:30):
We operated that way in engineering, particularly on the infrastructure side, because we have this series of projects that would just take forever, and the longer it takes, the longer it's going to take. And so we've done that exercise quite a bit. I'd say more on the more engineering heavy projects than others, but we're starting to adopt it more in the product side as well. The main exercise we've taken on the product side is more the consider, what would you do differently with different time boxes approach?
Lenny (28:56):
Just a thought exercise.
Vijay Iyengar (28:58):
Yeah, it's a good thought exercise. Then it just forces everyone to truly score the requirements. Critical, nice to have, is nice, but really if in two weeks, you're going to get pulled off to do something completely different, what would be a complete solution that addresses the core problem. And it forces you to peel the meat of the problem in first, as opposed to just doing the things that are surrounding it.
Lenny (29:17):
That's cool. I really like that. I've done that myself. I'm curious if anyone ever does the shape up process for real or it's just like we will ship anything that is ready within six weeks and not actually have specific deadlines or kind of concrete goals of products they need to ship in specific ways.
Vijay Iyengar (29:32):
Yeah. Well, I think the shape up process, if you run it all the way. They do... Their idea is that you can actually predict on a six week time horizon. So, you can just hammer down scope to something that is complete. It needs to be complete. It can't be milestone one that's like a half baked thing in six weeks, which I think that rigor... The rigor they applied to that across the board, you need to do it all the way. You can't adopt the process halfway. I think the is the challenge. Otherwise you end up with people shipping milestone one and then moving on, which is not the complete product.
Lenny (30:01):
Makes sense. A couple more questions around how you build product. You mentioned that you have a unique approach to keeping product teams close to customers. And I'm curious what you've learned there, what you found to be helpful and just kind of keeping product teams close to your customers.
Vijay Iyengar (30:15):
I think this is one thing that is something we invested in pretty early on at Mixpanel. Actually around that time, in 2018, when we refocused on our core product, one of our sales engineers, Aaron, built this automation where he piped all these customer gaps that we got that were reported by our customer success and sales teams, piped that into Slack and just a feed. And what this created was this culture where all engineers and designers could consume that raw feed of direct points of customer with no gatekeeper, no process to access it, no pre-aggregation, right? And I think this scale's pretty far. At a product team of our scale and with our reach of customers, we don't get so much feedback that someone couldn't read it in 20 minutes every day. And for four or five years in engineering, every day I would read all the gaps that we got, and many engineers would do that.
(31:04):
And one of the rituals that it's enabled is we'll find that engineers will go into that channel and react with a message with an email emoji, which means I'm going to email this customer and find out more, right? And they'll just email the customer and say, "Hey, I'm the engineer that built this feature. I saw you said this specific thing. Can you tell me more? I'd love to understand." They ask the five why's, and then they improve the product on their own. And I think that culture is just so important, and it just empowers all engineers and designers to think a PM a little bit, which I think takes a little bit of a load off on the PM to be the gatekeeper of all that information.
(31:39):
And then over time, we've evolved it quite a bit as our data stack stack's involved. So, we now not just take customer requests, but we take things that are posted on Twitter and NPS survey feedback and win loss notes from our competitive deals and pipe them both into Slack and into Notion so that we can both get the realtime feed, and then we can sort and aggregate and tag things accordingly. But the key artifact of this is that it's all open. There's no gatekeeper behind that process.
Lenny (32:04):
That sounds both amazing and wild. Do you still allow engineers just to email customers and ask them questions about this stuff, or is that harder to do it as you've grown?
Vijay Iyengar (32:12):
Oh no, we still allow that. Yeah.
Lenny (32:14):
Wow, that's awesome.
Vijay Iyengar (32:15):
One nice thing about the stack actually, the data stack, is that... So, basically all these feeds information land in our data warehouse, which is BigQuery. And from there, they're pushed out via a reverse CTL tool we use called Census to Slack and Notion that make the note code. But one of the benefits of that is that we can enrich all of these feeds with who's the account? What's their ARR? Who's the CSM? And all that other contact information. So, it's usually not an engineer's blindly reaching out to a customer without letting a CSM know if it's a million dollar account or something. The idea is just trust them with that context, and they can tag the right people and make the right call on that.
Lenny (32:50):
I'm so curious how that gets prioritized and how PMs are looped into all that, but we don't have to get too deep in that. That's a really cool process. I haven't seen that before. Our engineers were just emailing customers, digging into questions and problems.
Vijay Iyengar (33:01):
The trap of course is what you just called out is you can't be reacting to everything all the time. And certainly if you ship a redesign, the first two weeks of that, there's going to be a bunch of feedback that's like, I hate this. Go back. And I think that's sort of an organizational muscle you have to build, balance the reaction, and that's just a thing we've had to practice doing, but I think the trade offs are worth it.
Lenny (33:20):
Awesome. One last question along these lines, can you just talk about the tools you use, the SaaS products you use to run your product team for collaboration, communication, notes, docs. You mentioned Notion as an example.
Vijay Iyengar (33:31):
I think our stack is actually fairly standard these days. So, we have Slack, Zoom for communication, Notion for docs and any long form writing, and it's a [inaudible 00:33:42] database, and Figma and FigJam for design and whiteboarding. I think what's actually more interesting is our data stack and the productivity we get out of that. I briefly touched on this, where basically all of our data gets EPL'd out of all the systems we have, lands in BigQuery, gets joined and modeled, and then pushed out via census to all the other tools in our stack. And I think that's been a huge productivity unlock because you can build internal tools with very little code. If you can write SQL, you can build an internal tool basically, and that pushes information to the teams that need it. And so that, I think, just has unlocked a lot of these types of things like automating qualitative signals with no code in a reliable way.
(34:22):
And then if someone like, "Oh, can I get ARR on this?" Yeah, sure it takes two seconds to do that. So, I think that data stack has been a huge productivity unlock for us.
Lenny (34:29):
Awesome. Have you guys shared that anywhere online, just to show kind of the stack you guys have built?
Vijay Iyengar (34:33):
We have a couple blog posts that talks about our stack for... We use this both for our PLG infrastructure and our product, let sales, defining a PQL and alerting a new user who fits that criteria, but then we also use it for internal tools. We have a few blog posts on that topic.
Lenny (34:48):
Sweet. We'll follow up and include some of that in the show notes.
Vijay Iyengar (34:51):
Yeah, definitely.
Lenny (34:53):
Final line of questioning, you're one of the smartest people in the world on product analytics heading product for Mixpanel. I'm curious what you think most people get wrong when they're setting up product analytics for their site, their product, their company.
Vijay Iyengar (35:08):
It's maybe a bit of a hot take because I think so many people-
Lenny (35:11):
There we go.
Vijay Iyengar (35:12):
Yeah, so many people still do this, but I think the biggest mistake is setting up analytics using client side SDKs, client side tracking. So, web and mobile SDKs, putting a mixpanel.track or segment.track in your web app or your mobile apps. And reason it's a hot take is that for many people that's product analytics and SDK tracking are synonymous. They're like, "All right, Mixpanel means SDK, I have to put an SDK in my web and mobile app. But that's a mistake because it... We've just seen time and time again, it leads to poor data quality and difficulty to maintain that data. So, the problem on web is, just due to app blockers and other unreliable things, in the JavaScript world, you end up dropping 20 to 30% of your events, and so it just doesn't match your internal databases.
(35:55):
And then on mobile there's two problems. The first is that you have to reinvent tracking for both iOS and Android because it's two different languages and two different platforms, generally speaking. And so you end up with many duplicate events that semantically mean the same thing, but are just different because of the two platforms, and you might have two teams owning that. And the second issue, which is I think even worse, is that you are kind of beholden to clients updating their mobile app to get to the latest version that has your latest tracking. So if you want to add new tracking, it'll only apply to people at the latest version and beyond. Whereas yet all of your old tracking, whether it's broken or you made a mistake, is still out there in the wild, and so you're constantly getting events that are old and broken.
(36:32):
And so what we recommend instead, and that we've seen a lot more customers adopt recently is just track events from your servers instead of your clients. And that has three benefits. One, it's instantly cross platform. Web and mobile and TV and whatever other platform, they're all going to go through your servers, so you instantly get a hundred percent reach. The second is it's in an environment you control. So if you want to update tracking, you can update it and updates for a hundred percent of users. And then the third thing is that... And this is I think maybe unintuitive, but it's true, is that engineers have been tracking events from servers forever. It's called logs, right? And events are just logs where they user ID in them. And so they don't need to deal with learning a new SDK and dealing with all of that. They just have to track logs that have some structure and a user ID in them. They're tracking events.
(37:18):
And so if it's easier for the developer, it'll get done in a higher quality way. So, I think the really simple advice there is just start tracking events from your servers instead of from your clients. And if you need to supplement it later on with context that's only on the client, you can add that on later, but server side should be the default.
Lenny (37:34):
Maybe a last question is just what's changed most and how companies work with analytics in the past few years? And then just where do you think things are going in the space of analytics?
Vijay Iyengar (37:43):
Yeah, so I think one huge trend is the rise of the data warehouse. So these are Snowflake, BigQuery, Redshift, and they're really scalable and they speak this SQL standard, which has led to this explosion of tools that have emerged around them and make it really easy and cheap to load data into the data warehouse, and then also easy to push data out of the data warehouse by tools that can just do that. And this has a few implications. So, the first is that the data warehouse becomes the center of gravity for all data in your company. Whether it's product marketing and sales data, they all land there. And I think that's really valuable today in this product led growth world, and a lot of incus filled my bad. But from a data standpoint, that means all these teams need to be operating off of the same version of the truth, and that version of the truth is sitting in the warehouse, and it just needs to be joined correctly.
(38:33):
The second thing in terms of where things are going is the events, a time series of users at this action at this time, are the universal data model for analytics. And the reason for that is every action, every interaction a customer has, whether it's with your sales team, like a gong call, or with your marketing team, they clicked on that or viewed marketing article or their product, which is more well known, those are all events. They can all be modeled as events. And it's super granular, super intuitive as a way to understand what people are doing. And it's really powerful, because oftentimes you want to ask questions about sequences of events, right? Which user has spent this much time on my pricing page and then looked at three developer docs? That's probably a user I want to reach out to. So many things can be modeled off of that.
(39:17):
And so I think data warehouse is becoming the loading dock for all this data, which can be very easily modeled this events, but it's not a very great analytical tool for events because SQL is optimized for rows and tables and joints, and not events and sequences of events and segmentations of events. And so one of the things that we're spending a lot of time thinking about is how do we get that really rich, trusted, comprehensive dataset from the data warehouse into a tool that's optimized from the UI down to the data model for events, because that unlocks really fast intuitive exploration of data on dataset that people already have in trust? So, that's, I think, one of the big trends we're excited about and what we see as the future.
Lenny (39:56):
Interesting. And you think Mixpanel is in a good place to help people do that? Is that how see this, there's something that companies like yours will help people solve, or is this something everyone's going to have to figure out for themselves, or there's like a whole new class of startups launching to help them make the mess out of data warehouses?
Vijay Iyengar (40:11):
No, there's always a new class of startups joining in the analytics space. It's never dull moment. Yeah, I think this is something that we are looking to solve, because I mean, analytics only as good as the data. And if people are already collecting great data in the warehouse, I mean we integrate with the warehouse really well, then we get access to that good data. Increasingly, what we've been seeing is that companies like in the reverse ETL phase, like Census and Hightouch are effectively reinventing the CDP reinventing, data movement tool like segment on top of the data warehouse. And so really our strategy there is just tightening our integration with those tools. And we've seen just huge growth and people using their data warehouse as the source for events, not adding SDK tracking anywhere, and just saying, "I already have events sitting here. I trust all of them. They're from all parts of my business. Why can't I do analytics on my support tickets and my gong calls just as easily as I can do it about my user behavior." And so I think that's something we're seeing and we're investing in.
Lenny (41:04):
Awesome. Anything else you'd like to share before we get to our very exciting lightning round?
Vijay Iyengar (41:09):
Yeah, we opened talking about the transition from engineering to product, and I think one of the things that's just been really fruitful in my career, both on the engineering side and product side, is just adopting that product mindset and getting closer to customers, consuming the raw feed of customer context, taking every opportunity to talk to them. And I'm really excited to see things like this podcast and your newsletter and other forums for engineers to also develop that product mindset then and get closer to customers, because I think long term, that just means better products and services at lower and lower prices, which is just innovation. So, I'm really excited to see more of that in the world.
Lenny (41:45):
Here, here. With that, we've reached our very, very exciting lightning round. I've got six quick questions for you. I'm just going to go through them pretty fast. Whatever comes to mind, just share, and we'll see how it all goes. Sound good?
Vijay Iyengar (41:57):
Sure. Let's do it.
Lenny (41:58):
Okay. What are couple books that you recommend most to other people?
Vijay Iyengar (42:02):
On the business book standpoint, there's this book called The Goal by Eliyahu Goldratt. And it's kind of an old book, but I like it because it's sort of written in this fast-paced thriller model. It's like a fiction book, but it's about this idea of the theory of constraints, finding constraints in a system and how you can remove them to improve productivity. So, I found it's just a fun read, and also really insightful non-technical books that I recommend to folks, particularly those that live in SF, which is Cool Gray City of Love by Gary Kamiya, who is a longtime SF president. And it just goes into the history and the communities, and even the geography of San Francisco, and I've just discovered so many little pockets in the city from reading that book, so it's something I recommend to people who live in San Francisco.
Lenny (42:46):
What's a favorite other podcast that you enjoy other than this podcast?
Vijay Iyengar (42:50):
I'll do non-tech one for this. So, I'm a huge fan of the show The West Wing, and so there's this podcast called The West Wing Weekly that goes into each episode of the West Wing and brings in actors from the show, as well as folks from government to talk about each episode, and it's just a delight to listen to if you love The West Wing.
Lenny (43:06):
Wait, so they go back to the old show, The West Wing and talk about old episodes with politicians?
Vijay Iyengar (43:11):
Yeah.
Lenny (43:12):
That's cool.
Vijay Iyengar (43:12):
Yeah.
Lenny (43:13):
Wow.
Vijay Iyengar (43:14):
Exactly. So, the show's over. The podcast is over.
Lenny (43:18):
Oh, okay.
Vijay Iyengar (43:18):
You have all seven seasons, but I think it started in 2016 or 2015 or something.
Lenny (43:22):
Got it. So cool. Favorite recent movie or TV show that you've really enjoyed?
Vijay Iyengar (43:27):
Pretty mainstream TV tastes. So, I really enjoyed We Crushed and Severance. Those are two good shows I really enjoyed last year.
Lenny (43:35):
Awesome. Favorite interview question that you like to ask people that you're interviewing?
Vijay Iyengar (43:39):
I'm a big fan of open-ended questions, and so one of the questions I ask in the behavioral interview at the start is, walk me through the story of you from college to now, or high school to now, if they're a more junior candidate. And couple interesting things here, interesting to see where people spend most of their time talking and where they don't, and also how they describe the other people on that journey. And do they use a standard framework to describe everyone, or do they go into each person uniquely? So, just tons of follow up questions from that.
Lenny (44:09):
Final question is, who else in the industry do you most respect as a thought leader?
Vijay Iyengar (44:14):
Got a lot of inspiration from Gibson Biddle and his product strategy medium thing. And in particular, there's a piece on proxy metrics and the shape of metrics you should use, which I found is a really... The way he frames it is a really elegant way to measure, reach and impact at the same time of your metrics. And then also a big fan of Shishir from Coda, specifically his essays liaison on [inaudible 00:44:37] questions, framing problems, and the one on marginal churn contribution. It's really interesting.
Lenny (44:42):
Amazing. Both guests of this podcast and people I love. Great choices. Vijay, this was awesome. Thank you so much for joining me. Two final questions. Where can folks find you online if they want to reach out, learn more about what you're up to? And then how can listeners be useful to you?
Vijay Iyengar (44:57):
I'm on Twitter and LinkedIn. I think my handles will be in the show notes. Not super active there, but I definitely check DMs and would love to connect on either of those. And then how can listeners be useful to me? Yeah, I mean, ultimately at Mixpanel, we're building a product for product teams. So, two things. If you haven't used Mixpanel in the last four years, we've changed a lot, as I've described on the pod, so check it out, and happy to take any feedback to help us improve the product.
Lenny (45:23):
Awesome, Vijay, thank you so much.
Vijay Iyengar (45:26):
Thanks, Lenny. It's been great.
Lenny (45:29):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcast, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review, as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

---

## A framework for PM skill development | Vikrama Dhiman (Gojek)
**Guest:** Vikrama Dhiman  
**Published:** 2024-05-12  
**YouTube:** https://www.youtube.com/watch?v=ImSvm11GR0Y  
**Tags:** growth, churn, metrics, okrs, roadmap, iteration, experimentation, conversion, pricing, revenue  

# A framework for PM skill development | Vikrama Dhiman (Gojek)

## Transcript

Lenny Rachitsky (00:00:00):
Your name has come up more times than almost any other product person when I ask people for their favorite product leaders in Asia.

Vikrama Dhiman (00:00:07):
I created a career growth framework for product managers, which comprises of three things. What you produce, what you bring to the table, and what's your operating model.

Lenny Rachitsky (00:00:18):
Your advice is early in your career, focus on just getting stuff out and done.

Vikrama Dhiman (00:00:22):
Can you show me your last PRD? Can you show me the last product note that you sent? Can you show me the product strategy doc? You must have that impact through the artifacts that you work on.

Lenny Rachitsky (00:00:32):
I'm curious what you found most impedes people's career growth.

Vikrama Dhiman (00:00:37):
How you view change, whether you are focusing on things you control, and third is how you see yourself. The moment you are able to correct those stories, you may be back on the growth path again.

Lenny Rachitsky (00:00:52):
Today, my guest is Vikrama Dhiman. Vikrama heads all things product at Gojek, including product management, design, program management, research and insights with teams across India, Singapore and Indonesia. He has previously worked at companies like Directi, Airtel, MakeMyTrip and WizIQ and is among the most well-known product leaders in Asia. When I asked people who their favorite product leader is in Asia, Vikrama's name has come up almost more than anyone else's. We chat about how to move into product management, how to be a great product manager, how product managers often shoot themselves in the foot, and so much more. With that, I bring you Vikrama Dhiman after a short word from our sponsors. And if you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. It's the best way to avoid missing future episodes and it helps the podcast tremendously.

(00:01:45):
This episode is brought to you by Uizard, empowering product leaders to ideate and iterate faster than ever before with the power of AI. As a product manager, I often spend hours taking screenshots and then annotating them with feedback for my team. With Uizard, I can simply upload my screenshot and Uizard's AI will turn them into a fully editable UI design that I can then take, make tweaks to, and then share with my teams in minutes. And when I want to get really creative and explore totally new ways to improve our product experience, I can use Uizard's AI to generate new design concepts from simple text prompts and turn them into interactive prototypes effortlessly. There's a reason that over 2.6 million people have trusted Uizard to accelerate every phase of their product life cycle and speed up time to market. Developers can even export UI components to React and CSS to speed up their development. Uizard's drag and drop editor is super easy to use and you can collaborate in real time with your entire team. Even your CEO and customer service teams can contribute.

(00:02:48):
Unlock all of Uizard's game-changing AI-powered features and more with 25% off Uizard's Pro annual plan. Visit U-I-Z-A-R-D.io/lenny and use code Lenny to check out today. That's U-I-Z-A-R-D.io/lenny. This episode is brought to you by Webflow. We're all friends here, so let's be real for a second. We all know that your website shouldn't be a static asset, it should be a dynamic part of your strategy that drives conversions. That's business 101. But here's a number for you. 54% of leaders say web updates take too long, that's over half of you listening right now. That's where Webflow comes in. Their visual-first platform allows you to build, launch, and optimize web pages fast. That means you can set ambitious business goals and your site can rise to the challenge. Learn how teams like Dropbox, Ideo and Orangetheory trust Webflow to achieve their most ambitious goals today at webflow.com.

(00:03:56):
Vikrama, thank you so much for being here and welcome to the podcast.

Vikrama Dhiman (00:04:00):
Thank you for inviting me, Lenny. I'm very excited to be here.

Lenny Rachitsky (00:04:03):
So as you know and hopefully as listeners know, I'm on this quest to meet the most insightful product leaders from all over the world and your name has come up more times than almost any other product person when I ask people for their favorite product leaders in Asia. And you're also the third guest from Gojek, so there's definitely something in the water over there and I want to talk about that. To just dive right in, you have a very strong reputation for building incredibly strong product talent and also design talent, and also helping people transition from other roles into product management, which a lot of people listening to this podcast dream to do. So I'm going to ask a bunch of questions around this area. How does that sound?

Vikrama Dhiman (00:04:47):
Sounds good.

Lenny Rachitsky (00:04:48):
Okay. First question is just when you think back to the people that have done best in the product management role and have had a rapid career rise, what are some of the most common traits or behaviors or habits that you find in these people?

Vikrama Dhiman (00:05:05):
Over the last decade and a half, I've had the opportunity to work with some really strong product managers, learn from strong product managers, and some of them have had rapid career growth. When I was younger and I was starting off, I used to think it's all about the product. If you've got a really cool product to work on, your growth's guaranteed. And if you got really a product which no one cares about or a stream which no one cares about, then your growth is going to be slightly slower. But as I started seeing more and more product managers at their craft, I saw that working on a cool product area is not the only thing. In fact, sometimes some product managers would come back and complain that despite their product doing really well, they've not really grown.

(00:05:51):
And while some other product managers whose product didn't have the impact really grew. And as I started looking at it and as I started making notes, as I started talking to other product leaders, what I discovered was that the really strong product managers who were also growing in their careers did some things differently. And based on that, I created a career growth framework for product managers, which comprises of three things, and I call it three W's. So what you produce, what you bring to the table, and what's your operating model? The really strong product managers are good at usually two of the three things. The ones who rise and when they are rising, they are performing well on all the three access. So if you would like, let's talk a little bit more about each one of these W's.

Lenny Rachitsky (00:06:49):
Yeah, I would love to. I love that you put the word what at the top and that makes it the three W's, which is clever because I find even if the acronym is not necessary, it's really helpful to help people remember so I totally respect what you did there. So the three is what you produce, what you bring to the table and what your operating model is. Is that right?

Vikrama Dhiman (00:07:09):
Yes, absolute.

Lenny Rachitsky (00:07:09):
Okay, cool. Yeah, let's talk about these.

Vikrama Dhiman (00:07:11):
So what you produce, a lot of people index on the impact while and they start thinking about goals, they start thinking about direction and they start thinking about strategy. While it is important to know at what stage of the career you are and what kind of a product that you are working on, the very first thing that anyone, when you're starting off, produces is outputs, okay? The output can be launching a product, it can be analyzing and running an experiment, and it could even be just being a part of the team and contributing to a go-to market strategy. So focus on that output significantly. As you get comfortable with output and you start getting comfortable with working with different stakeholders, you start controlling what outputs are necessary, which is when you move to the outcomes. Outcomes are product areas, goals that you can own and or collaborate with other stakeholders on.

(00:08:14):
And when you start figuring out which outcomes are necessary, that is when you move to the leadership and directional areas. The mistake that I see a lot of product managers make is they start operating in either output or outcomes. And when you are transitioning to outcomes, it's very important that you continue to still hone your craft on outputs. For instance, do you just give up on the go-to-market strategy or do you start making product nodes which are then picked up by marketing people and are able to be used to create that go-to-market strategy? You always, always have to have the output and outcome even when you're moving up the so-called career management ladder. So that is very, very critical that as you are producing, even when you are at the senior most levels, don't forget your IC roots, don't forget the IC component. And sometimes it is necessary to just pull up your sleeves and go back and keep working on those things. That also gives you a lot of creds with others in the team as well.

Lenny Rachitsky (00:09:20):
So highlighting one insight here is that a lot of advice you hear about how to do well in your career, which you pointed out at the beginning here, is it's not just not immediately drive impact. That's not necessarily what you need to obsess over, which is actually what I recommend to people is just find ways to have impact. So this is really interesting. Your advice is early in your career, focus on just getting stuff out and done. Don't so obsess with the impact. Can you talk more about just what, when you say output, what are you describing there? Is it just ship products and be helpful and produce something?

Vikrama Dhiman (00:09:51):
Absolutely. So outputs is shipping products, but it also comes in smaller things. For instance, if you are sourcing content for your homepage, what are the different avenues that you can source content from? What is the easiest to source? What is the most difficult to source? Just ranking it all in that order goes a long way. And one of the product managers actually did that yesterday and I went, wow, it just made my life so much simpler. And not just my life but so many other people's lives so much simpler, and we were able to take that specific output and use it as part of our overall strategy. If that PM would have obsessed about the overall content strategy, overall how we are going to do it versus just how we are going to be sourcing it, they would have indexed on something bigger and maybe would have not even been able to make that impact. But now, they were able to show something which was a small part, which was an output, but it fell into the overall outcome.

Lenny Rachitsky (00:10:54):
The way I think about what you're describing, which I actually 100% agree with, is when you're starting out in your careers, execution is where you need to deliver. People just want you to get stuff done when you're just starting out. It's not like help us define our strategy and vision for the next three years. We just have stuff we need done. Can you help us get it done? Well, yes. And then essentially the advice is as you get more senior, you'll have more opportunity to think about strategy and what to build versus just how to build it and actually execute on it.

Vikrama Dhiman (00:11:25):
Absolutely. So focus on outputs at the start of your careers and don't forget outputs even when you grow in your career.

Lenny Rachitsky (00:11:33):
So along those lines, just to close the thread on this idea, it's still helpful if you work on something that does have impact that matters, right? How important is that? And you said that you've seen successful product managers work on things that aren't as impactful and still do really well, but I guess would your advice be tried [inaudible 00:11:52] be in a place that is going to drive more impact versus it's not actually that important in the early career?

Vikrama Dhiman (00:11:58):
So I'll give you my example. In one of my previous roles, there were two product areas that were important for the organization. My product area ended up being the center and focus of the organization, yet the product manager who was chosen to lead the area when it became big wasn't me. It was someone else. At that time, I really felt very bad that okay, why did that happen? But now when I look back, I can see why that happened because that product manager was so much better at the overall craft of output, yet when they were focusing on outcome, we're not forgetting the output as well. So they were just better at me on launching products, they were better at me on working with design, in producing design artwork, and they were definitely better than me in running the experiments as well.

Lenny Rachitsky (00:12:49):
I love that. Yeah, basically when you're just starting out, just execute well, execute smoothly, ship things on time. I'm going to say a few things, but I'm curious what else comes to mind here of just what does good output look like? Is it do things that are helpful to your team and manager, ship things on time, bug-free, have a clean road map, everyone's aligned behind, [inaudible 00:13:11] deadlines, things like that. I guess what else along those lines should people be like, "Okay, here's what I should be doing to have good outputs?"

Vikrama Dhiman (00:13:16):
Some of the things that I think are useful. So first, what's output? Output is something which is very tangibly defined, which doesn't take too much of your time, effort, and energy to visualize and think and strategize over and you are able to quickly get moving on. Go and ask your product leader, go and ask other leaders on what are the areas they are blocked on. Sometimes they will be blocked on, "Hey, I need to prepare this brief for this particular summit", "I need to prepare this particular slide for a leadership review", "I need to prepare a review, I need to prepare a review which has to be done with the legal." You can volunteer and definitely own and deliver the first drafts of those even if the final draft is not something that you own. That's a simple example of an output, which I feel a lot of people miss because they want to be focusing on the bigger strategic pieces.

Lenny Rachitsky (00:14:16):
It's basically be useful. That's the way I always like to talk about this, just like your job as a PM is be useful, make your team more effective, help your company be more successful. Just find ways to be useful to everyone around you.

Vikrama Dhiman (00:14:27):
Absolutely. And be useful in doing the small things which make an impact and also contribute to your learning versus being useful in areas which you think the mini CEO should be working on.

Lenny Rachitsky (00:14:44):
Right. There's all this talk about being an empowered product manager, building empowered product teams. I think there's an important nuance. When you're just starting out, you haven't earned the right to inform strategy and vision people. Why would people follow you at this point? We just need to get stuff done, so that comes over time.

Vikrama Dhiman (00:15:01):
Absolutely. And it's not just when you are starting off or when you are young. Even with if you are senior and you're starting off with a new team, even if you're starting with a new company, you need to have that mindset. And sometimes you will not know the best. And we'll talk more about how to, what is your operating model, which is how you work with others. It's a very, very important thing for you to know that you are one part of the cog wheel, you're not the entire wheel yourself. And a lot of the folklore around product managers can make you confused, especially when you're starting off in your career.

Lenny Rachitsky (00:15:40):
I love it. Okay, let's keep going. Number two.

Vikrama Dhiman (00:15:43):
Number two is what you bring to the table. Now, I think how I describe that is what is your impact on impact? So the first access is impact, but you also need to have an impact on impact. And this is what I had missed a lot in my early career, that you put the coolest product areas, your product area is successful and that automatically guarantees your growth. It doesn't. You have to also show that yes, you were a useful contributor to having that particular impact. The simplest thing on this is that is your PRD quality good enough? Are you writing that the draft notes that go and circulate to the care teams, to the marketing teams and so on? Are you making sure that you are deriving from the strategy that has been shaped or you're constantly just pushing back on the strategy? Similarly, you also how you are drafting the north stars, how you are working on the experiments, how you're working on the data, how you're working on the metrics.

(00:16:43):
All these things take time, effort, and energy. And I know there is some literature and there are some operating models where people are working only at strategy levels while all of these execution of these artifacts is being done by some other people. I don't think, especially when you are starting off, that's a very, very good thing. Even when you are mid-senior, I don't think that's a very, very good thing. You have to have to be able to produce these artifacts which are product artifacts. Even if there are people in strategy creating their artifacts, even if design is coming up with a design brief, you need to have a cohesive product strategy or product PRD and work backwards from PRD and product knows yourself. These things are important to show you are progressing on four pillars, which is data and metrics, design and research, technology skills, and strategy.

(00:17:41):
Product managers constantly are evaluated on this when you interview, but you also have to demonstrate these on the jobs. And the best way to demonstrate these is through the artifacts, through the notes that you are sending. So you must have that impact to impact through the artifacts that you work on. For a lot of product managers, when I ask, "Hey, I was working on this very impactful area. I'm not able to have the impact on my career, what is missing?" And when I go and ask, "Can you show me your last PRD? Can you show me the last product note that you sent? Can you show me the product strategy doc that you have or collaborated on? Can you show me the brief that you sent to the design team on the problems and the ranking of those problems?" Usually, you'll find something or the other missing.

(00:18:31):
In cases that those are bad, you will find that the pre-iteration planning, pre-sprint plannings are not running properly. You will find that the Jira storyboards are very empty and there's just a title in the subject and nothing gets described and so on. So you'll miss all these pieces. So these are the things which you bring to the table and it's very, very important that you work on these aspects as well. Finally, we have what's your operating model, which I feel is the most important thing which you have to have to focus if you are going from mid-senior to senior level. This is essentially about communication, collaboration, organizational skills and community skills.

(00:19:16):
And across product managers, again, because of the folklore of mini CEO and others, I see that a lot of people get carried away in the way they operate as product managers with other stakeholders. There are three tenets that I define in working well as a product manager with others. Number one is raise difficult issues without being difficult to work with. Bring out important topics without drawing importance to yourself. And finally, you are in charge of getting the decisions made and not making all the decisions yourself. I think as long as you follow these three tenets, you will have a successful relationship across stakeholders. These three tenets are easy to say, but they become very, very hard to embody and display on a day-to-day basis. But this is essentially going to be your struggle no matter at what level of product management you are operating at in your career or within your company.

Lenny Rachitsky (00:20:28):
First of all, can you just repeat them? Because I think this is... Essentially, it's like a mantra that PMs can think back to of, "Am I doing these things?"

Vikrama Dhiman (00:20:36):
So the three things which are very important for product managers to work with others and other stakeholders are raise difficult issues without being difficult to work with, bring out important topics without drawing importance to yourself, and be able to get decisions made without having to make all the decisions yourself.

Lenny Rachitsky (00:21:02):
I like this list a lot. It reminds me, there's this product leader I worked with who their team got pushed to do a bunch of stupid stuff. And he realized later that, "Hey, it's actually my job to have pushed back on doing this stuff." He was the head of product for this business unit and he realized, "Oh, I see. That's actually what I should be doing now that I'm in this role." And you sometimes forget that one, you have that influence. And two, that's something you should be doing.

Vikrama Dhiman (00:21:33):
Absolutely, absolutely. It's always within your control and it's always the things that are within your control that you should be controlling rather than focusing on the things that are not within your control and obsessing about those.

Lenny Rachitsky (00:21:49):
I'm so aligned with the way you think about all these things. Coming back to the second actually, just to give people something they can do with this trait. So the way I think about what you described, and correct me if I'm misinterpreting it, is there's a detail-oriented-ness, high quality-ness to the way that you should be crafting all the documents/artifacts you're creating, your one-pagers/PRDs, your roadmaps, your strategy docs, just like they should be really high quality. So along those lines, if you're an ICPM trying to get better at this stuff, how have you found is the best way to level up in these things? Is it working with your manager and getting feedback? Is it peers? What helps somebody get better at the quality and yeah, the quality of these documents?

Vikrama Dhiman (00:22:34):
What you bring to the table is one of the most misunderstood attributes and aspects of product management. On one end, you could get around and say, "Here is my PRD, here is my JIRA board, here are my stories, here is my pre-sprint planning or pre-iteration planning document" and go. It's not just about the spread and the width of the things that you're doing, but it's also about the depth of those things as well. Some product managers, what they bring to the table is arguments, what they bring to the table are debates, what they bring to the table are pushbacks, while others are able to channelize the questions, channelize the inputs, channelize the direction and convert that into strategic choices which can then shape discussions, which can then shape direction. Be the latter and you will rise faster in your career.

Lenny Rachitsky (00:23:26):
So you have these three buckets of what you produce, what you bring to the table, and what your operating model is, the three W's. So let try to summarize and see what I missed and then we'll move on. So one is just focus on executing, getting things done that are helpful to your team, your company, your manager, and focus on just getting stuff out. Not so much in necessarily in strategy. Even when you're a manager and a leader and a VP, just like you're still responsible for producing things, not just telling people and being wise. Two, what you bring to the table, my takeaway here is produce high quality artifacts that raise the bar.

(00:24:05):
The way I think about this is as a PM, you want to have this aura of I got this. People put something on your plate, you want to feel like Lenny's got this, I'm not going to have to worry. It's going to be forgotten and I know it's going to be done well. And then the third piece is this idea of an operating model. Basically just make sure decisions are being made. It's not about you that you're pushing back on bad ideas. Is there anything else I missed before we move on?

Vikrama Dhiman (00:24:31):
No. I think the art of pushback is another important factor because if you're pushing back a lot and the way you are pushing back matters a lot as well. Just don't be someone who's seen as an obstacle and a hindrance and as someone who's just very difficult to work with, but rather see as someone who's able to actually add value to whatever your leader, your stakeholders, your product area demands and you are able to advance the product and the direction and execution forward. Once you do that, I think keeping that as the intent and ensuring that your team is getting unblocked and not getting to do work on anything which is stupid or is likely to be changed, then you've really got it.

Lenny Rachitsky (00:25:23):
Do you have any advice for how to pushback in a way, the way you describe it is not to be difficult to work with or without seeking importance? I guess is there words or phrases or approaches you found are effective for pushing back against ideas that you disagree with?

Vikrama Dhiman (00:25:38):
What I've seen that people who do pushback very successfully and are still considered not difficult to work with, they are also able to bring the tempo of the conversation to a more logical space from an emotional space. I think that's such a useful skill and I sometimes am guilty of operating on a slightly emotional note, which is useful. Sometimes you need a war cry, you need a high pitch, you need execution on war footing. All that is fine, but it's only fine in some cases. In other cases, it's always very important that you're able to bring it down to the logical space so that a logical and a little more equal footing of the discussion can happen. And a lot of this is something that leaders need to ensure is happening, but product managers and product leaders who are working with executives who are able to bring this tempo down and bring it to a little more logical space will also do far better in their careers and they'll also have a lot more rapid career growth.

Lenny Rachitsky (00:26:55):
So let's talk about the flip side of rapid career growth, which is career growth that stalls. And I'm curious what you've found most impedes people's career growth. What do PMs do that shoot themselves in the foot and slow their career? Any pitfalls do you find are important to try to watch out for?

Vikrama Dhiman (00:27:15):
I think part of it is on a lot of us in product leadership space. We've not done a very good job in defining rubrics, growth frameworks and so on. But even in places where growth frameworks exist, like three W's, what I've seen is that clean mindset shifts and changes can enable faster growth, but those mindset and changes also can hinder your growth, right? So the first thing is whether you are focusing on things you control or whether you're focusing on things that are beyond your control. Second, what's your relationship with change? And third is how you see yourself. The third is very, very powerful and we'll talk about that as well. The first is what you control. If you drew an access of what you control and what you cannot control, as you're starting your career, most of the work that you're doing is in what you control, right?

(00:28:15):
You are very obsessed with feedback, you're very obsessed with, "Okay, can I do this?" "Can I do this?" "Okay, I'll probably not do this. I'll probably do this", and so on. You're not worrying about the overall corporate strategy, you're not looking at what the competitors are doing, what is their market cap and all those things. You're focused a lot on your craft, you're focused on a lot on your output and you're focused on how you are growing. As you start becoming mid-senior, I see the conversation shifts from what can I do, how am I learning, how am I growing, to why is the organization not doing this for me? Why can that stakeholder not change this thing about themselves? Why do I not get to work on projects like this? Things which start going outside your control. And it is very, very important that you keep your focus no matter what stage of career you get into what you can control.

(00:29:16):
And again, it's easy to say that everything in universe should be in your control. It doesn't happen like that, but a large number of things that impact your career are within your control. And go back to the three W's that we spoke about, what you work on, what you produce or what do you bring to the table, and what's your operating model? And there is tons to do on data, tons to do on technology, tons to do on communication, collaboration, design and research, strategy and community. And you can spend years and years and years crafting those things. Focus on those things, growth will happen at every single stage. The second aspect of it is your relationship with change. Again, when you are younger, when you're starting off, rate of change is crazy. You are growing almost every six months. You are picking up skills and experimentation, you're picking up skills in how to analyze.

(00:30:15):
You're picking up skills in how to work with different kind of stakeholders. And since the rate of change of your skills is high, your rate of growth is also high. Again, as you start becoming mid-senior, I start seeing conversations on, "Okay, maybe I should not do that. Maybe I should not take on this product. I don't know what it means for my career. I don't know what it means for my growth" and so on. So your rate of change slows down. So it's very important that as you get to mid-senior level, you are constantly checking on what you can do to keep increasing your rate of change. And one of the simplest things that you can do is if you think you are four on data, figure out who. And you may be four on data out of five in data. Within your organization, start benchmarking yourself with the best in the industry.

(00:31:13):
You'll automatically see that your scale drops and as your scale drops, you start seeing what you need to improve and do. If you start seeing that on communication and collaboration, you're reaching four out of five within the PMR, start mapping yourself to other stakeholders in other functions. Again, your score will fall in your eyes and you will start figuring out what are the things that you can do as well. So keep your focus on rate of change and rate of growth will automatically take care of itself. Sometimes it also involves changing your team or even changing your company, but those should be the last results. There are significant things that you can do within that as well. One of the final things that I see which limits you, especially as you start growing in your career and you reach mid-senior levels is how you see yourself.

(00:32:04):
I see a lot of product... And I've been guilty of that. When I see that a lot of product managers, that's included me at some stage, doing these things, people will come back and say, "Oh, I am a very high agency PM" or, "I'm a very collaborative PM." Earlier on, I used to think that okay, I need to give this kind of work to these product managers. I need to fit them with these kind of team, these kind of work areas, these kind of opportunities. But then I started understanding these things are not just signaling, they are also anti-signaling. They are like, "Oh, I'm high agency. So it's sometimes okay if I'm little brash, if I cut corners somewhere, if I sometimes come across as a little rude to some people" and so on, right?

(00:32:55):
Similarly, if I'm seen as a hyper-collaborative person, so it's okay if sometimes I'm not very decisive, if I'm not moving fast and so on because I'm this kind of a PM. So it's very important that you check for what are the stories that you're telling yourself because those stories are defining you at a basic level, which is then very hard to correct through frameworks and structures. So figure out what is the story that you are telling yourself. If you are not able to figure that out, talk to the people you trust so that they can tell you that as well, and then correct those stories. And the moment you are able to correct those stories, you may be back on the growth path again.

Lenny Rachitsky (00:33:39):
Wow, there's so much meat and wisdom in what you just shared. I want to go in so many different directions. Maybe just to follow on this last thread, did you go through something like that yourself where you have this sense of yourself that hindered you? Okay, awesome. You're nodding your head, if you're not on YouTube. Can you share that?

Vikrama Dhiman (00:33:57):
Yeah. So I'll give an example of when I joined Gojek. The very first thing that I learned in my career was SQL and Oracle. And I was very proud of the fact that my data skills are awesome and I know several frameworks and I know several tools and so on. And when I joined Gojek and I saw one of your guests, Crystal, and I saw the work that she was doing and her team was doing and I just immediately was like, "Yeah, no, this is not... I'm nowhere near", right? And similarly, I also thought that my communication skills are really good and my product strategy skills are very good, but then I worked with people like Dito and people like Sidu who was so good at their craft that it challenged me to see that okay, what is it that I am missing? What is it that I am doing wrong?

(00:34:57):
And it auto-calibrated me in my eyes on where it was, but that also created a hunger in me that this is what I need to fix. And I immediately corrected my assessment of myself that I'm not the strongest product manager on data. I'm not the one who knows all the strategy pieces or even strategy frameworks or how to bring everything to a strategy point of view or communicate it from an effective perspective. And then I started framing I'm still in a learning phase. When I see that I'm not in that phase now, I try and make myself humble by interacting with people who are far smarter than me on different scale or reading different books, or watching podcasts like yourselves. And that keeps you grounded on the fact that okay, you are always learning. And I also found that seeing yourself as someone who's a learner is an enabling story to tell yourself, okay?

(00:35:58):
It may not be the most exciting story, it may not be the most memorable story about yourself, but it is definitely one of the enabling stories as well. Similarly, I think one other thing that I used to say about myself was more that I'm very high agency PM. But as I started working more in Southeast Asia, I learned that mindfulness is also very, very important, that not every team, not every culture will work with you in a very hyper aggressive style. But you still need to get the work done. And I'm still learning on that and therefore, I've started using a word, I don't want to be a high agency person, I want to be a mindful agency person. And so these terms are very important because these are the stories that you keep telling yourself and these also then start shaping your behavior. I do feel that I have a lot to do, I have a lot to learn on these skills, but these things definitely keep you grounded and you keep coming back to the learning phase again.

Lenny Rachitsky (00:37:09):
It's interesting that when you saw Crystal being incredibly good at working with data, you just realized, "Hey, maybe I'm actually not very good at this." And your reaction wasn't, "God damn it, I'm really screwed and this is really depressing me", it's, "No, instead I'm going to try to get better at this." And that reminds me some of the feedback I get with this podcast, those people are like, "Man, these people are so good, I'm never going to be this good. It discourages me from thinking I will ever be super successful in this career." Clearly, you have a different approach. Do you have advice or guidance to folks that are sometimes discouraged seeing people being so incredible and helping them actually continue to level up in this rate of change you talked about versus just like, "Nope, I'm never going to be that good?"

Vikrama Dhiman (00:37:54):
I think as product managers it becomes difficult because a lot of your growth is being determined because of feedback of others. And because product management is so ambiguous and still not defined, the stakeholders can also give feedback on variety of dimensions. Some of them may not even be important enough to give feedback on, but they are important enough for them and so therefore, they give you feedback. And therefore, you have to shape that feedback in. But you also have to consider that there are these eight access that we spoke about, the data access, the design and research access, the technology access, the strategy access, communication access, collaboration access, organizational skills access, and the community access. You need to channelize feedback into okay, is this an area that you are targeting for growth or not?

(00:38:51):
And one of the most important things that I learned was that when I joined Gojek or even earlier, there would be so many different areas that I needed to improve on and still need to improve on. You can't improve on every single area. That's what overwhelms you. You need to pick which is the area which is the maximum leverage for you and improve on that particular aspect and then move on to the next area, then move on to the next area and so on. Obviously, if you are floundering in something, if you're really negative in something, then you fix that first because that will give you the highest leverage. But if you are picking up data and design and strategy and technology all at the same time, that's when you'll overwhelm you.

Lenny Rachitsky (00:39:33):
So to summarize the advice there is one, be actually very open to feedback you're getting. It's easy to say that, it's hard to actually listen to people criticizing you and act on it. So I think that's an important takeaway here is just actually, feedback is a gift and actually understand that and try to act on it. I have a great interview with Jules Walter who's a PM at Google now, and he has this awesome quote about how whenever people give him hard feedback, it's like internally he's just melting, but that's externally he's like, "Thank you so much for that feedback, I really appreciate it. It's very valuable."

(00:40:10):
And so that's a good way to get people to keep giving feedback. Okay. And then the other piece of advice you just shared there is pick a focus area. Like say you're getting all this feedback, your strategy isn't amazing, your PRDs aren't great, just find one thing to focus on. And I don't know, do you try to do somewhat quarter? Somewhat year? Do you have a heuristic of how long to spend on one thing?

Vikrama Dhiman (00:40:31):
So different skills take different time and how you are progressing also depends a lot as well. For skills which are softer in nature like communication and collaboration and community, those are skills that you will work on all your life. You'll never achieve anywhere near two or five on five on those ever. There'll always be something that you will miss, there will always be a new context, there'll always be a new set of stakeholders, new company cultures that you have to adapt to. For others, you have to see that what gives you the maximum leverage in your career. When you're starting off, my recommendation is that you pick between data and tech one, and definitely one on design and research and strategy.

(00:41:18):
So usually, that's the combo that I recommend. My advice is if you're coming from design and research background, then you pick data or tech. If you're coming from a data or tech background, then you pick design and research, and that gives you the maximum leverage because that's a skill that you will necessarily not have developed over the years. Once you've demonstrated on two of these three, between data, tech and design and research, then you start focusing on strategy. We've had great success at Gojek in transitioning a lot of product managers, especially in Indonesia, using this framework. And it's produced a lot of good product managers for us.

Lenny Rachitsky (00:41:59):
Well, let's actually follow that thread. That's really interesting. And so the approach is you have this access of skillsets and you pick, for this person moving from say customer service to product, here's the two things you need to focus on. Can you talk more about that?

Vikrama Dhiman (00:42:15):
Yeah. For instance, we recently had two PMs, one who came from a growth background. This is actually [inaudible 00:42:24]'s team. And one from a research background. And with both of them, we use very different tactics. So we gave one of finding driver redesign, which was very much a very design-focused product, but we still had them leverage their data skills because we were able to create a PRD with incredible amount of data on exactly what different segments of customers we're doing. And that then we worked with designers on what the designs and the framework for that will be. And even now, Lenny, if you will come and see our finding driver redesign next time you are in Asia, it's a piece of art. And if you would see that that was worked on by a product manager who actually came from a growth and data background, that makes it even more special.

(00:43:13):
Similarly, the PM who transitioned from research, I kept giving feedback on technology and data skills are the ones that we need to check. And I need to hear from engineers that yes, they're able to work with her very strongly. And once she was able to do that, she's recently turned a very heated question on one of the features that we were doing into a full-blown solution with designs, with trade-offs and everything, and able to now convert it into a question for leadership on how we should be approaching this particular product and direction. So I think that's proven successful as well. Similarly, there's another person who took risk who was originally from research and again, worked a lot on our products, including our enterprise product. And she's doing an amazing job as well. Again, going through that path of okay, these are the things that you need to leverage.

(00:44:14):
The only watch-out is that it doesn't work out always. In some cases, some PMs will pick these things up fast, and it also makes a big difference if you are transitioning when you are slightly younger in your career. If you are already senior in a function and then you are transitioning, sometimes it can take a lot of time in transitioning and picking up those skills. But it's definitely doable if you get a very strong product leader working with you who's able to shape those skills for you. So it's sometimes okay to go a little slow when you're transitioning so that you're able to go faster later rather than getting faster somewhere and then being stuck there for a while.

Lenny Rachitsky (00:45:00):
This episode is brought to you by Coda, and I mean that literally. I use Coda every day to help me plan each episode of this very podcast. It's where I keep my content calendar, my guest research, and also the questions that I plan to ask each guest. Also, during the recording itself, I have a Coda page up to remind myself what I want to talk about. Coda is an all-in-one platform that combines the best of documents, spreadsheets, and apps to help you and your team get more done. Now is the perfect time to get started with Coda, especially its extensive planning capabilities. With Coda, you can stay aligned and ship faster by managing your planning cycles in one location. You can set and measure OKRs with full visibility across teams and stakeholders. You can map dependencies, create progress visualizations, and identify risk areas. Plus, you can access hundreds of pressure-tested templates for everything from roadmap strategy to final decision-making to PRDs.

(00:45:56):
If you want a platform that empowers your team to strategize, plan and track goals together, you can get started with Coda today for free. And if you want to see for yourself why product teams at high-growth companies like Pinterest, Figma and Qualtrics run on Coda, take advantage of the special limited-time offer just for startups. Head over to coda.io/lenny to sign up and get $1,000 in credit. That's C-O-D-A.io/lenny to sign up and get $1,000 in credit. Coda.io/lenny.

(00:46:29):
Something that you mentioned earlier that I wanted to come back to is this confusion about what the PM role is and how that trips people up in being successful in the role and continuing to thrive in the role. You mentioned this to me offline too, that this is just something you deal with a lot, just this frustration of what the hell is this job? What am I actually responsible for? What am I not? What do you find is helpful in helping people work through that, get past that, not make that a big blocker in their career, not knowing exactly what the PM role is?

Vikrama Dhiman (00:46:56):
I think we've been in technology product for several decades now, but we are still figuring out what an exact definition of product management is. And even the strongest definitions are slightly principled and philosophical in nature, they're not very concrete, and that also means that every and different technology companies have gone through different journeys and they've defined the roles very, very differently. And even within a very large company, you will see that different teams, different divisions are approaching the roles very, very differently as well.

(00:47:34):
And on top of that, what that does is that not only internally the product managers are figuring this out, their managers, their leaders are figuring these things out for them, but the other stakeholders who have to work with these product managers are also confused and they don't know what to expect. And the number one question I get from stakeholders is, is a product manager expected to do this? Because they also don't know, okay, is this expected from a product manager or not? And my general answer to that is, if this is something which is blocking the progress on the product, then yes, the product manager should work on that.

Lenny Rachitsky (00:48:09):
Love that.

Vikrama Dhiman (00:48:09):
But that works if the product managers have had some training and they have had some training in working with different stakeholders and they have had something on the job. What I've figured out is that there are certain functions and there are certain disciplines which you can't define, but you can only become better at with practice. For instance, what is an actor or what is a dancer? Right? So these are things that you will get better at as you become skilled at it. And earlier, these things used to be looked at as something which is very artistic, only the people who are talented or only specific kind of people can do it. But now, each one of those has become [inaudible 00:48:57] and frameworks as well. So there are courses on filmmaking, there are courses on acting, there are courses on dancing and so on. And similarly, product management is that space as well.

(00:49:08):
So you have to understand there's an art to it and there's a science to it, but you can use the science to figure out the art. So that's the philosophical side of it. The second side of it is what we spoke about earlier that instead of figuring out what is product management, figure out what's your contribution, what's your output and figure out are you contributing on these access on data, on design, on technology and on strategy. And one of my favorite things is that if you created these four circles of strategy, of technology, of design and of data, and you created a product management circle which encircles each one of these, so you are the only discipline, which is the co-collaborator for all of these disciplines and tying all these things out.

(00:49:59):
So it's not about you standing alone, it's you always collaborating and pairing with someone else. But you are the only one who's pairing with everyone else and therefore, you have that unique insight which no one else in the team will have. That role can be played by someone else, it doesn't necessarily need to be called a product manager. But if you are being called a product manager, you figure out the [inaudible 00:50:24] the time piece that you are. And when you are added to the team, you must dream the team's overall contribution, overall energy and overall output up and not down.

Lenny Rachitsky (00:50:37):
I love that. Something I always tell people is the PM doesn't necessarily have the magical skills other team members don't have, it's that they don't also have another job. Engineers may do a great job at being the PM, they just also have to build and code. And they don't have time to do all the things that a PM has to do, and a designer is in the same way, a researcher or data person. And so oftentimes, that's just like there's this person that has the time to do all these glue, work things between teams. And the great PMs also are very good at these skills that help you do these things, but it doesn't mean other people can't do them.

Vikrama Dhiman (00:51:19):
You see yourself as playing a role and not your title and not your function, and that just clarifies a lot of things for people. And different people will play different roles. And depending on the kind of a PM you are, are you in a specific domain or you are slightly generalist, the role that you will be playing in different teams can be different and the variety of roles that you can play makes you a better product manager.

Lenny Rachitsky (00:51:47):
I love that. You've mentioned these four access attributes of great product managers, overall product managers. Let's just spend a little time here. So you say basically the things you need to be doing and good at, data, design/research technology, strategy, and then you also mentioned collaboration and communication. Maybe you're-

Vikrama Dhiman (00:52:08):
Yeah, organizational skills and community. I think those are very, very important because one of the things and one of the things which one of the product managers works with me continues to say, and I really plus on that a lot, is that product manager is the all community enabler in the team, in the organization. And that community is the software aspect which ties everyone together towards a common mission of delivering an output. And that I think is a very, very important goal in today's context, especially for teams which are becoming more remote or teams where people are not co-located or they're distributed. That community aspect becomes a very, very important part that product managers need to focus on and bring and channelize as well.

Lenny Rachitsky (00:53:05):
So let's just quickly describe each of these attributes. I imagine people might be thinking, "Okay, what should I get better at as a PM?" And this is an awesome list. Each company has their own career ladders and attributes and things like that, but not a lot of companies don't. So I think for people that are trying to figure out where do I need to get better, I think this is a really cool list. Can you just maybe just a sentence explanation of each of these attributes and skillsets that a PM needs?

Vikrama Dhiman (00:53:31):
So each one of those skills, like the most growth ladders, what they will do, is they will have say for data, they will have level one, exhibits these traits. Level two, exhibits this trait. Level three, exhibits this trait. Level four and level five and so on. That's how they'll describe it. But five is absolute ninja level data quality, like you could probably do a data startup of your own.

Lenny Rachitsky (00:53:55):
Like Crystal basically?

Vikrama Dhiman (00:53:57):
Crystal. And level zero is someone who cannot even basically define the basic metrics for this particular product and won't be able to figure out is this particular thing impacting orders or users or revenue. And so you'll really not be able to figure even that piece out. Similarly, on design and research, for product managers, we focus a lot more on problems and are you able to identify problems from a user's perspective. That's at level zero. And level five will be somebody who's able to define the user problems but is also able to tie them to business roles as well. So that makes it the holistic. Similarly, on technology, it's one of the skills which is relatively easier to define where you don't have any tech understanding. If somebody asked you what is HTTP or API or internet and you'll be like, "Okay, I don't know what it is."

(00:54:55):
And while on the other end, you are able to have deep debates and could probably write technology design documents yourself as well. I think sometimes people get confused between data science. And in different organizations, I see data science bucketed either in data or in technology. Either is fine as long as you are clear on what your organization's framework is. Similarly then, there is strategy. Strategy is I think another area in product management which gets very confusing because there is obviously corporate strategy, there is business strategy, there's pricing strategy, there's strategy everywhere. Product strategy for me is where you are able to define that while somebody defines that this is the mountain that you're going to climb, but okay, how are you going to climb that mountain is basically the product strategy piece.

(00:55:47):
So you are not in charge of okay, are you focused on growth? Are you focused on revenue? Are you focused on profitability? That's someone's choice. Are you going to pick this country? Are you going to pick that country? But once that is picked, what are the user segments that you're going to focus on? What are the needs of those user segments? How are we going to figure out what the right product for them will be? What is the order in which we are going to work on that? That whole piece of product strategy is with the product managers. And again, in the first case, you are basically going to rely on everyone to tell you, do this, do this, do this. In second and in the level five cases, you are able to articulate a very coherent product strategy at a broad level as well.

Lenny Rachitsky (00:56:33):
Amazing, thanks for sharing that. I think for people that are trying to craft career ladder for product managers, this could help inform the way they think about this. By the way, when we mentioned Crystal, for folks that have no idea who we're talking about, she was a early head of growth at Gojek back in the day. She was a previous guest on the podcast. I always forget how to pronounce her last name exactly, but I think it's Widjaja, Crystal Widjaja.

Vikrama Dhiman (00:56:33):
Widjaja.

Lenny Rachitsky (00:56:54):
Widjaja? Okay, okay. Great. Going in a different direction, we're going to move to contrarian corner. I'm curious if there's anything that you believe that other people wouldn't agree with or generally just don't believe?

Vikrama Dhiman (00:57:12):
I used to think intent is the most important thing, right? And when I was starting off, that used to be the advice that as long as your intent is right, even if some of your words are not landing, even if some of the comms are not landing, that will work out. What I've seen is that it's not enough. Your actions, your behavior, and the way you communicate, the way you collaborate, that also has to communicate and show who you are as well. So intent is not enough. And that's a thing which I think a lot of people in my age group just don't get, but people who are slightly starting off their career, it resonates well with them. Second thing I think where I feel that it's become, I don't know, is it contrarian or it's become politically incorrect, is that you still need to put in the effort and our number of hours is effort.

(00:58:23):
And I think that's one thing which has become very politically incorrect to say over the years when I was younger, it was the norm that yes, you will have to put in the effort, you will have to put in the hours to grow and improve your skills. And it's not even about your growth in the company, it's just your own growth. You have to spend the time, effort, and energy into growing. I think a lot of that is getting lost in the debates between complete workaholism and just being not very serious about your growth at all. So I think those are the two that I find myself having to explain myself again and again and why I feel this way.

Lenny Rachitsky (00:59:14):
I completely agree with that. I find a hugely strong correlation between hours you put into the work you do and success. And I think there's been a return to okay, working hard is really important and you shouldn't be afraid of promoting working really hard. So we've actually gone through everything that I wanted to ask you. Before we get to our very exciting lightning round, is there anything else you wanted to share or is there anything you want to leave listeners with?

Vikrama Dhiman (00:59:41):
No, I think it has been great talking to. I hope it was useful to people. I've tried to keep it real, but also in takeaway format. And if there are any questions that you have that I feel I have not answered, I'm happy to answer them.

Lenny Rachitsky (01:00:01):
Okay, amazing. Well, we'll have people post in the comments if there's anything else they would love to ask you. With that, we've reached our very exciting lightning round. Are you ready?

Vikrama Dhiman (01:00:12):
Yes.

Lenny Rachitsky (01:00:14):
First question, what are two or three books that you've recommended most to other people?

Vikrama Dhiman (01:00:19):
The first book is a book which I feel is not quoted enough in product management community, is a book called Small Data by Martin Lindstrom. This is a person who was an advertiser or marketeer who would go and make campaigns for big brands in different countries, and so would have usually very short time to get the pulse of that space and design a campaign around it. And how he got insights very quickly from, and what are some of the takeaways that are there for people working in product space, not just product managers, but designers, researchers, strategy people, anyone really, I can't recommend that book more. And I've cited that book a lot internally.

(01:01:09):
The second book that I recommend is Adam Grant's Originals. I think it's a very important book. It changed a lot of things. When I spoke about that I was going through this crisis of, oh, I'm behind so many things after joining Gojek, Originals was one book that I read which really, really helped me think about my growth and how I see myself. And anyone who is stuck or anyone who feels they are superstars, they are the innovators of the century kind of a thing, it's a book that gives you a very good reality check. And the third book that I recommend is definitely Daniel Kahneman's Thinking, Fast and Slow. I think especially the thinking slow part becomes very, very important piece as well.

(01:02:11):
And the reason why change is hard, the reason why feedback is hard is because we are used to thinking fast and we are not used to thinking slow. While if you actually think slow, you'll actually welcome change and growth.

Lenny Rachitsky (01:02:26):
Amazing. That book's come up a bunch actually recently on the podcast and it is always sitting under my laptop, holding up my laptop for these interviews. So I fully agree. Next question, do you have a favorite recent movie or TV show that you've really enjoyed?

Vikrama Dhiman (01:02:41):
I haven't seen a lot of movies recently, I think. But while I was on the flight back from Dubai, I saw Miss Congeniality again and I really, really enjoyed it. I thought it's a very fun movie, but also had a pretty good message. I know it's probably not the movie which anyone would want to cited, but I think it's sometimes good to just watch good entertainment.

Lenny Rachitsky (01:03:18):
That's quite the contrarian pick. Yeah, nobody has cited this movie, Miss Congeniality. This is a first, but I love it. It's way out there. I would never would've expected this.

Vikrama Dhiman (01:03:27):
In terms of TV shows, I think the show that I really go back to all the time is Schitt's Creek. I think it's a show which operates at so many different levels without taking itself that seriously, and it just lands. And especially as a product manager and as a leader who obsesses a lot about diversity, I think it did a fantastic job in showing different sides of motherhood, of the LGBTQIA communities, and also teenage girls figuring themselves out as well. I think it did a fantastic job.

Lenny Rachitsky (01:04:07):
Do you have a favorite interview question that you like to ask candidates when you're hiring product managers especially?

Vikrama Dhiman (01:04:13):
So it's not really one question, but what I like to do with them is to brainstorm choices on an actual product. And I'll typically pick up a product that they use most often and then I will be like, "Okay, what if this product were to do this? Then what do you think, it makes sense? Don't think it makes sense? What about this? Okay, how would it evolve in six months? What would happen in 12 months and so on?" I think it gives you a far better insight into how would it be on working with them on a real case. And you also keep... And what I like about it is that you can keep going back deeper into it and develop it together. So I typically try and pick product that I will also not have very strong opinions on so that it can become a two-way conversation.

Lenny Rachitsky (01:05:14):
What do you actually look for in an answer that tells you, "Okay, this candidate is amazing" versus flags that are like, "Hmm, maybe not?"

Vikrama Dhiman (01:05:21):
There are some obvious check marks that are they able to first abstract out and figure out what the overall goals for the product are, who the users for that product are, what would they be focusing on right now, whether this will align with that or not. And then a reason backwards that okay, maybe this may not work, but something on these lines. Are you obsessed about this feature or are you obsessed about okay, what this enables you to do? So if this is what it enables you to do, then are you okay with considering some other options and so on? So I think that's the direction which usually goes in the right way.

Lenny Rachitsky (01:06:04):
Is there a favorite product you've recently discovered that you really love?

Vikrama Dhiman (01:06:08):
So the reason why I've not watched a lot of drama or TV recently is because I've discovered these short video apps through Instagram and all of these apps, they dub Chinese TV serials into English or there will be subtitles in English and they are delivered in TikTok style two-minute videos. And it's a masterstroke in how the series are constructed. The first few episodes, which is like 10 episodes which is about 10 to 15 minutes, sets up the story in such a way that you have to unlock the next 10.

(01:06:47):
And these videos are quite expensive. They end up, one series takes more than the entire cost of monthly cost of Netflix to view. But it's just amazing how the whole product has been put, how all these products have been put together on unlocking the lamification aspects of it, the storytelling aspects of it, the content cutting part of it, and even the selection of the stories part of it. And what I'm told is that once I've learned about it, I've also been reading about it, they're actually companies which are able to give you tools of where you can construct this app yourself. And multiple people, two-people, three-people companies are churning these out and earning a lot of profit from it as well.

Lenny Rachitsky (01:07:41):
What is this called for people that want to check this out?

Vikrama Dhiman (01:07:43):
So you can start with DramaBox, you can start with [inaudible 01:07:47] Reels and so on. And there are multiple of these. And those of you who are very familiar with TikTok, you would've seen that some of these show you the first 10 episodes on TikTok and then they take you to their app to view the rest.

Lenny Rachitsky (01:08:01):
Wow. I love so many unusual contrarian pieces of advice here, I love it. Two more questions. Do you have a favorite life motto that you often come back to, share with friends or family, either in work or in life?

Vikrama Dhiman (01:08:15):
For me, the most important thing has been that I started my career very late in tech. I was already 25. For the first several years, I worked in a small [inaudible 01:08:32] town in India. I came to Delhi only in 2013, and I joined Gojek in 2018. I think I've done reasonably well for myself. And it's never late to do or what do you want to do and what do you want to be. I think that's the thing that I really, really believe in and I also advise in. Especially as the world is aging and a lot of people are thinking about it, I would say that it's not too late ever. You can be and do what you want right now.

Lenny Rachitsky (01:09:17):
So good. It's not too late. I really, really like that advice. My wife is an illustrator designer. She has a book she put out called Am I Overthinking This? It's in my background somewhere there. And she has a chart that communicates that exact message in a really cute way, and we'll try to link to it in the show notes. Final question. You live in Singapore, I know you travel a lot. But if someone were to come to Singapore, is there a food that you think they need to try that's unique to Singapore?

Vikrama Dhiman (01:09:45):
Singapore? There are multiple. So Singapore is a melting pot of different cultures. There are four official languages. And the only thing I will advise is depending on your taste buds, whatever you want to do, you should go and visit a Hawker Center. And it's an amazing experience in itself. And those of you who've seen Crazy Rich Asians, the first thing they do when they land in Singapore is go to the Hawker Center. So it's an experience of its kind. And if you are looking for a specific recommendation, go to Lau Pa Sat. If you are a fan of Indian, you'll get that. If you're a fan of Malay cuisine, you'll get that. If you're a fan of Singaporean Chinese, you'll get that. So you pick what works for you.

Lenny Rachitsky (01:10:36):
I love that. Vikrama, I feel like we've produced both a lot of output and we're going to have really great outcomes from our conversation. Thank you so much for being here. Two final questions. Where can folks find you online if they want to reach out and follow-up on any of the stuff we talked about? And how can listeners be useful to you?

Vikrama Dhiman (01:10:53):
Thank you, Lenny. It's been great talking to you as well. Hopefully, this turns out well. You can reach out to me either on LinkedIn, Vikrama Dhiman, or you can reach out on Twitter. Twitter works better. And the listeners can be useful to me by, well, just sharing whatever they feel. And I continuously follow a lot of people, a lot of people who are not yet famous. Just tell me what your story is, just tell me what you are working on. And as long as you are passionate about it, I will try and find time. Maybe I cannot talk to everyone, but I'll definitely try and find to chat with you and listen out and support or connect you to someone who can help support you.

Lenny Rachitsky (01:11:44):
That's a very generous offer, I think a lot of people are going to take you up on that. Vikrama, thank you so much for being here.

Vikrama Dhiman (01:11:51):
Thank you so much, Lenny.

Lenny Rachitsky (01:11:53):
Bye, everyone.

(01:11:55):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

---

## An inside look at how Figma builds product | Yuhki Yamashita (CPO of Figma)
**Guest:** Yamashata  
**Published:** 2023-01-08  
**YouTube:** https://www.youtube.com/watch?v=NepFo4zXyK4  
**Tags:** growth, retention, acquisition, onboarding, metrics, okrs, roadmap, experimentation, funnel, conversion  

# An inside look at how Figma builds product | Yuhki Yamashita (CPO of Figma)

## Transcript

Lenny (00:00:00):
There's something controversial about this idea that everyone can see what you're doing or that multiple designers can be in the file at the same time. We like to say that one of the first responses we saw Lenny [inaudible 01:08:35] Figma was, if this is the future of design, I'm quitting, right? I'm changing careers.

(00:00:17):
And there's that tension of that narrative tension, but that is signal that you're part of this revolution and you're trying to change something. And when it equips your customers or user base with that, then I think that's something that they can really get behind and champion.

(00:00:35):
So it's not just that they're championing for a tool, they're also championing for a new way of working. Obviously, that's a tall order or don't want to come up with that, but hopefully, if you're a founder and you're working on something, your vision is so big that you have those kind of ideas and it's like, how do you actually equip your customers to want to talk about that?

(00:00:58):
Welcome to Lenny's podcast. I'm Lenny, and my goal here is to help you get better at the craft of building and growing products, interview world class product leaders and growth experts to learn from their hard won experiences, building and scaling today's most successful companies.

(00:01:12):
Today my guest is Yuhki Yamashita. Yuhki is Chief Product Officer at Figma, where he's been for almost four years. Prior to Figma, he was at Uber, both as a Product Leader and also, interestingly, as Head of Design for one of their bigger product teams. Before Uber, Yuhki spent time at Google and Microsoft, even taught an introductory computer science course at Harvard.

(00:01:33):
In our conversation, we explore Figma's product development philosophy, how they build such consistently great products, how they hire, what habit Yuhki has found to be the most instrumental in his success in his career, and also what Yuhki and his product team have learned by building a product led growth business.

(00:01:50):
This episode builds on a newsletter post where I interview Yuhki about how Figma builds product. So if you enjoy this episode, or even while you're listening to it, I highly recommend you check it out. It's currently my fourth most popular newsletter post of all time. You can find it at lennysnewsletter.com. With that, I bring you Yuhki Yamashita, after a short word from our wonderful sponsors.

(00:02:15):
This episode is brought to you by Notion. If you haven't heard of Notion, where have you been? A's notion to coordinate this very podcast, including my content calendar, my sponsors, and prepping guests for launch of each episode. Notion is an all-in-one team collaboration tool that combines note-taking, document sharing, wikis, project management, and much more into one space that's simple, powerful and beautifully designed.

(00:02:40):
And not only does it allow you to be more efficient in your work life, but you can easily transition to using it in your personal life, which is another feature that truly sets Notion apart. The other day, I started a home project and immediately opened up Notion to help me organize it all. Learn more and get started for free. At notion.com/lennyspod, take the first step towards an organized happy team today. Again, at notion.com/lennyspod.

(00:03:08):
This episode is brought to you by Vanta, helping you streamline your security compliance to accelerate growth. If you're business stores any data in the cloud, then you've likely been asked, or you're going to be asked about your SOC 2 compliance. SOC 2 is a way to prove your company's taking proper security measures to protect customer data and builds trust with customers and partners, especially those with serious security requirements.

(00:03:33):
Also, if you want to sell to the enterprise, proving security is essential. SOC 2 can either open the door for bigger and better deals, or it can put your business on hold. If you don't have a SOC 2, there's a good chance you won't even get a seat at the table. Beginning a SOC to your port can be a huge burden, especially for startups. It's time consuming, tedious and expensive.

(00:03:55):
Enter Vanta. Over 3000 fast growing companies use Vanta to automate up to 90% of the work involved with SOC 2. Vanta can get you ready for security audits in weeks instead of months, less than a third of the time that it usually takes. For a limited time. Lenny's podcast listeners get $1,000 off Vanta. Just go to vanta.com/lenny, that's V A N T A.com/lenny to learn more and to claim your discount. Get started today.

(00:04:28):
Yuhki, welcome to the podcast.

Yuhki Yamashita (00:04:30):
Thank you for having me, Lenny.

Lenny (00:04:32):
I'm quite honored to have you on this podcast. For folks who don't know, we actually collaborated already on a newsletter post that has quickly become my fourth most popular post of all time, which you can find if you search for how Figma builds product. And so I am really excited to dig into a lot of the stuff that we, maybe, didn't cover in that newsletter. Also, just like how product works at Figma in more depth, how the PM team works, how you think about product, and things like that. So again, thank you for joining me.

Yuhki Yamashita (00:05:00):
Hi, team, as a huge fan of this podcast, so really honored to be here.

Lenny (00:05:04):
Wow, that means a lot. I really appreciate that. So you are currently Chief Product Officer at Figma, which is such an epic role. It's such an epic company. Could you take just, maybe, a minute or two to high level share your career arc, how you got to where you're today as CPO at Figma?

Yuhki Yamashita (00:05:22):
My first job out of college is actually at Microsoft, and I was the Product Manager on Hotmail. If anyone, any listener remembers Hotmail, and I didn't really know what product management was at the time, and I mute it as a interdisciplinary function that will give me exposure to all my other functions so that I can actually decide which function's interesting to me.

(00:05:48):
And so, spent a couple years at Microsoft. Through that, also, moved on to Hotmail to Windows. And at the time, they were working on Windows 8 and Windows 8 was really interesting because it's a very touch forward version of Windows. And so there's just a lot of conversations about UI and UX, and that was really fun for me.

(00:06:07):
And as I was thinking about what's next, I really felt the draw of Silicon Valley and I ended up at YouTube, and I believe Shishir has been on this podcast before?

Lenny (00:06:19):
[inaudible 00:06:19] you.

Yuhki Yamashita (00:06:19):
Yeah, so Shishir was leading YouTube at the time, and he continues to be a great mentor of mine, but had the opportunity to lead the YouTube app on iOS over there. And it was really funny because I had never touched the iPhone before my first day, so my manager, on my first day, just sent me to the Apple Store to buy an iPhone. But that was my next job and that was a really interesting change for me, too, of, and we can talk about this later, as well as different companies and different styles of product management and really figuring out, I think it was a place that taught me a lot about some of my product last weeks to date.

(00:06:58):
And this is also around a time where there are a lot of interesting companies that were working in the physical and digital space. And so Airbnb was one of them, Uber was another. So I felt this draw just because it seemed just a really interesting space to be in. So eventually, ended up at Uber. Uber was another company where I feel like a lot of my philosophy that, hopefully we can get into today, around how to build products, how to build products in the kind of environment that's really fast moving. And so that I learned a lot from there.

(00:07:33):
And to date, all those companies has really been focusing on the core experiences on consumer products, and that's really been most of my career. And as part of that, worked with a lot of amazing designers. But at Uber, I realized that I wanted to dip my toes into design directly. For the tail end, I actually switched from PM to design and managed a few design teams working on our bikes and scooter efforts just to understand what that's like. And it was around this time, around my Uber career, where we encountered this tool called Figma.

(00:08:08):
I'd happened to be working on a project that experimentally brought Figma into the company. It was a time in the company where we were trying to transform our culture to be much more transparent and inclusive, and Figma was the perfect fit for that. So, I got to watch how Figma changed the way it worked, how it's spread within the company. We got to know the Figma team a little bit, as well. And yeah, I was really drawn to that mission and as a product manager who's been straddling that boundary between design and products for all my career, I really loved how Figma proactively blurred that boundary and opened up that process of participating in design. So I really got behind that mission and that's how I ended up here, at Figma.

Lenny (00:08:49):
It's so fascinating that you moved into design from product, and then back into product. At Uber, were, what was the role? You were Head of Design for the mobility team?

Yuhki Yamashita (00:08:59):
Yeah, it's called New Mobility, focused on just our micro mobility efforts, basically. Yeah.

Lenny (00:09:05):
Do you recommend this path for PMs to switch into design? I know it's not something anyone can do, but do you feel like that is an important skill role to experience as a PM, you encourage people to try that?

Yuhki Yamashita (00:09:16):
Well, I decided it's not for everyone, but I think that it's, first of all, a really great empathy building exercise of understanding that point of view, and also pushing yourself to push on the product from a different angle. Because I think as a PM, you're in the center facilitating all these different trade offs, and when you go into design, you have to ignore some of those other aspects to really be insistent on pushing on the best experience possible. Just suspend everyone's disbelief in business feasibility or engineering feasibility to push on a vision. And that's just an interesting exercise to do.

(00:10:00):
And then, I think the last thing is, I actually think it's an opportunity for in design and PM to learn from each other. When I became manager of design teams, one of the things that I coach designers on, are how to win over PMs, and how to speak in PM's language, and likewise, it's important for PMs to understand that, as well. So those are some of the things that I thought were helpful, but again, it has to come from a place of passion that you know you really want to do this.

Lenny (00:10:29):
Which job would you say is harder; design or product management?

Yuhki Yamashita (00:10:32):
They're hard for different reasons. I would say managing designers is harder than managing product managers.

Lenny (00:10:38):
Interesting.

Yuhki Yamashita (00:10:39):
And I think part of it is that designers are, it's really important to focus on growing their craft and helping them develop as designers. So it might not be that the company's biggest problem is one where you can actually learn this new thing you're trying to learn as a designer, and this probably happened for engineers, too, right? You could be working on the onboarding funnel, and that might not be the best place to be learning micro interactions, or maybe it is, but those aren't always aligned.

(00:11:10):
Whereas, with Pms, it's a little bit more like PMs are just hungry for impact, and so you can point them to the biggest problems a company has. And while PMs also do want to understand different kinds of problems or have the experience working on different kinds of problems, at the end of the day, I feel they want to be working on the thing that matters most in the company. So from that perspective, it's easy.

(00:11:31):
But as you know, and the reason this podcast exists is because PM isn't easy. And so the discipline, I think, is harder in a sense that it's sometimes hard on a day-to-day pace to know if you're doing the best thing you could possibly be doing. And so I think that makes it a little bit harder as a PM, as well.

Lenny (00:11:52):
I had a designer friend who moved into a PM role, I had a product role at a startup and she's like, "Holy shit, I had no idea how hard being a product manager was, and a product leader. I have so much more empathy for the PM role." And so, it's interesting, it works in both ways. Similarly, I was actually a manager of engineers, at one point, and I felt the same way where managing PMs was a lot easier than managing engineers. So, translates to a lot of different roles.

Yuhki Yamashita (00:12:19):
Yeah, I can see that.

Lenny (00:12:20):
Folks listening to your career arc and just all the places you've been, all the wonderful things you've done. Imagine many people are like, wow, how do I have a career like that? Microsoft, Google, Figma, Uber. If you had to think back and identify maybe one habit, or one skill, or behavior that you think has most contributed to your success as a leader, as a product leader, what do you think that would be?

Yuhki Yamashita (00:12:45):
People who work with me know that I often talk about storytelling and, in fact, if you've ever reported to me, storytelling has showed up in some kind of performance review, I feel, and that's how much I care about it. And I actually think that a lot of being a great product manager is being a great storyteller. And I know a lot of us have already talked about it out there. I think the importance of storytelling is understood, but maybe I would share two things that are specific about it that I think are interesting.

(00:13:13):
One is to understanding the power of synthesis and it's this idea that maybe even as a early career PM, you're inside some of these reviews and a lot of people say, "Hey, at least you could take some notes for the meeting so that you're adding value." And so that's common advice, here, but I think the most powerful part of that is that in some ways, you can synthesize what happened. And a lot of things are said in a review and there's still this bring it all together into a distillation of a message. And even that's like, that's a lot of power, I think. And what do you take away from all these different opinions that all these leaders had, and how do you push that, push the project forward from there? So that's one example.

(00:14:02):
Or another example is, I really love thinking through frameworks and offering ways of talking about a problem or ways of thinking about a problem. And that's synthesis, too, of figuring out all these different disparate parts and coming up with a way to a lens to look at something. And I feel like it's something that was, I learned, mostly through literature classes almost, where you're doing literary commentary and you're reading a William Yates poem and you're trying to, you observe all these interesting things, but then you have to take those different observations and distill it into a thesis, into something cohesive. And I think that's what a good PM can do. All these different ideas, and opinions, and problems, and how do you distill it down? And so I think that's one aspect of storytelling that's really important.

(00:14:54):
And the other aspect of storytelling, of course, is a story is only as good as the action that it's capable of driving. And a lot of times that I often coach my product managers are on, we're living in a world where everyone is constantly distracted, and you get these 30 seconds of attention at a time. And so, just the ability to really tell something powerful that sticks is really important, the memorability of it.

(00:15:21):
And I often talk about memification, which is this idea that I found this out most at Uber, I feel, where there's certain insights, data insights, research insights that were memmified to the point where someone like Travis or Dara would just cite this insight in the middle of a meeting, and you know that you've really done your job as, maybe, a researcher or a data scientist or product manager if people are able to do that and draw from that in that way. And that's what, ultimately, sticks.

(00:15:52):
And so when you start thinking about it from that perspective, it's really powerful because it's the way in which knowledge is transferred within the company and you compel action for it. Or when I'm being, maybe, asked questions by other leaders or stakeholders, the thing that's going through my head is, okay, there's this story that, that leader is trying to develop, or a meme about what this project is about or what the biggest problem is. And so, what story are they trying to create in their head so that they can remember or talk about what's happened?

(00:16:28):
And if you take that mindset, you just realize that it's a really useful way to think about everything.

Lenny (00:16:35):
I'm really excited to chat about this idea because it comes up a lot. The power of storytelling, it's similar to being good at vision. It's like PMs are always told, "Hey, you got to improve in vision." Here's a skill the great PMs are really strong at. And I feel like storytelling is similar. It's this vague cloud of a skill that you build over time. And you mentioned a few things that you recommend to people that you work with. Think of it as a meme, maybe.

(00:17:01):
Is there anything else? When you're doing a performance review with a PM and one of their skill gaps is storytelling, is there anything else you recommend they specifically do to get better at the skill, or is it just do it again and again and watch me do it, watch other people do it and you'll learn?

Yuhki Yamashita (00:17:16):
Yeah, I think of it as resetting the internal computer of my brain a little bit so that I start from scratch again. And when I'm starting from no context at all, can I build up the story from bare and explain what's happening? And oftentimes, you're just caught in the middle of everything and you have all this context that might not be obvious if you step away from it for just a second.

(00:17:39):
I guess the way to think about it is, put yourself in another user's shoes, and that user is someone who has no idea what's happening and still wants to understand, in a nuanced enough way, what you're grappling with. And so, that reset moment, and to pull yourself out helps you tell a better story, in many cases. So that's one thing that comes to mind, yeah.

Lenny (00:18:03):
Got it. So it's escape the curse of knowledge a little bit and just assume people don't know anything about the context, the background, why this is important, come back to the beginning.

Yuhki Yamashita (00:18:12):
Yeah, I think another thing that where I learned storytelling is through teaching. So when I was a course assistant for a computer science class and I had to explain pointers, you're like, okay, I really have to borrow on real world metaphors or something that is much more grounding because if you assume a lot of knowledge, then it can be inaccessible to a lot of people. And so if you can tell a story that any student can understand, then you've really done your job. And once you've learn that skill of being able to tell anyone who has no context, then it becomes much easier to turn to these other audiences that are closer and closer.

Lenny (00:18:51):
When I asked you in our newsletter interview what one of the core philosophies of product managers is, in the way you think about product and the role of PM at Figma, an interesting thing that you highlighted is that to you, it's really important that PMs own the why of a product and an idea. And I think it connects to what you're talking about, now. I'm curious just why you think that's so important for product managers and why that's so core to the way you think about product, and at Figma.

Yuhki Yamashita (00:19:17):
I really can't remember why I heard this, but it really stuck with me because oftentimes, there's this debate about well, is a PM the person who comes up with the idea. And the answer is usually no, it doesn't have to be at all. And in many cases, in our case, your customers come up with a ton of different ideas and certainly, the what and how are things that are shared within the company and not something that PM uniquely drives. But I do think the why is something that I really always hold the PM uniquely responsible for.

(00:19:48):
And I think the place where I learned this, the importance of this the most, was actually first, at YouTube. I had been working at Microsoft for a long time and I was early in my career, so I was just really focused on my, what we called, our feature crew, our engineer designer, our tester, and just writing specs that really specified exactly how everything works. And so that was the Microsoft culture back then, and your specs had to be perfect, right?

(00:20:19):
Then moved over to YouTube, and all of a sudden, you're responsible for an entire app, and you have a pretty big team, and you cannot specify everything that happens. And so, naturally, designers and engineers are just making their own choices. Made is an error handling situation, and in Microsoft culture, you would've had a table that specifies exactly what happens during that error. But in Google culture, it's like, okay, well the engineers and designers, they can figure it out.

(00:20:47):
So then it's like, how do they make a really great decision? How do they make all these local decisions that you're not a part of, how do you make it so that a great decision's made? And if everyone has an understanding of why we're doing this, what problem we're solving, then people can make really great decisions. It's the only way you can really scale. So that's where it came from.

(00:21:06):
And then since then, I've started to realize, also, that there are other functions that do this well. So for example, our engineering team at Figma, whenever we do a retro or postmortem, we do this thing called five why's. And it's the idea behind it, it's like, well, why did this happen, outage happen, okay, and why did that thing happen? And go deep enough where you can find the root cause and go fix all those things.

(00:21:28):
And I think a PM can do this, too, which is a customer is asking for a feature, but then you would say, okay, why are they asking for it, and back up the problem. But I think there's one more step you can take, which is, why do they have that problem in the first place? And maybe there's something there, and that could be an opportunity to make a bigger product impact by fixing that underlying condition that created the problem in the first place.

Lenny (00:21:55):
That's so cool that you actually do the five whys. I hear people talking about the five whys all the time, and I don't know, I haven't heard people actually using it. So you actually do this at your post-mortems, you said?

Yuhki Yamashita (00:22:03):
Yes. Engineering team that's accepting them, yeah.

Lenny (00:22:07):
That's so interesting. Can you talk a bit more about these postmortems? Is this just when something goes wrong or is this just every project you retrospective postmortem thing?

Yuhki Yamashita (00:22:14):
As it relates to five whys, it's more when something went wrong. But I do think we have a retro culture, [inaudible 00:22:24], where there's always opportunity to make things better. And if you don't create the environments to talk about it, then some of those will go unaddressed forever, so.

Lenny (00:22:33):
Cool. Okay.

Yuhki Yamashita (00:22:33):
Yeah.

Lenny (00:22:34):
Another attribute of the product team and how you build product at Figma that you shared that was really interesting is you mentioned that you just have an obsession with a proximity to customers, that you make sure your PMs and product team are really close to customers. When you hear that, you're just, imagine everyone listening is like, oh yeah, we're really close to customers, we talk to customers all the time. Of course you got to talk to customers. I'm curious what it is that, maybe, you think sets you apart, in terms of how you think about being close to customers, and if there's a story, maybe, of just, wow, this is how close we are to customers and maybe something that emerged out of that, that'd be really cool to hear.

Yuhki Yamashita (00:23:07):
Well, I think a lot of it starts with our origin story in many ways, which is that way back when, when Dylan, the small group of people were building Figma, this is the time when no one believed it was possible to have a design editor in the browser. And so it just seemed like science fiction, almost. And yet, what Dylan did consistently throughout, was just put the product in front of designers, ask them for feedback, come back to them the next time with that feedback implemented, and it becomes better and better and better.

(00:23:40):
And at no moment was there a tentative expectation that the designer suddenly turns around and implements that tool in their organization. It was really just about listening really carefully to what the community had to say, and through that process, making them evangelists. And that's where a lot of how Figma came to be and why we have such a strong connection with our community where we've actually, they've really helped shape the product to date, and there's a deep belief in that, and they're the ones in that are now advocating for Figma and helping us spread within the community and within their company.

(00:24:20):
So that's the backdrop for why we have such a strong connection with our customers, and there's a lot of things that you see. So for example, maybe someone on my team Sho, and oftentimes, Sho will tweet out to the community, here's what we're thinking, or we're actually thinking about focusing a lot more in prototyping. What are the top problems you're seeing? And people come back with all these different answers because everyone's passionate. And we go in there and just look at all the feedback and understand what people are saying and just have a stronger pulse on how people are feeling. And that's not to say that everything is then implemented verbatim, but we really find it useful to feel like we have a sense of what people are thinking.

(00:25:05):
And I think the most crazy version of it, maybe, is Dylan's always reading customer feedback. In fact, has reads the most customer feedback of all of us and has been doing that for a decade. And oftentimes, there used to be this thing where he would drop in tweets that he sees into different Slack channels to be like, hey, this seems concerning, or we're getting this feedback. And it got to a point where we got big enough where people would feel like they had to drop everything and deal with that tweet.

(00:25:31):
So Chris, our CTO, and I intervened. We created this new channel, private channel called Concerning Tweets, and it just, we're this small group of us that Dylan can drop us in. And these are tweets that aren't going viral, by any means. They're just things that you see is with one like, sometimes zero likes, but he feels there's an essence of truth to them and we make sure that we look at what's going on there and see if there isn't something much bigger that we should be focusing on. But that's the extent to which someone like Dylan, from top down, implements this idea that we need to be staying close to what our users are saying.

Lenny (00:26:13):
That's an awesome idea for a channel, a way to contain that potential madness that it creates. Is there anything else you've learned around hearing feedback like that in a tweet, let's say, or just a few loud voices and deciding what to actually work on? Do you have an approach there? Just deciding what's worth paying attention to?

Yuhki Yamashita (00:26:31):
As we built out our research and data functions, it's really important to balance out the vocal minority with what's actually happening. So I really view some of those tweets more as canaries in the coal mine, in a way, and inputs into, many inputs we have around everything our customers could possibly be experiencing. And it's important to realize that we have certain forums, like our support tickets, where customers are, tend to be much more dissatisfied. And we have other kinds of inputs that are sales conversations with prospects, where it's really more about perceptions around Figma, in some cases.

(00:27:11):
And I think it's just important, especially as a product manager, to feel like you have this balanced portfolio of different kinds of feedback to know that you don't have any blind spots. So I think that's one of the things that I focused a lot on when I came in, which is the Figma team is very good at Twitter and staying on top of the sentiments. And luckily for us, a lot of designers are on Twitter, but the reality is that most of our audience, at this point, probably aren't. And so building our capabilities to extract feedback or more insight from those other sources, as well.

Lenny (00:27:46):
That reminds me, I think Twitter was really instrumental to the beginnings of Figma. I believe Dylan made this social graph of the most influential designers on Twitter, and that was his go-to market strategy, get those designers on Figma, and then I think he open sourced his code to do that. Is that right?

Yuhki Yamashita (00:28:02):
Yeah, that sounds right to me. And he is very intentional about which designers we need to win over. I think it was very novel at time.

Lenny (00:28:11):
What is it like to work with Dylan Field? As an outsider, he's a legend, feels like he's an incredibly smart, talented, hardworking, CO. There's always tension a little bit between a Chief Product Officer and a CO, and so I'm just curious, what do you like to work with as a product leader? And then, is there, I don't know, a memory that comes to mind of just a way that encapsulates what it's like to work with Dylan?

Yuhki Yamashita (00:28:32):
We're very different, actually. And Dylan is very, he's very based on intuition and instinct. And that intuition is actually built off of thousands and hundreds of thousands of customer interactions where he might look at something and be like, "You know what? This isn't going to land well," or, "Here's the biggest problem right now." And you're like, well, how does it conclude that? And part of my job is to build out that logic streak for him of how did you arrive at that conclusion so that people can understand that at scale, in a way. But he's very much about that.

(00:29:09):
Or I think there's a way which, sometimes, it's a product manager, you want to lay out a problem and say, okay, we're going to first focus on this problem, and then [inaudible 00:29:21] these three approaches. We're going to take this approach and have a review at every step along the way. But for Dylan, I think, it's very hard for him to really fully get bought into it until he sees the end implementation to viscerally feel if this is a good solution or not. And so I think that's the kind of thinker he is where he really needs to see it to feel it. But it's not totally random. It's based on all these interactions with customers and somehow encoded in him to build up some of those intuitions.

(00:29:55):
And I think one of the things that's really interesting about him is that he actually really cares very deeply about any given user and how they're feeling about Figma. I remember when, during the height of the pandemic, we were doing a one-on-one walking around Delores Park, because this is the era where you would take meetings, if you take meetings, they're all outside, and then he needed to use the bathroom. So he came out to my house in the Castro, he used the bathroom, and then he met my partner, and my partner was on Figma, had Figma pulled up because he is just doing work. And then Dylan just went straight in there and wanted to ask what the biggest problems were or what's not working, and they started geeking out on some issue around Google fonts, and this is the first major interaction between the two of them.

(00:30:45):
But it's one of those things where that's how much Dylan cares. And on one level it's just easy to say, "Hey, this is a single user who just happens to be using your product," and be dismissive with it or not care that deeply because you think you already know all the biggest problems, but that's not his attitude. And so that's the level of, I guess, customer obsession, if you will, that he exhibits and then, in turn, informs his intuitions.

Lenny (00:31:16):
That's amazing. Figma is 10 years old at this point. He's been at this for a long time, like a decade. And the fact that he's still so obsessed with just a random person just using Figma and he's taken the opportunity to experience it in real time every chance he gets, sounds like.

Yuhki Yamashita (00:31:31):
Yeah.

Lenny (00:31:33):
Hey, Ashley, Head of Marketing at Flatfile, how many B2B SaaS companies would you estimate need to import CSP files from their customers?

Ashley (00:31:41):
At least 40%.

Lenny (00:31:42):
And how many of them screw that up, and what happens when they do?

Ashley (00:31:45):
Well, based on our data, about a third of people will consider switching to another company after just one bad experience during onboarding. So if your CSP importer doesn't work right, which is super common, considering a customer files are chalk full of unexpected data and formatting, they'll leave.

Lenny (00:32:05):
I am 0% surprised to hear that. I've consistently seen that improving onboarding is one of the highest leverage opportunities for both signup conversion and increasing long-term retention. Getting people to your a-ha moment more quickly and reliably is so incredibly important.

Ashley (00:32:19):
Totally. It's incredible to see how our customers like Square, Spotify and Zora are able to grow their businesses on top of Flatfile. It's because Wallace data onboarding acts like a catalyst to get them and their customers where they need to go faster.

Lenny (00:32:36):
If you'd like to learn more or get started, check out Flatfile at flatfile.com/lenny.

(00:32:44):
As an outsider, it feels like Figma is just always firing in all cylinders, shipping the best product. People love it. I use it, I should've mentioned this, but I use it probably every day for my newsletter for illustrations and banners and all this stuff. Yeah, I don't know what I do without it. And it always feels like Figma is just killing it. I know that's never the reality. I'm curious, is there a story of something that just, maybe, didn't work out the way you hoped? Whether it's a feature, a launch, or something like that that just shows people that it's, not everything always works out.

Yuhki Yamashita (00:33:14):
We run experiments all the time that don't come back with winning results, and we certainly have built a lot of more complex features that took a while to take off.

(00:33:24):
So a good example of this is in the design system space, we have something called branching and merging. And branching and merging is this workflow of maybe you're building a really complex design system, and then you don't want anyone ever randomly touching your components that are used by thousands of other projects, so you create this workflow of, someone, maybe, effectively suggesting a change, you're reviewing it and then pushing it in.

(00:33:48):
And so, in theory, makes a lot of sense and things that our customers asked us for, but once we built it, in the initial stages, just didn't really see that much adoption and didn't feel great because it's a really big investment for us. It's a lot of work that we put into it and there's just many different reasons. Some of it was performance, some of it was, this is a foreign workflow and it just takes time, and us helping customers implement some of those workflows, we realized some gaps because we don't really use it that much ourselves.

(00:34:20):
And so, I think as we're getting bigger, one of the things that I'm realizing is that we're starting to build a lot of features that are not, necessarily, for organizations like ours. And when we do that, we really need to be creative about how we understand how effective those are because we've had such a strong culture of internal testing and dogs looting, and those are the things that really helped make sure the quality of our product was good enough. But now we're working with really new types of customers and needing to push ourselves and build that muscle, as well.

Lenny (00:34:54):
Speaking of high quality software, again, I'll repeat, I think Figma is one of the most beloved software products. It's become central to a lot of the ways people work. It's also, I think, one of the fastest growing SaaS products, in general. And I don't know, this is maybe the ultimate softball question, but I'm just curious, what is it that you do at Figma to build such high quality software? Because it's rare for B2B software, especially. What do you do as a product leader, as a product team to just set this high bar, make sure that the stuff that you put out is great consistently, and the more tactical the better?

Yuhki Yamashita (00:35:27):
It's so important that you're using your own products. And I think we're in a very lucky position where all of us can get creative around using Figma in some way. And obviously, designers are the, internally within Figma, are the most vocal and the ones who are in the product six hours a day, essentially. But even for PMs, one of the first things I did when I arrived was we were a little bit more of a memo culture, and I was like, you know what? We should be a deck culture because we can build those decks in Figma, and just that act alone allows you to encounter a lot of issues and for you to get familiar with it.

(00:36:06):
And so I think there are ways in which, sometimes, you have to get creative to enable your company, your entire company to use a product more. Or as an example, recently, we just did calibrations for performance reviews in FigJam, and our Head of Design, Noah, came up with this amazing template and we distributed it through HR and that was another reason for everyone to use FigJam. And so that's the biggest thing. The more hours people are spending inside your product, internally, I think, just naturally becomes better. Because a lot of times, it's not just about people raising their hands and saying this is the problem, it's more about you just want to make your own workflows, your own day-to-day better, and derive satisfaction from improving that.

Lenny (00:36:50):
So the takeaway there is get your product teams to use the product as often as possible. That is a really clever way of doing that at Figma. I know you mentioned in our newsletter interview that you switch from memos to decks. Usually, it goes the other way around, and now I get the second order effects of that where people are building their decks in Figma. That is very clever, and not everyone's building collaboration software, but that is a really clever idea. And I think there's probably a bit of trickle down from Dylan's obsession with the product in making it, just continuing to just be obsessed with making a great experience combined with that, people using the product and this trickle down of we really need to make this as awesome as possible.

Ashley (00:37:27):
There are other companies, for example, when I was at Uber, especially working on the driver's side, of course we went out and driving, and that speaks to some aspects of it. But one of the things that I've realized is when you are logging a bug and you add some engineers to it, to have them look into it, the degree of motivation is so different if that engineer has, somehow, experienced a problem in some way.

(00:37:51):
So for example, everyone at Uber would take Ubers into work, and if an engineer working a driver app saw a driver struggling with something, they would find it embarrassing and feel personally accountable to go and fix that. And when you can create that sense of personal accountability, then all these crazy things happen and all this progress happens. So I think for us, as getting creative at Uber about, okay, well how do we increase those interaction points at the point where, if someone building feels like they have some kind of personal relationship with the end user, and this is what happens, at Figma, too, where a lot of our designers feel personally accountable, in a way, because all their customers are people they already know in the community on Twitter and all those kinds of things, so they feel like they have to put something out there that's defensible or that they're really proud of. So I think that personal accountability can really make a difference.

Lenny (00:38:48):
That begs a question of, I imagine this engineer at Uber coming back to their desk and like, I've got to fix this bug. And then their PM's like, no, we got goals to hit, here's our priorities, we got this roadmap, we don't have time to fix this right now. It's just one random bug. And so there's a two part question, just like you have a approach to that, do you encourage engineers, designers just fix stuff that seems broken/you mentioned that you have a fun experience with OKRs and how you've approached OKRs at Figma, and you've gone back and forth a little bit. And so maybe, as a second part, just talking about your experience with OKRs at Figma.

Yuhki Yamashita (00:39:21):
The first part, I would say that I think one of the most powerful things, especially for startups, is that bottoms up energy, and maybe a developer noticing something is wrong and just going off and fixing it. And for the most part, I try not to get in the way of that because if people are doing that constantly, and everyone the company is trying to make the product better, that is sometimes a way more effective way to improve the quality of experience than this top down of, oh, let's define this quality experience metric and try to change all the things, because you might miss these things. So that's one aspect.

(00:40:01):
And the second thing is, I think a lot of PMs have grown to realize this, which is, if you ask an engineer about how much time it'll cost to go and build something, and it's something that they came up with or they're advocating for, it's almost always half the time as something that you are asking for, as a PM. And that motivation is so different.

(00:40:24):
And that's why getting the buy-in of developers is really important, because you want to feel like they're personally vested in this problem, and then, all of a sudden, their willingness or their creativity, or all these things spike. And so when you think about all those things, when there's a situation where an engineer or a designer's trying to fix a real custom problem, I'm like, by all means.So that's on that.

(00:40:50):
OKR is totally bigger topic, and maybe I'll set the conflicts of why I have such this love-hate relationship with it, which is that a lot of my career, I've actually just worked on core experiences, and OKRs were the bane of my existence, in a way. Because when you're working on a core experience, sometimes you're just, I'm just trying to make the experience better. And sure, I can come up with this BS way to measure what that looks like, but that's not what I'm thinking about every day, anyway. So it just seems very performative, and there's just a lot of work that goes into it.

(00:41:26):
And you encounter one of two situations. One is, you come up with some secondary metric that nobody actually cares about that, technically, you can measure and, technically, you can move, but you haven't actually proven that it really matters. So maybe it is some satisfaction metric that you have on some survey, but you haven't actually done the work to show that, that actually has correlations with retention or anything that actually "matters for real" in the business, or it's some weird usage metric or something like that.

(00:42:00):
And then the other extreme is to say, no, we're going to be ambitious and we're going to send it for business goals. So for example, even if I was the PM for the rider experience at Uber, I'd be like, you know what? We're going to contribute incremental trips because the experience is going to be so good that we can get more people to come back. And I think the reality for a lot of that is, it's a metric that you don't have full control over or there are many hops until it can affect it, and okay, well maybe we can make the experience better and maybe that improves your attention and maybe this. And by the time you get there, you actually can't even prove that you moved the top level metrics. So either you anchor something that matters, but you can't move, or you anchor something that you can't move but doesn't actually matter. So that's the relationship I've had with [inaudible 00:42:45], so even it's really frustrating.

(00:42:47):
So when I write that thinking about, one of the things I realized is that we had OKRs, but people were treating it almost as a to-do list or a task list of, okay, here's how, by the end of quarter, I need to complete these tasks and then I'll feel like I did my job, kind of thing. And we would have these dreadful meetings where we go through these spreadsheets and have people stand up in front of everyone and talk about those commitments, or those key results, rather. But they were dreadful for a reason, which is that you just couldn't really understand what the team actually really cared about. And it got to this point where we had all these, and this is similar to the secondary metric problem, but either you couldn't approve that you actually moved it, or you're trying to work on something that I don't actually understand why it's useful.

(00:43:39):
And so that was when I deprecated it and said, "I just want to understand your headline. What are you trying to do, philosophically?" And just don't stress about whether you can measure it or not. I just don't understand what you're optimizing for, and let's first have that to date. And then once we get there, then let's talk about, okay, well what are some ways that you can measure it? And some of it's qualitative, so it's quantitative, and that's fine. And I almost feel like sometimes, it's better to take the report card approach of saying, Hey, just give yourself a score, tell me how you derive that score, let's all understand that the metrics and those inputs that go into it can change over time, and we're going to get more sophisticated about how we measure it. But at least everyone understands what on earth you're trying to go for.

(00:44:29):
So that's where I moved in my first year, I would say, and then we hired a Head of Data who is a friend of mine from Uber, too. And one of the things she felt was, okay, but it's still very loosey goosey, and super subjective, so let's just try to bring OKRs back and see if we can just do them better next time. And so we've done that, and they were definitely better than when I first arrived just because we had a data science team and we had more rigor around metrics and things like that. But again, this time it was less about not understanding what people were doing, but more not understanding if teams are actually committed to moving those OKRs. And one of the problems that you find is we have these OKRs, but they feel like these post-rationalizations of the projects that you're working on, anyway.

(00:45:17):
And at the end the quarter, you come back and see if those OKRs move, fingers crossed. But if you stop an engineer in the middle of the hallway or the virtual hallway, so to speak, and ask them, okay, what are your team's biggest goals or OKRs? [inaudible 00:45:31], they wouldn't be able to say it. They're just like, well, I'm working on this project that's really important. And so it's, well, what's the point of publishing this OKR if you're actually not thinking about moving it on a daily basis almost, right?

(00:45:46):
And so that's when we've tried to experiment with this terminology, well, maybe if we should call it commitments instead, people would take it a little bit more seriously. And it's my belief that oftentimes, commitments are this care between the why and the what, and sometimes the face of the commitment is the what.

(00:46:05):
It's a project and there are many why's behind it, or it's the why and there are many projects behind it. So that what's trying to formalize that idea, but it definitely felt a little bit complicated, a little bit. Sometimes people are like, well, OKRs exist for a reason and this is, basically, an OKR with just a different name. So my honest sense is we still haven't figured it out and we're still iterating on a bunch of different things, but I think I've developed some philosophies around it, which is, no matter what you call it, because it doesn't matter as much.

(00:46:38):
I think that, for me, there are three things that really matter about the good OKR, and one is legibility. People look at it and understand what it is, and it's not some weird obfuscated metric that doesn't mean anything to anyone. I think actionability, I want OKR to inspire action. You look at that and you're like, it's stirs action, makes me want to do something differently. And the third one is authenticity, which is, does this actually, honestly depict what you're doing, what you're trying to do on a day-to-day basis? Because if it doesn't, then it's hard for me to trust that, that it matters. Or if that's something that just happens to describe what you're doing but isn't really connected in a meaningful way, then I question the value of it all.

(00:47:28):
So that's why I am in the process. But I definitely am all ears to advice around this kind of stuff, because I feel like we haven't quite cracked the code.

Lenny (00:47:38):
I love hearing that. That ,hole journey. I feel like you always hear from product teams, here's what we do now. You never hear, here's the experiments we've been through, here's what we've tried, here's what worked for a while, here's what doesn't work now, and here's what we're doing now. So it's really cool just to hear all the experimentation you've done. Clearly, Figma is a company where you encourage experimentation and trying new things that aren't working, and it's cool they have the flexibility to just like, let's just do headlines for now, and no more specific goal metrics. We're just going to build things that we think are important.

(00:48:09):
And in the newsletter post, for folks that are listening, you actually show the templates that you're using these days for planning your projects and laying out your OKRs, so folks can check those out if they're interested in seeing how you're doing that, now. You also mentioned you've hired this awesome data scientist, and maybe just expanding that further, I imagine a lot of the success of Figma and the product that you built is the people that you hire. At Figma, I believe you have 22 product managers, which sounds very small for a company like Figma, and I imagine they're all amazing. I'm curious what you look for in product leaders and product managers that you hire that, maybe, other folks aren't as focused on, and just what does the interview process look like at Figma?

Yuhki Yamashita (00:48:51):
Yeah, I shared some of these things. I really feel passionately about storytelling, and not to give it away or anything, but one of my favorite interview questions is asking, "describe to me a time when you're part of controversial product decision, and what did you do," and all those things. And I think it's really revealing because if they can set up this conflict and understand why this problem was really important and represent both sides in such that you can understand why that conflict existed in the first place, then they can do it in this even-keeled way, where you realize that they can take on these different perspectives. You start to learn a lot about that person, I think.

(00:49:35):
Or sometimes, I just ask them for basic things, okay, talk about a big problem that you worked on. And the thought experiment, for me, is always coming out of that, do I feel compelled to work on that problem? And no matter how boring it sounds on the surface, I think a really great product manager can cash something, it's like, well, this is why it's so existential for us, and this why it's so interesting, and really rally the troops up. So that's one big thing of storytelling communication because at the end of the day, so much of our job, it's around that.

(00:50:07):
I think other than that, some of the things that I value or things I think about as, hi Dan with UX conversations, it's like we talk about problem, and I think about when you're exploring solutions, it's this tree of, okay, there's just these branches of explorations and you finally arrive at these solutions. And a ton of people who can go up and down branches really quickly, have a really high command of all these different altitudes, as well, so that we can talk through a lot of things at the end of the day, feel like we walk away with some progress.

(00:50:43):
And I think that at Uber, our first two Product Officer, Jeff Holden, was someone who often talked about fast forwarding to the future and this idea that, okay, let's just pretend we ran that experiment. What do you think it'll come back with? Or let's pretend we ran that, you just use a study. And the PMs who have the ability to imagine those outcomes, I think, it helps us be much more efficient, too, because we're like, well, if we all think that it's going to go there and that's not going to compel us to take any action, why do it at all?

(00:51:17):
And so I think a lot of PM is about those shortcuts that you have to take. And it's not just about what we build, it's about building the right things. And sometimes, it's just as important to decide not to build something, but it's all only possible if you can have that kind of imagination or that ability to see around corners.

Lenny (00:51:37):
I love that. I was going to ask you for your favorite interview questions in our lightning round and you jumped ahead, which is great. And those are really good examples. Hopefully, they don't give too much away. I want to chat a bit about growth and how Figma grows. If you ask people about product led growth, and just whenever people talk about product led growth, they're always companies like Figma, Slack... Figma is always seen as a model of product led growth and a product that grew through product.

(00:52:04):
I imagine now, there's a very robust sales team, and I imagine, even earlier than people, probably, imagined there was a sales team. I'm curious, as a product leader, what you've learned about how to effectively work with sales and what you teach your product managers about how to work with sales to collaborate effectively.

Yuhki Yamashita (00:52:24):
We're really lucky to have a sales team that understands their product really well and can hold their own with customers who are often also design leaders, product leaders and things like that. And I think that kind of credibility goes a really long way. One of the things that we all are collectively realizing is, we talk about product like growth, but in some ways, I like to think about it more as community led growth or there are certain people inside a company that feel so strongly about Figma and that they're helping push for it in these advocates and evangelizing for Figma.

(00:53:03):
And so oftentimes, what the sales team does is really empower those individuals to make a stronger case or connect them to the rest of the company so that we can get a wider deployment or more leadership buying and things like that. And so oftentimes, a sales team is playing that role of creating those human connections and helping equip designers that feel passionately inside a company with the data, with the stories and all those things to help make a case. And I think that's the most powerful way in which we can spread where the space of Figma is not the sales team, but in fact, it's the internal designer.

(00:53:47):
And so that's the mental model that I think we've been using it. We're fortunate enough to have people inside companies who are so passionate to want to play that role. And so when you take that lens on, then you start to understand, okay, how can we help set this person up for success? And the sales team has different ways to do it. The product team can help, in terms of giving them visibility into how we're thinking about evolving the product or what other customers might be doing. And so, I really see it as this partnership to enable that much as possible. And I think that's what, to me, product growth looks like at Figma, is that.

Lenny (00:54:29):
That is really interesting. Basically, making your champion inside the company a superhero, helping them be more effective at what they're already doing, which is evangelizing this product that they really love. Interesting.

(00:54:42):
Is there anything that you think Figma did early on that you think was really important for it to start to grow, either in this way or in a different way? Imagine there's just a lot of product led growth founders that are trying to create a product led growth product, and they fail. And so I'm curious, just what do you think people often miss and what do you think Figma did right that got it going?

Yuhki Yamashita (00:55:02):
I think a lot of it was about the level of intention around building community. And the more there are organic conversations happening about Figma, the better. And one of the nice things about Figma is you can share out a file that you've been working on, and effectively open source something, but it's your way of showing, here's how we do it at so X, Y, Z company, and sharing that with the rest of the community. And when people see that and when people feel like they have this insider view in how other companies work, that's where there's a lot of interest.

(00:55:38):
And more recently, over the last few years, we've really been focused on a program called Friends of Figma where we have people who are passing about Figma, and all our different geographies come together in a Discord channel. They meet regularly and are helping us evangelize. And again, that's that human connection between users, and then between us and the users is something that really helps build that kind of loyalty, which is the thing that, then, fuels all the champions to really push for it, internally, and give people the enthusiasm and courage to do that inside their organization.

Lenny (00:56:16):
It's interesting how many corollaries there are to Notion and how they got started. I recently chatted with Camille, I don't know if you heard that episode, but there's a lot of similarities with how Notion use their community to help jumpstart growth and continue to grow.

Yuhki Yamashita (00:56:29):
Totally.

Lenny (00:56:30):
It's interesting that you can call that community growth, product growth. There's a lot of overlap there, potentially.

Yuhki Yamashita (00:56:36):
For sure.

Lenny (00:56:37):
What advice would you have for folks that are, I don't know, maybe you already shared this, but just if you're a product led growth founder listening to this, do you have any other piece of advice to that founder about how to get started with their product, their community, their growth strategy? Anything else you'd want to share there?

Yuhki Yamashita (00:56:52):
Maybe a different way to talk about what we just talked about, is just, there has to be this, almost irrational, this emotional response to your product and this like love for it. First, it has to be cultivated internally, too. People, internally, have to authentically love something to really stand behind it. But then, externally, too, if people are loving something to the point where they can sing at the top of their lungs and just really talk about how Figma's, great, if we can get there, that's a wonderful place to be.

(00:57:27):
And I think that's both a combination of you've really solved their problems well, but you also equip people with a philosophy around a different way of working. And I think that's what worked well for Figma, too, which is, there's something controversial about this idea that everyone can see what you're doing, or that multiple designers can be in the file at the same time. We like to say that one of the first responses we saw [inaudible 00:57:51] Figma was, if this is a future of design, I'm quitting. I'm changing careers. And there's that tension of that narrative tension, but that is signal that you're part of this revolution and you're trying to change something. And when it can equips your customers or user base with that, and I think that's something that they can really get behind and champion, so it's not just that they're championing for a tool, they're also championing for a new way of working.

(00:58:20):
Obviously, that's a tall order or [inaudible 00:58:23] come up with that. But hopefully, if your a founder, you're working on something, your mission is so big that you have those kind of ideas, and it's how do you actually equip your customers to want to talk about that?

Lenny (00:58:35):
That's awesome. Reminds me of a quote and a tagline that the Airbnb's first growth team had for a long time. Love drives growth, not the other way around. They made posters of this, put it all over the product teams.

Yuhki Yamashita (00:58:48):
I love that.

Lenny (00:58:49):
Part of the office and seemed to have worked for Airbnb, clearly working for Figma.

(00:58:54):
One last question feels like a question we have to touch on. I don't know how much you can say about all this stuff, but with the potential acquisition with Adobe, which I know isn't done, yet, but I'm just curious, what do you think will change, may change, you're hoping will change, you're hoping won't change in how you build product at Figma within Adobe?

Yuhki Yamashita (00:59:12):
Totally. Yeah. As you said, it hasn't closed, yet, and so we're still independent companies, but when we think about that theoretical future, I think about people often ask me, so what's going to happen, in terms of the products that you work on, and how is that going to influence Figma? And the answer is, we don't know, yet, but I get excited about two avenues. One is just really continuing our current mission of making product design better. And the reality is we look at product design, a lot of people are still using both Adobe and Figma alongside each other. And maybe you're creating that micro interaction in After Effects, or maybe you're doing that intricate illustration in Illustrator, or editing Raster in Photoshop, and then you're bringing some of those things into Figma. But when you think about the end product development process, there's so many ways in which, if we can make all those things seamless so that you're not juggling a bunch of apps, or maybe you can have one single source of truth, that's really exciting to me to think about. So concretely what that means, I don't know, yet, but as thinking through those journeys, that gets exciting for me.

(01:00:22):
And then the other thing is really collaborating with the rest of Adobe and thinking about, we've figured out something really interesting in the form of realtime multiplayer collaboration, and that, as a platform. Adobe has a much broader set of use cases that they've been pursuing, and what do those two things together, what could that enable? And that gets exciting for me to think about all the creative tools that I've used in the past, be it video editing or 3D objects or things like that where it's, okay, if we can bring in the power of the browser, of multiplayer, of this feeling of openness, would that make it way easier for people? Would it make it much easier for people to share work or get involved?

(01:01:04):
So those are the things that go through my heads, in terms of what's possible. In terms of what I don't want change. I really think that we've figured out something really amazing, in terms of our relationship with the community. We talked about proximity to community and our users. Those are things that we intend to keep and keep doubling down on. And I think it's such an important part of the magic of how Figma works. So it's something that, I think, I will continue to do and that's what I draw a lot of motivation from in the first place.

Lenny (01:01:34):
Awesome. You also get to work with Scott Delski, which is going to be pretty sweet and hoping to get Scott on this podcast at some point, too.

Yuhki Yamashita (01:01:41):
That'll be awesome.

Lenny (01:01:42):
Any closing thoughts before we get to our very exciting lightning round?

Yuhki Yamashita (01:01:46):
It's really easy to listen to some of these podcasts and feel like, oh, these people have kind of figured everything out.

(01:01:53):
But the reality is, we haven't, and we're still experimenting with a lot of things. OKRs is a really good example of that, but a lot of other things. And so, just the other day I wrote about this idea of us living in a work in progress world, and I was talking about more from the context of we live in a world where all of our products, our product players, our strategies are work in progress, and how do you work in a world like that, when what you're reviewing can change the next day.

(01:02:23):
But in a similar way, I think the way we work, the way we run product processes as product managers is, itself, very much a work in progress. So I would love to encourage this kind of conversation, Lenny, that you're facilitating just because you have so much to learn from each other. And I'd love to continue to learn more from all of you on interesting ways that you grapple with these age old problems around things like how to set goals, or how to review work, or how to plan.

(01:02:54):
So anyway, just wanted to signal that we are very far from perfect, and I really eager to learn from everyone else, as well.

Lenny (01:03:04):
I love that. That also reminds me of something the Airbnb founders always came back to. Joe and Brian were both designers, and as you learn to be a designer, you are taught that everything around you is designed by someone. Someone just decided this webcam's going to look this way and work in this way, this chair, somebody decided very specifically, it's going to be like this. And we assume the things that we are working within are just, they're figured out. Someone much smarter than me figure this out. But it's usually just someone just like you that had to figure something out quickly, and then that's what you're doing now. And so they always encouraged everyone to just remember someone designed this, doesn't mean it's the perfect solution, and you should always rethink things like that and not assume.

Yuhki Yamashita (01:03:44):
Yep.

Lenny (01:03:44):
Well, with that, we've reached our very exciting lightning round. I've got six short quick questions for you. I'll just go through them pretty quick, whatever comes to mind, share, and we'll see how it all goes. Sound good? All right.

Yuhki Yamashita (01:03:56):
Sounds great.

Lenny (01:03:56):
Awesome. What are two or three books that you've most recommended to other folks?

Yuhki Yamashita (01:04:02):
First one that comes to mind is Switch, and it's really about how to affect organizational change, something that's Shishir recommended to me and we have the difficulty of affecting change in a large organization, basically, and how to overcome that.

(01:04:16):
The second one I would say is my favorite book of all time is one called The Story of the Stone, and it's a Chinese novel, one of the most famous Chinese novels of all time. And it's thousands of pages. It all takes place in a garden, but it's one of the most beautiful piece of work I've read, so I like to recommend that, even though it's nothing to do with PM.

Lenny (01:04:38):
Did you say thousands of pages?

Yuhki Yamashita (01:04:39):
Yeah.

Lenny (01:04:41):
About a stone. Wow. I will check this out. I love it. I've not heard this one before. Favorite other podcast, other than the one you're currently on?

Yuhki Yamashita (01:04:49):
Well, I'll have to admit, I'm actually much more of a visual learner, not a listener, and so I rarely listen to podcasts, but the two that I have listened to, in earnest, was first one was Cereal a long time ago, and then yours.

(01:05:04):
So I think some of the best, actually, but otherwise, more into reading.

Lenny (01:05:09):
Awesome. This show's also on YouTube, for folks that don't listening and like watching things. Plug, plug. Favorite recent movie or TV show?

Yuhki Yamashita (01:05:18):
The last movie I watched was called The Good Nurse, and it was about a serial killer working in a hospital, but it was a very different take on it. It was very human. It wasn't grotesque at all, and was talking about how broken our system was. So, highly recommend it. Quite sad, but yeah.

Lenny (01:05:37):
Okay, good tip. What are some SaaS products that you love that you, maybe, use at Figma or that you just discovered that you find very useful?

Yuhki Yamashita (01:05:45):
Kind of cheating, but as I mentioned earlier, we're starting to use FigJam for everything from calibrations, to interview debriefs, to product reviews, to everything. So that's thoroughly started to dominate our usage. It's been cool to see. And then we have our usual suspects like Slack and Asana, and then we're all over the place on the rest. Some of us use Notions, some of these use Dropbox Paper, some of these uses Koda, and so we're still figuring that one, out, I'd say.

Lenny (01:06:16):
Dropbox Paper. Very cool.

Yuhki Yamashita (01:06:17):
Yeah.

Lenny (01:06:18):
I love that product, but I feel like no one uses it anymore, but it's cool that you guys do. Final question, favorite FigJam or Figma plugin or template?

Yuhki Yamashita (01:06:27):
We have this one called the Alignment Scale, which is a widget that you can insert into FigJam or Figma Design, actually. And we use it all the time. So basically, it's just a simple scale and whenever people click it, their face appears on one end of the spectrum or the other. And so it's our quick way of being like, we're doing a product review, we on a pulse check, we drop it in and we're like, how are people feeling aligned, not aligned?

(01:06:52):
And if people are aligned, we just move on. If not, then you know that it's worth a discussion. So it's just a fast way to figure out where all the hotspots are.

Lenny (01:07:01):
Awesome. And if folks want to find that, they can actually go to the newsletter interview that we did. I think if you just Google how Figma builds product, it comes up number one, and then there's a link to actual template, so you can plug that right in.

(01:07:13):
Yuhki, thank you so much for being here. I am going to go play with Figma and FigJam right after this. Two final questions. Where can folks find you online, if they want to reach out, learn more? Are you guys hiring, anything there? And then, two, how can listeners be useful to you?

Yuhki Yamashita (01:07:30):
Yes, you can find me online on Twitter or LinkedIn. Feel free to reach out there.

(01:07:36):
In terms of how you can be useful to us? We're really starting to build a lot of products for this audience, for product managers. FigJam is one example of this, so definitely try it out, give us the feedback, tell me all about all the cool things that you're doing or you wish you could do on FigJam or Figma. And you can tweet at me, you can find me anywhere. And, of course, we're also hiring, so if you know great people or are interested, yeah, there's a lot of roles, so please get in touch.

Lenny (01:08:06):
Awesome. Yuhki, thank you so much for being here.

Yuhki Yamashita (01:08:08):
Thank you so much for having me, Lenny.

Lenny (01:08:11):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcast, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

---

## An inside look at how Figma builds product | Yuhki Yamashita (CPO of Figma)
**Guest:** Yuhki Yamashata  
**Published:** 2023-01-08  
**YouTube:** https://www.youtube.com/watch?v=NepFo4zXyK4  
**Tags:** growth, retention, acquisition, onboarding, metrics, okrs, roadmap, experimentation, funnel, conversion  

# An inside look at how Figma builds product | Yuhki Yamashita (CPO of Figma)

## Transcript

Lenny (00:00:00):
There's something controversial about this idea that everyone can see what you're doing or that multiple designers can be in the file at the same time. We like to say that one of the first responses we saw Lenny [inaudible 01:08:35] Figma was, if this is the future of design, I'm quitting, right? I'm changing careers.

(00:00:17):
And there's that tension of that narrative tension, but that is signal that you're part of this revolution and you're trying to change something. And when it equips your customers or user base with that, then I think that's something that they can really get behind and champion.

(00:00:35):
So it's not just that they're championing for a tool, they're also championing for a new way of working. Obviously, that's a tall order or don't want to come up with that, but hopefully, if you're a founder and you're working on something, your vision is so big that you have those kind of ideas and it's like, how do you actually equip your customers to want to talk about that?

(00:00:58):
Welcome to Lenny's podcast. I'm Lenny, and my goal here is to help you get better at the craft of building and growing products, interview world class product leaders and growth experts to learn from their hard won experiences, building and scaling today's most successful companies.

(00:01:12):
Today my guest is Yuhki Yamashita. Yuhki is Chief Product Officer at Figma, where he's been for almost four years. Prior to Figma, he was at Uber, both as a Product Leader and also, interestingly, as Head of Design for one of their bigger product teams. Before Uber, Yuhki spent time at Google and Microsoft, even taught an introductory computer science course at Harvard.

(00:01:33):
In our conversation, we explore Figma's product development philosophy, how they build such consistently great products, how they hire, what habit Yuhki has found to be the most instrumental in his success in his career, and also what Yuhki and his product team have learned by building a product led growth business.

(00:01:50):
This episode builds on a newsletter post where I interview Yuhki about how Figma builds product. So if you enjoy this episode, or even while you're listening to it, I highly recommend you check it out. It's currently my fourth most popular newsletter post of all time. You can find it at lennysnewsletter.com. With that, I bring you Yuhki Yamashita, after a short word from our wonderful sponsors.

(00:02:15):
This episode is brought to you by Notion. If you haven't heard of Notion, where have you been? A's notion to coordinate this very podcast, including my content calendar, my sponsors, and prepping guests for launch of each episode. Notion is an all-in-one team collaboration tool that combines note-taking, document sharing, wikis, project management, and much more into one space that's simple, powerful and beautifully designed.

(00:02:40):
And not only does it allow you to be more efficient in your work life, but you can easily transition to using it in your personal life, which is another feature that truly sets Notion apart. The other day, I started a home project and immediately opened up Notion to help me organize it all. Learn more and get started for free. At notion.com/lennyspod, take the first step towards an organized happy team today. Again, at notion.com/lennyspod.

(00:03:08):
This episode is brought to you by Vanta, helping you streamline your security compliance to accelerate growth. If you're business stores any data in the cloud, then you've likely been asked, or you're going to be asked about your SOC 2 compliance. SOC 2 is a way to prove your company's taking proper security measures to protect customer data and builds trust with customers and partners, especially those with serious security requirements.

(00:03:33):
Also, if you want to sell to the enterprise, proving security is essential. SOC 2 can either open the door for bigger and better deals, or it can put your business on hold. If you don't have a SOC 2, there's a good chance you won't even get a seat at the table. Beginning a SOC to your port can be a huge burden, especially for startups. It's time consuming, tedious and expensive.

(00:03:55):
Enter Vanta. Over 3000 fast growing companies use Vanta to automate up to 90% of the work involved with SOC 2. Vanta can get you ready for security audits in weeks instead of months, less than a third of the time that it usually takes. For a limited time. Lenny's podcast listeners get $1,000 off Vanta. Just go to vanta.com/lenny, that's V A N T A.com/lenny to learn more and to claim your discount. Get started today.

(00:04:28):
Yuhki, welcome to the podcast.

Yuhki Yamashita (00:04:30):
Thank you for having me, Lenny.

Lenny (00:04:32):
I'm quite honored to have you on this podcast. For folks who don't know, we actually collaborated already on a newsletter post that has quickly become my fourth most popular post of all time, which you can find if you search for how Figma builds product. And so I am really excited to dig into a lot of the stuff that we, maybe, didn't cover in that newsletter. Also, just like how product works at Figma in more depth, how the PM team works, how you think about product, and things like that. So again, thank you for joining me.

Yuhki Yamashita (00:05:00):
Hi, team, as a huge fan of this podcast, so really honored to be here.

Lenny (00:05:04):
Wow, that means a lot. I really appreciate that. So you are currently Chief Product Officer at Figma, which is such an epic role. It's such an epic company. Could you take just, maybe, a minute or two to high level share your career arc, how you got to where you're today as CPO at Figma?

Yuhki Yamashita (00:05:22):
My first job out of college is actually at Microsoft, and I was the Product Manager on Hotmail. If anyone, any listener remembers Hotmail, and I didn't really know what product management was at the time, and I mute it as a interdisciplinary function that will give me exposure to all my other functions so that I can actually decide which function's interesting to me.

(00:05:48):
And so, spent a couple years at Microsoft. Through that, also, moved on to Hotmail to Windows. And at the time, they were working on Windows 8 and Windows 8 was really interesting because it's a very touch forward version of Windows. And so there's just a lot of conversations about UI and UX, and that was really fun for me.

(00:06:07):
And as I was thinking about what's next, I really felt the draw of Silicon Valley and I ended up at YouTube, and I believe Shishir has been on this podcast before?

Lenny (00:06:19):
[inaudible 00:06:19] you.

Yuhki Yamashita (00:06:19):
Yeah, so Shishir was leading YouTube at the time, and he continues to be a great mentor of mine, but had the opportunity to lead the YouTube app on iOS over there. And it was really funny because I had never touched the iPhone before my first day, so my manager, on my first day, just sent me to the Apple Store to buy an iPhone. But that was my next job and that was a really interesting change for me, too, of, and we can talk about this later, as well as different companies and different styles of product management and really figuring out, I think it was a place that taught me a lot about some of my product last weeks to date.

(00:06:58):
And this is also around a time where there are a lot of interesting companies that were working in the physical and digital space. And so Airbnb was one of them, Uber was another. So I felt this draw just because it seemed just a really interesting space to be in. So eventually, ended up at Uber. Uber was another company where I feel like a lot of my philosophy that, hopefully we can get into today, around how to build products, how to build products in the kind of environment that's really fast moving. And so that I learned a lot from there.

(00:07:33):
And to date, all those companies has really been focusing on the core experiences on consumer products, and that's really been most of my career. And as part of that, worked with a lot of amazing designers. But at Uber, I realized that I wanted to dip my toes into design directly. For the tail end, I actually switched from PM to design and managed a few design teams working on our bikes and scooter efforts just to understand what that's like. And it was around this time, around my Uber career, where we encountered this tool called Figma.

(00:08:08):
I'd happened to be working on a project that experimentally brought Figma into the company. It was a time in the company where we were trying to transform our culture to be much more transparent and inclusive, and Figma was the perfect fit for that. So, I got to watch how Figma changed the way it worked, how it's spread within the company. We got to know the Figma team a little bit, as well. And yeah, I was really drawn to that mission and as a product manager who's been straddling that boundary between design and products for all my career, I really loved how Figma proactively blurred that boundary and opened up that process of participating in design. So I really got behind that mission and that's how I ended up here, at Figma.

Lenny (00:08:49):
It's so fascinating that you moved into design from product, and then back into product. At Uber, were, what was the role? You were Head of Design for the mobility team?

Yuhki Yamashita (00:08:59):
Yeah, it's called New Mobility, focused on just our micro mobility efforts, basically. Yeah.

Lenny (00:09:05):
Do you recommend this path for PMs to switch into design? I know it's not something anyone can do, but do you feel like that is an important skill role to experience as a PM, you encourage people to try that?

Yuhki Yamashita (00:09:16):
Well, I decided it's not for everyone, but I think that it's, first of all, a really great empathy building exercise of understanding that point of view, and also pushing yourself to push on the product from a different angle. Because I think as a PM, you're in the center facilitating all these different trade offs, and when you go into design, you have to ignore some of those other aspects to really be insistent on pushing on the best experience possible. Just suspend everyone's disbelief in business feasibility or engineering feasibility to push on a vision. And that's just an interesting exercise to do.

(00:10:00):
And then, I think the last thing is, I actually think it's an opportunity for in design and PM to learn from each other. When I became manager of design teams, one of the things that I coach designers on, are how to win over PMs, and how to speak in PM's language, and likewise, it's important for PMs to understand that, as well. So those are some of the things that I thought were helpful, but again, it has to come from a place of passion that you know you really want to do this.

Lenny (00:10:29):
Which job would you say is harder; design or product management?

Yuhki Yamashita (00:10:32):
They're hard for different reasons. I would say managing designers is harder than managing product managers.

Lenny (00:10:38):
Interesting.

Yuhki Yamashita (00:10:39):
And I think part of it is that designers are, it's really important to focus on growing their craft and helping them develop as designers. So it might not be that the company's biggest problem is one where you can actually learn this new thing you're trying to learn as a designer, and this probably happened for engineers, too, right? You could be working on the onboarding funnel, and that might not be the best place to be learning micro interactions, or maybe it is, but those aren't always aligned.

(00:11:10):
Whereas, with Pms, it's a little bit more like PMs are just hungry for impact, and so you can point them to the biggest problems a company has. And while PMs also do want to understand different kinds of problems or have the experience working on different kinds of problems, at the end of the day, I feel they want to be working on the thing that matters most in the company. So from that perspective, it's easy.

(00:11:31):
But as you know, and the reason this podcast exists is because PM isn't easy. And so the discipline, I think, is harder in a sense that it's sometimes hard on a day-to-day pace to know if you're doing the best thing you could possibly be doing. And so I think that makes it a little bit harder as a PM, as well.

Lenny (00:11:52):
I had a designer friend who moved into a PM role, I had a product role at a startup and she's like, "Holy shit, I had no idea how hard being a product manager was, and a product leader. I have so much more empathy for the PM role." And so, it's interesting, it works in both ways. Similarly, I was actually a manager of engineers, at one point, and I felt the same way where managing PMs was a lot easier than managing engineers. So, translates to a lot of different roles.

Yuhki Yamashita (00:12:19):
Yeah, I can see that.

Lenny (00:12:20):
Folks listening to your career arc and just all the places you've been, all the wonderful things you've done. Imagine many people are like, wow, how do I have a career like that? Microsoft, Google, Figma, Uber. If you had to think back and identify maybe one habit, or one skill, or behavior that you think has most contributed to your success as a leader, as a product leader, what do you think that would be?

Yuhki Yamashita (00:12:45):
People who work with me know that I often talk about storytelling and, in fact, if you've ever reported to me, storytelling has showed up in some kind of performance review, I feel, and that's how much I care about it. And I actually think that a lot of being a great product manager is being a great storyteller. And I know a lot of us have already talked about it out there. I think the importance of storytelling is understood, but maybe I would share two things that are specific about it that I think are interesting.

(00:13:13):
One is to understanding the power of synthesis and it's this idea that maybe even as a early career PM, you're inside some of these reviews and a lot of people say, "Hey, at least you could take some notes for the meeting so that you're adding value." And so that's common advice, here, but I think the most powerful part of that is that in some ways, you can synthesize what happened. And a lot of things are said in a review and there's still this bring it all together into a distillation of a message. And even that's like, that's a lot of power, I think. And what do you take away from all these different opinions that all these leaders had, and how do you push that, push the project forward from there? So that's one example.

(00:14:02):
Or another example is, I really love thinking through frameworks and offering ways of talking about a problem or ways of thinking about a problem. And that's synthesis, too, of figuring out all these different disparate parts and coming up with a way to a lens to look at something. And I feel like it's something that was, I learned, mostly through literature classes almost, where you're doing literary commentary and you're reading a William Yates poem and you're trying to, you observe all these interesting things, but then you have to take those different observations and distill it into a thesis, into something cohesive. And I think that's what a good PM can do. All these different ideas, and opinions, and problems, and how do you distill it down? And so I think that's one aspect of storytelling that's really important.

(00:14:54):
And the other aspect of storytelling, of course, is a story is only as good as the action that it's capable of driving. And a lot of times that I often coach my product managers are on, we're living in a world where everyone is constantly distracted, and you get these 30 seconds of attention at a time. And so, just the ability to really tell something powerful that sticks is really important, the memorability of it.

(00:15:21):
And I often talk about memification, which is this idea that I found this out most at Uber, I feel, where there's certain insights, data insights, research insights that were memmified to the point where someone like Travis or Dara would just cite this insight in the middle of a meeting, and you know that you've really done your job as, maybe, a researcher or a data scientist or product manager if people are able to do that and draw from that in that way. And that's what, ultimately, sticks.

(00:15:52):
And so when you start thinking about it from that perspective, it's really powerful because it's the way in which knowledge is transferred within the company and you compel action for it. Or when I'm being, maybe, asked questions by other leaders or stakeholders, the thing that's going through my head is, okay, there's this story that, that leader is trying to develop, or a meme about what this project is about or what the biggest problem is. And so, what story are they trying to create in their head so that they can remember or talk about what's happened?

(00:16:28):
And if you take that mindset, you just realize that it's a really useful way to think about everything.

Lenny (00:16:35):
I'm really excited to chat about this idea because it comes up a lot. The power of storytelling, it's similar to being good at vision. It's like PMs are always told, "Hey, you got to improve in vision." Here's a skill the great PMs are really strong at. And I feel like storytelling is similar. It's this vague cloud of a skill that you build over time. And you mentioned a few things that you recommend to people that you work with. Think of it as a meme, maybe.

(00:17:01):
Is there anything else? When you're doing a performance review with a PM and one of their skill gaps is storytelling, is there anything else you recommend they specifically do to get better at the skill, or is it just do it again and again and watch me do it, watch other people do it and you'll learn?

Yuhki Yamashita (00:17:16):
Yeah, I think of it as resetting the internal computer of my brain a little bit so that I start from scratch again. And when I'm starting from no context at all, can I build up the story from bare and explain what's happening? And oftentimes, you're just caught in the middle of everything and you have all this context that might not be obvious if you step away from it for just a second.

(00:17:39):
I guess the way to think about it is, put yourself in another user's shoes, and that user is someone who has no idea what's happening and still wants to understand, in a nuanced enough way, what you're grappling with. And so, that reset moment, and to pull yourself out helps you tell a better story, in many cases. So that's one thing that comes to mind, yeah.

Lenny (00:18:03):
Got it. So it's escape the curse of knowledge a little bit and just assume people don't know anything about the context, the background, why this is important, come back to the beginning.

Yuhki Yamashita (00:18:12):
Yeah, I think another thing that where I learned storytelling is through teaching. So when I was a course assistant for a computer science class and I had to explain pointers, you're like, okay, I really have to borrow on real world metaphors or something that is much more grounding because if you assume a lot of knowledge, then it can be inaccessible to a lot of people. And so if you can tell a story that any student can understand, then you've really done your job. And once you've learn that skill of being able to tell anyone who has no context, then it becomes much easier to turn to these other audiences that are closer and closer.

Lenny (00:18:51):
When I asked you in our newsletter interview what one of the core philosophies of product managers is, in the way you think about product and the role of PM at Figma, an interesting thing that you highlighted is that to you, it's really important that PMs own the why of a product and an idea. And I think it connects to what you're talking about, now. I'm curious just why you think that's so important for product managers and why that's so core to the way you think about product, and at Figma.

Yuhki Yamashita (00:19:17):
I really can't remember why I heard this, but it really stuck with me because oftentimes, there's this debate about well, is a PM the person who comes up with the idea. And the answer is usually no, it doesn't have to be at all. And in many cases, in our case, your customers come up with a ton of different ideas and certainly, the what and how are things that are shared within the company and not something that PM uniquely drives. But I do think the why is something that I really always hold the PM uniquely responsible for.

(00:19:48):
And I think the place where I learned this, the importance of this the most, was actually first, at YouTube. I had been working at Microsoft for a long time and I was early in my career, so I was just really focused on my, what we called, our feature crew, our engineer designer, our tester, and just writing specs that really specified exactly how everything works. And so that was the Microsoft culture back then, and your specs had to be perfect, right?

(00:20:19):
Then moved over to YouTube, and all of a sudden, you're responsible for an entire app, and you have a pretty big team, and you cannot specify everything that happens. And so, naturally, designers and engineers are just making their own choices. Made is an error handling situation, and in Microsoft culture, you would've had a table that specifies exactly what happens during that error. But in Google culture, it's like, okay, well the engineers and designers, they can figure it out.

(00:20:47):
So then it's like, how do they make a really great decision? How do they make all these local decisions that you're not a part of, how do you make it so that a great decision's made? And if everyone has an understanding of why we're doing this, what problem we're solving, then people can make really great decisions. It's the only way you can really scale. So that's where it came from.

(00:21:06):
And then since then, I've started to realize, also, that there are other functions that do this well. So for example, our engineering team at Figma, whenever we do a retro or postmortem, we do this thing called five why's. And it's the idea behind it, it's like, well, why did this happen, outage happen, okay, and why did that thing happen? And go deep enough where you can find the root cause and go fix all those things.

(00:21:28):
And I think a PM can do this, too, which is a customer is asking for a feature, but then you would say, okay, why are they asking for it, and back up the problem. But I think there's one more step you can take, which is, why do they have that problem in the first place? And maybe there's something there, and that could be an opportunity to make a bigger product impact by fixing that underlying condition that created the problem in the first place.

Lenny (00:21:55):
That's so cool that you actually do the five whys. I hear people talking about the five whys all the time, and I don't know, I haven't heard people actually using it. So you actually do this at your post-mortems, you said?

Yuhki Yamashita (00:22:03):
Yes. Engineering team that's accepting them, yeah.

Lenny (00:22:07):
That's so interesting. Can you talk a bit more about these postmortems? Is this just when something goes wrong or is this just every project you retrospective postmortem thing?

Yuhki Yamashita (00:22:14):
As it relates to five whys, it's more when something went wrong. But I do think we have a retro culture, [inaudible 00:22:24], where there's always opportunity to make things better. And if you don't create the environments to talk about it, then some of those will go unaddressed forever, so.

Lenny (00:22:33):
Cool. Okay.

Yuhki Yamashita (00:22:33):
Yeah.

Lenny (00:22:34):
Another attribute of the product team and how you build product at Figma that you shared that was really interesting is you mentioned that you just have an obsession with a proximity to customers, that you make sure your PMs and product team are really close to customers. When you hear that, you're just, imagine everyone listening is like, oh yeah, we're really close to customers, we talk to customers all the time. Of course you got to talk to customers. I'm curious what it is that, maybe, you think sets you apart, in terms of how you think about being close to customers, and if there's a story, maybe, of just, wow, this is how close we are to customers and maybe something that emerged out of that, that'd be really cool to hear.

Yuhki Yamashita (00:23:07):
Well, I think a lot of it starts with our origin story in many ways, which is that way back when, when Dylan, the small group of people were building Figma, this is the time when no one believed it was possible to have a design editor in the browser. And so it just seemed like science fiction, almost. And yet, what Dylan did consistently throughout, was just put the product in front of designers, ask them for feedback, come back to them the next time with that feedback implemented, and it becomes better and better and better.

(00:23:40):
And at no moment was there a tentative expectation that the designer suddenly turns around and implements that tool in their organization. It was really just about listening really carefully to what the community had to say, and through that process, making them evangelists. And that's where a lot of how Figma came to be and why we have such a strong connection with our community where we've actually, they've really helped shape the product to date, and there's a deep belief in that, and they're the ones in that are now advocating for Figma and helping us spread within the community and within their company.

(00:24:20):
So that's the backdrop for why we have such a strong connection with our customers, and there's a lot of things that you see. So for example, maybe someone on my team Sho, and oftentimes, Sho will tweet out to the community, here's what we're thinking, or we're actually thinking about focusing a lot more in prototyping. What are the top problems you're seeing? And people come back with all these different answers because everyone's passionate. And we go in there and just look at all the feedback and understand what people are saying and just have a stronger pulse on how people are feeling. And that's not to say that everything is then implemented verbatim, but we really find it useful to feel like we have a sense of what people are thinking.

(00:25:05):
And I think the most crazy version of it, maybe, is Dylan's always reading customer feedback. In fact, has reads the most customer feedback of all of us and has been doing that for a decade. And oftentimes, there used to be this thing where he would drop in tweets that he sees into different Slack channels to be like, hey, this seems concerning, or we're getting this feedback. And it got to a point where we got big enough where people would feel like they had to drop everything and deal with that tweet.

(00:25:31):
So Chris, our CTO, and I intervened. We created this new channel, private channel called Concerning Tweets, and it just, we're this small group of us that Dylan can drop us in. And these are tweets that aren't going viral, by any means. They're just things that you see is with one like, sometimes zero likes, but he feels there's an essence of truth to them and we make sure that we look at what's going on there and see if there isn't something much bigger that we should be focusing on. But that's the extent to which someone like Dylan, from top down, implements this idea that we need to be staying close to what our users are saying.

Lenny (00:26:13):
That's an awesome idea for a channel, a way to contain that potential madness that it creates. Is there anything else you've learned around hearing feedback like that in a tweet, let's say, or just a few loud voices and deciding what to actually work on? Do you have an approach there? Just deciding what's worth paying attention to?

Yuhki Yamashita (00:26:31):
As we built out our research and data functions, it's really important to balance out the vocal minority with what's actually happening. So I really view some of those tweets more as canaries in the coal mine, in a way, and inputs into, many inputs we have around everything our customers could possibly be experiencing. And it's important to realize that we have certain forums, like our support tickets, where customers are, tend to be much more dissatisfied. And we have other kinds of inputs that are sales conversations with prospects, where it's really more about perceptions around Figma, in some cases.

(00:27:11):
And I think it's just important, especially as a product manager, to feel like you have this balanced portfolio of different kinds of feedback to know that you don't have any blind spots. So I think that's one of the things that I focused a lot on when I came in, which is the Figma team is very good at Twitter and staying on top of the sentiments. And luckily for us, a lot of designers are on Twitter, but the reality is that most of our audience, at this point, probably aren't. And so building our capabilities to extract feedback or more insight from those other sources, as well.

Lenny (00:27:46):
That reminds me, I think Twitter was really instrumental to the beginnings of Figma. I believe Dylan made this social graph of the most influential designers on Twitter, and that was his go-to market strategy, get those designers on Figma, and then I think he open sourced his code to do that. Is that right?

Yuhki Yamashita (00:28:02):
Yeah, that sounds right to me. And he is very intentional about which designers we need to win over. I think it was very novel at time.

Lenny (00:28:11):
What is it like to work with Dylan Field? As an outsider, he's a legend, feels like he's an incredibly smart, talented, hardworking, CO. There's always tension a little bit between a Chief Product Officer and a CO, and so I'm just curious, what do you like to work with as a product leader? And then, is there, I don't know, a memory that comes to mind of just a way that encapsulates what it's like to work with Dylan?

Yuhki Yamashita (00:28:32):
We're very different, actually. And Dylan is very, he's very based on intuition and instinct. And that intuition is actually built off of thousands and hundreds of thousands of customer interactions where he might look at something and be like, "You know what? This isn't going to land well," or, "Here's the biggest problem right now." And you're like, well, how does it conclude that? And part of my job is to build out that logic streak for him of how did you arrive at that conclusion so that people can understand that at scale, in a way. But he's very much about that.

(00:29:09):
Or I think there's a way which, sometimes, it's a product manager, you want to lay out a problem and say, okay, we're going to first focus on this problem, and then [inaudible 00:29:21] these three approaches. We're going to take this approach and have a review at every step along the way. But for Dylan, I think, it's very hard for him to really fully get bought into it until he sees the end implementation to viscerally feel if this is a good solution or not. And so I think that's the kind of thinker he is where he really needs to see it to feel it. But it's not totally random. It's based on all these interactions with customers and somehow encoded in him to build up some of those intuitions.

(00:29:55):
And I think one of the things that's really interesting about him is that he actually really cares very deeply about any given user and how they're feeling about Figma. I remember when, during the height of the pandemic, we were doing a one-on-one walking around Delores Park, because this is the era where you would take meetings, if you take meetings, they're all outside, and then he needed to use the bathroom. So he came out to my house in the Castro, he used the bathroom, and then he met my partner, and my partner was on Figma, had Figma pulled up because he is just doing work. And then Dylan just went straight in there and wanted to ask what the biggest problems were or what's not working, and they started geeking out on some issue around Google fonts, and this is the first major interaction between the two of them.

(00:30:45):
But it's one of those things where that's how much Dylan cares. And on one level it's just easy to say, "Hey, this is a single user who just happens to be using your product," and be dismissive with it or not care that deeply because you think you already know all the biggest problems, but that's not his attitude. And so that's the level of, I guess, customer obsession, if you will, that he exhibits and then, in turn, informs his intuitions.

Lenny (00:31:16):
That's amazing. Figma is 10 years old at this point. He's been at this for a long time, like a decade. And the fact that he's still so obsessed with just a random person just using Figma and he's taken the opportunity to experience it in real time every chance he gets, sounds like.

Yuhki Yamashita (00:31:31):
Yeah.

Lenny (00:31:33):
Hey, Ashley, Head of Marketing at Flatfile, how many B2B SaaS companies would you estimate need to import CSP files from their customers?

Ashley (00:31:41):
At least 40%.

Lenny (00:31:42):
And how many of them screw that up, and what happens when they do?

Ashley (00:31:45):
Well, based on our data, about a third of people will consider switching to another company after just one bad experience during onboarding. So if your CSP importer doesn't work right, which is super common, considering a customer files are chalk full of unexpected data and formatting, they'll leave.

Lenny (00:32:05):
I am 0% surprised to hear that. I've consistently seen that improving onboarding is one of the highest leverage opportunities for both signup conversion and increasing long-term retention. Getting people to your a-ha moment more quickly and reliably is so incredibly important.

Ashley (00:32:19):
Totally. It's incredible to see how our customers like Square, Spotify and Zora are able to grow their businesses on top of Flatfile. It's because Wallace data onboarding acts like a catalyst to get them and their customers where they need to go faster.

Lenny (00:32:36):
If you'd like to learn more or get started, check out Flatfile at flatfile.com/lenny.

(00:32:44):
As an outsider, it feels like Figma is just always firing in all cylinders, shipping the best product. People love it. I use it, I should've mentioned this, but I use it probably every day for my newsletter for illustrations and banners and all this stuff. Yeah, I don't know what I do without it. And it always feels like Figma is just killing it. I know that's never the reality. I'm curious, is there a story of something that just, maybe, didn't work out the way you hoped? Whether it's a feature, a launch, or something like that that just shows people that it's, not everything always works out.

Yuhki Yamashita (00:33:14):
We run experiments all the time that don't come back with winning results, and we certainly have built a lot of more complex features that took a while to take off.

(00:33:24):
So a good example of this is in the design system space, we have something called branching and merging. And branching and merging is this workflow of maybe you're building a really complex design system, and then you don't want anyone ever randomly touching your components that are used by thousands of other projects, so you create this workflow of, someone, maybe, effectively suggesting a change, you're reviewing it and then pushing it in.

(00:33:48):
And so, in theory, makes a lot of sense and things that our customers asked us for, but once we built it, in the initial stages, just didn't really see that much adoption and didn't feel great because it's a really big investment for us. It's a lot of work that we put into it and there's just many different reasons. Some of it was performance, some of it was, this is a foreign workflow and it just takes time, and us helping customers implement some of those workflows, we realized some gaps because we don't really use it that much ourselves.

(00:34:20):
And so, I think as we're getting bigger, one of the things that I'm realizing is that we're starting to build a lot of features that are not, necessarily, for organizations like ours. And when we do that, we really need to be creative about how we understand how effective those are because we've had such a strong culture of internal testing and dogs looting, and those are the things that really helped make sure the quality of our product was good enough. But now we're working with really new types of customers and needing to push ourselves and build that muscle, as well.

Lenny (00:34:54):
Speaking of high quality software, again, I'll repeat, I think Figma is one of the most beloved software products. It's become central to a lot of the ways people work. It's also, I think, one of the fastest growing SaaS products, in general. And I don't know, this is maybe the ultimate softball question, but I'm just curious, what is it that you do at Figma to build such high quality software? Because it's rare for B2B software, especially. What do you do as a product leader, as a product team to just set this high bar, make sure that the stuff that you put out is great consistently, and the more tactical the better?

Yuhki Yamashita (00:35:27):
It's so important that you're using your own products. And I think we're in a very lucky position where all of us can get creative around using Figma in some way. And obviously, designers are the, internally within Figma, are the most vocal and the ones who are in the product six hours a day, essentially. But even for PMs, one of the first things I did when I arrived was we were a little bit more of a memo culture, and I was like, you know what? We should be a deck culture because we can build those decks in Figma, and just that act alone allows you to encounter a lot of issues and for you to get familiar with it.

(00:36:06):
And so I think there are ways in which, sometimes, you have to get creative to enable your company, your entire company to use a product more. Or as an example, recently, we just did calibrations for performance reviews in FigJam, and our Head of Design, Noah, came up with this amazing template and we distributed it through HR and that was another reason for everyone to use FigJam. And so that's the biggest thing. The more hours people are spending inside your product, internally, I think, just naturally becomes better. Because a lot of times, it's not just about people raising their hands and saying this is the problem, it's more about you just want to make your own workflows, your own day-to-day better, and derive satisfaction from improving that.

Lenny (00:36:50):
So the takeaway there is get your product teams to use the product as often as possible. That is a really clever way of doing that at Figma. I know you mentioned in our newsletter interview that you switch from memos to decks. Usually, it goes the other way around, and now I get the second order effects of that where people are building their decks in Figma. That is very clever, and not everyone's building collaboration software, but that is a really clever idea. And I think there's probably a bit of trickle down from Dylan's obsession with the product in making it, just continuing to just be obsessed with making a great experience combined with that, people using the product and this trickle down of we really need to make this as awesome as possible.

Ashley (00:37:27):
There are other companies, for example, when I was at Uber, especially working on the driver's side, of course we went out and driving, and that speaks to some aspects of it. But one of the things that I've realized is when you are logging a bug and you add some engineers to it, to have them look into it, the degree of motivation is so different if that engineer has, somehow, experienced a problem in some way.

(00:37:51):
So for example, everyone at Uber would take Ubers into work, and if an engineer working a driver app saw a driver struggling with something, they would find it embarrassing and feel personally accountable to go and fix that. And when you can create that sense of personal accountability, then all these crazy things happen and all this progress happens. So I think for us, as getting creative at Uber about, okay, well how do we increase those interaction points at the point where, if someone building feels like they have some kind of personal relationship with the end user, and this is what happens, at Figma, too, where a lot of our designers feel personally accountable, in a way, because all their customers are people they already know in the community on Twitter and all those kinds of things, so they feel like they have to put something out there that's defensible or that they're really proud of. So I think that personal accountability can really make a difference.

Lenny (00:38:48):
That begs a question of, I imagine this engineer at Uber coming back to their desk and like, I've got to fix this bug. And then their PM's like, no, we got goals to hit, here's our priorities, we got this roadmap, we don't have time to fix this right now. It's just one random bug. And so there's a two part question, just like you have a approach to that, do you encourage engineers, designers just fix stuff that seems broken/you mentioned that you have a fun experience with OKRs and how you've approached OKRs at Figma, and you've gone back and forth a little bit. And so maybe, as a second part, just talking about your experience with OKRs at Figma.

Yuhki Yamashita (00:39:21):
The first part, I would say that I think one of the most powerful things, especially for startups, is that bottoms up energy, and maybe a developer noticing something is wrong and just going off and fixing it. And for the most part, I try not to get in the way of that because if people are doing that constantly, and everyone the company is trying to make the product better, that is sometimes a way more effective way to improve the quality of experience than this top down of, oh, let's define this quality experience metric and try to change all the things, because you might miss these things. So that's one aspect.

(00:40:01):
And the second thing is, I think a lot of PMs have grown to realize this, which is, if you ask an engineer about how much time it'll cost to go and build something, and it's something that they came up with or they're advocating for, it's almost always half the time as something that you are asking for, as a PM. And that motivation is so different.

(00:40:24):
And that's why getting the buy-in of developers is really important, because you want to feel like they're personally vested in this problem, and then, all of a sudden, their willingness or their creativity, or all these things spike. And so when you think about all those things, when there's a situation where an engineer or a designer's trying to fix a real custom problem, I'm like, by all means.So that's on that.

(00:40:50):
OKR is totally bigger topic, and maybe I'll set the conflicts of why I have such this love-hate relationship with it, which is that a lot of my career, I've actually just worked on core experiences, and OKRs were the bane of my existence, in a way. Because when you're working on a core experience, sometimes you're just, I'm just trying to make the experience better. And sure, I can come up with this BS way to measure what that looks like, but that's not what I'm thinking about every day, anyway. So it just seems very performative, and there's just a lot of work that goes into it.

(00:41:26):
And you encounter one of two situations. One is, you come up with some secondary metric that nobody actually cares about that, technically, you can measure and, technically, you can move, but you haven't actually proven that it really matters. So maybe it is some satisfaction metric that you have on some survey, but you haven't actually done the work to show that, that actually has correlations with retention or anything that actually "matters for real" in the business, or it's some weird usage metric or something like that.

(00:42:00):
And then the other extreme is to say, no, we're going to be ambitious and we're going to send it for business goals. So for example, even if I was the PM for the rider experience at Uber, I'd be like, you know what? We're going to contribute incremental trips because the experience is going to be so good that we can get more people to come back. And I think the reality for a lot of that is, it's a metric that you don't have full control over or there are many hops until it can affect it, and okay, well maybe we can make the experience better and maybe that improves your attention and maybe this. And by the time you get there, you actually can't even prove that you moved the top level metrics. So either you anchor something that matters, but you can't move, or you anchor something that you can't move but doesn't actually matter. So that's the relationship I've had with [inaudible 00:42:45], so even it's really frustrating.

(00:42:47):
So when I write that thinking about, one of the things I realized is that we had OKRs, but people were treating it almost as a to-do list or a task list of, okay, here's how, by the end of quarter, I need to complete these tasks and then I'll feel like I did my job, kind of thing. And we would have these dreadful meetings where we go through these spreadsheets and have people stand up in front of everyone and talk about those commitments, or those key results, rather. But they were dreadful for a reason, which is that you just couldn't really understand what the team actually really cared about. And it got to this point where we had all these, and this is similar to the secondary metric problem, but either you couldn't approve that you actually moved it, or you're trying to work on something that I don't actually understand why it's useful.

(00:43:39):
And so that was when I deprecated it and said, "I just want to understand your headline. What are you trying to do, philosophically?" And just don't stress about whether you can measure it or not. I just don't understand what you're optimizing for, and let's first have that to date. And then once we get there, then let's talk about, okay, well what are some ways that you can measure it? And some of it's qualitative, so it's quantitative, and that's fine. And I almost feel like sometimes, it's better to take the report card approach of saying, Hey, just give yourself a score, tell me how you derive that score, let's all understand that the metrics and those inputs that go into it can change over time, and we're going to get more sophisticated about how we measure it. But at least everyone understands what on earth you're trying to go for.

(00:44:29):
So that's where I moved in my first year, I would say, and then we hired a Head of Data who is a friend of mine from Uber, too. And one of the things she felt was, okay, but it's still very loosey goosey, and super subjective, so let's just try to bring OKRs back and see if we can just do them better next time. And so we've done that, and they were definitely better than when I first arrived just because we had a data science team and we had more rigor around metrics and things like that. But again, this time it was less about not understanding what people were doing, but more not understanding if teams are actually committed to moving those OKRs. And one of the problems that you find is we have these OKRs, but they feel like these post-rationalizations of the projects that you're working on, anyway.

(00:45:17):
And at the end the quarter, you come back and see if those OKRs move, fingers crossed. But if you stop an engineer in the middle of the hallway or the virtual hallway, so to speak, and ask them, okay, what are your team's biggest goals or OKRs? [inaudible 00:45:31], they wouldn't be able to say it. They're just like, well, I'm working on this project that's really important. And so it's, well, what's the point of publishing this OKR if you're actually not thinking about moving it on a daily basis almost, right?

(00:45:46):
And so that's when we've tried to experiment with this terminology, well, maybe if we should call it commitments instead, people would take it a little bit more seriously. And it's my belief that oftentimes, commitments are this care between the why and the what, and sometimes the face of the commitment is the what.

(00:46:05):
It's a project and there are many why's behind it, or it's the why and there are many projects behind it. So that what's trying to formalize that idea, but it definitely felt a little bit complicated, a little bit. Sometimes people are like, well, OKRs exist for a reason and this is, basically, an OKR with just a different name. So my honest sense is we still haven't figured it out and we're still iterating on a bunch of different things, but I think I've developed some philosophies around it, which is, no matter what you call it, because it doesn't matter as much.

(00:46:38):
I think that, for me, there are three things that really matter about the good OKR, and one is legibility. People look at it and understand what it is, and it's not some weird obfuscated metric that doesn't mean anything to anyone. I think actionability, I want OKR to inspire action. You look at that and you're like, it's stirs action, makes me want to do something differently. And the third one is authenticity, which is, does this actually, honestly depict what you're doing, what you're trying to do on a day-to-day basis? Because if it doesn't, then it's hard for me to trust that, that it matters. Or if that's something that just happens to describe what you're doing but isn't really connected in a meaningful way, then I question the value of it all.

(00:47:28):
So that's why I am in the process. But I definitely am all ears to advice around this kind of stuff, because I feel like we haven't quite cracked the code.

Lenny (00:47:38):
I love hearing that. That ,hole journey. I feel like you always hear from product teams, here's what we do now. You never hear, here's the experiments we've been through, here's what we've tried, here's what worked for a while, here's what doesn't work now, and here's what we're doing now. So it's really cool just to hear all the experimentation you've done. Clearly, Figma is a company where you encourage experimentation and trying new things that aren't working, and it's cool they have the flexibility to just like, let's just do headlines for now, and no more specific goal metrics. We're just going to build things that we think are important.

(00:48:09):
And in the newsletter post, for folks that are listening, you actually show the templates that you're using these days for planning your projects and laying out your OKRs, so folks can check those out if they're interested in seeing how you're doing that, now. You also mentioned you've hired this awesome data scientist, and maybe just expanding that further, I imagine a lot of the success of Figma and the product that you built is the people that you hire. At Figma, I believe you have 22 product managers, which sounds very small for a company like Figma, and I imagine they're all amazing. I'm curious what you look for in product leaders and product managers that you hire that, maybe, other folks aren't as focused on, and just what does the interview process look like at Figma?

Yuhki Yamashita (00:48:51):
Yeah, I shared some of these things. I really feel passionately about storytelling, and not to give it away or anything, but one of my favorite interview questions is asking, "describe to me a time when you're part of controversial product decision, and what did you do," and all those things. And I think it's really revealing because if they can set up this conflict and understand why this problem was really important and represent both sides in such that you can understand why that conflict existed in the first place, then they can do it in this even-keeled way, where you realize that they can take on these different perspectives. You start to learn a lot about that person, I think.

(00:49:35):
Or sometimes, I just ask them for basic things, okay, talk about a big problem that you worked on. And the thought experiment, for me, is always coming out of that, do I feel compelled to work on that problem? And no matter how boring it sounds on the surface, I think a really great product manager can cash something, it's like, well, this is why it's so existential for us, and this why it's so interesting, and really rally the troops up. So that's one big thing of storytelling communication because at the end of the day, so much of our job, it's around that.

(00:50:07):
I think other than that, some of the things that I value or things I think about as, hi Dan with UX conversations, it's like we talk about problem, and I think about when you're exploring solutions, it's this tree of, okay, there's just these branches of explorations and you finally arrive at these solutions. And a ton of people who can go up and down branches really quickly, have a really high command of all these different altitudes, as well, so that we can talk through a lot of things at the end of the day, feel like we walk away with some progress.

(00:50:43):
And I think that at Uber, our first two Product Officer, Jeff Holden, was someone who often talked about fast forwarding to the future and this idea that, okay, let's just pretend we ran that experiment. What do you think it'll come back with? Or let's pretend we ran that, you just use a study. And the PMs who have the ability to imagine those outcomes, I think, it helps us be much more efficient, too, because we're like, well, if we all think that it's going to go there and that's not going to compel us to take any action, why do it at all?

(00:51:17):
And so I think a lot of PM is about those shortcuts that you have to take. And it's not just about what we build, it's about building the right things. And sometimes, it's just as important to decide not to build something, but it's all only possible if you can have that kind of imagination or that ability to see around corners.

Lenny (00:51:37):
I love that. I was going to ask you for your favorite interview questions in our lightning round and you jumped ahead, which is great. And those are really good examples. Hopefully, they don't give too much away. I want to chat a bit about growth and how Figma grows. If you ask people about product led growth, and just whenever people talk about product led growth, they're always companies like Figma, Slack... Figma is always seen as a model of product led growth and a product that grew through product.

(00:52:04):
I imagine now, there's a very robust sales team, and I imagine, even earlier than people, probably, imagined there was a sales team. I'm curious, as a product leader, what you've learned about how to effectively work with sales and what you teach your product managers about how to work with sales to collaborate effectively.

Yuhki Yamashita (00:52:24):
We're really lucky to have a sales team that understands their product really well and can hold their own with customers who are often also design leaders, product leaders and things like that. And I think that kind of credibility goes a really long way. One of the things that we all are collectively realizing is, we talk about product like growth, but in some ways, I like to think about it more as community led growth or there are certain people inside a company that feel so strongly about Figma and that they're helping push for it in these advocates and evangelizing for Figma.

(00:53:03):
And so oftentimes, what the sales team does is really empower those individuals to make a stronger case or connect them to the rest of the company so that we can get a wider deployment or more leadership buying and things like that. And so oftentimes, a sales team is playing that role of creating those human connections and helping equip designers that feel passionately inside a company with the data, with the stories and all those things to help make a case. And I think that's the most powerful way in which we can spread where the space of Figma is not the sales team, but in fact, it's the internal designer.

(00:53:47):
And so that's the mental model that I think we've been using it. We're fortunate enough to have people inside companies who are so passionate to want to play that role. And so when you take that lens on, then you start to understand, okay, how can we help set this person up for success? And the sales team has different ways to do it. The product team can help, in terms of giving them visibility into how we're thinking about evolving the product or what other customers might be doing. And so, I really see it as this partnership to enable that much as possible. And I think that's what, to me, product growth looks like at Figma, is that.

Lenny (00:54:29):
That is really interesting. Basically, making your champion inside the company a superhero, helping them be more effective at what they're already doing, which is evangelizing this product that they really love. Interesting.

(00:54:42):
Is there anything that you think Figma did early on that you think was really important for it to start to grow, either in this way or in a different way? Imagine there's just a lot of product led growth founders that are trying to create a product led growth product, and they fail. And so I'm curious, just what do you think people often miss and what do you think Figma did right that got it going?

Yuhki Yamashita (00:55:02):
I think a lot of it was about the level of intention around building community. And the more there are organic conversations happening about Figma, the better. And one of the nice things about Figma is you can share out a file that you've been working on, and effectively open source something, but it's your way of showing, here's how we do it at so X, Y, Z company, and sharing that with the rest of the community. And when people see that and when people feel like they have this insider view in how other companies work, that's where there's a lot of interest.

(00:55:38):
And more recently, over the last few years, we've really been focused on a program called Friends of Figma where we have people who are passing about Figma, and all our different geographies come together in a Discord channel. They meet regularly and are helping us evangelize. And again, that's that human connection between users, and then between us and the users is something that really helps build that kind of loyalty, which is the thing that, then, fuels all the champions to really push for it, internally, and give people the enthusiasm and courage to do that inside their organization.

Lenny (00:56:16):
It's interesting how many corollaries there are to Notion and how they got started. I recently chatted with Camille, I don't know if you heard that episode, but there's a lot of similarities with how Notion use their community to help jumpstart growth and continue to grow.

Yuhki Yamashita (00:56:29):
Totally.

Lenny (00:56:30):
It's interesting that you can call that community growth, product growth. There's a lot of overlap there, potentially.

Yuhki Yamashita (00:56:36):
For sure.

Lenny (00:56:37):
What advice would you have for folks that are, I don't know, maybe you already shared this, but just if you're a product led growth founder listening to this, do you have any other piece of advice to that founder about how to get started with their product, their community, their growth strategy? Anything else you'd want to share there?

Yuhki Yamashita (00:56:52):
Maybe a different way to talk about what we just talked about, is just, there has to be this, almost irrational, this emotional response to your product and this like love for it. First, it has to be cultivated internally, too. People, internally, have to authentically love something to really stand behind it. But then, externally, too, if people are loving something to the point where they can sing at the top of their lungs and just really talk about how Figma's, great, if we can get there, that's a wonderful place to be.

(00:57:27):
And I think that's both a combination of you've really solved their problems well, but you also equip people with a philosophy around a different way of working. And I think that's what worked well for Figma, too, which is, there's something controversial about this idea that everyone can see what you're doing, or that multiple designers can be in the file at the same time. We like to say that one of the first responses we saw [inaudible 00:57:51] Figma was, if this is a future of design, I'm quitting. I'm changing careers. And there's that tension of that narrative tension, but that is signal that you're part of this revolution and you're trying to change something. And when it can equips your customers or user base with that, and I think that's something that they can really get behind and champion, so it's not just that they're championing for a tool, they're also championing for a new way of working.

(00:58:20):
Obviously, that's a tall order or [inaudible 00:58:23] come up with that. But hopefully, if your a founder, you're working on something, your mission is so big that you have those kind of ideas, and it's how do you actually equip your customers to want to talk about that?

Lenny (00:58:35):
That's awesome. Reminds me of a quote and a tagline that the Airbnb's first growth team had for a long time. Love drives growth, not the other way around. They made posters of this, put it all over the product teams.

Yuhki Yamashita (00:58:48):
I love that.

Lenny (00:58:49):
Part of the office and seemed to have worked for Airbnb, clearly working for Figma.

(00:58:54):
One last question feels like a question we have to touch on. I don't know how much you can say about all this stuff, but with the potential acquisition with Adobe, which I know isn't done, yet, but I'm just curious, what do you think will change, may change, you're hoping will change, you're hoping won't change in how you build product at Figma within Adobe?

Yuhki Yamashita (00:59:12):
Totally. Yeah. As you said, it hasn't closed, yet, and so we're still independent companies, but when we think about that theoretical future, I think about people often ask me, so what's going to happen, in terms of the products that you work on, and how is that going to influence Figma? And the answer is, we don't know, yet, but I get excited about two avenues. One is just really continuing our current mission of making product design better. And the reality is we look at product design, a lot of people are still using both Adobe and Figma alongside each other. And maybe you're creating that micro interaction in After Effects, or maybe you're doing that intricate illustration in Illustrator, or editing Raster in Photoshop, and then you're bringing some of those things into Figma. But when you think about the end product development process, there's so many ways in which, if we can make all those things seamless so that you're not juggling a bunch of apps, or maybe you can have one single source of truth, that's really exciting to me to think about. So concretely what that means, I don't know, yet, but as thinking through those journeys, that gets exciting for me.

(01:00:22):
And then the other thing is really collaborating with the rest of Adobe and thinking about, we've figured out something really interesting in the form of realtime multiplayer collaboration, and that, as a platform. Adobe has a much broader set of use cases that they've been pursuing, and what do those two things together, what could that enable? And that gets exciting for me to think about all the creative tools that I've used in the past, be it video editing or 3D objects or things like that where it's, okay, if we can bring in the power of the browser, of multiplayer, of this feeling of openness, would that make it way easier for people? Would it make it much easier for people to share work or get involved?

(01:01:04):
So those are the things that go through my heads, in terms of what's possible. In terms of what I don't want change. I really think that we've figured out something really amazing, in terms of our relationship with the community. We talked about proximity to community and our users. Those are things that we intend to keep and keep doubling down on. And I think it's such an important part of the magic of how Figma works. So it's something that, I think, I will continue to do and that's what I draw a lot of motivation from in the first place.

Lenny (01:01:34):
Awesome. You also get to work with Scott Delski, which is going to be pretty sweet and hoping to get Scott on this podcast at some point, too.

Yuhki Yamashita (01:01:41):
That'll be awesome.

Lenny (01:01:42):
Any closing thoughts before we get to our very exciting lightning round?

Yuhki Yamashita (01:01:46):
It's really easy to listen to some of these podcasts and feel like, oh, these people have kind of figured everything out.

(01:01:53):
But the reality is, we haven't, and we're still experimenting with a lot of things. OKRs is a really good example of that, but a lot of other things. And so, just the other day I wrote about this idea of us living in a work in progress world, and I was talking about more from the context of we live in a world where all of our products, our product players, our strategies are work in progress, and how do you work in a world like that, when what you're reviewing can change the next day.

(01:02:23):
But in a similar way, I think the way we work, the way we run product processes as product managers is, itself, very much a work in progress. So I would love to encourage this kind of conversation, Lenny, that you're facilitating just because you have so much to learn from each other. And I'd love to continue to learn more from all of you on interesting ways that you grapple with these age old problems around things like how to set goals, or how to review work, or how to plan.

(01:02:54):
So anyway, just wanted to signal that we are very far from perfect, and I really eager to learn from everyone else, as well.

Lenny (01:03:04):
I love that. That also reminds me of something the Airbnb founders always came back to. Joe and Brian were both designers, and as you learn to be a designer, you are taught that everything around you is designed by someone. Someone just decided this webcam's going to look this way and work in this way, this chair, somebody decided very specifically, it's going to be like this. And we assume the things that we are working within are just, they're figured out. Someone much smarter than me figure this out. But it's usually just someone just like you that had to figure something out quickly, and then that's what you're doing now. And so they always encouraged everyone to just remember someone designed this, doesn't mean it's the perfect solution, and you should always rethink things like that and not assume.

Yuhki Yamashita (01:03:44):
Yep.

Lenny (01:03:44):
Well, with that, we've reached our very exciting lightning round. I've got six short quick questions for you. I'll just go through them pretty quick, whatever comes to mind, share, and we'll see how it all goes. Sound good? All right.

Yuhki Yamashita (01:03:56):
Sounds great.

Lenny (01:03:56):
Awesome. What are two or three books that you've most recommended to other folks?

Yuhki Yamashita (01:04:02):
First one that comes to mind is Switch, and it's really about how to affect organizational change, something that's Shishir recommended to me and we have the difficulty of affecting change in a large organization, basically, and how to overcome that.

(01:04:16):
The second one I would say is my favorite book of all time is one called The Story of the Stone, and it's a Chinese novel, one of the most famous Chinese novels of all time. And it's thousands of pages. It all takes place in a garden, but it's one of the most beautiful piece of work I've read, so I like to recommend that, even though it's nothing to do with PM.

Lenny (01:04:38):
Did you say thousands of pages?

Yuhki Yamashita (01:04:39):
Yeah.

Lenny (01:04:41):
About a stone. Wow. I will check this out. I love it. I've not heard this one before. Favorite other podcast, other than the one you're currently on?

Yuhki Yamashita (01:04:49):
Well, I'll have to admit, I'm actually much more of a visual learner, not a listener, and so I rarely listen to podcasts, but the two that I have listened to, in earnest, was first one was Cereal a long time ago, and then yours.

(01:05:04):
So I think some of the best, actually, but otherwise, more into reading.

Lenny (01:05:09):
Awesome. This show's also on YouTube, for folks that don't listening and like watching things. Plug, plug. Favorite recent movie or TV show?

Yuhki Yamashita (01:05:18):
The last movie I watched was called The Good Nurse, and it was about a serial killer working in a hospital, but it was a very different take on it. It was very human. It wasn't grotesque at all, and was talking about how broken our system was. So, highly recommend it. Quite sad, but yeah.

Lenny (01:05:37):
Okay, good tip. What are some SaaS products that you love that you, maybe, use at Figma or that you just discovered that you find very useful?

Yuhki Yamashita (01:05:45):
Kind of cheating, but as I mentioned earlier, we're starting to use FigJam for everything from calibrations, to interview debriefs, to product reviews, to everything. So that's thoroughly started to dominate our usage. It's been cool to see. And then we have our usual suspects like Slack and Asana, and then we're all over the place on the rest. Some of us use Notions, some of these use Dropbox Paper, some of these uses Koda, and so we're still figuring that one, out, I'd say.

Lenny (01:06:16):
Dropbox Paper. Very cool.

Yuhki Yamashita (01:06:17):
Yeah.

Lenny (01:06:18):
I love that product, but I feel like no one uses it anymore, but it's cool that you guys do. Final question, favorite FigJam or Figma plugin or template?

Yuhki Yamashita (01:06:27):
We have this one called the Alignment Scale, which is a widget that you can insert into FigJam or Figma Design, actually. And we use it all the time. So basically, it's just a simple scale and whenever people click it, their face appears on one end of the spectrum or the other. And so it's our quick way of being like, we're doing a product review, we on a pulse check, we drop it in and we're like, how are people feeling aligned, not aligned?

(01:06:52):
And if people are aligned, we just move on. If not, then you know that it's worth a discussion. So it's just a fast way to figure out where all the hotspots are.

Lenny (01:07:01):
Awesome. And if folks want to find that, they can actually go to the newsletter interview that we did. I think if you just Google how Figma builds product, it comes up number one, and then there's a link to actual template, so you can plug that right in.

(01:07:13):
Yuhki, thank you so much for being here. I am going to go play with Figma and FigJam right after this. Two final questions. Where can folks find you online, if they want to reach out, learn more? Are you guys hiring, anything there? And then, two, how can listeners be useful to you?

Yuhki Yamashita (01:07:30):
Yes, you can find me online on Twitter or LinkedIn. Feel free to reach out there.

(01:07:36):
In terms of how you can be useful to us? We're really starting to build a lot of products for this audience, for product managers. FigJam is one example of this, so definitely try it out, give us the feedback, tell me all about all the cool things that you're doing or you wish you could do on FigJam or Figma. And you can tweet at me, you can find me anywhere. And, of course, we're also hiring, so if you know great people or are interested, yeah, there's a lot of roles, so please get in touch.

Lenny (01:08:06):
Awesome. Yuhki, thank you so much for being here.

Yuhki Yamashita (01:08:08):
Thank you so much for having me, Lenny.

Lenny (01:08:11):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcast, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

---

## How to grow a subscription business | Yuriy Timen (Grammarly, Canva, Airtable)
**Guest:** Yuriy Timen  
**Published:** 2022-09-01  
**YouTube:** https://www.youtube.com/watch?v=8-iN7sweFBM  
**Tags:** growth, retention, acquisition, activation, onboarding, churn, metrics, okrs, kpis, prioritization  

# How to grow a subscription business | Yuriy Timen (Grammarly, Canva, Airtable)

## Transcript

Yuriy Timen (00:00:00):
The only thing that's worse than a channel or a tactic that you tried not working. The only thing that's worse now is when you didn't give it the appropriate shot, right? And you prematurely were erroneously concluded that it doesn't work and it's remarkable how often you find that to be the case when I talk to companies, "Oh, YouTube, we tried it. It doesn't work." I'm like, "Okay, can I see what you've tried?" And then you look at it and you're like, "Oh, this thing was not designed to even have a shot at working from the get go."

Lenny (00:00:40):
Yuriy Timen is a full-time advisor to companies looking to figure out their growth strategy. He's worked with companies like Canva, Airtable, Otter, Whimsical, Hims, Flow Health, and a dozen others. I know a number of founders who have worked with Yuriy and they all tell me that he transformed how they think about their growth. Before becoming an advisor, he spent nine years at Grammarly where he led growth in marketing and helped turn that into the household name that it is today.

Lenny (00:01:07):
In our chat, we get incredibly tactical about all of the ways that you can grow your product, including when and how to invest in virality, SEO, and paid growth. What's changing across each of those channels and the most common failure modes for B2C startups. This is the most tactical and actionable conversation I have had yet on how to grow your product, particularly a subscription product. And I'm really excited for you to hear it. With that I bring you Yuriy Timen.

Lenny (00:01:36):
Hey, Ashley, head of marketing and Flat File. How many B2B SAS companies would you estimate B to import CSV files from their customers?

Ashley (00:01:44):
At least 40%?

Lenny (00:01:46):
And how many of them screw that up and what happens when they do?

Ashley (00:01:49):
Well, based on our data, about a third of people will consider switching to another company after just one bad experience during onboarding. So if your CSV importer doesn't work right, which is super common, considering customer files are chalk full of unexpected data and formatting they'll leave.

Lenny (00:02:08):
I am 0% surprised to hear that. I've consistently seen that improving onboarding is one of the highest leverage opportunities for both signup, conversion and increasing long term retention. Getting people to your aha moment more quickly and reliably is so incredibly important.

Ashley (00:02:23):
Totally. It's incredible to see how our customers like Square, Spotify, and Zuora are able to grow their businesses on top of flat file. It's because flawless data onboarding acts like a catalyst to get them and their customers where they need to go faster.

Lenny (00:02:40):
If you'd like to learn more or get started, check out Flat File at flatfile.com/lenny.

Lenny (00:02:47):
This episode is brought to you by Modern Treasury. Modern Treasury is a next generation operating system for moving and tracking money. They're modernizing the developer tools and financial processes for companies managing complex payment flows. Think digital wallets via crypto on ramps, ride sharing, marketplaces, instant lending, and more. They work with high growth companies like Gusto, Pipe, Class Pass and Marketa. Modern Treasuries robust APIs allow engineering to build payment flows right into your product while finance can monitor and approve everything through a sleek and modern web dashboard. Enabling real time payments, automatic reconciliation, continuous accounting and compliance solutions. Modern Treasuries platform is used to reconcile over $3 billion per month. They're one of the hottest young FinTech startups on the market today. Having raised funding from top firms like Benchmark Altimeter, SB Capital, Salesforce Ventures, and Y Combinator. Check them out at moderntreasury.com.

Lenny (00:03:50):
Yuriy, welcome to the podcast.

Yuriy Timen (00:03:52):
Thanks for having me man. This is great.

Lenny (00:03:55):
It's even better for me.

Yuriy Timen (00:03:57):
All right.

Lenny (00:03:58):
So I'm going to give a quick bio. Let me know if I missed anything really important. You were head of growth at Grammarly. You spent nine years there kind of doing all the things that helped turn that company into the killer product that it is today. You left that I think a couple years ago. Now you're advising companies mostly full-time. I think mostly on growth strategy. I think mostly consumer startups, is that about right?

Yuriy Timen (00:04:21):
A couple of super critical corrections. Number one, it was only eight and a half years.

Lenny (00:04:26):
Okay. Usually people round those up. I'm impressed that you get-

Yuriy Timen (00:04:31):
I think eight and a half is long enough. Yeah, not sure I want to round up. I know, but I'm kidding obviously. Yeah. That's largely it. Grammarly was a hell of a run and trying to take a step back from that, and stepping back has kind of taken on a life of its own vis a vis advising.

Lenny (00:04:54):
How many companies have you worked with at this point advised and what are some examples, just like companies people would know.

Yuriy Timen (00:05:01):
It's now been about, I guess two years and three months since my last day at Grammarly in an operating capacity. I've probably worked with maybe 15 companies in the last two and a little bit of years. Obviously, not all at once. It's usually four to five at any given point in time. But some of the ones that I've been really lucked out with in terms of getting aligned with companies like Canva, Airtable, Hims and Hers in the personal care space, there is otter.ai. Who else? Flow Health, the world's most downloaded period tracker.

Lenny (00:05:47):
I used that for my wife. It's handy.

Yuriy Timen (00:05:49):
Good, good. Yeah. I was trying to get my wife to try it out, but been unsuccessful.

Lenny (00:05:59):
You're failing in your growth.

Yuriy Timen (00:06:01):
She was like, "Are you trying to push me to having a third kid?" I was like, "No, no, I swear." This is just product testing.

Lenny (00:06:08):
Clever. So I've had Casey Winters on this podcast and Elena Verna. It's kind of like the three of you that it feels like have worked with the most companies as advisors. I don't know if there's some kind of contest y'all have or anything, but do you think about that at all? Is there anyone else out there that you think is in the running?

Yuriy Timen (00:06:26):
First of all, just being mentioned the same breath as those two is an accolade in and of itself. I mean, I look up to both of them. They've gone first. Also, I credit a lot of my getting started to both of them because they've been very generous with their time when I was just kind of considering advising, especially Casey, if they listen to this. Huge shine out to both of them, but Casey especially. He's such immense when it comes to just being generous with his time. So no, there is no competition, but had there been one, I suspect I'd be in lead right now because I've done it. I've done it in a shorter period of time. I'm much newer to advising than both of those, but no, I have a ton of aberration respect both of them. They're phenomenal what they do and I learned a ton from them.

Lenny (00:07:24):
I love that acceleration is fastest. Wow, sweet. So we're going to talk a lot about consumer growth strategies and your experience working with companies and a bunch of insights on things you've learned from working with companies. Before we get there just one quick question in your advising. I'm curious how many companies do you work with at once normally?

Yuriy Timen (00:07:43):
Yeah, so I play around with different quantities. So a couple of things. So you mentioned, you alluded to earlier that I advise full time. What I'll say is that mostly the only thing that I do right now professionally is advising, but it's not quite full time. I hard count my week at about three to three and a half days a week worth of work, which is a personal choice. And so that is a hard constraint that I'm working with. And within that constraint, I also feel like for me to do my best work and the work that I also enjoy the most and find the most fulfilling four to five companies is probably the max. If I try to go beyond that, the overhead that it creates in terms of the cost of context switching just becomes overwhelming. I feel like I'm not showing up as best as I can with each individual company.

Lenny (00:08:43):
As early plug or anti plug, depending on how you answer this. Are you looking for more companies to work with right now or are you just like, "Don't even try. I am so at capacity right now."?

Yuriy Timen (00:08:53):
I'm so at capacity right now. I've also just been very fortunate to always be at capacity. But I think for every four to five companies that I'm working with, think of it as a concentric circles, right? There are another, maybe 10 to a dozen companies that we're actively exploring if we want to work together in the future. And then there is another concentric circle so maybe 30 plus companies that I'm just friends with. So I'll take the plug. I'm always up for meeting Austin founders working on important problems.

Lenny (00:09:31):
Cool. Well, we're in the plug I guess. How do people find you online? What's your Twitter?

Yuriy Timen (00:09:34):
I mean, honestly, probably throw Lenny's podcast. That's one, but honestly LinkedIn is really the only place I'm pretty low key otherwise.

Lenny (00:09:45):
Okay, great. That was a lot of Meta stuff. So let's get into some meat stuff here. So you talked to a lot of consumer startups. You help them figure out how to grow, how to evolve their product, something I'm always curious about and I love your thoughts on is when you look at a consumer startup, I imagine there's a few archetypes of how they grow. I'm curious if that's a mental model you use when you're like, "Oh, I see company X. They're probably going to grow this way, and here's what they should focus on." How do you see that?

Yuriy Timen (00:10:11):
Great question. I think there are ways to answer that. My sweet spot is subscription properties and it's not just consumer. I do work with a lot of B2B companies. It's just that most of them, but what they all have in common is they lean into consumerized type of growth loops and growth motions. So they're very kind of self-serve nature or have meaningful self-serve engines. So if I think about subscription companies, I think there are probably a couple of buckets that I see them falling into. If you were able to nail your unit economics and you have really strong consumer LTVs, think Grammarly, think Canva. The single player LTVs for those companies are very, very high. They're kind of average S&B LTVs for B2B companies.

Lenny (00:11:03):
What's a number there just for folks to have a little context?

Yuriy Timen (00:11:06):
I'm not a liberty to speak to those, but we're talking in the hundreds of dollars. Most consumer subscription companies that are $5 to $7 a month. Their LTVs typically cap out at 50 to 60 bucks.

Lenny (00:11:25):
Cool.

Yuriy Timen (00:11:26):
And so if you have really healthy LTVs, and that usually means that you're attracting a proconsumer buyer, so they may be single player, but they're using it for work. And so maybe they're dispensing it or just the perceived value so much higher that they're willing to bear that $120 and $130 a year subscription. If I'm seeing things like that and I'm seeing that you're converting seven, like five plus percent of your free users to a paid subscriber, then there is a big opportunity to play paid and lean into paid growth loops and paid acquisition loops. There is another archetype, which is if there are network effects for instance, you don't find that as much with single player consumer subscription companies, but obviously social media, consumer companies.

Yuriy Timen (00:12:17):
There may be a strong referral viral loop angle if the utility increases, the utility of the product increases, the more users are using it. Another archetype I see are companies that can lead into SEO very heavily, especially if there is a long tail programmatic angle. Take Canva for instance, their biggest initial growth loop and I think this is public knowledge was their long tail SEO strategy where any kind of design project that you could think of would search for designing. It's kind of two categories of keywords, make keywords and template keywords. So if you're searching for a template of any kind, a wedding invitation, yada yada, they had incredibly strong SEO and they were just capitalizing on all the long tail traffic. Not every product is going to lend itself to that, but I always look for that early on, because you can build incredible mold with that kind of strategy.

Lenny (00:13:21):
That makes sense. There's kind of like these three engines that you can tap into. I imagine the preference would be word of mouth reality and then if that isn't going to work SEO, and if that is going to work paid, maybe just to simplify it for listeners, what are kind of signals you can go after virality and invest in that and think that could work because every founder would be like, "Yes, virality. That's how I'm going to grow." Yeah.

Yuriy Timen (00:13:47):
Yeah. Honestly, the first thing you look for is that, is there inherent product network effects? It's something that it's either there, or isn't from inception from my experience. I think it's very difficult to manufacture. You'd only study when... It's very hard to manufacture product network effects if they aren't there from the get go. So Airbnb from your days, obviously marketplace very strong product network effect dynamics. You think of collaboration tools, Airtable, monday.com, Whimsical, whom we both know very strong inherent product network effects, contrast that with a company like Grammarly. It just wasn't there. It's not an inherently multiplayer task constructed communication. And so you can try to engineer that, but from my experience, it is an uphill battle. So if you have inherent product network effects, that's when I think layering on referral loops and viral loops. You think about what Dropbox has done around file sharing. That's an iconic example.

Yuriy Timen (00:15:02):
Then it's really powerful. I think that there is another case where referral and viral loops could work even when there are inherent network effects. If you have a really beloved product, beloved brand. There's a company out of Australia that I have opportunity to invest it called Laika. They do fresh dog food subscriptions and incredibly beloved brand, a premium product. And so they're able to lean into a give one, get one referrals, even though there isn't inherent product network effects, they're still able to generate meaningful results off of the, and incentivize referring program.

Lenny (00:15:39):
When you talk about network effects, what does that mean to you? How would you define that briefly?

Yuriy Timen (00:15:45):
Yeah, to me, I mean, honestly I define it I think probably a pretty quintessential way, which is for every individual user, the utility that they derive from the product increases the more users there are on the platform. The expanded version of that is in a case of marketplaces. It may not be the bore users broadly speaking, but the more users in the markets that you care about, in the case of collaboration tools, it's not the more users in abstract terms. It's the more users within your team, the more users within your company, right? That correlates with your kind of the rise in your utility curve.

Lenny (00:16:33):
Awesome. So if you have network effects, AKA if the product becomes more useful with more people or there's amazing word of mouth already, or there's collaboration, probably a good sign that you could lean into virality or maybe referrals. What about SEO?

Yuriy Timen (00:16:50):
Oh, that's a good one. It's a very timely question because I actually in a process of helping a couple of my companies figure out if it's the right time to invest in SEO. So I've been sort of a forefront of taking exploratory meetings with agencies and SEO consultants and things like that. I mean, I would say the first thing to figure... I mean, there are a couple of pillars, because obviously we all know that SEO has a different return horizon than say paid acquisition. It's longer out. It's maybe six months is the earliest you can see results. Even then it's going to be a small trickle that compounds over time, if you're successful or you may spend three to six months leaning into an SEO strategy and then realize that it's not going to back out typically at least in historically a company probably isn't like Series B before it starts feeling like it passed a luxury of making these kind of medium to long term investments.

Yuriy Timen (00:17:58):
But I think that's shifting right now, but that's maybe a topic for later or even for another bot but a lot of the strategies that I think we're reserved for Series B are trickling down to Series A companies because they have to diversify way for pay, but maybe more on that later. So I think with SEO, it's like the first pillar I would say is, do you have a unique angle when you take a look at the SEO landscape today, you look at editorial, the landscape, which is to how to searches and who are the players there and what kind of information is being offered? Do you have something unique to contribute to that conversation? Another thing if I have to do an audit checklist, another thing is, do you have a unique programmatic angle, right? For instance, Canva did dealt with templates. Who else is programmatic?

Yuriy Timen (00:18:54):
CWELL, Redfit, obviously all the real estate, right? That's really strong-

Lenny (00:19:00):
Saint Pier.

Yuriy Timen (00:19:01):
Saint Pier, right. So do you have a programmatic angle and then understanding the competitive landscape or the other one is, do you have a unique data angle? So for instance, a company I work with called Monarch Money, which is in the personal finance management space. Think of it as a new and improved version of MIT. There is a lot of users are connecting accounts and you have a sense percenting patterns and things like that. Clearly there is a unique data, and so it's a question of, can you turn it into some kind of valuable organic search experience?

Yuriy Timen (00:19:39):
I won't go into too much detail in terms of what we're thinking of there, but that's another checkbox. If you can check two of those three boxes as a back of the envelope framework, you may be in good shape. And then it's a question of like, "How can you lower the cost of experimentation SEO as much as possible?" I think as a rule of thumb, if you can time box it to three months, what can I do at the end of three months? Is this likely to work or not?

Lenny (00:20:14):
Awesome. Couple follow up questions.

Yuriy Timen (00:20:16):
Absolutely.

Lenny (00:20:16):
One is SEO feels like this dark art where you need some SEO wizard to come help you through this.

Yuriy Timen (00:20:24):
Yeah.

Lenny (00:20:25):
Do you suggest companies find somebody or work with an agency or something else? What's your general feeling on SEO versus some other route?

Yuriy Timen (00:20:33):
I think SEO is pretty specialized skill set. There are some basic principles that always hold like best content wins and don't do shady back linking and make sure that you're on page. SEO is good and your pages are easily crawl, but I feel like everybody knows that. And where the winners are determined are between the lines. Better than a sports' analogy? Maybe you can.

Lenny (00:21:10):
Between the lines. I don't know what that comes from.

Yuriy Timen (00:21:15):
But anyway, what I mean is that there is a lot of more nuance, SEO developments and angles, where I think is where the opportunity really lies to differentiate yourself. And that requires keeping up with the latest algorithm changes. It's very hard to do that unless you are specializing in the art where the black magic of SEO, and so that's why I think getting an outside resource at least for an audit is really helpful. Now, whether it's a boutique agency or a solo consultant, I think that's more circumstantial, but I've found at least with the companies that I've worked with, if we wanted to quickly vet the SEO opportunity, I can do it in a very kind of amateur, at an amateur level.

Yuriy Timen (00:22:02):
Plug things into similar web and try to figure out the right option is there, but you can get these relatively inexpensive audits done from companies that you can then choose. Do I hire them to help with my SEO or not? But I think that audit is usually a very good use of time because they have templates. So what they can turn around for five to 10K would take you many, many human hours to try to pull together yourself.

Lenny (00:22:28):
Awesome. Are there agencies that you want to name that people can go check out or would you prefer just to keep it from having-

Yuriy Timen (00:22:35):
I'll give one plug.

Lenny (00:22:37):
Great.

Yuriy Timen (00:22:37):
I think one of the most innovative, disciplined first principles SEO thinkers and I have met is Ethan Smith from Graphite. It's not for everyone. It's a pretty high end SEO shell. So I wouldn't send the Series a company there, but Ethan also produces a lot of resources and what they've been focusing on at Graphite lately has been actually automating a lot of their work and turning it into SAS. So I don't know how far along they are, but you could probably already get into some of the betas from the tools that they're offering.

Lenny (00:23:18):
Sweet. I'm going to try to get Ethan on this podcast.

Yuriy Timen (00:23:20):
Yeah.

Lenny (00:23:21):
I've seen his stuff and it's awesome.

Yuriy Timen (00:23:23):
Yeah. He is a math scientist when it comes to SEO. Yeah.

Lenny (00:23:25):
We need those. We need math scientist on ship.

Yuriy Timen (00:23:28):
Right.

Lenny (00:23:28):
Okay. So we've talked about virality talked about SEO, paid. Imagine that's pretty straightforward if your LTV are high enough and you can pay back ads on those, then that's where you go. Imagine everyone can try it. Doesn't work for everyone. What if yeah, anything you want to add there?

Yuriy Timen (00:23:43):
I mean, there's a lot. There's a lot. I mean, I don't know how deep you want to go down the paid rabbit hole because it's changing. It's probably the most affected growth bucket in light of the market turbulence, the venture sentiment shifting. I've seen paying acquisition strategies at budgets. They are at the brunt of that fallout. And so the question is where do you want to go there?

Lenny (00:24:16):
Yeah. That's a really good topic. I was saving that for later, but let's chat it better right now.

Yuriy Timen (00:24:19):
Yeah.

Lenny (00:24:20):
I imagine part of this is Apple's tracking changes too.

Yuriy Timen (00:24:22):
Yeah.

Lenny (00:24:22):
So I guess my big question is paid still lucrative and a good path for many companies is like 50% of the time less effective. How do you see that shifting recently? And how should people think about paid in the consumer subscription startup?

Yuriy Timen (00:24:38):
Well, I think in the short term, let's break it down into phases. I think in the short term paid acquisition and just paid media dollars are contracted and we're seeing it already with Metas advertising revenue, Snaps advertising revenue. There's clearly a global contraction happening to paid media budgets. A big part of it is because all of a sudden the definition of efficient acquisition and good payback windows is shifting. So before for a consumer subscription company, 12 month payback was decent. Now it's like, you better pay back your paid media in six months or less. That's the sentiment.

Yuriy Timen (00:25:23):
So the thought is reaction is like anything that's more than six months we're well board of six months, we're cutting that and so there's that. Then there is just less tolerance for ambiguity and attribution when the sentiment is like, "Let's grow at [inaudible 00:25:38]. Grow at all costs." If you can't attribute things perfectly, that's okay. Now it's like, especially with venture back companies, you have to have two plus years of runway, managers burn a lot more diligently now. And so whatever you can't attribute to sales sue like, "That shits got to go." I don't know if we can curse on the pod or not.

Lenny (00:25:59):
Only available-

Yuriy Timen (00:26:03):
Well, I've been holding back for the last 30 minutes. No, I'm kidding.

Lenny (00:26:03):
At least.

Yuriy Timen (00:26:04):
All right.

Lenny (00:26:05):
We're not kid friendly, but nobody's cursed yet. So this could be okay. So you'll be the first.

Yuriy Timen (00:26:09):
All right. Way loud. All right. But anyways, yeah. So I think there is a short term contraction. However, that opens up an opportunity for smart kind of attribution investments. So you're seeing an emergence of some interesting attribution related attribution for incrementality related products. A couple that I personally started exploring and looking into, and then you just see a lot more heads of growth, heads of user acquisition, thinking about attribution in building their attribution stacks. And so I think that once we settle into some kind of new normal, which is going to be a combination of just better attribution stack on average for companies combined with just the level of acceptance, that attribution will never be as good as it maybe once was. We're going to probably get hit. Come out of that and you'll see paid budgets start making their way back. But even right now, during contraction, there are going to be some winners.

Yuriy Timen (00:27:26):
The companies that had strong cash positions, have strong unit economics, strong paid back periods already like Grammarly, Canva to name two that I know personally. A couple of others or many others probably, they're going to be winners because all of a sudden, if previously they were competing with companies who were nowhere as efficient as them, but for whatever reason had the green light to keep spending, now all of those are going to pull back their budgets. And so those that have been disciplined, have the instrumentation to track things better than average. They're going to benefit from decreased competition on app platforms, decreasing CPMs, et cetera. So they're going to do winners for sure.

Lenny (00:28:09):
Wow. Haven't heard this perspective. It's so interesting that the fact that it's gotten harder, it's creating new opportunities for companies to do it better and more intelligently. You said you mentioned a couple tools products that you found to be potentially helpful in this. Is there anything you could mention there?

Yuriy Timen (00:28:22):
Yeah. Yeah. I mentioned a couple that I've kind of connected with in the last couple of months. So first of all, Media Mix Modeling is making a comeback, which is something that kind of got popularized in the math meant kind of advertising era of the fifties, pre-digital, and that's how that was the piece of the methodology. I can't speak of the specifics there. The science is a little bit out of depth there, but it was basically a way to use some data to determine a budget allocation across channels at the time was probably newspapers and billboards, et etcetera.

Yuriy Timen (00:29:03):
It was leveraging data to some extent. You would were doing it maybe on a quarterly basis. And then you would only update it every quarter. There was no way with media mix modeling. There was no way to adjust budget in quarter because you weren't getting the data feedback loop that frequently. But media mix modeling is now making a comeback because there are so many offline channels that are part of folks channel portfolio today and that plus a lot of the online channels are becoming less trackable like Meta for instance, with the iOS 14 shift. And so Media Mix Modeling is going to comeback and the company that's leading the charge of bringing the Media Mix Modeling methodology of the traditional advertising era and ushering it into the digital world is a company called the Recast.

Lenny (00:29:48):
Recast.

Yuriy Timen (00:29:48):
Recast. Yeah. So I've heard really good things. I haven't tried them with any of my companies yet, but there are a couple that are on the horizon hopefully.

Lenny (00:29:58):
Double click there for a moment. Is that still useful if you're not doing TV and other forms of advertising?

Yuriy Timen (00:30:04):
I think it's still-

Lenny (00:30:04):
You're just doing-

Yuriy Timen (00:30:04):
Yeah, I think it's useful if you're spending a considerable amount, what's considerable, I'd say worth of a hundred thousand a month update media. And if you have some level of channel complexity, so you're not just like a Google Go or a Facebook, but maybe you're on three plus the channels. Then I think it still makes sense. The other ones in the incremental space, they have very different methodologists actually, because at end of the day, this might be obvious to folks, but maybe some will find value.

Yuriy Timen (00:30:34):
Click based attribution or the digital attribution were all fawning over cookie based and click based, a real parameter based attribution. It never demonstrated a causal relationship between our media spend and business results. It was only good for correlative insights. And the only way to determine causality is through real controlled experiments, randomized control experiments through incrementality testing, which is typically really hard to do cleanly and also companies have always been often wary about doing it because you have to turn off a channel potentially in a key demo and you're like, "Yeah." The benefit is to learning of whether it's actually incremental, but the cost or the sales that I will lose today. But the only way to really know how effective your paid media is through ongoing incrementality testing. So there are two companies that are addressing that. Two that I'm excited about. One is measured, can be found, measured.call, amazing domain name.

Lenny (00:31:44):
Amazing domain name, go with that.

Yuriy Timen (00:31:45):
And then the other one is incremental, but incremental-

Lenny (00:31:50):
Outcome.

Yuriy Timen (00:31:51):
... no vows except the last A between the T and the L.

Lenny (00:31:57):
Excellent, great job.

Yuriy Timen (00:31:58):
So many free plugs today.

Lenny (00:32:00):
Yeah. I love it. That's great. This is what people need. They're just like, "Okay, what do I actually do"? And so the more it's clear what to actually try and how to solve these problems. The more people can actually make change. I had a couple questions here that I wanted to follow up on. One is founders might be listening to this and they're like, "Amazing. Okay, we're going to grow. There's three ways to grow. Let's do it all. Get someone on SEO to get Jane on paid. Let's get Fred on virality."

Yuriy Timen (00:32:32):
Yeah.

Lenny (00:32:32):
So in your experience, is it smart to focus on one and then expand down the road or try them all see which one works best? How do you advise companies think about these options?

Yuriy Timen (00:32:44):
I would say focus paired with rapid iterations, right? With limited resources. Naturally you have to practice some form of essentialism and ruthless prioritization, but at the same time, the clock is always ticking. You can not burn. That there is a finite number of tries that you have at finding what works, right? What's going to help you unlock the next level of growth, get to the next funding round, extend your runway. And so I think either one taking to an extreme focus or trying multiple things is not a good thing. And just in case, it's not obvious if you focus on one thing and it ends up being the wrong thing, you've wasted really valuable time and now you have so much less time left to find something that does work. Spreading yourself very thin oftentimes in the early stage companies, it's one person who's in charge of all of growth, but they also have some other kind of responsibilities like maybe ops and customer success.

Yuriy Timen (00:33:54):
If you get them to try five different things, they may not try them anyone individually fully enough, because I like to say the only thing that's worse than a channel or a tactic that you tried not working. The only thing that's worse now is when you didn't give it the appropriate shot and you pretty much surely or erroneously concluded that it doesn't work. And it's remarkable how often you find that to be the case when I talk to companies, "Oh, YouTube, we tried it doesn't work." I'm like, "Okay, can I see what you've tried?" And then you look at it and you're like, "Oh, this thing was not designed to even have a shot at working from the get go." So to answer your question, I think it's focus with some guard rails so that you know exactly when it's time to move on to the next thing.

Lenny (00:34:51):
This episode is brought to you by Eppo. Eppo is a next generation A/B Testing platform built by Airbnb alums for Modern Growth Teams. Companies like Netlify, Contentful, and Cameo rely on Eppo to power their experiments. Wherever you work, running experiments is increasingly essential, but there are no commercial tools that integrate with a modern grow team stack. This leads to waste of time building internal tools or trying to run your experiments through a clunky marketing tool.

Lenny (00:35:21):
When I was at Airbnb, one of the things that I love about our experimentation platform was being able to easily slice results by device, by country, and by user stage. Eppo does all that and more. Delivering results quickly, avoiding annoying prolonged analytics cycles and helping you easily get to the root cause of any issue you discover. Eppo lets you go beyond basic click-through metrics and instead you turn north star metrics like activation, retention, subscriptions and payments. Eppo supports test on the front end, the back end, email marketing and even machine learning clients. Check out Eppo at geteppo.com. Geteppo.com and 10X your experiment velocity.

Lenny (00:36:01):
This might be too hard to answer in a chat like this, but do you have any guidance for how to know when you've gone far enough? I imagine there's a lot nuance and detail there. Is there anything that you could share?

Yuriy Timen (00:36:12):
Love the question. It's very thought provoking. I think with some tactics and some channels you can fairly objectively create some test guard rails where it's like, if it's YouTube, we know kind of minimum number of impressions that you got to get. Try two to three creative angles. Here's the click through rates range that you're looking for. If you get within these ranges on these KPIs, keep going. If you don't, abandon.

Yuriy Timen (00:36:48):
I think that's important to also know that abandonment doesn't mean we will never revisit it again, right? It just means that because every time you're evaluating, the concept of sunk cost. So you have these periodic, I think periods of reevaluation where it's like, "Okay, did we try enough? Is this more art than science frankly." It's like, "What's the incremental lift for us as a team to try to experiment with the next phase of this channel or this tactic? What is the opportunity cost of that? What are the other high profile things that we could be trying?" You were right and save this topic too hard to answer in this format, but I would break things down maybe into two types. There are some channels or tactics where you can objectively figure out som guard rails for when it's showing promise or not, because you can pull benchmarks on good click through rates and things like that. Then there are other tactics where you just have to exercise more judgment outside of benchmarks.

Lenny (00:37:54):
Yeah. Yeah. That was actually really valuable and very challenging question to try to summarize quickly so thank you. One more quick question along these lines. So you talked about these three broad ways companies grow. Oftentimes a couple of them work, something I've seen and I'm curious if you agree, usually one is like 80% of your growth and then you layer on a couple more to optimize. Is that what you see?

Yuriy Timen (00:38:18):
Yes. I think companies that we know and admire and reference in case studies or in podcast, such as this one. From the outside looking in, you oftentimes assume that it's a highly diversified growth engine. I have to say it's often not the case. Definitely the 80/20 applies. There is a kind of strategy that's working overwhelmingly well, and there is a scramble internally to minimize reliance on that one thing. And on the discover slash on the walk, the next step function, the next growth horizon. In the case of Grammarly, it was performance marketing kind of over reliance on performance marketing during part of the company's life cycle. And so it was like, "Okay, this thing is working." It's efficient so you don't want to stop pouring fire on it, but you're also thinking months and years ahead, what kind of risk does it open you up to?

Yuriy Timen (00:39:35):
And so there is a scramble to fight and at Grammarly, it's been successful there. With Canva, it was the SEO angle. So for them, that was working really well, which is more defensible than paid. That's sort of long tail programmatic SEO angle, but look, you're always susceptible to Google algorithm updates and so how do you derisk yourself from that? But to your point, yes. And I think that surprising thing to people probably is that it's also the case with some later stage companies. It's not just early stage companies that are kind of one trick pulleys. Sometimes it's later stage companies as well.

Lenny (00:40:11):
This makes me think about is there's kind of these three phases to growth. There's the kickstart phase where you're just doing a bunch of stuff, trying to get things moving. Then there's that you discover your first main growth engine and then there's layer on additional engines because you want to diversify.

Yuriy Timen (00:40:25):
Yep. And one interesting, what I believe is an interesting period and a lot of it is gut feel, right? And I try to direct companies. I encounter sometimes early stage companies is when one thing is working well and they're already worried about over reliance and they're starting to talk about diversification and I come in all the times and I see showing up in their OKRs. I come, "No, no. Too early. I'm glad that you're such a forward thinker. Put all of your energy. Sure, this one tactic is accounting for say 80 plus percent of your new user acquisition, but your user acquisition is still small. So don't get distracted with diversification. We'll get there. Lean more into this, hit this growth rates, stand this up. Build this into a real strategic advantages thing that's working."

Yuriy Timen (00:41:17):
So I actually have to talk them out, focusing on diversification too early. Contrast that with some later stage companies for who are... At scale, I know 50 plus million ARR, 90 plus percent reliant on a single acquisition channel, which just mire with risk and diversification is a blind spot for them. And then with those, I have to be like, "Hey y'all. Here's the risk that you're carrying. Let's start carving out bandwidth resources to try to go and explore these other channels with tactics."

Lenny (00:41:49):
That's such an important point. It reminds me Casey has this hilarious line that he uses that the money's always in the banana stand or there's always more money in the banana stand from [inaudible 00:41:59] development. That basically your growth is probably going to come from the same place it's already come from.

Yuriy Timen (00:42:03):
Yep.

Lenny (00:42:04):
And that you shouldn't take that for granted. And you should put most of your efforts into continuing to optimize that versus being distracted by, "Oh, let's do SEO now."

Yuriy Timen (00:42:11):
I see that argument for sure.

Lenny (00:42:13):
So you mentioned at this point about how later stage growth strategies are starting to move earlier into growth strategy planning. I'd love to hear more on that.

Yuriy Timen (00:42:22):
Yeah. Let me expand on that in the world that we lived in last 18 months, or let's say up until say three to five months ago. We were living in a world where funding was abundant and plentiful, startups were conditions to think that they could raise twice a year. Valuations were quite toppling within a year. You raise in January and then you raise in November and your valuation five X. And so companies were coming off of these ridiculous Series As of 15 to 25 million dollar As and they were like, "We got to grow as quickly as possible. What can we activate to give us immediate return?" And the answer is almost always paid. That one going to give you, especially if you're think you want to go back to raising less than 12 months later, that forces you to focus on very kind of short term tactics, short payoff tactics.

Yuriy Timen (00:43:28):
And so things that SEO, there was no room to think about that for early stage companies. Because payoff is going to come maybe in 12 months in terms of meaningful payoff. We care about getting to the next round and maximizing our valuation between now and then. SEO is for the grown up companies. When we're that we could think about it. And they were getting the reinforcement from everywhere, from peers, from VCs. It's like it's growth, growth, growth. The growth at any cause.

Yuriy Timen (00:44:02):
I think what happened now and we'll see where things stabilized because I think we're still in the midst of a little bit of chaos. What's happening now is the same VCs are saying, "Okay, it's now survival." You have to extend your runway, minimize burn, high burning if you have to. And all of a sudden growth, whether explicitly or via inference becomes kind of a secondary objective, especially for all these companies that are far from being cash flow positive. They have to figure out how to stay alive, but not have to go back to the market and be sort of a victim of shitty terms. And so I feel this is me extrapolating because venture capitalist didn't actually tell me this, but I'm extrapolating that growth is a secondary objective now. It's really focusing on sustainability due to economics, accepting your runway control your destiny, getting to default life.

Yuriy Timen (00:45:00):
And all of a sudden it's like, "Okay. Plus paid is a lot less attractive now. Can't afford to be acquiring users at like LTV cap one to one." That's now a no-no. And so SEO is now becoming more attractive because once you got your burn under control and you're thinking, "Okay, we saved all this money by reducing our paid budget. We're cutting it entirely. How do we put some of those resources back to work?" And all of a sudden SEO starts looking a lot more lucrative because it's almost like you took the urgency of grow at any cost in the next six months, you took that out of the equation. So now it's like we're in a position where we don't have to go back to raising 12, 18, 24 months. We have 18, 24 months worth of runway and now companies are starting to think more in terms of building more sort of sustainable and defensible growth initiatives.

Lenny (00:46:02):
Fascinating. And as much as people may want to do SEO, like we talked about earlier, doesn't mean they will be able to pull it off because there's these things that have to be approved for your type of company and-

Yuriy Timen (00:46:12):
Yes.

Lenny (00:46:12):
Yeah. Going back to point you made earlier about paid being a really interesting opportunity right now because it's become harder. Would you say generally you're kind of like pro, tri paid, go paid be in this time because I'm finding a lot of startups are like, "Oh, we can't do paid anymore. We're trying all these other approaches to grow." Is that like alpha right now? Start thinking about paid in a creative way and maybe this is going to be a huge advantage.

Yuriy Timen (00:46:35):
So there are two pieces to do paid. I mean I'm oversimplifying, but I think people will hopefully appreciate the over the oversimplification. Number one, because it actually drives returns at efficient unit economic, whatever that may mean for your company, your business, your industry. The other way to do it is because it's a very quick way to get learnings on messaging and positioning on designs on features. You're thinking of launching et cetera, right? It's hard to get faster learnings at scale than A/B testing headlines, Google search or whatever. I think the problem that I find is when a company can't have which camper in or where they try to say that they're in both, but really it's like, "Okay, you're funneling a hundred K a month." It's super inefficient and they're not even running experiments to actually get the learnings. I can assess the company, even if I don't download the industry as well, based on just seeing their funnel performance, their conversion rates, their retention curves, their LTDs, understanding their churn.

Yuriy Timen (00:47:43):
I could say whether they stand the chance at making paid work as a former strategy. So not just the learning mechanism, not just the kind of a feedback engine, but actually a profitable at delivering acquisition channel or strategy. And if I see that they're not there because the funnel doesn't convert well, the users don't retain the LTDs are too low. Then I say, "Hey, it's not time for paid. Maybe car on a little bit of budget if you want to quickly test positioning and things like that. But it's just too soon." But instead I encounter a company that's really healthy conversion rates, strong LTDs. I do a little bit of competitor research and I can see where the opportunities are, which channels are less saturated than others. Then I may say, "Hey, it's worth it. It's worth a go." And also just seeing the bigger picture of their financial health, how much runway do you have? What does your monthly burn look like?

Lenny (00:48:41):
Right? Because paids like cash going out the door and it will return hopefully at some point might be six months might be a year, and so that's a real constraint. You mentioned onboarding and funnel conversion. Two questions there. One, do you have a heuristic of here's good for conversion rates? Is there something that you think about there that you could share or is it very case dependent?

Yuriy Timen (00:49:03):
I think it's case dependent, but yeah, it is. It's not case dependent. It's category dependent. So it's not that every company is so case, but it's like, we got to know about what buckets we're talking about. I will say that... Let's say we talk about prosumer premium SAS, ala Grammarly, ala Canva, Whimsical, InVideo, things like that. Yeah. I can confidently say a healthy website visit to a free user, a free account creation conversion rate. It's probably in that 20 to 35% range.

Lenny (00:49:43):
From landing on the site to signing up?

Yuriy Timen (00:49:45):
From landing on site to a free user at scale. Earlier stage, you have strong product market fit with some kind of small audience segment that conversion can be 40 to 50%, but as you go broader, it'll probably asymptote at like 25, 30%. What about a conversion if you're premium from a free user to a premium account or paying account? I think anything under 5% is not going to work long term, regardless of how big your top of funnel is. You may get the soft point, but for you to remain an independent company continuously growing pre IPO, I don't think it's going to happen. It's got to be north of 5%, ideally like more than 7%.

Lenny (00:50:39):
Wow. Super handy. On the onboarding point, what's your thoughts on investing in onboarding and that part foe of how often is that a fruitful area of investment?

Yuriy Timen (00:50:49):
Almost always. A lot of my work is in that sort of a prosumer space. So the products tend to be more complex. Airtable, whimsical, Canva, InVideo. They're very robust products. And so it's very easy to get lost in their editors. I think what all of those companies are trying to do for their respective verticals and use cases is they're trying to democratize access to fades that previously you have to rely on professionals for. Maybe in the case of bayer team bot, it's your engineers. In the case of PM bot, it is professional graphic designers. In the case of a video, it's professional video editors. So when they're trying to democratize access, but they're also trying to make the products robust enough to be comparable to a professional great quality. And it's a very difficult place to play it, right? It's like, how do you make it simple enough where a nonprofessional can use it, but robust enough where they go and say, "Oh yeah, this is as good as if I would've hired a professional fill in the blank."

Yuriy Timen (00:52:19):
And that's where onboarding, sorry for the long answer. That's where onboarding is really, really important because there's such a huge difference between landing someone on that initial editor page, be it Airtable, Canva having that left to their own devices versus getting as much information or as much relevant information front and then customizing that landing experience for them. So that if they're there to do X and we know XYZ about them, we're able to guide them and not expose them to the robustness of the product all at once. So the short answer is almost all the time onboarding is a big opportunity.

Lenny (00:53:04):
Awesome. That's what I was expecting to hear, to give folks some context. What's kind of an order magnitude that you've seen improvement on onboarding and maybe impact on a company improving onboarding.

Yuriy Timen (00:53:15):
Earlier stage companies where still haven't really approached the local maximal, but you haven't experimented with a ton of things. I mean, you can two to four X activation rates easily through onboarding. I think later stage companies like maybe Series B beyond, I think you can still probably get to 20 to 30% lift at activations. It depends on how many low hanging fruit are left to tackle.

Lenny (00:53:46):
That makes sense. Yeah. Till the onboarding, there's always money in the onboarding banana stand. On that kind of same idea, do you have a general feeling of investments in this stuff often pays off and helps you grow and is often higher ROI and investments in bucket B are rarely successful. What would those two buckets be?

Yuriy Timen (00:54:07):
So thinking of investments rawly, right? Not just monetarily.

Lenny (00:54:13):
Yeah. Yeah. Time and resources.

Yuriy Timen (00:54:15):
Yeah. I mean, I would say that getting to know your customer always pays off. So it's user interviews and getting to know your market, your customers, and your prospects always pays off. Customer research, inside surveying, interviewing panels incredibly useful. And I found that to be very especially early stages. The amount of clarity at momentum that it can create inside of a seed Series A up to Series B company when you first do some proper research push. The way it can galvanize the team and give them focus and clarity and purpose is remarkable. So that always pays off. What doesn't pay off? I mean, I think over reliance on paid, it comes to bite you in the rear end. When I think about tracking an attribution, I think it's a question of the right level of investment at the right stage.

Yuriy Timen (00:55:19):
Rarely do companies get it right. They usually fall into one of two buckets where they underinvest in attribution and they are now, their budgets are up high. They have a broad channel portfolio and they have a hard time figuring out what's working, what isn't and they just get into this inertia. It's like, "Well, overall, the company's been growing and it's been growing roughly over the same time that we've been increasing our spend. We're scared to break it. So we're just going to keep spending." Or companies that read horror stories about other companies overspending. They sometimes try to invest in attribution too much, believe it or not where they're trying to get everything perfect and scientifically pure. But what they don't realize is that the payoff may not always be there. And so how do I fit this into your question of, I think tracking attribution incrementality is definitely a worthwhile investment arena, but it could both be a good or bad depending on the level. So you got to make sure the level investment is appropriate for your stage when you stand to aim for-

Lenny (00:56:35):
Awesome. You're such a good interviewee that you come back to the question.

Yuriy Timen (00:56:39):
No, that I promise.

Lenny (00:56:40):
That was great. Okay. One last question. Before we get to our very exciting lightning round. I'd love you to get your thoughts on advertising on TikTok and YouTube and broadly is there any other tactics, avenues that you think are kind of underutilized or emerging that folks should be thinking about?

Yuriy Timen (00:56:58):
Yeah. So TikTok, one thing I'll say about TikTok is I'm seeing it come up more and more as a channel that works well. And sometimes even the most efficient channel, most efficient digital channel for some brands. But I think that the thing about TikTok that oftentimes I was surprised about is you often hear, "Oh, TikTok that's for the 15 to 22 year olds." I'm bad with my gens Z and oh, my audience is different. So I'm just going to ignore the champ. TikTok has so many users and it's still so relatively unsaturated with advertisers that your audience is on there. You'd be surprised.

Yuriy Timen (00:57:46):
I've worked with brands that their core demo is like 40 plus married making 200K plus in household annual income. And you wouldn't think that demo is on TikTok and it is. So what point about TikTok? Other channels, I think out at home is still not getting enough love. Podcasts? Okay. Yep, yep.

Lenny (00:58:14):
Spots through this one. I recall you heard it from Yuriy.

Yuriy Timen (00:58:17):
Direct mail, what has happened? They've gotten better with attribution because before a lot of those channels were written off as sort of attribution is just too hard on there and attribution is so good and reliable on digital. So that's that gap that canyon that existed in attribution capabilities of online and offline, deterred a lot of people from offline. Today offline has gotten better and actually positioning themselves as being able to do attribution, but also online attribution is deteriorated. So all of a sudden that argument kind of slimmed out a little bit and I'm seeing offline get a lot more traction and in podcasts, especially are actually very, very performant for a lot of brands. Those are a couple of things that come to mind.

Lenny (00:59:11):
Those are great. Happy to hear the podcast piece. Excellent. And then I actually, I'm an investor in a startup that Databig at a home campaign and they just told me that it was a 10 to one positive ROI on the deals that they got out of it. So I've been seeing that too, and that's such a good point that the measurement and attribution online has come down where it maybe makes more sense to try stuff like that. Amazing. All right. Are you ready for our very exciting lightning round? I'm going to ask you five questions I think, and then just, yeah, let's go through it quick.

Yuriy Timen (00:59:44):
Let's do it.

Lenny (00:59:45):
Let's do it. Okay. What are two or three books that you recommend most to other people?

Yuriy Timen (00:59:50):
Ooh, that's something that I think is very wrong to recency bias, right? It's like, what are some of the books you've read recently that you've enjoyed? But I would say there are a couple of books that stuck with me over the years. I think on the business side, where on the business side productivity side, it's a book called Essentialism. I forget the author's name. I think his last name is McKeown or something. And it's basically the book about cutting out the noise and finding a singular focus and doing that really well. It's a book that was a game changer for me at Grammarly being sort of new in my career, having really aggressive goals, not being scared to say no. Taking on a lot, just feel it thinking like, "Well, I'm only working 12 hours a day. There's 12 more left. I can do it."

Yuriy Timen (01:00:45):
And then when you end up stepping into a leadership role, which happened for me, I mean, that happened prior to grounded, but really I was able to grow into that role at Grammarly. That book was incredible and I used it a lot. I pretty much got copies for everybody on the team, like 40 plus people. So that is a book I swear by.

Yuriy Timen (01:01:06):
I read a lot outside of work and business. So I don't know if it's appropriate, but I'll say that. It's Frankl's, A Man's Search for Meaning is just a remarkable memoir on perseverance and I think that biggest takeaway is you can't control what's happening around you, but you can control your reaction to it. And then I'd say the book that I read recently, because I was very affected by the Russia invasion of Ukraine. I'm originally from Ukraine. I believe you are as well. So it hit very close to home and there have been a lot of references drawn between the President's Zelensky and his response in the war and Winston Churchill's response in 1941 when Hitler started marching through Europe. And so I read a book called I think The Splendid and the Vile by Eric Larson.

Lenny (01:02:02):
Yeah. I read that. I read that.

Yuriy Timen (01:02:03):
Did you also read it since the invasion?

Lenny (01:02:06):
No, it was before that, but I totally get that now.

Yuriy Timen (01:02:09):
Reading it right now because I've been following the conflict very closely, but for people who haven't followed the conflict or maybe have only followed the rush, the war kind of in a cursory way, you can put what's happening into historical context remarkably well. So I feel like that book accomplishes two things. Number one, it's like you learned something about not so distant history that maybe you didn't know, which was about Great Britain and Winston Churchill kind of courageous response in the face of Hitler's invasion of Europe. But you also can draw so many parallels to what's happening today. And hopefully that helps us understand what's at stake, not to end on two grandiose of a note.

Lenny (01:02:57):
We'll go less grandiose quickly, but I will add one thing that stood out in that book that is also true in the Ukraine is how during the fire bombing of Britain, people are just going out every day, going to clubs, still having-

Yuriy Timen (01:03:09):
I know. Steal them their life.

Lenny (01:03:11):
And same thing even today in Ukraine is.

Yuriy Timen (01:03:14):
And not just keep, but it's very life.

Lenny (01:03:17):
I love that. Okay. We'll move on to less, less serious stuff maybe. What a transition to, what's your favorite other podcast?

Yuriy Timen (01:03:27):
Honestly, there's only one other podcast that I'll listen to right now because I've just been so consumed. I listened to a lot of live streams and read a lot about the conflict, which has taken up so much of my head space. That's not work related, but I would say that the All in Pod. I feel like it's a cool way for me to just catch up on everything that's going on through their unique filter.

Lenny (01:03:50):
Yeah.

Yuriy Timen (01:03:50):
That's probably the-

Lenny (01:03:52):
Cool. Yeah. I learned a lot.

Yuriy Timen (01:03:53):
Yeah.

Lenny (01:03:53):
I learned a lot from that one. That's so much drama on that show. Okay. Great. Favorite recent movie or TV show. Anything stand out.

Yuriy Timen (01:04:00):
So that's another thing. Since February I've watched nothing. My Netflix skew just keeps growing because they keep emailing me saying this new season is out. I'm like, "Oh yeah. I used to that show. Let me add it to the queue." I mean, recently I had some downtime. The kids were with grandma, so I watch movie Hustle with Adam Sandler.

Lenny (01:04:22):
Love that. So good.

Yuriy Timen (01:04:23):
Yeah. It was good. It was it's very light. It's not like a movie that's going to make you think a lot, but it was just good old entertainment. Yeah.

Lenny (01:04:31):
I like that. I like that summary. Yeah, it was so delightful. Maybe one more question. Who else in the industry do you most respect as a thought leader? Maybe someone people may not know or if anyone else comes to mind.

Yuriy Timen (01:04:43):
That's a very good question. So I would say first off, I do believe that some of the brightest minds, honestly, in any craft are people that you never hear because it takes a certain personality, energy, and probably a lot of other circumstances to invest in your personal brand. And also it's very hard to do that while still staying relevant as a practitioner. I mean, when I think about myself two years ago before starting advising, I was just kind of living in my Grammarly cave. And I felt like I was probably at the top of my craft, but I didn't have time to pick my head up or not, maybe not even just tie, but I didn't know where to start to pick my head up and do something like this. I would say some people that, I mean, I mentioned Ethan in terms of SEO. SEO and just organic growth loops and content as a growth engine, he is best in class.

Yuriy Timen (01:05:49):
Who else? So Mark Fisk, he shows up in the Reforge chats a lot. He was leading growth and marketing at Credit Karma for a while. And right now he's an investor I think at the HRG Capital, but he is a really, really strong thought leader on all things, performance marketing attribution, and just kind of paid acquisition at large. Those are two people that I make sure I... And there are others of course, but those are two who I make sure I stay in touch with at least on a quarterly basis because any casual catch up just yield so many unique nuggets.

Lenny (01:06:25):
Amazing. Where can folks find you online if they want to reach out, learn more and how can listeners be useful to you?

Yuriy Timen (01:06:31):
Honestly, I don't have a very strong online presence. I would say LinkedIn is probably the only place where I seek things the recent, so folks can find me there. They can also find me inside of Lenny's Newsletter. I do. I do. I do, but you can appearance there once in a while and on that's odd.

Lenny (01:06:53):
True.

Yuriy Timen (01:06:54):
How folks can be helpful to me, honestly, promote and shout out of Lenny's Newsletter and Lenny's Pod and that if you're building awesome things, come talk to me. I always carve out some amount of time in my life just for noncommercial things, just to have conversations with founders and spent 30 minutes with them on a phone, expecting nothing in return and maybe save them some time from making some of the mistakes that I've made and help direct them on a more path. So it's about it.

Lenny (01:07:27):
Amazing. You are awesome. Thank you so much for making the time to do this. I learned a ton. I can't wait to get this episode out. There's just so much meat to this thing,

Yuriy Timen (01:07:36):
Dude this was good.

Yuriy Timen (01:07:37):
I feel like my nervousness was unfounded. This was super organic. You are just as welcoming as you are outside of the pod. So yeah. Thanks for having me.

Lenny (01:07:50):
Thanks Yuriy. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

---

## Lessons from Airtable’s unconventional growth strategy | Zoelle Egner
**Guest:** Zoelle Egner  
**Published:** 2023-01-29  
**YouTube:** https://www.youtube.com/watch?v=0P8LMyeYl1U  
**Tags:** growth, retention, acquisition, metrics, mvp, experimentation, funnel, conversion, hiring, culture  

# Lessons from Airtable’s unconventional growth strategy | Zoelle Egner

## Transcript

Zoelle Egner (00:00:00):
There is sometimes a recommendation or an instinct just like, "Ship things super, super quickly and get them out there." And I'm not saying don't move fast. Obviously you need to move fast in the early days, but make sure someone rereads your email so that it sounds good. Invest in having a decent photo or a decent illustration. If you have sample content, this is actually a big one, sample content for your productivity app as an example. Take the time to not have it be like Jane Doe 12 times in the name list. Have it be references to your industry so that people are like, "Oh, hey. That's a joke about Steve Jobs. I'm a designer. This person is thinking about me."
(00:00:35):
It's small stuff, but it tells that person, like, "The people who worked on this were thinking about me as a customer, they built it with me in mind, and that means that it is more likely that this is going to fit my needs than something generic." And that builds up both the brand trust that we've talked about, but also the personality of the company, and makes people want to root for you. And frankly, when you are small, you need everyone rooting for you that you can possibly get.
Lenny (00:01:02):
Welcome to Lenny's Podcast, where I interview world-class product leaders and growth experts to learn from their hard won experiences building and scaling today's most successful companies. Today my guest is Zoelle Egner. Zoelle was one of the earliest employees at Airtable, where she led their early marketing and customer success teams, and generally just helped Airtable grow into the legendary business that it is today. She also spent time in Box. She's advised dozens of startups on marketing and growth, and is now head of marketing and growth at a startup called Block Party. 
(00:01:32):
In our conversation, Zoelle shares how to punch above your weight as a startup, the most effective and impactful growth and marketing tactics throughout Airtable's history, including their use of billboards, marketing investments that are often high ROI, and those that are rarely a good use of time, why PR and launches are actually useful to startups, and also when they aren't, and a lot more. It was so much fun chatting with Zoelle, and I'm really excited for you to learn from her. With that, I bring you Zoelle Egner after a short word from our wonderful sponsors.
(00:02:03):
Today's episode is brought to you by OneSchema, the embeddable CSV importer for SaaS. Customers always seem to want to give you their data in the messiest possible CSV file. And building a spreadsheet importer becomes a never ending sync for your engineering and support resources. You keep adding features to your spreadsheet importer, the customers keep running into issues. Six months later, you're fixing yet another date conversion edge case bug. Most tools aren't built for handling messy data, but OneSchema is. Companies like Scale AI and Pave are using OneSchema to make it fast and easy to launch delightful spreadsheet import experiences, from embeddable CSV import to importing CSVs from an SMTP folder on a recurring basis. Spreadsheet import is such an awful experience in so many products. Customers get frustrated by useless messages like, "Error on line 53." And never end up getting started with your product. OneSchema intelligently corrects messy data so that your customers don't have to spend hours in Excel just to get started with your product. For listeners of this podcast, OneSchema is offering a $1,000 discount. Learn more at oneschema.co/lenny.
(00:03:10):
This episode is brought to you by Pando, the always on employee performance platform. How much do you love the performance review process? Yeah, it's time consuming, subjective, biased, and there's rarely any transparency. With the rapid shift to distributed work, it's a struggle to create the structure and transparency that you want to help your employees have the highest impact and growth in their careers. Pando is disrupting the old paradigm of performance management, including a continuous employee-centric approach, so employees stay engaged, see their progression in real time, and know exactly when and how they can level up. With Pando, managers can leverage competency based frameworks to effectively coach and develop their teams and align on consistent growth standards resulting in higher quality feedback and higher performing teams. Visit pando.com/lenny for more info and get a special discount when you sign out and reference this podcast. That's pando.com/lenny. Zoelle, welcome to the podcast.
Zoelle Egner (00:04:12):
Hi, thanks for having me.
Lenny (00:04:14):
It's very much my pleasure. Something that is pretty cool is that we actually met in my newsletter Slack community. I actually looked this up of how we actually started chatting, and it was me cold DMing you to get a discount on Airtable for the newsletter subscribers. And you very happily got me that, hooked us up, and then you became a go-to Airtable person for advice on what Airtable did right and wrong over the years. And so thank you for being that person and also I'm really excited to have you on this podcast and to learn from you.
Zoelle Egner (00:04:43):
I am super excited to chat.
Lenny (00:04:45):
Awesome. You're probably best known for your time at Airtable, which, correct me if I'm wrong, you're employee number 11.
Zoelle Egner (00:04:53):
That's right.
Lenny (00:04:55):
Okay, and at Airtable you led marketing, you led the customer success teams, so we're going to chat about all that stuff. But before we get into that, I want to chat briefly about this other project that you worked on, that from the outside felt like a really fascinating thing, and a really impactful project, and a really cool team. And it's called Vaccinate California, I think, is that how you pronounce it?
Zoelle Egner (00:05:13):
Mm-hmm.
Lenny (00:05:13):
See, I just-
Zoelle Egner (00:05:13):
VaccinateCA.
Lenny (00:05:15):
VaccinateCA. Okay. Could you just talk a little bit about what this was? What were you trying to do? What was the impact you had? How did it all go?
Zoelle Egner (00:05:21):
Yeah, absolutely. So VaccinateCA existed to help people in California find and get a COVID vaccine as quickly as possible, and that sounds really trivial right now, but you have to wind back to January of 2020, when vaccines were first coming out, and it was really hard. So just as a reminder, because most of us have blocked that from our memory. 
Lenny (00:05:40):
Yeah.
Zoelle Egner (00:05:41):
The federal and state systems didn't really exist yet, and so everything was this horrible hodgepodge, where eligibility depended on not only what state you were in, it was down to the county, and even sometimes the individual facility. You would be at a Walgreens, and talk to them, and they'd be like, "Oh, you have to be over 65, and also in one of these 12 categories of employment in order to get the vaccine." And then you'd go a mile away and they would tell you something totally different. So people would stand in line for hours. There were phones going off the hook, utterly madness, and really, really scary for a lot of people who were trying to figure out how to keep themselves safe. 
Lenny (00:06:17):
Yeah, I remember those days well.
Zoelle Egner (00:06:19):
Yeah. So this organization was founded essentially by a tweet by Patrick McKenzie, for those of you who are on Hacker News Patio11. And he had basically this really simple premise, which is, "If you call a pharmacist, and you ask them who they can give a vaccine to, and what vaccine they have, and then you put that answer on a map, someone else doesn't have to make the same phone call. And that takes lots of pressure also as a healthcare system and also helps people to match supply and demand." 
(00:06:47):
So surprisingly, somehow, that tweet, which is essentially like, "Call people, put in spreadsheet, put online," turned into an entire, full nonprofit that was mostly on Discord, Zoom, Airtable, and not only had this entire hundreds of volunteers who were making phone calls in the state of California and eventually, actually, nationally, we became Vaccinate The States eventually, we were also doing this thing called web banking. So we would go and scrape all the official sources as they started coming out, and then validate them because they were not always correct. And eventually we had the most comprehensive database and map of locations in the entire country, including more comprehensive than the federal government and most of the states because they had really complicated limitations on what they could and couldn't publish based on some relationships they had. We didn't have those limitations.
(00:07:37):
So it meant that we became this clearing house, essentially, for this information and we built an API. We were working directly with Google. And if you ever looked up vaccine locations on Google Maps, that was us feeding that to them, which was really cool. And we also made maps you could see on county websites, so it would help you understand what was available in your area. One of the coolest things that I've ever worked on.
Lenny (00:08:01):
Okay, exactly. That's exactly I imagined how epic this was. Just to make sure people understand what you're describing, basically you had hundreds of people sitting there on phones calling vaccine locations, getting the specifics of who is able to get a vaccine there, and then just giving people a pointer of where they can get a vaccine.
Zoelle Egner (00:08:18):
Exactly. So I came in initially, a colleague of mine at Airtable had been helping out with the building out of the backend. And they started getting media attention. And they thought, "Oh, well this will help more people understand that this resource is available." So I got brought in to do some PR help, basically help them figure out how to get the word out, and then ended up actually quitting my job at Airtable to work on it full-time.
Lenny (00:08:40):
Oh wow.
Zoelle Egner (00:08:41):
Yeah, I was on the board and also managing all outreach and other stuff. So we did lots of really cool education, helping people understand their eligibility at all. Built a bunch of fun tools for that as well, but it was a pretty incredible six months, where we filled a really critical gap in the infrastructure of the country. 
Lenny (00:08:58):
It's wild that was the best solution, is just call people and create your own. 
Zoelle Egner (00:09:03):
You know?
Lenny (00:09:03):
I imagine there was, at Airtable, were you using to store the data?
Zoelle Egner (00:09:07):
Oh yes. 
Lenny (00:09:07):
Okay.
Zoelle Egner (00:09:07):
We built an entire insane database, and then eventually custom software on top of that, to make the people who are making the phone calls more easily get the information in. It was a whole thing. Very cool to see, though, not just tech people get involved. We had, in our volunteer base, people from absolutely every walk of life, not just in California, globally. I remember there was a volunteer who said that he decided to join, he was based in Israel, and he had had no trouble getting the vaccine whatsoever, but seen something on Twitter about it, and just decided he wanted to make sure that people were able to get the vaccine as easily as he did. And he spent dozens of hours calling folks, even though he was in a totally different time zone. But really lovely to see all these different people, retired teachers. I think we had a bunch of 12 year olds who were helping out on the code, of all things, all who just really wanted to make sure that they could keep their community safe.
Lenny (00:10:02):
What happened with this organization? It's a nonprofit that now continues to run or what's happening?
Zoelle Egner (00:10:06):
No, we did something which is not common. We actually decided to shut it down after six months. Partially, that's because the existing system finally caught up. And frankly we didn't want to be in a place where we were pulling away resources that could be put towards other things that are going to be more impactful. We always saw ourselves as a stop gap, and once we got to the place where we felt like we weren't really being additive, we wanted to get people's time back, so they could work on other things. So it doesn't exist anymore. I think you can still go check out the archive. We found some researchers who are doing interesting research on it, because there's very fascinating data in there about the equitability of some of the distribution of the vaccine based on where it was available, but the organization is gone. We had that beautiful moment in time and have all moved on. Hoping we don't have to get the band back together, because hopefully it's not necessary anymore.
Lenny (00:10:58):
Oh, man. I'm watching The Last of Us right now about this-
Zoelle Egner (00:11:02):
Mushroom people.
Lenny (00:11:03):
... mushroom based disease, and that scares me now. 
Zoelle Egner (00:11:06):
Yep.
Lenny (00:11:06):
Anyway, on this podcast I try to get to things people learn from these experiences, and so I have to ask what you learn about forming something like this, just ad hoc, pulling a bunch of people together, and having them focus, and get things done, or just scaling it, or even shutting down. I guess what have you taken away from that experience that you maybe will bring to either future one-off things like this or even just your work in general?
Zoelle Egner (00:11:31):
Yeah, I'd say probably three things. One, the incredible power of a simple idea to bring people together. One of the reasons why VaccinateCA was so powerful and got so many people to help is everybody immediately understood why it would be useful and how they specifically could be making a difference. And combining those two things was an incredible way to bring a lot of people on board very quickly, because from a messaging perspective, messaging, something very important to me as a marketer, it was so concise. Like, "Pick up phone, help save lives." Really straightforward. People really, really got that. It allowed them to feel like they had agency in a time when everything felt really, really out of control. I think there's a lot of opportunities we have to activate our communities and give people that sense of control that are both going to be helpful more broadly for society, but also just for those individuals as well to make them feel a little bit more safe, a little bit more like they can actually have a difference in things. 
(00:12:34):
I think in tech we often don't jump into these problems. This was not sophisticated technology. It was phones, Discord, and Airtable mostly being used like a spreadsheet. It wasn't anything wild. Even that very simple infrastructure was enough to make a huge difference. And we have some evidence that we saved a lot of lives as a result of it, which is pretty special. I think part of it is also just saying, "We don't have to be hesitant to jump into these problems. It's important to engage with experts in the field, is not to say that tech solutionism is always the answer." And again, this is not super sophisticated technology, but because we were able to go in and talk to the people who are actually affected, get into the system that already existed, and make something really simple, really fast, it actually did have a huge difference and that's really exciting.
Lenny (00:13:24):
Just to double-click on that one, actually reminds me, some founders of companies I've invested in, I often hear how much easier it is for companies that have a mission that people are excited about for them to hire versus companies that don't. And so it's a really good reminder of just the power of having a mission and a vision that is really compelling to people versus some B2B software that people aren't [inaudible 00:13:47] excited about, even though there's a great reason to have great B2B software. Love B2Bs.
Zoelle Egner (00:13:50):
There are. I love great B2B software. I've spent most of my career on it. But I agree with you. I think if you have an authentic mission and people aren't just like, "Oh, sure, okay. You're connecting the world." But really it's some telephony startup. Like, "Okay."
Lenny (00:13:50):
Yeah. 
Zoelle Egner (00:14:05):
If people feel like it's genuinely authentic to what you're building, it can be incredibly meaningful.
Lenny (00:14:11):
Yeah. I just remember a founder who, he is a second company, because the first company did not have an amazing mission. The second one did. And like, "Wow. So much easier to hire for this new startup."
Zoelle Egner (00:14:20):
Yes. 
Lenny (00:14:20):
So totally get that. 
Zoelle Egner (00:14:20):
Absolutely. 
Lenny (00:14:22):
Okay, number two and three.
Zoelle Egner (00:14:23):
Number two and three, I'll try and be more brief. 
Lenny (00:14:25):
It's all good.
Zoelle Egner (00:14:26):
Number two, I would say just the importance of relentlessly repeating the exact same stuff over and over again, even if you feel like everyone definitely knows. This is something that I've seen play out in every single leadership role that I've had, but it was never more acute than here, particularly because we had this broad coalition of hundreds of people with very different backgrounds. Some people coming to the meeting, some people not, whatever else. I think I repeated the same three talking points about why what we were doing mattered 5,000 times. Cannot overemphasize how many times I said the same stuff, and so did every other member of the board. It really is important and people will fill in the blanks with totally wild things if you don't continuously have that discipline of repeating yourself. You just have to get used to saying the same stuff. And if you do it correctly, it's super motivating. Even if you're sitting there being like, oh my gosh, "I have to say it again." it's worth it.
Lenny (00:15:22):
This reminds me, I don't know where I saw this, it's just in my head right now, that the CEO and founder's job, their actual title is repeater in chief.
Zoelle Egner (00:15:22):
It absolutely should be.
Lenny (00:15:31):
It resonates. Yeah.
Zoelle Egner (00:15:31):
I've worked with some leaders who never wanted to. They're like, "No, this is going to be boring for people." And you just have to be like, "Honestly, most people are never listening as much as you think that they are."
Lenny (00:15:39):
Yeah.
Zoelle Egner (00:15:39):
"We wish that they would. But you have to say it 12 different ways in writing, and out loud, and all this other stuff. You're never as important as you think you are, unfortunately, when it comes to that." 
Lenny (00:15:48):
Oh, these are great lessons. Okay. What else do you tell? 
Zoelle Egner (00:15:51):
I think my last learning was really about the power of having a laughably small MVP for something. By the end of this, we were covering the entire United States. We had an API, we had custom software on the front end, this whole behemoth of stuff that we got to in four months or something. In the beginning it was truly, basically, a spreadsheet, and phones, and that was it. Even that, for the first few weeks while we were getting the rest of the infrastructure really going, not only had tremendous impact at one of the most important parts in the pandemic, but also gave us so much information about we actually needed to build that was going to be helpful. And I remember having all of these assumptions about what was going to be necessary to manage this coalition of people to make sure that we had really good data quality.
(00:16:41):
Because one of the most important things you can do if you're trying to be a trusted source of truth is actually have the correct information. Sounds trivial, it's not at all at that scale. And I was totally wrong about all my assumptions. I thought we were going to have to have totally different types of oversight. I thought we were going to have totally different tooling. And it turned out we could do something way lighter weight that would allow us to move much faster as the regulatory landscape kept changing, as all the rule making at individual places kept changing. And that agility, that willingness to do just the smallest possible thing is obviously a little bit of a trope in the industry. 
(00:17:15):
People talk about it a lot, but it's never been driven home to me so much, because we're talking about something that had incredibly high stakes as people's health, and we're still able to do it in that context. So if we could do it there, you can imagine that the applications of that in other industries are just tremendous. So yeah, if you're listening to this, and you were thinking maybe you needed to add more stuff, I bet you could prune.
Lenny (00:17:39):
And it's nice to have the forcing function where the world is changing so quickly and the team's probably small, where you are forced to build small. Which I think is why this reminder is so important. Oftentimes you have more resources, and you end up building more just because you can. And yeah, what you're saying is oftentimes, "It'll shoot you in the foot."
Zoelle Egner (00:17:55):
Yes.
Lenny (00:17:56):
Amazing. I didn't expect to get into this much detail with VaccinateCA and so I'm glad we did. Let's zoom out a little bit, and just fill in some gaps on your background, briefly. Can you just highlight some of the other wonderful things you've done in career? Airtable, we talked about, VaccinateCA, just broadly, what else have you been up to? 
Zoelle Egner (00:18:13):
Yeah, absolutely. Okay, so I'll try and be brief. I worked in tech for more than a decade, mostly marketing and customer success, a little bit of ops. Before I got into tech, I was a little bit of a dilettante, so some non-profit, healthcare, dying big box retail, because I graduated right into the recession and I was certain no one would hire me. Turns out that was actually wrong. But on the plus side, now I know what dysfunction looks like at great scale, which is actually quite an education and very useful. But I always knew I wanted to get into tech, partially because I'm from the Bay area, and partially because I had been obsessively power mapping the industry, and looking at its flocking patterns, and who had what types of influence, because I'm a nerd. And I really wanted to see if I could get in, in the first place. Because- 
Lenny (00:18:59):
Wait, can you talk about this, which, what is it you did? What did you call, a flocking pattern?
Zoelle Egner (00:19:05):
Sure. You can imagine in any community, there are nodes of influence, people who know a lot of folks, they have money, whatever it might be. And they're able to direct how that community or that ecosystem evolves. In the tech industry, typically VCs will often play a role in this, but so will certain types of executives. And you can follow how they move between different companies, and who they worked with, and then see that influences who gets investment in the future. It influences the different partnerships that evolve. It influences the assumed wisdom in various different careers. And because I'm a big old nerd, I was literally drawing diagrams based on-
Lenny (00:19:48):
Whoa.
Zoelle Egner (00:19:48):
... reading people's blog posts of who was influential in what way? Because I was non-technical. I tried programming, and I hated it, frankly. And so I was like, "Okay, it's 2010, it's 2011. There's not clear ways to get into the industry as a non-technical person. I need to figure out how to do this with people. Because otherwise I'm not sure why someone would take a chance on me with what I have done historically. And that sounds a little insane, but it's very effective. And I ended up getting my start in tech basically by identifying a company where I thought I had a unique set of connections or understanding of the space that they were working in, where I thought I could maybe email the CEO and be helpful.
Lenny (00:20:29):
And did this connect to that diagram you drew? Did this help you point in that direction?
Zoelle Egner (00:20:34):
Yeah, absolutely. So I was closely tracking YCombinator and that whole ecosystem. So I knew I wanted to find a smaller company, where they maybe were having more difficulty hiring, because they were less well known or a little bit less, I don't know, sexy. But while they were still connected into that broader group, because it has with a pedigree that people would take you seriously if you had worked at a YC backed startup.
Lenny (00:20:55):
Right.
Zoelle Egner (00:20:55):
Anyway, I got really pointy hat strategic about this, but it was effective. 
Lenny (00:21:00):
Do you still-
Zoelle Egner (00:21:00):
And-
Lenny (00:21:00):
... have this diagram, by the way? It'd be so funny to look at it right now.
Zoelle Egner (00:21:03):
No, I don't think I have it anymore. I might be able to dig it up, but alas, I think it may have been lost in one of my many moves since then. 
Lenny (00:21:03):
All right.
Zoelle Egner (00:21:03):
It's been-
Lenny (00:21:03):
No problem.
Zoelle Egner (00:21:03):
... more than a decade. 
Lenny (00:21:18):
Okay. I imagine that was true. Okay, so I think I cut you off. You were talking about some of the things you've done in your career.
Zoelle Egner (00:21:20):
Yeah, ended up using my studies of the space to get into a role as employee one at a developer focus YC backed startup. And the funny story on that is that I got that role by cold emailing the CEO while I was still in college. And then he actually followed up with me almost immediately, because I'd offered to introduce him to some professors, which was useful for the type of business. And then I ignored him for two years because I got busy with my thesis, and got other jobs, and whatever, came back to it and wrote this ridiculous apology email, being like, "I promise I respond to emails faster. I see that you're hiring. Would you give me a second chance? Please, can I come work for you? I have no experience that's useful, but I work really hard." And I figured he would either laugh me off of the internet or give me a job, and very fortunately for me, he gave me a job. So thanks, Ryan. Appreciate that. That was how I got into tech.
Lenny (00:22:11):
Thanks, Ryan. 
Zoelle Egner (00:22:12):
Yes, we appreciate it. So that startup got acquired by Box. And when I went over to Box, they had never had paying developers before. So we were bringing over seven figure contracts. So I started developer success programs there. And then in a totally wild shift, I ended up moving over to run their social media editorial and internal comms, which doesn't sound related to developer success, but I had always been a writer, and I wrote this blog post about what it was like to be an early stage non-technical employee. There was a little spicy, talking about some of the challenges, and I didn't tell anyone I was going to do it. And I got this email from PR being like, "We need to have a meeting." And I was like, "Oh, they're going to fire me. I went too far." I thought I was being circumspect, that I went too far. And in the meeting they were like, "Hey, we really think you should apply for this job. We would love to have you run social media." Which is not the outcome I expected.
Lenny (00:23:05):
That's a cool learning, there. Just like, "Do stuff." You know? "Don't be afraid."
Zoelle Egner (00:23:08):
Yeah, it was definitely not the expected outcome, but one that was very exciting. So got to go run those programs for a couple years through the IPO, which is a whole education in and of itself, to see how comms changes when you become a public company. And then I was on Hacker News obsessively at the time, and I saw the beta for Airtable come out. Immediately signed up, and became obsessed with the product, and evangelizing it to everybody that I knew and ultimately ended up figuring out a way to finagle my way into that role as employee 11 there. 
(00:23:43):
And it sounds like we're going to talk about Airtable more, so I won't belabor that, but marketing and customer success stuff, ended up leaving for VaccinateCA, and then the last little bit here is just when that ended, I really thought I wanted to start my own company. So I gave myself a certain window in which to try out different ideas, and at the same time was advising and consulting. Ultimately didn't end up finding anything that I felt so much conviction that it was worth blowing up absolutely everything else about my life in order to go heads down on a company. So eventually decided to go in-house with one of the companies I've been advising, Block Party, and now I run marketing and growth there.
Lenny (00:24:19):
Can you just explain Block Party briefly? [inaudible 00:24:21]-
Zoelle Egner (00:24:21):
Absolutely. We're an online safety company. We help users have more control over their digital experience. And our first product is anti-harassment and anti-spam tools for Twitter.
Lenny (00:24:30):
So you've worked at Box, Airtable, now Block Party. You've advised a lot of companies around marketing product growth. I'm curious if there's a thread that has maintained through all of those experiences in terms of what works well for marketing, and growth, and things you've learned that just consistently- [inaudible 00:24:52]
Zoelle Egner (00:24:52):
A few pieces that go into how I choose companies that create that thread. And part of this is about me wanting to match what I think I'm really good at with what will have the greatest leverage for a company that I work at. I've mentioned I'm a writer, really care about telling stories, and helping people to understand new or novel things. I also really care about product quality. I'm a little bit of a product snob. And one of my strengths is enthusiasm. So if I can't genuinely go to a customer and tell them, "This product is going to solve a real problem for you and it's going to be amazing." I can't do my job. So all of the companies that I've chosen to go to have had this foundation of an incredible product experience that maybe people didn't fully understand, and where I could come in and help connect the dots between that amazing product that's going to be really, really helpful and the opportunities for a much wider range of people to benefit from that.
(00:25:46):
So in practice, what that means is I often end up working at companies that are in a position to really punch above their weight from a brand perspective. They're typically much lower headcount than you would ever expect. They're typically way earlier stage than you would expect, but I've been able to put together a brand or an experience that allows people to invest themselves into the company with a high level of trust, I guess. 
(00:26:13):
I'll be more specific because that's really ambiguous. Airtable, it manages mission critical workflows, highly sensitive data. It's super important. You only use tools you can trust for that type of thing. The same thing is true at Block Party, online safety. You have to trust the company that you're entrusting your safety to. And in my experience, people, and especially founders really underestimate how much every single touchpoint a customer has from word of mouth or the ad that brings them in the door, landing pages, signup flows, customer service experiences. Every single one of those moments is building a brand that is adding or removing trust.
(00:26:48):
So for me in the early days, that means thinking about like, "What are the signals that I can provide to future customers that say, 'We understand you specifically, and our solution is designed for a person like you.' And two, that will say, 'Hey, we're actually operating on a much higher level than you might expect for a company of our size or our stage. We take this really seriously. We have all the things in place to take care of you. So you shouldn't be afraid to spend six figures or put your safety in our hands because we've got your back. We're doing this the right way.'" Has tremendous dividends when you're in a business that is often driven by word of mouth. Because if you take care of people and you follow up that brand experience with a product experience that is really powerful and actually does the things that says it's going to do, then your word of mouth can become a huge driver of growth for the company.
(00:27:40):
Of course, the outcome of this in practice is really funny. So I remember really distinctly having to invite customers to go out to lunch with us when they would come to San Francisco back in the Airtable days, because we had 15 people in a teeny tiny office. It's not that I wanted to mislead anyone, but I didn't need to reinforce the fact that they were spending six figures with us when we had 15 people. If they had gone to look on LinkedIn, they could have figured that out, but we didn't need to remind them that we were so small, and they were running some of their most important processes with our product. I think I was on the phone with Slack at one point. And they were like, "Oh, well you guys are probably about the same size company as we are, right?" And I was like, "Not quite. A little smaller, just an entire order of magnitude, no big deal, it's totally fine. We're all smooth. We'll take care of you. It's going to great." But it-
Lenny (00:27:40):
Amazing.
Zoelle Egner (00:28:27):
... really makes a difference, all of those little things.
Lenny (00:28:31):
That reminds me, I heard stories of very early Airbnb days where they had to take meetings in a bathroom, or in the hallway, and they did interviews, I think in the hallway because there was no space.
Zoelle Egner (00:28:41):
We did a lot of calling from the hallway at Airtable, also from this weird internal patio you could only get to through climbing through a window. The window kept breaking. And so I, at one point, remember someone getting stuck outside trying to interview someone with the windows closed. Utter, utter ridiculous nonsense. But you know, that's all the fun things that happened in the early days before you become bigger.
Lenny (00:29:06):
Yeah, I love those early day stories. 
Zoelle Egner (00:29:08):
Yeah.
Lenny (00:29:09):
I really love the concept of punching above your weight as a startup. What else did you do at Air Table or other places that help you do that? One is just don't let them see how small you are, necessarily. Are there any other technical things you recall that like, "Oh, here's things that really worked really well for punching above our weight as a small company at that point."
Zoelle Egner (00:29:29):
A couple of these things are very unsexy, but very useful. One, make sure that your landing pages, and your emails, and other things have a level of polish that makes them feel a little bit more done. I think there is sometimes a recommendation or an instinct just like, "Ship things super, super quickly and get them out there." And I'm not saying don't move fast. Obviously you need to move fast in the early days, but make sure someone rereads your email so that it sounds good. Invest in having a decent photo or a decent illustration. If you have sample content, this is actually a big one, sample content for your productivity app as an example. Take the time to not have it be like Jane Doe 12 times in the name list. Have it be references to your industry so that people are like, "Oh, hey. That's a joke about Steve Jobs. I'm a designer. This person is thinking about me."
(00:30:20):
It's small stuff, but it tells that person, like, "The people who worked on this were thinking about me as a customer, they built it with me in mind, and that means that it is more likely that this is going to fit my needs than something generic." And that builds up both the brand trust that we've talked about, but also the personality of the company, and makes people want to root for you. And frankly, when you are small, you need everyone rooting for you that you can possibly get.
(00:30:45):
So those little bits of polish that don't take a ton of time are absolutely worth it. The last thing I would say is making sure that in your public communications launches, if you ever talk to press, which some companies can and some companies can't, having more of a point of view than just about your product, you can try and say, like, "We are part of something bigger. Here's the broader circle or movement that we are a part of." It makes it feel more inevitable and more like you're not just self servingly talking about your tiny corner of the world, but that it's actually part of this much bigger trend. It will be more compelling and it feels like you're operating at a different level of sophistication that can be really helpful.
Lenny (00:31:28):
I love that. On the first point, basically, it's attention to detail and obsession with quality is what I'm hearing. 
Zoelle Egner (00:31:34):
Yes. 
Lenny (00:31:34):
Just to make it clear, this isn't just a tiny team just pushing the stuff out. I imagine most founders would be like, "Yes, I would love, we are going to focus on quality. We'll make sure everything looks great." In reality it always is this trade off against other things they could be doing. 
Zoelle Egner (00:31:50):
Yep. 
Lenny (00:31:50):
What do you think folks can do to help keep that level of quality high? Is it just one person being obsessed and just reviewing everything like a founder? Is having someone like you that's just very detail oriented, just review everything? How do you actually execute that when you have 1,000 things to do?
Zoelle Egner (00:32:05):
100%. I'd say there's one of two approaches and you articulated them here. One is you can have the founder that is the avatar of quality, who is just relentlessly being like, "Hey, we're going to do the 15 minute check. Yes, we're going through it. Yes, I'm going to send you a copy of this email, and someone else going to click every link in it, and make sure they're not broken." Or, you can have someone else be the avatar of that who is in the company. I would say in many of the companies I have worked at, that has been me, because I've been the marketing human who cares. But it doesn't have to be a marketing person, it can be someone on product. It can be, honestly, even someone on customer success if you're willing to let them provide their feedback on the way that you're showing up in the world, which you should because they have fantastic insight. There just needs to be someone. 
(00:32:50):
And I think building that into how you interview can be very helpful, as well. So finding people who understand those trade-offs and that balance, and who are willing to put in the extra 15 minutes, but aren't going to spend an extra week trying to obsessively QA everything. You don't want to go that far. Just who has that bent towards detail can be very helpful. Also, just make yourself a checklist. It doesn't have to be complicated. "Every time we put out a blog post, these are the three things we're going to do. Every time we send out an email, it needs to be seen by at least one other person." None of this is rocket science. You just need to make a little process for yourself, and then it can be very fast and lightweight, but the dividends are worth it, I think.
Lenny (00:33:31):
I like how simple this is, just to look like a bigger company, is just pay attention and focus on the little things. It's not a big, whole thing. [inaudible 00:33:39]
Zoelle Egner (00:33:39):
There are some bigger things you can do if you really need to. My favorite silly example of this is Airtable, back in the day, got roasted on Twitter for having billboards that were not super specific about a specific problem or whatever. They were just billboards that we had out. And everyone was like, "This makes no sense. Why are you doing this? We don't understand." They were actually super effective for us because we had a different goal than everyone thought that we did. 
(00:34:03):
For us, it was all about signaling to some very large companies that we were a legitimate and large enough company that they could trust, and we had geographical concentration in specific areas, because we were in the fashion industry, the media industry in New York, we knew exactly where all of their offices were and we knew if they saw our billboards, walking to work, and then got the request to IT for the budget in order to pay six figures for Airtable, they were more likely to be like, "Oh, it's not just some weird startup we never heard of." Like, "Oh, I've seen that billboard, they must be legitimate." And that sounds really silly, but it wasn't actually that expensive.
(00:34:40):
We got mostly remnant inventory, which is at the end of a particular buying cycle. Sometimes they haven't fully sold everything, and you can get the slightly less good ones that are still maybe where you want them for really cheap. And everyone thinks that you only buy billboards if you're huge. So that small signaling thing was a way for us to make sure that we remove some of the risk of not being able to close deals because we were so small. So you can get creative about it. Most of the time you're not going to do that. Most of the time it's like, "Reread your emails." But you could also push it even further if you need to.
Lenny (00:35:12):
What is that full rough cost of billboards like? Because I think people think about billboards and it's hard to even know what they cost. What's a number?
Zoelle Egner (00:35:20):
It really, really depends, so I'm hesitant to give you a number because which metro you're in, it ranges vastly. I would say you can expect that some of that inventory is in the low thousands of dollars, which is way lower than you might expect.
Lenny (00:35:34):
For one billboard.
Zoelle Egner (00:35:36):
Yeah. So you don't need to get a million. And I'm not suggesting you go get one on 101. Good luck to you on that. That's expensive. But you can get one in a reasonable neighborhood in New York for way less money than you might expect, if you're willing to do remnant.
Lenny (00:35:52):
Are you hiring? Or on the flip side, are you looking for a new opportunity? Well, either way, check out lennysjobs.com/talent. If you're a hiring manager, you can sign up and get access to hundreds of hand curated people who are open to new opportunities. Thousands of people apply to join this collective, and I personally review and accept just about 10% of them. You won't find a better place to hire product managers and growth leaders. Join almost 100 other companies who are actively hiring through this collective. 
(00:36:22):
And if you're looking around for a newer opportunity actively or passively join the collective, it's free. You can be anonymous and you can even hide yourself from specific companies. You can also leave any time and you'll only hear from companies that you want to hear from. Check out lennysjobs.com/talent. 
(00:36:41):
Following this thread a bit, my next question is, and this may be the answer, is when you think about Airtable's growth strategy, growth tactics over time, what would you say are one, or two, or three of the most impactful marketing or growth tactics that work best over time? And maybe billboards are one of them.
Zoelle Egner (00:37:02):
I wouldn't say they were the highest ROI, but they're certainly one of the more interesting things that we did. They were useful, don't get me wrong. But I think maybe some other ones are more interesting. The boring answer that I will caveat this with is that one of the pieces of our acquisition playbook, it was very standard, that did work quite well, was some unconventionally targeted Facebook ads. That era is over. So don't expect that that is going to work for your B2B business now because that that's totally changed.
Lenny (00:37:29):
And when you say unconventional, what do you mean?
Zoelle Egner (00:37:31):
We spent a lot of time thinking about a psychographic profile for our users. So the challenge of Airtable is that you can use it for anything. It can be used in every department within an organization. It can be used for personal stuff, you name it, it has a use, because you're functionally building your own software and you can build software for anything. Unfortunately, if you go out to the market with a message of, like, "Build your own software." The vast majority of people are like, "I want to do that. That sounds hard. That sounds stupid. No." 
(00:38:01):
And so we couldn't really use super generic messaging, but to go really specific into verticals, which we did end up ultimately doing, didn't give us the broad coverage to go find new opportunities. You go really deep into one particular vertical or two particular verticals at a time with a small team, but then we weren't surfacing new opportunities that might be even more important. So we tried to balance that vertical specific work that we did with also trying to find this type of person who we had discovered was going to be the best champion for us. 
(00:38:33):
And this is a tinkerer persona, someone who likes new technology, they like putting together the Lego building blocks of things, and you couldn't really find Tinkerer's Magazine. There's not like a place those people hang out. They don't just have one title. It's a psychographic profile as a type of person that could have many, many different roles. And so instead-
Lenny (00:38:56):
And Facebook doesn't let you do that anymore, right?
Zoelle Egner (00:38:59):
No. You can't target based on-
Lenny (00:39:01):
[inaudible 00:39:01] go.
Zoelle Egner (00:39:02):
... like, "They have a tinkerer mentality," unfortunately. 
Lenny (00:39:04):
Okay, got it.
Zoelle Egner (00:39:05):
It's so sad. 
Lenny (00:39:05):
Okay. I see-
Zoelle Egner (00:39:05):
But-
Lenny (00:39:05):
... that it's not possible. 
Zoelle Egner (00:39:07):
Yeah. But what you can do is you can say, "That type of person often likes these types of media. We've heard that they often are really into these podcasts, so they're really into reading about this type of personal development." And often that is associated with people who have these broad set of roles but have this typical mentality. So we would find clusters of interests that people might have, that often were shared by those people, and do targeting around that. And then when that worked, they'll look alike based on it.
Lenny (00:39:38):
Did not expect Facebook ads as one of these answers. So that's interesting. 
Zoelle Egner (00:39:42):
No, and it's not a good idea anymore. Don't do it now. 
Lenny (00:39:44):
Disclaimer.
Zoelle Egner (00:39:44):
Back in the day, it was great. Now I would not recommend. But I have some unconventional ones that I can suggest that are- 
Lenny (00:39:44):
Get into it.
Zoelle Egner (00:39:52):
... not Facebook. There's a few different things, but I want to give some context first for people who are not as familiar with Airtable's business, because I do think these are really helpful pieces of context. The first is because of the types of industries that we are often very successful in, had a very similar network effect that we would see, where basically it was within specific professions, we would see people who, in order to distinguish themselves in that job market, would build a brand around the tools that they used, essentially. We found different ways to accelerate their process of identifying those roles, where it was really, really helpful to build a brand for yourself so that you could hop around to different jobs more quickly, accelerate your process, et cetera, and thus bring along a tool with you and evangelize for it a lot. So that's one set of things we were trying to achieve.
(00:40:46):
The second set of things we were trying to achieve that's also useful context here, is although industry virality was really important for us, even more important was inside of company virality, that was the real superpower of Airtable. We'd go from 10 people to 1,000 people a year. And so we were always looking for ways to make that happen within companies in more and more efficient ways.
(00:41:08):
And then the third piece here is no one had a good generic explanation of Airtable that worked for everybody. This is perhaps partially my fault as marketing, but it's also the fault of the fact that the market was not ready for the good, generic explanation to mean anything, like I mentioned before, people just did not care about the generic explanation. And the magic of Airtable was always seen in its specificity. 
(00:41:32):
So we knew if we can get to the right people and we can connect the dots to them to the correct use case, so they want to go and evangelize to improve their careers, they will do that both externally and within their companies, and more importantly within the companies, they'll be able to go to their friends and say, "Hey, I'm using Airtable as a content calendar, but you have a UX research problem. And I understand Airtable enough that I can help you build a system. And now I'm a superhero internally because I helped you build this whole new thing. Look at me, I'm amazing." And they suddenly have fully done a sales pitch for Airtable without us having to do any work or understand their use case, which is great and very necessary when you are as horizontal as we are. So we had to figure out essentially, "How do we catalyze that word of mouth and build champions at scale?"
(00:42:21):
All of that is to say the two interesting things that we did were all around that. In the very early days, what that meant in practice was we literally had a Slack integration that we pulled in a whole bunch of information about anyone who signed up for Airtable, including their title, the company that they worked at, et cetera. And literally would sit there and had a little button in each of the records that came in that would allow us to email them immediately if we had decided that they might be someone we want to talk to. And we set up this whole automated system so that it would take two seconds to reach out to a ton of different people, being like, "Hey, we'd really love to get your feedback and help make sure you're as successful as possible on Airtable." 
(00:43:02):
This is not scalable in the long term because there's a whole bunch of sending emails and doing meetings. But what it meant is that we were able to start building our mental model for what these champions looked like in practice by finding the patterns across them. And building the foundation is what ultimately became our customer success motion very early. And then we were able to say, "Okay, we found five people who have a content calendar use case with this type of title. And now we'll be able to go run an ad campaign based on that. We can build a bunch of templates based on that. Here's all these different hooks we can use, because we know this is what a champion can look like," in a way that was not going to be obvious if we hadn't talked to a ton of people. So it seems really unobvious as an investment, per se, but tremendous number of human hours going into just having an efficient way to talk to as many people as possible to build those mental models. That's number one.
Lenny (00:43:57):
That is fascinating. Essentially, you weren't even sure who would be excited about Airtable. Part of this is like, "Figure out the personas and groups of people that we believe are the right target to encourage and help support." And then part of that is, "Get it spreading within a company once you figure out these folks within a company." It's such a cool idea to just have a feed of ... I imagine the squad had certain attributes of the person, like, "Here's the company they work. Here's how big it is." And then they talk about, there's a mention of what they're using it for. Is that part of this?
Zoelle Egner (00:44:31):
Ideally. Though we were always very privacy minded, so we couldn't actually get much information about what they were doing in Airtable. We could never see their data, because that would be a tremendous failure of trust, to go back to what we were talking about before. So a lot of this, we would have guesses, and maybe we could see that they'd use certain templates but we didn't otherwise really know. And that was part of the reason why we wanted to talk to them in the first place. 
(00:44:54):
The second reason is that if we could talk to them early, we could help them build their first space, and from there, if they were successful, they would have the tools to go and help other people within their organization. So if we catch them at the beginning, make sure one person was successful by over investing in them, then they essentially became support for everybody else. I should also clarify, these were not necessarily people who were going to be the buyers. The buyers and the champions here look very, very different for Airtable, which is a really an interesting dynamic that many companies do not have. But for us, the person who is going to sit down with a glass of wine on a Friday and build an Airtable base was not the person who had the budget who was going to pay for this thing. 
(00:45:36):
And so we weren't initially looking for buyers, we were looking for champions, in part so that we could then go to IT six months down the line and be like, "Look, you have 500 people using this product, it's been very useful for them. It is time for you to pay now." Not sure IT loved those conversations, but they were really effective for us and meant that it was very, very easy to sell.
Lenny (00:45:57):
Fascinating. It makes me think a lot about the product led sales movement and how this is essentially that, but even earlier, because it's people just signed up and they're just helping them be successful, versus like, "This company's got 14 people using it. You should go try to sell them on an enterprise contract." Essentially this was a tool to help you figure out how to, basically scaling customer success and helping you prioritize who to go after, and being very hands-on with the strongest potential future big buyers.
Zoelle Egner (00:46:24):
Exactly. And I think what's interesting here is it helped us bootstrap two things. One was, to your point, building out the personas, and champions, and so on. And ultimately there's more scalable ways to reach those people in the long run. But secondarily, it also helped us deal with a real product education problem that we had in the early days. Because it was really complicated. Airtable, unfortunately, has two education issues that it needs to solve. It's not just, "How do I put the Lego blocks together?" It is also, "How do I design a piece of software and a workflow?"
(00:47:01):
And unfortunately if you're selling to content marketing manager or a UX researcher, there's no guarantee that they know how to make a workflow. Most software is opinionated, and it does that work for you, and you're like, "It either works for you or it doesn't." And maybe you're frustrated about what it forces you to do in order to work, but you can't really control it, which means when suddenly, you have the ability to create whatever workflow that you want, there's actually some education that needs to go into it in order to be able to make that successful. 
(00:47:28):
It's not enough to just make an Airtable base that's pretty or that functions. You can't get your team to use it effectively if it doesn't fit into the broader context of the organization. It's still going to fail. And so a lot of this was us figuring out, like, "Okay, how do we help these people not only use our product but build something that is going to be durable, so that we do see that growth, so they don't see it as a failure, so it doesn't fail at that second order moment when it starts to get spread out to more people?"
Lenny (00:47:53):
It's a really good tactic for any SaaS product that just is hard to understand and needs, Airtable had both problems. Like, "I don't know what this is for and I don't know exactly how it's going to fit into my workflow." Imagine most-
Zoelle Egner (00:48:05):
But-
Lenny (00:48:05):
... companies still have to deal with both those problems. 
Zoelle Egner (00:48:07):
No, hopefully not. Hopefully not. 
Lenny (00:48:07):
Yeah.
Zoelle Egner (00:48:08):
But once you actually get in with folks, it's very difficult to remove it. So suddenly your retention rates are incredible, your word of mouth is incredible, if you're willing to do that initial work. A lot of people think that Airtable was a pure product led growth company, and missed that huge customer success component that was always very, very important in the early days. And that helped us ultimately move more towards that PLG motion for a while, but was essential to getting it set up in the first place.
Lenny (00:48:35):
Fascinating.
Zoelle Egner (00:48:36):
The other one that we did related to this champions at scale was we spent a hilarious amount of money on really fancy swag. I know this sounds silly, but branded AirPods level of fancy swag. Admittedly more people were in the office back then. Now they are more remote and this would not work as well. But back in the day, if you gave people something really good, not a pen or a sticker, really good, they would show it off to absolutely everyone that they talked to, because they were so excited they got branded AirPods. People would ask about it, walking by their desks. It sounds so like trivial. But for that couple hundred bucks that we spent knowing like, "Hey, this person's already a champion and if someone asks them, they're going to give a really good pitch." Totally worth it. Sometimes better to not skimp on swag. Hard to measure, very effective.
Lenny (00:49:27):
That's a great tip. And it connects to the general idea of find your champions and just do a lot to make sure they're successful, excited, want to evangelize, and an AirPod here and there feel like a really good ROI investment.
Zoelle Egner (00:49:40):
Was for us.
Lenny (00:49:41):
Anything else along those lines?
Zoelle Egner (00:49:42):
I think those are the big ones that I would highlight. The only other small note I would make from a process perspective is if you are going to overinvest in customer success, which I recommend, make sure that you have also set up a process to take the insights that your customer success people are coming up with and turn them into as much content as you can. Because that's where you're going to find scale in the long run. So for us, what that meant was we would talk to a bunch of customers and then customer success would have helped them build bases, and then we would create templates. So were not exact copies, because we're not trying to steal their intellectual property. We would say, "What is the fundamental workflow here, that other companies might have? How do we make a template that is useful from this?" And some blog posts that explain it, whatever else, that we can then put out into the market. 
(00:50:25):
And the next time a smaller company that's not a Fortune 500 wants this sort of thing, someone can just email them that template and we don't have to go through this whole build process, they have something to start with. If you can find those insights and put them genuinely into use as a little conveyor belt, it will be much easier to scale. It will be much easier to come up with genuinely compelling content because it's coming from your customers, so they already care about it. You have strong signal that's going to be valuable if you already built it for them. Use that to your advantage, make that into a little machine. And it makes all of the go-to market that you need to do later easier.
Lenny (00:50:57):
I know that you have the strong opinion that customer success and marketing are basically the same thing and should be maybe one team. Can you speak to that?
Zoelle Egner (00:51:05):
Yeah. This is my spicy opinion, but both of them have to do the same things. They have to identify customer needs. They have to help the customers see your product as a solution to those needs. They need to remove friction from the process of getting value. They are hopefully both encouraging those customers to share with other people, and both of them should be engaged in translating insights from those individuals into resources that can help everybody. 
(00:51:31):
They use different tactics. Marketing is going to use more scalable tactics. Customer success is going to be in the weeds, really talking to individual people, but all of the things they care about are actually the same thing. They just use different ways to do it. And if you, as a marketer, are not pretty confident in being able to say, like, "What I'm doing is getting the right people to get genuine value from this product," so much so that they want to tell other people about it because it's going to make them look good, then maybe figure out if there's ways to bring more of that to your process, because it will make what you are doing more effective.
(00:52:05):
And frankly, there's not a better evangelist than a person whose career you have materially helped to improve based on matching the right person to the solution so that they can have more impact at their company. So much said, one of my unofficial metrics for both marketing and customer success at Airtable, unofficial, was how many people we'd gotten promoted for using the product. I had a running tally of those people, and I knew if we were getting those at the major accounts we were trying to win, something good was happening and we were going to be successful with really large deals.
Lenny (00:52:36):
So curious how you tracked that. I guess you just check in with them occasionally?
Zoelle Egner (00:52:40):
No, I had my CSMs literally, they had really strong relationships. We were actually tracking it. It was a little embarrassing, but it worked really well.
Lenny (00:52:47):
I love it, with the great KPI. It's like dating apps and how many people get married, I guess.
Zoelle Egner (00:52:52):
Exactly. 
Lenny (00:52:53):
Zooming out a little bit, you advise a lot of companies on marketing, customer success, growth, and things like that. Maybe there's a two part question, and see where you want to take it. 
Zoelle Egner (00:53:03):
Yeah.
Lenny (00:53:03):
One is just what are activities that marketing, and growth, and customer success teams often do that are impactful and consistently impactful, things that you think startups should invest in that maybe they aren't, or they already aren't and they should definitely keep doing this. And on the flip side, things that don't work, things that maybe they should avoid. So maybe let's start there and there's going to be a followup. 
Zoelle Egner (00:53:26):
Cool. Okay. I'm going to start with things to avoid, because I try and not to make too many blanket statements on this, but I have a couple that I am willing to make. So this is all with the caveat that channel market fit is really real, and sometimes these things might work for you. Don't discount just because I say that they don't work for me. There are certain types of flashy event marketing and sponsorships that you will get relentlessly invited to do, that will seem like they're going to be really great for signaling purposes, or for leads, or whatever. 
(00:53:55):
And they're almost always a waste of your time, unless you are in an industry where you desperately need to get to a trade show, because that's where everyone hangs out. At that point, yeah, of course you're going to have to go do that. But if you're in more standard B2B SaaS, or that's not really a thing, there are better ways to get in front of those people than having your logo out there. That doesn't tell them anything. Maybe you get a branded session at the conference or whatever, but who's going to go to that branded session? Probably not that many people. And then you will have spent so much money and gotten nothing for it. Go to the event, do not fund your money on the sponsorship. It's stupid. And then the second one, which is definitely a very spicy opinion, but I'm going to go there. 
Lenny (00:54:40):
Go there. 
Zoelle Egner (00:54:41):
A lot of people think that the epitome of product marketing is creating your own category. And while I agree that it is useful to have strong differentiators, because it is, I think creating a category, getting a new thing in Gartner or whatever, is often a waste of your time. It is a huge lift, absolutely enormous, particularly in B2B SaaS, and I'm not always sure that it's helpful to have your super teeny tiny, little niche over here where you're like, "Oh, we have no competitors." That's not actually how buyers work. It's not really worth it. 
(00:55:21):
That said, there are things you can do that feel like category creation that are actually effective, and that I do think make more sense. And specifically if you can elevate a profession instead of a category, that can make way more sense. So the great example of this is that Gainsight creating customer success or many companies altogether carving out DevOps, or rebranding DevOps, to be a thing that was suddenly a sexy job to have. 
(00:55:47):
And I think that's valuable because a job is an identity and people will fight for an identity. A category of software is a line item on your budget. No one is excited about that. But people are very excited about their job being meaningful, and their job being important, and being taken seriously. And so if you could hold up either an existing or a brand new job and say, "This is really important for much broader business metrics, whatever else. We're going to create community for those people to come together and it's all about the job," and not about you. That can be very powerful and they'll take them with you. You become part of the identity of that career. Amazing. Do that, for sure. But like the Gartner Square, there's some opportunities for that where it makes sense. A lot of the times it doesn't. Don't do that.
Lenny (00:56:34):
Amazing. I love that. Is there more you wanted to add, there?
Zoelle Egner (00:56:34):
No. 
Lenny (00:56:34):
Okay.
Zoelle Egner (00:56:39):
I think that's enough on not to do.
Lenny (00:56:40):
What this reminds me of broadly is just, "Stay focused on the customer and their problems. Don't obsess with who you are, who are you selling to and how will you make their life better." Reminds me of this old idea from Kathy Sierra. Does that ring a bell? 
Zoelle Egner (00:56:55):
Yeah.
Lenny (00:56:55):
Where-
Zoelle Egner (00:56:55):
Oh totally. 
Lenny (00:56:56):
... you make your customer a superhero, you want them to feel like a superhero. And if they-
Zoelle Egner (00:56:56):
It works-
Lenny (00:56:59):
... feel like a superhero. And yeah, that sounds like that's essentially what you did with Airtable, a lot of these companies you worked with.
Zoelle Egner (00:57:05):
That that is always the goal. Like, "How can you make them the hero of the story and not you? Because no one cares about your company, what they care about is themselves, frankly."
Lenny (00:57:12):
Are there any products or companies you think of off the top of your head that are really good at this, that are just like they nailed this?
Zoelle Egner (00:57:18):
Yeah, that's a good question. Certainly the two that I mentioned, that helped rebrand some of the professions, so like the Gainsights of the world. I'm blanking a little bit on the ones that have done this for DevOps really effectively, but there's certainly some that have.
Lenny (00:57:32):
Maybe Datadog?
Zoelle Egner (00:57:33):
Yeah, Datadog has done a pretty good job of that. I think where I get excited is when the companies do this in a way that feels less self-serving, or less obviously self-serving. And that means that sometimes you have to be willing to invest in things that will not have super obviously immediate ROI for you, but they will for the community, and for building the community. Oh, actually one really good example, I think Notion has actually done a pretty good job of this. People are really, really invested in the templates that they create, because it feels like you're not pushing Notion, you're pushing the beautiful creation that you have to solve a problem. I think they've done a really nice job on that process, and several of their competitors, I think have done a pretty decent job as well, but they certainly come to mind.
Lenny (00:58:18):
Thinking of templates, I know Airtable, known for templates, and you've mentioned this being a big part of the success, and I imagine a lot of companies now are just creating templates left, because they imagine that's the core, what helped a lot of these companies, Notion being an example. What is your take on the power and importance of templates for software?
Zoelle Egner (00:58:38):
I think they can be tremendously helpful if you are horizontal because they help to narrow the surface area for a user, so they understand how to connect the dots between their problem and your product. And if it is not obvious to someone how they can solve a specific problem, they're going to be like, "Oh, hey, that seems really cool. When I think of something I'll definitely come back." And then you have lost them. And so if you can be like, "Here are three templates that a person you might be excited about." That can be really helpful. Where people sometimes get confused about templates, or have the wrong expectations about templates, is when they think that templates are going to be an acquisition mechanism, and they don't build in the foundation that is necessary for that to be true. So a lot of people think that templates were what drove Airtable's top of funnel. That is not the case. 
(00:59:27):
I was having a conversation with someone who worked a lot on SEO at Airtable in the much later days, and laughing over the fact that people thought that was a big source of traffic, because it was not. We did not optimize them for that. Good luck finding them in search most of the time. Not at all useful. Where they were helpful, narrowing that surface area, helping with matching patterns, helping people understand how the product worked, super helpful. Expansion within companies, tremendously useful. 
(00:59:55):
But they were not a top of funnel mechanism for us, because we didn't put the work in to do that. We did not have an SEO engine. We weren't Zapier. Zapier has done a great job with that. They get a ton of traffic because they built it as a programmatic SEO play, but you have to be clear about what your goals are and what problem they're solving, because otherwise it is very easy to be like, "I'll just build a bunch of templates, and then all of the leads will appear," And that's not going to happen unless you invest in a lot more than at least Airtable did. So it can be useful to build them, know what you're doing it for, and how you're going to measure it, or otherwise you'll waste your time.
Lenny (01:00:29):
Do you think Airtable could have taken advantage of that top of funnel approach if they invested from an SEO perspective or do you think it wasn't an opportunity that worked?
Zoelle Egner (01:00:37):
I think it could have been. We would've needed to hire more humans. Airtable was an incredibly lean team for a very, very long time. From 2015, when I joined, until 2017 or 2018, we had barely 50 people. It was small for many, many years and so we had to make really difficult choices about what to prioritize and what not to prioritize. Should we have hired more people and done more things? I would argue in retrospect, absolutely, yes, there were opportunities that were left on the table, but in early days you leave good opportunities because you have to focus on other things.
Lenny (01:01:13):
Got it. And so a takeaway here is templates could be really useful for customer success versus SEO top of funnel. Right? That's-
Zoelle Egner (01:01:13):
Yeah.
Lenny (01:01:20):
... where they became powerful. 
Zoelle Egner (01:01:21):
Still maybe helpful. Maybe for you, it makes sense to do the SEO play, just know that that is not a small play. It is an investment. It is not and not just like, "Have some people make some templates." You got to do way more than just that. It's not going to be sufficient.
Lenny (01:01:35):
Final potential question, depending on where this goes, and I'm curious how spicy this answer gets, and-
Zoelle Egner (01:01:35):
Oh boy.
Lenny (01:01:40):
It's around launches and PR. You work with a lot of startups, I imagine founders are always trying to plan a launch, get PR. I'm curious your take on the value of investing a bunch of resources in a big launch, the value of just getting PR as an early stage startup.
Zoelle Egner (01:01:56):
Yeah, just getting PR is not a good goal. I know that's been well stated in the market, but just to reiterate it, most of the time PR is not going to get you leads or users, it's just not. And you have to think about when you are creating a launch or doing a piece of PR, what are the breadcrumbs that bring someone back to something that can actually convert? If you have your big tech crunch piece and it's super exciting, it says all these great things about you, and it maybe links to you once, somewhere in the 12th paragraph or whatever, how many people are actually going to click on that link? Not that many people. How many people are going to read that and remember to go Google it? Not as many as you want. Okay? There's going to be so much coming out of the funnel, it is not a useful acquisition mechanism.
(01:02:43):
What it is good for is credibility. And that's where, if you have really clear goals, and you know how you are ready to leverage the asset of a piece of PR coverage, then it can be helpful to you. So the two goals I always recommend to founders when thinking about using PR, are either hiring or maybe improving the response rate for your cold outbound. Those are the two that I think make the most sense, because in both cases they have a different distribution mechanism. In hiring, you're going to include that in an email that you're sending to a candidate. And so it's going to increase the likelihood that they take you seriously, and get excited about the company, and maybe actually end up ultimately joining your team. 
(01:03:22):
Cold outbound, you're using it as credibility to say, "Hey, we're a real company you can trust." Great. Both of those things are all emails that you are proactively sending. You know exactly who they're going to, and you know that asset is going to have, hopefully, the impact that you're looking for, and you can measure whether it makes a difference or not. But just getting a piece of PR, to get a piece of PR is like it'll help with your internal morale, but I'm not sure it's going to do much help for you. So have really clear goals and have realistic goals, or you will be disappointed.
(01:03:51):
Launches however, do not need to just be about PR. In fact, in many cases PR is a distraction, and instead you can have not just one big launch but a series of launches that allow you to stay top of mind, to create momentum with your users, and to show up in lots of different places because audiences respond to novelty, it gives them a reason to care about your company. And so have your big, annual launch or whatever, but also have one two months from then, and another one, and another one. Find ways to use that novelty to your advantage and to get into communities that you think are going to be good fits for your company.
Lenny (01:04:26):
I love that advice. Any final thoughts before we get to our very exciting lightning round?
Zoelle Egner (01:04:34):
Mostly just all of this is easier if you talk to your customers more. Build a system for yourself that will allow you to have those touchpoints. That's not just making everyone answer customer support tickets, though I do think that is a great idea, because it gives so much empathy and it's really helpful. You as a founder, if you're a founder, or a product manager, or whatever else, should find a way to get that on your calendar weekly or monthly. Go talk to people, it makes it better. You will have a better mental model. The other thing is strongly consider investing in customer success if you are a B2B company, early. Airtable had it before sales, which is a very unconventional approach, but early is worth it. It has huge dividends if you actually listen to them. If you're not going to listen to them, though, don't hire them, because that's sad.
Lenny (01:05:22):
I have followup questions on the customer success piece, say someone wants to invest in customer success, is there a resource, or person, or anything that you could point folks to, to understand and think about how to do this well?
Zoelle Egner (01:05:36):
There's a lot for people within that profession. There's not as much for founders out there right now, unfortunately. This is an area that I very eagerly am looking for more resources to share with people. Minimally. I'll say, if you care about this, send me a message. I will give you some advice. All of our industry will be better if there are more people working on customer success. So I will help you. Send me a note. Otherwise, I'll try and dig out some other things and maybe you can share them, but there's not a ton. So people in customer success, please share your learnings more with founders. All of us-
Lenny (01:05:36):
Have-
Zoelle Egner (01:05:36):
... would like to see it.
Lenny (01:06:09):
Yeah, I've actually been looking for someone to write a guest post in the newsletter, about just how to set up a customer success team. And so if you're listening, you think you could be that person. Let me-
Zoelle Egner (01:06:21):
Yeah, I have some people that I will not put on the spot right now, that I will send your way that I think- [inaudible 01:06:26]
Lenny (01:06:26):
Amazing. [inaudible 01:06:27]. Let's make this happen.
Zoelle Egner (01:06:28):
Yeah.
Lenny (01:06:29):
And then I wanted to ask you a question on the first piece of advice, which is, "Founders talk to the customers more often." Is there one tactical piece of advice you could recommend for how to do that?
Zoelle Egner (01:06:37):
Yeah.
Lenny (01:06:37):
How to find a customer, how to set it up consistently?
Zoelle Egner (01:06:40):
Totally. The simplest way to do this is to write a template email for yourself that you can send out very easily, that essentially says like, "Hey, thank you so much for using the product. I would really love to hear about your experience so far and get your feedback. Do you have 10 minutes to talk on the phone?" I know it is important that it's on the phone and not a survey because you get way more instinct from unstructured conversation than you're going to get from sending them three things in a Google survey.
(01:07:05):
Set it up, come up with a hypothesis of the type of person that you want to talk to and then run a query against your database, find someone and send three of those emails a week. And it's not exciting, but you can automate most of it and it will be helpful. None of this stuff has to be complicated. You just got to have a system.
Lenny (01:07:23):
Great advice. With that, we've reached our very exciting lightning round. 
Zoelle Egner (01:07:27):
Yes.
Lenny (01:07:27):
I've got six questions for you. I'm going to go through them pretty quick. Whatever comes to mind, let's see where it goes. 
Zoelle Egner (01:07:34):
Okay.
Lenny (01:07:34):
Question number one. What are two or three books that you recommend most to other people?
Zoelle Egner (01:07:40):
Okay, I hate this question because I take pride in making highly targeted recommendations, but I will do it anyway. I'm pretty sure you mostly talk to product and growth people. Right now, obviously, AI is a big topic of conversation, so here are two books that will enrich your mental model for artificial intelligence and encourage you to think about it from different perspectives. The first one, a little bit academic, highly recommend it, though. It's a book called Computing Taste by Nick Seaver. 
(01:08:09):
He's a professor of anthropology and he did this study of people and companies who build music recognition algorithms. And it's a really interesting book for a bunch of reasons, including that it's a academic take on both tech culture, and more specifically, the unspoken and underlying assumptions that many workers who are building in this space have. It can be a little spicy and uncomfortable for a person in tech to read, but I think it is a fascinating perspective and very relevant to the stuff that's going on in AI right now. So go check it out. Computing Taste by Nick Seaver.
(01:08:42):
The second is a fiction book, but the Ancillary Justice series by Anne Leckie, about a spaceship AI that ends up separated from its ship and trapped in a body. I'm going to leave it at that. Worth reading for a different way of thinking about AI.
Lenny (01:08:56):
I think we need a Zoelle full episode on book recommendations. These are amazing. Let's keep going.
Zoelle Egner (01:08:56):
So fair.
Lenny (01:09:02):
What other podcast of yours that you love to listen to other than this podcast?
Zoelle Egner (01:09:07):
Probably either Happiness Lab or Gastropod. I love food and also psychology, one of those two.
Lenny (01:09:13):
Interesting. Okay, we'll keep going. Favorite recent movie or TV show?
Zoelle Egner (01:09:17):
Movie, Everything Everywhere All at Once. And TV show, there's a Korean drama called Extraordinary Attorney Woo. That, I really enjoyed.
Lenny (01:09:26):
Favorite interview question that you like to ask?
Zoelle Egner (01:09:29):
Yeah. Okay, so this one is related to customer success. It's my favorite question of all. People hate it, sorry. But I like to ask anyone who's going to be in a customer facing role, who needs to be able to keep their cool, and also learn stuff on the fly, and respond to customers, to solve an unfamiliar problem using Zapier. And they can use the internet to look things up, whatever, but I basically lay out for them a problem that I, as the customer want to solve, and have them build it for me live. This both is surprising for most people, so you get to see how they respond to an unfamiliar situation, which every client will give you at some point, and it shows how they learn things in a very concrete way, which is really interesting. So check it out. It works really well for customer success.
Lenny (01:10:10):
I've not heard that one before. Fascinating. Top five SaaS products that you enjoy and an Airtable cannot be one?
Zoelle Egner (01:10:18):
Ugh. Okay, then I'll try and avoid any company that I have worked for. I really like using Figma. It's nice when designers let me play with things. I've been really enjoying working with Webflow, also means that I can do stuff on my own. This is maybe spicy, but I actually love Google Docs. I'm not a Notion's fan stand, sorry.
Lenny (01:10:18):
Hey.
Zoelle Egner (01:10:36):
But Google Docs-
Lenny (01:10:37):
Can't [inaudible 01:10:37] them all.
Zoelle Egner (01:10:36):
... is like my best friend.
Lenny (01:10:37):
Google Docs is great.
Zoelle Egner (01:10:38):
Yeah. And then there is a personal CRM company that I invested in, so sorry, maybe this is not allowed, but called Clay, and it is the only way I've ever been able to keep track of my-
Lenny (01:10:47):
Wow. [inaudible 01:10:47]-
Zoelle Egner (01:10:47):
... relationships in a real way.
Lenny (01:10:48):
Clay's great product.
Zoelle Egner (01:10:49):
They're the best. And then I don't know if I love it, but I use Zoom so much that I feel like I must say it, because I spend so much of my time on it and it's categorically better than Google Meet.
Lenny (01:11:01):
Final question, favorite book, course, article, any resource on marketing that non marketers can learn from?
Zoelle Egner (01:11:10):
Okay, it's a newsletter. Does that work?
Lenny (01:11:12):
Absolutely.
Zoelle Egner (01:11:13):
Amazing. Okay, so there is a specialist VC firm called MKT1. It's run by Emily Kramer and Kathleen Estreich, sorry if I pronounced your last name, there, wrong, Kathleen. It's all about marketing. They are marketing experts and operators who now invest, but they make the best frameworks that you can immediately apply. And there's templates and all sorts of super, super tactical stuff, which a lot of tactical marketing content is terrible because it's actually content marketing for some bad platform. Theirs is not. It is genuinely good. Go check it out. 
Lenny (01:11:43):
A huge fan. Emily has been on the podcast. 
Zoelle Egner (01:11:45):
Oh, [inaudible 01:11:47].
Lenny (01:11:47):
Yeah. And I look at that newsletter as the Lenny's newsletter of marketing, and it's exactly how you described.
Zoelle Egner (01:11:53):
It's the best.
Lenny (01:11:53):
Huge fan. Great recommendation. With that, Zoelle, thank you so much for being here. This was a lot of fun. And we got through a lot of stuff, which makes me really happy. Two final questions, where can folks find you online if they want to reach out, learn more, and how can listeners be useful to you?
Zoelle Egner (01:12:09):
I am on Twitter @Zoelle. I'm also on LinkedIn, so I live there, come find me there. Otherwise, how can you be useful to me? Mostly like go forth and believe in customer success, and talk to your users, number one, because I am an avid user of technology, and I want it all to be better. Number two, no, that's all I got. Just go do those things and I will be so happy. Also, if you want to talk about customer success, anytime, hit me up. I'm here.
Lenny (01:12:35):
I'm going to add a couple more things, which you mentioned to me offline, that you're hiring at Block Party.
Zoelle Egner (01:12:39):
Yes.
Lenny (01:12:39):
You're hiring growth people, PMs, engineers, and then you're also advising on the side with marketing customer success. Anything else you want to add, there?
Zoelle Egner (01:12:48):
Yeah, absolutely. Love advising early stage companies. I'm especially helpful for pre seed and seed, usually, anything PLG, positioning, messaging, figuring out your channels, experimentation, all that early, fun stuff. I love it. Happy to help anytime. And we are hiring across all of the teams, but especially mine. So if you would like to come and do all sorts of fun experimentation, and also help keep people online safe, come look up, Block Party. I'd love to have you on my team. 
Lenny (01:13:18):
Blockparty.com, or where do folks- [inaudible 01:13:19]
Zoelle Egner (01:13:18):
Blockpartyapp.com. Did not-
Lenny (01:13:18):
App.com
Zoelle Egner (01:13:19):
... get blockparty.com. 
Lenny (01:13:19):
You didn't. Zoelle, thank you. Very good.
Zoelle Egner (01:13:23):
Thank you. 
Lenny (01:13:28):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review, as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

---

