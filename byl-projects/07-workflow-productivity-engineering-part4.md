# BYL Brain: Workflow, Productivity & Engineering (Part 4)
_Auto-generated from Lenny's Podcast Transcripts Archive_
_Last updated: 2026-02-23 00:40 UTC_
_This is part 4 of a multi-part project file._

---

## FULL TRANSCRIPTS

---

## Why AI is disrupting traditional product management | Tomer Cohen (LinkedIn CPO)
**Guest:** Tomer Cohen 2.0  
**Published:** 2025-12-04  
**YouTube:** https://www.youtube.com/watch?v=R-zCfLQD_84  
**Tags:** growth, acquisition, okrs, kpis, user research, mvp, iteration, experimentation, funnel, team building  

# Why AI is disrupting traditional product management | Tomer Cohen (LinkedIn CPO)

## Transcript

Tomer Cohen (00:00:00):
When we look at the skills required to do your job, by 2030, it will change by 70%. So whether or not you're looking to change your job, your job is changing. In order to stay competitive, you actually have to go back to some first principles, go back to the drawing board and reimagine what it means to be building.

Lenny Rachitsky (00:00:15):
You're experimenting with a very different way of building product at LinkedIn that fully embraces what AI unlocks.

Tomer Cohen (00:00:24):
We call it the full stack builder model. The goal itself is to empower great builders to take their idea and to take it to market, regardless of their role and the stack and which team they're on. It's really fluid interaction between human and machine.

Lenny Rachitsky (00:00:37):
This feels like this could be a model for how a lot of companies operate and how product ends up being built in the future.

Tomer Cohen (00:00:42):
Change management here is going to be a critical part, but it's not enough to give them the tools. You have to build the incentives programs, the motivation, the examples to how you do it. I see a lot of companies roll out their agents and just expecting companies to adopt. It doesn't work this way.

Lenny Rachitsky (00:00:56):
There's always been this question, is AI going to just make people that are not amazing, more amazing, or is it going to make amazing people even more amazing?

Tomer Cohen (00:01:01):
Top talent has this tendency of continuously trying to get better at their craft. The key trait that I'm emphasizing for builders is...

Lenny Rachitsky (00:01:11):
Today, my guest is Tomer Cohen, longtime chief product officer at LinkedIn, who is piloting a new way of building that I think will become a model for how companies operate in the future. It's called the Full Stack Builder Program, and essentially the idea is to enable anyone, no matter their function, to take products from idea to launch. They've scrapped their APM program and replaced it with an associate full stack builder program. They've introduced a new career path with the title Full Stack Builder that anyone from any function can become. And as you'll hear in the conversation, they've built a bunch of internal tools and agents and processes to basically build a human plus AI product team that can move really fast, adjust to change quickly, and do a lot more with a lot less. If you're looking for inspiration for how to rethink how your team operates and to lean into what AI is unlocking for teams and companies, this episode is for you.

(00:02:06):
A huge thank you to Shira Gasarch for suggesting topics for this conversation. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. It helps tremendously. And if you become an annual subscriber of my newsletter, you get a year free of a bunch of incredible products, including a year free of Devin, Lovable, Replit, Bolt, n8n, Linear, Superhuman, Descript, [inaudible 00:02:29], Gamma, Perplexity, Warp, Granola, Magic Patterns, Raycast, ChatPRD, Mobbin and Stripe Atlas. Head on over to lennysnewsletter.com and click product pass. With that, I bring you Tomer Cohen after a short word from our sponsors.

(00:02:42):
My podcast guests and I love talking about craft and taste and agency and product market fit. You know what we don't love talking about? SOC 2. That's where Vanta comes in. Vanta helps companies of all sizes get compliant fast and stay that way with industry-leading AI, automation, and continuous monitoring. Whether you're a startup tackling your first SOC 2 or ISO 27001 or an enterprise managing vendor risk, Vanta's trust management platform makes it quicker, easier, and more scalable. Vanta also helps you complete security questionnaires up to five times faster so that you can win bigger deals sooner. The result? According to a recent IDC study, Vanta customers slashed over $500,000 a year and are three times more productive. Establishing trust isn't optional. Vanta makes it automatic. Get $1,000 off at vanta.com/lenny.

(00:03:36):
This episode is brought to you by Figma, makers of Figma Make. When I was a PM at Airbnb, I still remember when Figma came out and how much it improved how we operated as a team. Suddenly, I could involve my whole team in the design process, give feedback on design concepts really quickly, and it just made the whole product development process so much more fun.

(00:03:56):
But Figma never felt like it was for me. It was great for giving feedback and designs, but as a builder, I wanted to make stuff. That's why Figma built Figma Make. With just a few prompts, you can make any idea or design into a fully functional prototype or app that anyone can iterate on and validate with customers. Figma Make is a different kind of vibe coding tool. Because it's all in Figma, you can use your team's existing design building blocks, making it easy to create outputs that look good and feel real and are connected to how your team builds. Stop spending so much time telling people about your product vision, and instead show it to them. Make code-backed prototypes and apps fast with Figma Make. Check it out at figma.com/lenny.

(00:04:42):
Tomer, thank you so much for being here and welcome to the podcast.

Tomer Cohen (00:04:45):
Thank you. It's great to be back.

Lenny Rachitsky (00:04:47):
It's great to have you back. I'm really excited to be chatting because you're experimenting with a very different way of building product at LinkedIn that fully embraces what AI unlocks, kind of leans into what is now possible, and to me, this feels like this could be a model for how a lot of companies operate and how product ends up being built in the future. There's a lot of product leaders that are talking about AI, what they can do. It feels like you're actually doing this in a really, really radical way, and so I'm excited to learn from you to hear about this for listeners to understand what you're seeing, what you've learned. Let me start with just why did you decide this was necessary? Why are you rethinking all of these things about how product has been built for a long time? AKA, why do people need to pay attention to what we're about to be talking about?

Tomer Cohen (00:05:34):
It really starts with kind of the basics. For me, technology has always been about empowerment. It's not about what it does for us. It's about what enables us to do. And now we have this amazing opportunity in my mind to make it about meritocracy, and I think it's an opportunity, but it's also a necessity right now, and I want to put this in context where we're entering this phase where the time constant of change is far greater than the time constant of response. Basically means that change is happening faster than we're able to respond to it. Now, LinkedIn has this unique view of the world of work. So we actually have some pretty, in my mind, mind-blowing stats to put this in perspective. When we look at the skills required to do your job, by 2030, which is literally four years from now, sounds a long time, but four years from now, it will change by 70%.

(00:06:25):
So whether or not you're looking to change your job, your job is changing. The only question is, do you keep it? And then we look at organizationally, the fastest growing jobs right now, the most in demand jobs in the market are growing by north of 70% from last year's fastest growing job. So there's a new kind of iteration of what you need as an organization to thrive. And then you apply that to building products and you realize that in order to stay competitive, you actually have to go back to some first principles, go back to the drawing board and reimagine what it means to be building. And what I love about this is when you think about the role of a builder, which the builder is at the heart of company, the goal is actually quite simple. The builder takes an ADN, she brings it to life. That's really the process, right?

(00:07:11):
And we all build those, let's call them best practices. You research the problem really well, you spec it out, you design it, you code it, you launch it, and you iterate. That's basically it. But what happens at many at scale companies, LinkedIn included and many other companies, over time that process became very complex very quickly. So what happened? We took every step and we expanded it to a lot of sub-steps. Researching, the problem became looking at for us 10 to 15 sources of information, obviously talking to customers about doing data pools, looking at feedback tickets in multiple sources, social media, interactions with customers. We probably have 10 to 15 sources of information we go for before we feel like we have research department really, really well.

(00:07:58):
Think about reviews for product. There is design reviews, privacy reviews, security reviews. I can go on and on and on. And each one of those substeps actually has a valid reason to exist. But when you add a whole thing together, you're like, "Oh my God. This is why it takes, to build a small feature, multiple teams, multiple code bases, multiple sprints just to get it out to launch," and not talk about iterating, which is actually where you seek success. You never see success in the launch itself. So really the work itself is not complex, but the process we made very complex. And when I was digging in, I found it doesn't end there because somebody has to do all those substeps, so what happened is you actually move from process complexity to organizational complexity as well.

(00:08:41):
And then you actually led to microspecialization. All those subsets are doing by somebody specific. So from one builder, we have multiple functions. Obviously we have engineering, product and design, and you can start questioning those lines. At least I am internally. And from there, we have a lot of subspecialties. It happens in every one of those functions, but imagine design. We have interaction design, animation design, content design, research. There's so many aspects to that. So they're all valid, but they all have people, and that entire process basically means a lot of... It's basically bloating. It's complexity. And then without noticing, you end up with this massively complex... We actually have this diagram that basically shows the process complexity, organizational complexity together.

(00:09:26):
And usually people are mind blown because they're working on one thing very specific, but when you zoom out, you have this overwhelming experience you're kind of thinking about. And now we have this real opportunity to collapse the stack backup, go back to craftsmanship, rethink the product development lifecycle, which is where the full stack builder model comes to life.

Lenny Rachitsky (00:09:47):
Wow. Okay. And there's so much here. We're going to be showing the visuals as you talk to help people see what you're explaining here. And all of this is very rational. If you have 15 sources of information, why not pull from it? Why miss out on that stuff? And what you're describing here is as you get more power and more specialized... It all makes sense rationally, but when you start to step back and look at this like, holy shit, it takes six months to launch one feature. I want to ask about the stat you shared. I think this is an incredibly powerful stat and you have very unique data here to tell you this sort of stuff. So you said that something like 70% of the skills that people will need in the future are going to change.

Tomer Cohen (00:10:28):
To do their current job.

Lenny Rachitsky (00:10:29):
To do their current job. And what is this looking at? Is this just based on historical data or how do you find that?

Tomer Cohen (00:10:36):
Yeah. To be fair, there was always a change, right? So it was never about just keep the skills you have today, but we've never seen such a dramatic part of your role today. So whether you are a marketer right now or a seller, a recruiter, an engineer. Engineering is where a lot of the investment is going in right now in terms of agents. Those jobs will change dramatically. I remember I said my role, my life as an engineer and even then it's changed materially after 10 years, and then the change we're seeing right now, just thinking about in four years, what did it take to actually engineer really, really well would be dramatically different, or to build software, to build an artifact of some sort. But it's true for almost every function. It's not equal. Some job like nurses will see less impact, but some jobs will see 90%, 95% impact.

Lenny Rachitsky (00:11:28):
There's also a stat that I don't think you mentioned here that I saw on the post when you first talked about this program is that 70% of today's fastest growing jobs were not even on the list of jobs a year ago.

Tomer Cohen (00:11:39):
Yeah. No, so this is the fastest growing job on the list were not there a year ago, and then many of them don't even exist a decade or two ago. There's actually some pretty amazing stats across the board.

Lenny Rachitsky (00:11:52):
Okay. So let's talk about this program that you built. Tell us the name and then tell us the gist of what it is today and the vision of where you want it to be.

Tomer Cohen (00:12:03):
Yeah. So we call it the full stack builder model. And the goal, always start with the goal. The goal itself is to empower great builders to take their idea and to take it to market, regardless of their role and the stack and specifically which team they're on. And the idea ultimately is to be able for that builder is to develop experiences end to end, to combine skills and expertise across what was traditionally distinct domains to bring it all together. And it's not a sequence of steps. It's really a fluid interaction between human and machine. That's how the way I see it. And then when you look back at that product development life cycle from the idea, the insight all the way to launch, the key trait that I'm emphasizing for builders is where I want them to spend their time is where I think great builders should shine in.

(00:12:54):
So the idea of vision. Coming up with a compelling sense about the future. Empathy, super critical, right? Having a profound understanding of an unmet need. Communication is critical. And we see this a lot in job descriptions right now for almost every role, but ability for you to align and rally others around an idea. Creativity, which for me is about coming up with possibilities beyond the obvious. For example, I don't think AI yet is great at creativity. I think it's kind of, in many ways, brings back the things you might not know about, but it's not the kind of next level creativity, which I think still humans are much better at.

(00:13:33):
And then ultimately what I think is the most important trait for a builder is judgment. Some people call it test making, but it's making high quality decisions in what is complex ambiguous situations. Everything else, I'm working really hard to automate. Really, really hard. And then when you think about the outcome, it's not just about having more shots at the goal, which I think people go like, "Oh, the iteration speed is going to be very high." Yes, but what you're really doing to an organization of at scale organizations is they're a lot more nimble, a lot more adaptive, a lot more resilient. They can navigate the future. They can actually match the pace of change to the pace of response.

(00:14:13):
And an analogy I have in mind is kind of Navy SEALs. You come to training, they're all kind of learning, they're cross-trained, across multiple areas. What they specialize in is the mission and they operate in small pods and they're very nimble and you can assemble them very quickly. And I think that's going to be the organization that will win in the future.

Lenny Rachitsky (00:14:33):
Okay. So the simple idea, if you're just to boil it down to a sentence, the idea here is there's a builder who goes through the entire product development process essentially on their own. They have an idea, they research, they do data, they prototype design ship. That's kind of like the vision of where this goes?

Tomer Cohen (00:14:50):
Yes, but it doesn't have to be on their own. It's not like... I still believe in teams.

Lenny Rachitsky (00:14:51):
Got it. So smaller teams.

Tomer Cohen (00:14:55):
Just smaller teams. Smaller teams and much more focused on the problem, the mission, per say, versus... Actually, one of the things we've done as an example, we started to do the idea of pods. We're no longer large teams. We assemble a team, ideally a full stack builders coming together and it's less about can I have an engineer design PM working together and trying to combine this trio looking at folks who can flex across and then they tackle something for a quarter or so and then we reassemble those two different pods. That's one example of an manifestation we're doing right now and seeing actually some great success in both in terms of velocity, but also in terms of that focus and nimbleness of that team.

Lenny Rachitsky (00:15:37):
And it feels like the goal here, what you're trying to adjust and that broke as teams bloated as speed and adaptability and flexibility, because going back to your original point that change is happening so much more quickly now that companies that have been building in this traditional way just can't compete.

Tomer Cohen (00:15:56):
Yeah. It's not that you have to break the model. I think the model is broken. It's just this pace of change is helping us realize it.

Lenny Rachitsky (00:16:03):
Okay. So then going back to the things that these builders still do versus what you want to automate. So the list you shared is they're responsible for the vision, empathy, communication, creativity, and judgment.

Tomer Cohen (00:16:16):
Yes. Yeah. And I would put a lot of the focus on the latter. I think if you ask me at the end of the day, what's the kind of most important trait? I would say it's that judgment, test making ability.

Lenny Rachitsky (00:16:27):
And then in terms of what you're automating, what are some of the areas you've seen a lot of success in actually automating and where do you think this goes?

Tomer Cohen (00:16:35):
Yeah. So I think just to kind of break it to pieces, and I think this is... If you were a startup right now, in many ways you can start this way. There's no legacy code, there's no legacy structure you run. And in fact, a lot of the startups I talked to that are built AI natively, they're just working at full stack builders. That's the way they start. If you're at a company at a scale of ours and many others in the market, you're like, this is almost like a new production function and mindset that you have to do. And there's really three components that we're working on. One is platform. The second one is the tools and the agents. And lastly is the culture.

(00:17:17):
The platform one, this is the kind of level of investment you have to do before, before this actually starts, you start to see all the benefits accrue. But the platform for us as an example is rearchitecting all of our core platforms so AI can reason over it. So we're building kind of this composable UI components with server side that we actually build. We're basically building for AI to be ready to bring it in. So you can't just go and bring a third party tool and have it work on the LinkedIn stack. In fact, that's one of our biggest learnings. It never works. Never works. You have to bring it in and customize a lot of it, working almost in alpha mode with those companies to make it work internally.

Lenny Rachitsky (00:17:59):
So this is essentially re-architecting your code base to work more efficiently with AI. Is that one way to think about it?

Tomer Cohen (00:18:04):
Yes. And in many ways, working with those companies to adjust something in their stack to work with our stack as well.

Lenny Rachitsky (00:18:12):
When you say those companies, meaning the development agents like Cursors and [inaudible 00:18:16] and such?

Tomer Cohen (00:18:16):
Yes. Or Figma on design. Or you can think about design systems is another example of that. But you have to have that back and forth because they're not... In many ways, we haven't seen anybody be able to work off the shelf immediately on our code-based design systems and unique context we have.

Lenny Rachitsky (00:18:34):
Just to follow that thread briefly, so there's Figma. That's interesting. So basically the way Figma exports and keeps your design system, that has to change to work better with AI is what I'm hearing.

Tomer Cohen (00:18:41):
They first need to know how to work with our design systems, which is something, in many ways a lot of those companies are working on. Same with coding. It doesn't work that you just bring it in and it just reasons over your code base really well. We tried. We are building that layer that basically allows it to do so, whether it's Copilot or Cursor, Windsurf and so on.

Lenny Rachitsky (00:19:02):
Got it. Okay. Oh yeah, Copilot. Microsoft. I get it. I get it. Okay. Okay. So that's the platform. So that's an investment that you guys have to make to make AI effective at building and doing all these things.

Tomer Cohen (00:19:17):
And then you have tools. So tools is where you really build the agents. I mentioned I want to automate everything outside of those five trades that we talked about, and then we're building the tools for that. And then for that, actually very similarly, I can't just bring a tool from the outside and work. So I'll give you an example. One of our biggest things is building a trust agent. Trust is really important for us at LinkedIn. There's a lot of unique vectors which trust plays at LinkedIn doesn't place it anywhere else. So we need to bring all of that know how and context and information base into that agent. So we ended up building our own trust agent at LinkedIn.

Lenny Rachitsky (00:19:53):
And so what is this trust agent doing? Telling you when you're maybe exposing information that you shouldn't be?

Tomer Cohen (00:19:58):
So when you build a spec, you build an idea, you walk through the trust agent and it'll basically tell you what are your vulnerabilities, what harm vectors potentially you're introducing or will be introduced as a result of that. And I had our head of trust build it. So the head of craft for every area is building their own agent. As an example, we have one of our features for job seekers is called Open to Work. If you're looking for a job, you can put an open to work.

Lenny Rachitsky (00:20:24):
Yeah, a little green loading thing on the circle.

Tomer Cohen (00:20:25):
Exactly. And actually it's a great signal. I've seen some great success from it. People are helping each other. The community really thrives around helping each other. But at the same time, it introduces a trust vector for bad actors because they're open to work. People who are looking for a job are potentially more vulnerable to scams than other folks. So being able to think about how do we prevent all of those ahead of time. So we walked that spec from a couple of years ago through the trust agent. Not only was it able to find all the stuff we initiated at the beginning, but all the holes that we did not catch until later. So that's a great example of something that actually worked really well.

(00:21:03):
That's one. The other one is a growth agent, as an example. Again, LinkedIn has a very unique... Actually, we have an incredible growth team, growth process. We've kind of funneled all of our unique loops, our funnels, our tests of the past, everything into this growth agent, and now you can basically rock your respect for it, your idea for it. And it would not just allow you to do it better. It would actually critique how good is your idea. This is something you cannot bring off the shelf. It's very unique to LinkedIn. So we had to invest dramatically in it. And one team which is using it right now, which is almost... I wasn't thinking about it at the beginning, but our UXR team, our UER team, the user research team is usually using that growth agent to understand out of all the things that are basically surfacing for members, which one has the biggest growth opportunity to have the biggest impact? That was not in the cards when we thought about that idea, but teams are basically funneling those ideas into this one.

(00:22:05):
An example is our research agent. So research agent basically is trained on the personas of our members. You can think about a small business owner, a job seeker and so on. And it's using not just world knowledge, it's using all the research we've done in the past, all the support tickets coming in. So it's pretty good at understanding that persona at LinkedIn. So one examples we had is a team came out with a spec. They weren't aware we had the research agent yet. I asked the research agent for a small business owner, wanted to think about the marketing spec we had, and it critiqued it extremely well. Actually, in many ways shifted the direction of the team to focus on other integrations tools we can focus on, but it's very hard to have that visibility all to all that corpus of knowledge inside of the company.

(00:22:56):
That's another example. We have an analyst agent trained on all how you basically can query the entire LinkedIn graph, which is enormous. And instead of relying on your SQL queries or data science teams, you can use the analyst agent. All of those I would say are, I would call them still MVP+. The goal for us in the next couple of months to basically roll them out externally. Externally, I mean, internally at LinkedIn.

Lenny Rachitsky (00:23:20):
Not as new product lines.

Tomer Cohen (00:23:22):
Exactly.

Lenny Rachitsky (00:23:22):
Okay. So many questions. One is just how are you building this? Is there a platform you're using? What does it take to build an agent at LinkedIn? Is it all internal tools or is there third party use?

Tomer Cohen (00:23:31):
It's a great call. So I think we've been experimenting with a lot of tools. And I would say for a lot of those kind of knowledge corpus agents, we're using everything from Copilot Enterprise to ChatGPT Enterprise. By far though, the most important part was basically our own customization of it. That's been where we saw the biggest gains. Even building the orchestrator across those because you want the agents to start following to each other, the trust agent should work with the growth agent and go do a back and forth versus doing what more sequentially. So we've done a lot of work internally to make it happen. This is why I think it does require that level of investment.

(00:24:09):
And then in some cases, let's talk about the design agent that we're working with. We're working with multiple companies to try and understand which product works best for us. And interestingly enough, and this is another learning, different teams gravitate to different products. So that's something we'll have to resolve and think about how we do this really well, because ultimately we were trying to simplify the process as much as possible, but that was a big learning for us and which tools we use and how we basically integrate them in.

Lenny Rachitsky (00:24:39):
Got it. So you might have an amazing Figma agent, but some teams want to use a different design tool.

Tomer Cohen (00:24:44):
Yeah. So we've kind of experimented with Figma and Subframe and Magic Patterns and so on, and we saw people gravitating depending on the function, their level of visibility, their know how of the tool before, they're gravitating to different tools. And ultimately, I don't want to have eight design agents in the company, so we have to converge into at least a few. And I think it's similar across many areas because the appeal of those, a lot of those agents are trying to solve similar end goal, but they're doing it very differently. And what you'll see that ultimately, I don't think there's going to be a winner takes all because the starting point of the customer or the user will dictate a lot how simple they are for that use case.

Lenny Rachitsky (00:25:28):
Super interesting. The other interesting takeaway here is you're designing very specific agents that are one job to be done. Is that a very intentional decision? Did you try an agent that just is super intelligent on all these things?

Tomer Cohen (00:25:41):
Ultimately, they will do an orchestrator. We're going to really orchestrator across, but we did want to be able to rate and grade those agents really well on how they're doing. And I think there is a level of expertise. Now, we're kind of building this in a way where we'll be able to mask a lot of those. You might not know that there's a trust agent. You might have, we call this internally the product jammer agent that basically does your product jam, which is a process we do internally. You might just use the product jam engine, and that product jam agent will work with all the other agents. But now we're starting with that building blocks until we build the orchestrating layer across.

Lenny Rachitsky (00:26:20):
Another interesting takeaway from what you've been sharing is that so much of the work has gone into the beginning of the product development process, just like helping you craft the right requirements, clarify trust, and then here's product jam and here's the research we've done. And I imagine it's because coding has already been accelerated with all these IEE tools. Talk about just why that's maybe where most of the investment's gone and where you've seen the most impact so far.

Tomer Cohen (00:26:43):
Well, 100% our coding investment has gone, started a while back, and those are fall into place. We have our coding agent. In fact, we've kind of staged it into two parts of it. There is the idea to design part, and then let's call it the code to launch part. The code to launch part has gotten a lot of attention and we're making some big inroads there. Everything from the coding agent to what we call the maintenance agent when you have a failed build, it will do it for you. In fact, I think we're close to 50% of all those builds being done by the maintenance agent and a QA agent.

Lenny Rachitsky (00:27:19):
Wow. So this is when a break builds instead of engineers hopping on the issues that an agent fix.

Tomer Cohen (00:27:24):
You can still go and finish your coffee before you have to go and redo the build again.

Lenny Rachitsky (00:27:27):
Extremely cool.

Tomer Cohen (00:27:28):
But we haven't had much investment until we kind of launched this program in the idea to design area. And that's a material part of work. It's also where the quality a lot of the work comes from, at least before you start to go into the coding phase. The idea is to empower everybody. So if you're an engineer, you can basically use all those tools at the front of the process and be able to be a full stack builder.

Lenny Rachitsky (00:27:51):
How long did it take to get this kind of in place for you to actually form your first team to build these, the initial agents and some of this backend, redo the code base sort of thing?

Tomer Cohen (00:27:59):
I announced this internally end of last year, we really kind of started working, but it was more setting up the teams and the processes internally. We had our first MVPs of those agents I think like four to five months after it was really trained, I would say. But really the work itself has been kind of couple of months of dedicated work. A lot of it has been getting all the corpus of data together, cleaning it up. And that's actually a good learning as well. It's not great to just give it access to your drive and say, "Reason all over this knowledge base." It actually does a very poor job understanding importance of the past and putting weights on stuff. You actually want to think about specifically what the context when do you want to give it to and what's the knowledge base that you want to have it focused on. So even cleaning up, let's call them gold examples or golden examples to learn from, has been one of the biggest learnings. Just reasoning over your entire knowledge base did not work.

Lenny Rachitsky (00:28:54):
Yeah, that makes sense. There may be just like a researcher with a strong opinion about something that you disagree with and it wouldn't know. It's like, oh, of course, this is data, this is fact.

Tomer Cohen (00:29:03):
Exactly. And then it doesn't always understand ties to original specs to success. You have to actually build... This is a really interesting way. When you think about how you bring those tools in, you can't just bring them in. You have to know what you feed them with. And what you feed them with is not just access. I see a lot to just focus on the connectivity and integration and it reminds me of the... This is almost like, this is actually more than 10 years ago when I was co-rebuilding the team, co-rebuilding the feed at LinkedIn and we started from scratch and I had to literally sit down and filter through examples of what is a good professional post on LinkedIn and what is not. And this was like weeks of work getting up that golden sample of examples, but it wasn't... The most important part was feeding at the right data, not all the data.

(00:29:57):
So it requires work. This is where I would say for many companies who are thinking about this phase, and I do a lot of sessions today with CPOs and COs on this process. You have to put this initial work to get the gains after. When I think about it, I think there's a takeaway there in generally with AI, even if you're learning it for the first time and so on, whether it's Cursor or whether it's design, if it's Figma or other tools or Lovable, you should be ready to invest those hours before you start seeing yourself pick up in velocity and quality, which will come up, but you have to invest that time.

Lenny Rachitsky (00:30:35):
This episode is brought to you by Miro. Every day, new headlines are scaring us about all the ways that AI is coming for our jobs, creating a lot of anxiety and fear. But a recent survey for Miro tells a different story. 76% of people believe that AI can benefit their role, but over 50% of people struggle to know when to use it. Enter Miro's innovation workspace, an intelligent platform that brings people and AI together in a shared space to get great work done. Miro has been empowering teams to transform bold ideas into the next big thing for over a decade. Today, they're at the forefront of bringing products to market even faster by unleashing the combined power of AI and human potential. Guests of this podcast often share Miro templates. I use it all the time to brainstorm ideas with my team. Teams especially can work with Miro AI to turn to unstructured data like sticky notes or screenshots into usable diagrams, product briefs, data tables, and prototypes in minutes. You don't have to be an AI master or to toggle yet another tool. The work you're already doing in Miro's Canvas is the prompt. Help your teams get great work done with Miro. Check it out at miro.com/lenny. That's M-I-R-O.com/lenny.

(00:31:46):
What's the current state of the pilot? How large is it? How many teams are doing it? What kind of stuff have you shipped? Just give us a sense of today's world.

Tomer Cohen (00:31:54):
Yeah. I wouldn't say we are yet at a very high sample rate where it's kind of a high percentage of the organization, but we have a substantial part of the organization already using it to provide a lot of the feedback. We're seeing a lot of great examples. So the way I think about the benefits is a function of experimentation volume multiplied by quality. How good are those experiments divided by the time it takes to actually pull them out, like idea to launch. So on saving times, we're seeing, whether it's PMs, designers, engineers, saving hours of work a week right now, whether it's the analyst agent we talked about or the prototyping really quickly or the product jamming experience has been a big part of that. On the quality side, we're seeing insights discussions just be much, much better. And by the way, quality and time, sometimes they help each other because it's high quality, you don't have to spend as much time on something.

(00:32:52):
So we are seeing that applied in. And the volume, I wouldn't say we had a rate where I'm seeing a high percentage organization doing it yet, but this will come once we... We haven't GA'd this internally. That will come in the next couple of months once we have all the stuff in place. But we're seeing designers and PMs picking up bugs directly from Jira tickets, pushing them in, something we haven't seen before, and there's just an appetite for everybody to just join. So in fact, the biggest thing right now is everybody wants access. Everybody wants access to the tools to be able to do it together, and we just want to make sure it's good enough to make sure the whole organization can do it really well.

Lenny Rachitsky (00:33:32):
So how is it that you're piling it? Is it some number of people have access to these agents and they just work the way they've worked with access to these tools? Or is there a team dedicated, this is the way you work now and this is it, and we'll see what happens.

Tomer Cohen (00:33:47):
So that's a great call. So basically we have a team building. It's the core team building the FSB track across all of R&D, FSB, full stack builder. And then there are pockets and pods of teams using it. So basically we are looking at specific areas that we're basically giving it to. The condition there is they give feedback. As a response for that, they make the tool better, so it's not just access. We want people who will use it. So one of your early adopters would be the ones who help [inaudible 00:34:15] up the product really well. So we're doing this in a pod model right now.

Lenny Rachitsky (00:34:19):
So it's like a pod within a larger team, like a designer, PM, engineer kind of group within... Is there an example? You have a part of LinkedIn that's trying this out?

Tomer Cohen (00:34:27):
Yeah. So if I think about some of our teams, whether it's... Actually, we just launched Semantic People Search and the Semantic Job Search as well. That team was using part of those tools to actually help build it. So that team actually, this was PMs building their own dashboards with those tools without waiting for design resources to come in. Then we have a design team who is now... This started really from the manager rolling this out. And in many ways, what I tell this team is, "Don't wait for the official GA. Start doing it. Start leaning in." We're seeing designers of that team starting to push PRs, which never happened before. And now other teams, they want to do this as well. So it's starting with this kind of grassroots experience. I would say the places have been very formal. I would say the beginning has been the top.

(00:35:22):
The product executive teams, basically we move from functional leaders, design, PM, BD, and so on to product areas leaders, and they basically rock across the stack and they also go for a 360 with all of those functions to see if they're really able to do a full stack building experience. Then we're also launching at the junior side a new program called the Associate Product Builder Program, where basically we used to have our APM program, which this is about it's ending this year. And then starting January, we're going to start having our APB program and they're going to come into LinkedIn. We're going to teach them how to code, design and PM at LinkedIn. They're going to go through a pretty rigorous training process, and then they're going to join those pods, and gradually we're going to grow that program to be a material part of LinkedIn as well.

Lenny Rachitsky (00:36:14):
Wow. So this might be the future of the APM program is this full stack builder APM-ish program.

Tomer Cohen (00:36:21):
In many ways, we've built some pretty amazing... I'm really excited for that group. I wish I could join it. But we build amazing training for them. And in many ways, we're going to use that training to think about how we roll it across the organization. We're kind of using the lens of you have great technical skills, but you're not an engineer at a company yet, or you have great design taste, but you haven't designed at scale in company yet, and we're going to teach you how to do it at LinkedIn, but the training we're going to use a lot to extend across the company as well.

Lenny Rachitsky (00:36:51):
Okay. So you have these programs, these pilots and these pods, and you said what you're looking at to see if this is something you roll out is experiment velocity times quality times time.

Tomer Cohen (00:37:01):
Divided by time.

Lenny Rachitsky (00:37:02):
Divided by time. Okay.

Tomer Cohen (00:37:03):
Yeah.

Lenny Rachitsky (00:37:04):
Got it. And I guess I know it's early, but just you said you're seeing that it's saving teams a few hours a week at this point, something like that?

Tomer Cohen (00:37:11):
Yeah. And I think the feedback has been the most important part. Right? The way to think about this is just like you build a product. So we're building this product internally and you want to experiment with some kind of early adopters who will give you feedback, and the feedback has been amazing. In fact, our top talent are the ones who are using this the most at LinkedIn. And the feedback from them has been incredible in terms because they're also willing to spend the time and give the feedback as well. And the response from them has been incredible in terms of like the quality of their output, the time they're spending on this to get the value back, their desire to be part of this and actually scale this and make this even better. So that's where a lot of the excitement has been from how they're using it and the quality we've seen there. I would say in six months or so, we'll be able to see a lot more of the organization use it and you'll start seeing those top line numbers will build as well.

Lenny Rachitsky (00:38:12):
That is a really interesting insight that the top performers are finding the most success, because there's always been this question, is AI going to just make people that are not amazing, more amazing, or is it going to make amazing people even more amazing? And it sounds like it's likely the latter.

Tomer Cohen (00:38:24):
Yes. And in many ways, it's surprising, it's not surprising. I've seen this also when we were... It's surprising because you want everybody else to be part of this and lean in. I think top talent has this tendency of continuously trying to get better at their craft and this innate need to be at the cutting edge of how you build, and I think we're seeing this here as well. This is why I had this phrase I say with the team that if we build all those tools, will they use it? And I know right now the answer is no. It's not enough to give them the tools to use it. You have to build the incentives programs, the motivation, the examples to how you do it. They need to see other people being successful as well.

(00:39:11):
And I've seen this also when we're shifting LinkedIn from a desktop company into a mobile company. It was a very similar process. It's very hard. Change management here is going to be a critical part. I think I see a lot of companies roll out their agents and just expecting companies to adopt. It doesn't work this way. Some will adopt. That tends to be your cutting edge 5% of talent that just wants new tools and they have a bias for change. But the vast majority needs to work for change management in how they do it, and that requires being a lot more thoughtful about the cultural aspect of it, which is by far from me the biggest and most important thing to do.

Lenny Rachitsky (00:39:48):
Yeah. I want to spend time there. And it makes a lot of sense why people don't spend time here because they have so much to do. They got to ship things. Their days are already busy. You have to now carve out time to learn this new tool that'll not pay off for a while. So I get why people are like, "Okay, okay, I'll get there. I'll use it someday," but they don't. This idea of culture, when I saw you share this initially, this is the third piece of making this successful. So there's the platform of getting the code base ready for people for AI to work with. Then there's the tool, like the agents you've talked about, and then there's the culture. Is there more there that you can share of just what has actually worked in helping get people on board? One thing I heard is creating a little bit of FOMO of like, okay, only a few people can use this and you have to sign up to get access. What's worked in getting people to get on board?

Tomer Cohen (00:40:39):
Yeah. I think this is where I emphasize to people that getting everything done, the platforms, the tools is not going to be sufficient. It's a prerequisite for this to work, but not sufficient for this to work because it really requires you to invest a lot in the cultural aspects of how do you get people to lean into this one. And this one might feel slow at first, but I've seen this before with our transformation of thinking from desktop to mobile. And once it picks up, it actually maintains very high velocity. One, people are really incentivized by how you define expectations for them. So to think about what is the expectation of somebody in the role, whatever-

Lenny Rachitsky (00:41:21):
So like changing performance review sort of things.

Tomer Cohen (00:41:23):
Very much so. So everything from how you hire to calibration and evaluation. And one thing I want to see there early is this kind of AI agency and fluency. Like I mentioned, the tools are there. The question is, would you use them? Because the tools will be good enough, but not great at the beginning. That's the classic thing of every good MVP tool. They're good enough, but they're not great. And then you kind of want to build that agency to make the tool better. We're in this kind of notion of we're going to make this better for LinkedIn together. Two is piloting success inside of your organization. That's the pod model where you're showing that not only this could work, it's actually having success. So we have even our partnerships team, our BD team, being able to go instead of relying on waiting for an engineer to help build the developer portal and build the connectors there.

(00:42:17):
Literally one of our head of partnerships just went and did it himself. Didn't even delegate to his team. And their goal is to say like, "Hey, I can do it. You can do it as well." Those examples are really, really powerful. I talked about the associate product builder program where we are going to be very focused on training. I think that will send a really strong message across the organization. People will see this talent and what they can do, and I think that will create that movement. But celebrating wins in all hands, highlighting people and showing those examples. One example we've seen recently, people really looked at it in a surprise lens, but then it kind of, I think, really opened up a lens for them. We had somebody in our user research team. We had an opening for a PM on the growth team, and that role was open for a while, and she said that, "I think I can do it."

(00:43:11):
And she used all these tools. This is a user researcher becoming a growth PM, not usually the career path you see, but she was excited about the area. She used all those tools, and she's now a growth PM on the team. And really, you can start thinking about her more as a full stack builder ultimately. But seeing those openings and then highlighting those two people, actually people who are doing this have been a great example of it. And then just making sure that those tools are accessible. People can provide feedback, you share a lot, has been an incredible part of this. It's not enough to be top-down directive that this is how we want to work. People want to feel like there are success stories. They feel like it's worth their time. It feels it's a movement they want to be part of, and then ultimately they can see successes in how they do it.

Lenny Rachitsky (00:44:02):
I love this kind of comparison to the shift to mobile. We all went through that and there's all these stories of companies requiring you to show mobile mocks. That's the only way we're going to operate. Now everything you have to ship has to be on mobile, and it's interesting how similar this is to them, to that experience. And so a few things you just shared here just to kind of summarize some of the things that have worked for you. Showing wins, celebrating wins, showing people what other folks are doing with AI tools, creating a program that people enroll into and make it a little bit exclusive. This performance review piece is really interesting because that really will change people's behaviors. Here's how we get promoted. Have you actually already made that change to the PM? I guess it's every track, I imagine, not just product management. Have you already made that change or is it kind of like a work in progress?

Tomer Cohen (00:44:45):
So there was two aspects to it. Once I moved my team, my directs, we did 360 for them. So their 360 was, if you came from PM, you had the designers on your team rate you. And so that had its own, and then we shared those with them, and that had its own kind of motivation. But then we broadly took it across. So when we hire right now, we look for those. And then this upcoming cycle, we do a bi-annual. That's going to be part of the performance evaluation piece and we announce it to everybody. And for what, it's where people are excited to show. And they're excited to know how they're going to be... It's always about, like, "I want to know how I'm being rated or evaluated." So just being able to show those examples has been a big part of it.

(00:45:31):
The other thing I would say, it takes time for this program and its formality to roll out across the entire organization, and I was intentionally not trying to be quick at rolling this out to everybody because I think that just dilutes the value of it really quickly because it's not about... I could care less about your title. I care about how you work. So calling you a full stack builder is not what I'm looking for. Changing your mindset to a full stack mindset is what I'm looking for. You're thinking you can do the whole thing. You're looking at those tools and looking at how to do it.

(00:46:07):
So one of the things I've said is if you're looking for a formal reorg or declaration to start building differently, you're waiting too long. Look, my biggest thing is here's a permission for me to just not wait and just go. So whether or not you have the right tools or not, go build the tool, use a tool from the outside, bring it in, show those examples. In many ways, prove that you are a full stack builder in mindset before anything else come to mind. And that just naturally will happen, and that's also where we've seen some of our best talent just goes and leans a lot into.

Lenny Rachitsky (00:46:41):
I love that. I was going to actually mention that quote. Someone you shared, you work with told me exactly that quote you just shared, so I'm glad you brought it up of just if you're waiting for a reorg, you're not thinking about it the right way. How do you encourage people to actually play with these tools on their own? Are you just like, "Go take a few days to play with AI?" Is it just try it? Or is there anything formal you've seen of just getting people to more try this on their own without joining this program?

Tomer Cohen (00:47:05):
A lot of the tools we've made, we've been sharing them regularly. A few of my all hands have been all about how to use those tools. But then at the same time, we're kind of inviting, have you found a new tool that works really well for you? Share it, show it. Again, it could be Slack, could be Messages, Teams and so on, how you do it. But the idea is really to start getting that investment in how things work. Actually, I think in general, you can feel overwhelmed by tools right now, by recipes and how to do things like what's your prompt and what's my prompt. But really it's finding something that kind of works really well, that can gravitate around and really invest in that's been those areas. But I think we've had this invitation to go and explore and go and bring in stuff that you think are great. And in many ways, bring others along on the journey. It's one good way to make the influence much bigger than a few folks who are doing really well with this.

Lenny Rachitsky (00:48:00):
Are there any surprises on the negative side that have come out of this, of PRD is just feeling like AI driven, people slowing down unexpectedly? Is there anything that surprised you of just like, "Okay, this is actually not great"?

Tomer Cohen (00:48:12):
Yeah, we mentioned a few of them. I was hoping for some tools to work off the shelf really well. It was never the case because we had to invest quite a lot.

Lenny Rachitsky (00:48:21):
Never the case.

Tomer Cohen (00:48:21):
Never the case. We had to invest quite a lot. And again, part of it is we just have a lot of legacy information and code based and knowledge and designs and so on. So a lot of the companies we work with are seeing this as a great growth opportunity for them as well to invest, but I do think it's a big area of investment as well. We talked about not just giving access to all of your context which we started with, and we were like, "Oh, here's access to all the drive, all information," failed miserably and hallucinates like crazy." People gravitating towards different tools, like our goal was to converge on tools, but that was pretty hard.

(00:48:58):
And then I think in terms of quality, we've just seen better quality, but I think it's because, again, where we are in the stage is still the early adopters and they're doing a few iterations in terms of how to do it. But I would say the tooling adoption is hard. And then I think for some people, this is important for me to kind of state, some people do not want to be full-stack builders, and that's completely okay. Some people see themselves in specialization, and I think specialization has a place and a role. So I didn't want the message to be across the organization I expect everybody to be a full-stack builder. I do not. I think there are system builders that empower full-stack builders, and then you have people who are specialized. But I don't think we need as many specialized people as we did in the past.

Lenny Rachitsky (00:49:46):
I didn't actually realize this until just now. So is this their title now instead of product manager engineer, they're full stack builder?

Tomer Cohen (00:49:52):
We have a full stack builder title formally inside the organization, and we are gradually putting people in that bucket.

Lenny Rachitsky (00:49:59):
So there's a whole career ladder that's forming. There's a whole... Okay. That's a bigger deal than I even thought. So where are you finding these folks mostly coming from, like product, engineering, design? I imagine it's a mix, but just is there a most common trend?

Tomer Cohen (00:50:13):
It's a mix. People listening, I would just think about just go over your org and imagine who can do it, who can right now flex across those functions, whether it is engineering, design, product, even BD, and what you'll find is there's already quite a few that can flex across.

Lenny Rachitsky (00:50:34):
Interesting. Are there any functions you think are especially successful at this? Not to play any favorites, but I don't know. Are you finding like, okay? Or you could also not highlight any specific.

Tomer Cohen (00:50:45):
No, I think it's a mental model of how you do it. I think if I were to play what's the hardest craft to potentially learn, I think design has a lot more work to get the design agents to be really, really good. So I think designers have a little bit of a leg up in terms of others learning their craft than the vice versa. But I honestly think it's a mindset. I've seen designers code, I've seen PMs kind of design and do well. And this is why I think when you kind of step back and you think about people in your organization and who can flex, I think you'll see them show up in many areas. And what I think you'll find there is they have the agency, they're leaning into new things, they have the fluency, like they're already building new experiences and they have that growth mindset that they just want to get better, so it doesn't matter what they learn at school or what label somebody put in them when they join the company.

Lenny Rachitsky (00:51:44):
What I love about a lot of this is it's the easiest time to transition between different product roles than it's ever been. Design's moving to PM, and sure, or just moving to this new role, it makes it so much easier to, like you said, that researcher became a growth PM.

Tomer Cohen (00:51:58):
And this is probably my biggest advice slash motivation I give to the team because what I tell them is ultimately... By the way, this is for me as well. I think about it the same way. The incentives for you are so aligned with your organization of what we're asking for, right? Because we need you to change. We want to be a more agile, adaptive, resilient organization that can deal with the pace of change, but you want as well for your own career. You want to be at the cutting edge of how you build. So the incentives are really aligned between what you need for your own career and what the organization needs you to do. So there's that permission to go and do it for me is ideally kind of a tailwind in what they want to do more than anything else.

Lenny Rachitsky (00:52:46):
Maybe a last question for people that are inspired and like, "Okay, this is what we need to be doing," any just tips for someone starting down this road to be successful at trying something like this at their company?

Tomer Cohen (00:52:58):
I would say I would start with the notion of how do you want to bring this just structure. I would think about the platform you need to build, the tools you want to bring, and then I would spend a lot of time on the culture. Platform and tools I think would be, again, a prerequisite, but not sufficient, and the cultural aspect is really important. I would think a lot about how you bring people along. So for one of the learnings we had that probably able to do it differently right now, if I were to redo this program was, for a while I was working very closely with my core team on it, the core kind of full stack building team that were in charge of building all this material, but the organization was always asking questions. "What's going on? Who is doing it? What are the tools?" And in retrospect, we could have done a lot more in the flow to just show them and get them to already use early tools or be aware of it versus doing a small team on the side.

(00:53:49):
So it's okay to start with a small team. I think it's really important. But at the same time, just making sure there's visibility across the whole thing is really powerful. Being patient and being willing to invest. I always give this example of, we always give this example of like, "Oh, look at this startup. They built this in a week." Yes, you can build lifestyle in a week right now if you start from scratch. It's actually not hard. But when you are trying to transform a large organization, you want to have this impatient about the goal and you have to have a high ambition, but being very thoughtful and patient about how you bring it to life and the key things you have to invest in. If you don't invest in your platform, I just don't see how this could be a successful outcome. If you don't invest in customizing the tools for you, then you're just going to get vanilla generic agents from the outside.

(00:54:39):
So being aware of the investment and making sure you actually allocate resource to it, this is kind of the classic, be willing to invest upfront so you can reap the benefit after, versus saying, "Hey, why am I not seeing us moving into 2X the productivity in a week?" That's not going to be this way. You can see it with some people, but starting to collect those examples and starting to really think about the transformation is really key.

Lenny Rachitsky (00:55:05):
This is so incredibly cool. I know that a lot of CPOs and heads of product and all kinds of leaders are reaching out to you trying to figure out what you've learned how to do this. So I love that we went deep on all these things. Just final question, is there anything else that we haven't shared that you think might be helpful for listeners to hear or maybe just to double down on before we get to our very exciting lightning round?

Tomer Cohen (00:55:26):
Whether you're in an organization, you're waiting for your leader to roll this out or you're a leader trying to roll this out, I would not wait. The first thing I've done, which I thought in retrospect was very hopeful is I did announce this upfront we are going to this mode. We're starting in pockets, we're starting in pods, we're building the tools, but this is the mountain we're going to go after, and in many ways, we're going to make it great. I also announced that this is not just an end state, it's a kind of continuous progress. There's no state we're going to get to as much as continuously just trying to be better. And in many ways, to compete, you just want to be better than others in how you build because the version of building will completely just transform itself every few years or so.

(00:56:13):
So do not wait. Really focus on the progress you're making, over communicate with your team, not just the vision, but also the progress you're making, almost like holding yourself responsible. If you're a leader, give yourself KPIs you share with your own teams or OKRs. And if you're inside of the organization, and I would say whether or not or not your CPO or your CEO is announcing this type of program, go do it or join an organization that does it so you can be at the cutting edge of how you build in the future.

Lenny Rachitsky (00:56:43):
Tomer, with that, we've reached our very exciting lightning round. I've got five questions for you. Are you ready?

Tomer Cohen (00:56:48):
I'm ready.

Lenny Rachitsky (00:56:49):
First question, what are two or three books you find yourself recommending most to other people?

Tomer Cohen (00:56:54):
I love to give trios of books that I really like. So my current trio is, they're very diverse in topics, so apologies if it's not falling all into tech. But the first one is called Why Nations Fail. It's a book I read a decade ago even more and the authors of it just won the Nobel Prize last year. And it basically talks about why does some nations succeed and some fail? And it's not the usual explanations we go for, which is, oh, it's culture, it's natural resources, it's the kind of religion. A lot of those tends to be the kind of immediate excuses people have. It kind of falls into two camps. Are there extractive or inclusive institutions? Can people participate broadly and opportunities shared or there are institutions that basically are supposed to be attracting from many and give to some.

(00:57:48):
So it's just an incredible way to just think about how you build a nation. And for us at LinkedIn, we think a lot about the idea of opportunities, so how you build a product as well. And it's just a good way to move away from easy explanations into what really makes a country really successful as well. Second book, it's called Outlive. It's really about the idea, it's kind of like the author, Peter Attia talks about the idea of medicine 3.0, which is really the notion of building personalized medicine, which I think in the world of AI will become incredible in the future. But it's all those, let's call those categories that you should think about for your life so you can just optimize your health as much as possible and goes for everything through fitness to diet to the biggest health factors you should think about. But it's a great long book. Then lastly-

Lenny Rachitsky (00:58:41):
The one in my bookshelf behind me.

Tomer Cohen (00:58:42):
There you go.

Lenny Rachitsky (00:58:43):
It's up top. You can't actually see it, I think.

Tomer Cohen (00:58:47):
And then lastly, it's a book that also came out many years ago, but it's called The Beginning of Infinity, which I really like, by Deutsche. It wasn't an easy read for me, but I love the idea. In fact, especially in products, I love the idea of cause and effect, like really finding great explanations for why things happen and then building on top of that your next iterations. And this book really pushes on the idea of explanations that only once we have a clear understanding of what things happens, then we can have breakthroughs on top of that. But until we get to a point of clear scientific breakthroughs, we are not going to make significant progress. But when you do that, it's really almost like infinite progress you can make on top of that.

Lenny Rachitsky (00:59:33):
Naval's always talking about that last book. I think I bought it and it was just hard reading this.

Tomer Cohen (00:59:39):
It's not an easy read, at least for me. It wasn't an easy read, but it's a very powerful read.

Lenny Rachitsky (00:59:41):
Awesome. Is there a favorite recent movie or TV show you really enjoyed?

Tomer Cohen (00:59:46):
Can I do a podcast?

Lenny Rachitsky (00:59:48):
Absolutely.

Tomer Cohen (00:59:50):
So there's a podcast in, it's in Hebrew, it's called One Song, and it takes a song that generally is ideally popular and then goes really deep on the origin and the history of the song, and I love it. I love music and just dissects songs so well. It does a great job also in bringing to life the story behind it. So for me, it just goes back to you thought the song was about something, but then it goes really deep into the actors behind the song, and sometimes it's the words chosen or it's how the lyrics match the music itself, and I just really enjoy that one.

Lenny Rachitsky (01:00:30):
There's a podcast called Song Exploder, I believe, that is a similar concept that's not in Hebrew, in English, that I'll point people to if you love that one.

Tomer Cohen (01:00:39):
That's awesome.

Lenny Rachitsky (01:00:40):
Is there a product you've recently discovered that you really love? Could be an app, could be some clothing, could be a kitchen gadget, type gadget.

Tomer Cohen (01:00:48):
Can it can be a product I want to have, which I think is actually really easy to do?

Lenny Rachitsky (01:00:53):
I love that. This is a product thinking 101 and just the vision of what you want to see.

Tomer Cohen (01:00:58):
So in my car right now, there's Alexa built-in, which is great because the kids can ask for songs all day long and it's a whole show inside of the car. But one of my favorite things to do when this has been doing it for well over two years is I go in and I go into voice mode.

Lenny Rachitsky (01:01:17):
ChatGPT.

Tomer Cohen (01:01:18):
Yeah, ChatGPT, and then just have a conversation, and that's just friction. I would love to have on my steering wheel a button that invokes my AI friend that can sit next to me in the passenger seat, and I just think that would be such a... I actually think it would [inaudible 01:01:36] rides for people. Just that movement, that's just like elimination of friction will transform the experience for me.

Lenny Rachitsky (01:01:43):
On that note, I recently discovered Teslas actually do this now. If you hold the right wheel, Grok appears and you could talk to Grok. So it's here. The AI has arrived. Yeah. I just did it by accident and then it's, "Okay, cool."

Tomer Cohen (01:02:01):
Great. So for me, if anybody from Rivian is listening, please bring this in the car.

Lenny Rachitsky (01:02:06):
Rivian's falling behind. Yeah. And you have to use Grok. It'd be cool if you could switch to different AIs because it has a personality. Just give me information. I don't need you to laugh and give me jokes.

Tomer Cohen (01:02:20):
Did you need to spend some time with it before or did it have any memory from... Did you bring any memory into it?

Lenny Rachitsky (01:02:27):
There's a logged out version and then you could just log in and it connects to your account. Yeah, it's extremely cool. No one's talking about it. It's crazy because I don't know if they launched it fully, but it just appeared.

Tomer Cohen (01:02:38):
Do you talk in the car a lot to it?

Lenny Rachitsky (01:02:41):
I don't use it that much, to be honest, but I should. My wife just doesn't love Grok. I think the brand of Grok is a specific brand. And so she's like, "Don't talk to Grok in here with me."

Tomer Cohen (01:02:52):
I love voice mode, so I use it all the time.

Lenny Rachitsky (01:02:55):
Yeah, I love voice mode too. It just interrupts too often. That's the issue there, right? It's just it stops.

Tomer Cohen (01:02:59):
By the way, you can set it up. You can basically say like, "Hey, just let me finish."

Lenny Rachitsky (01:03:03):
I now know that. I'm learning so much. Okay. Two more questions. Do you have a life motto that you often find useful in work or in life?

Tomer Cohen (01:03:11):
I think last time I talked about it, I most associated here with, I might be wrong, but I'm not confused, although I don't say it as much anymore. But I think the one I love, growth mindset is a second religions for us at home. And one thing I love about, there's a phrase there that is becoming is better than being, which I think ties into the FSB mode a little bit, which is you're always in progress mode, iteration mode. It's not about reaching a state. It's about the journey, the process. That's what you should fall in love with. It's about continuously growing and evolving without the negativity of it or there's no sense of FOMO there. It's just this continuous thing. If I look back a year from now and I look back, how much did I grow? How much do I know? What skills to do that again? Where are I becoming better? Do I feel like Tomer version 2026 versus 2025? What's the delta there? And I kind of love that as a way of thinking.

Lenny Rachitsky (01:04:13):
A great segue to our final question. By the time this episode comes out, it won't be a secret that you're leaving LinkedIn after 14 years. Legendary run. You joined way before the acquisition, you helped them integrate. Just like the way LinkedIn was perceived 14 years ago is so radically different from the way it is today. It's actually really fun and interesting to be there versus how people for a long time felt about LinkedIn. So I guess the question just how you feeling and what's next? I imagine you're going to get a lot of calls from a lot of people, but what are you planning?

Tomer Cohen (01:04:48):
Yeah, so I feel proud. It's been an incredible ride at LinkedIn. The way I've got to know about LinkedIn deeply the very first time was when I moved to the Valley and I went to a lecture at Stanford about social networks in 2008 and Reid was there and he talked about the power of being a professional communities online, and I was very nerdy about it and thought it was incredible vision, had no plans to join and actually started my own company after. But as luck would have it, found myself joining a few years after and just thought the mission was incredible. So in many ways it aligned with my purpose and just was an incredible ride to be here.

(01:05:32):
And I also feel very grateful. I shared this with the company recently. I was starting to take learnings from my experiences here. A lot of it was from tough situations. We had a lot of tough situations at LinkedIn and hard calls and late nights, but you learn so much from those and I'm just incredibly grateful. And I'm excited. I'm excited. I have a bias for change. I have a bias for kind of positioning myself in a place where I can learn the most and learn a lot. And it's an incredible time to build, so I'm just excited to be thinking of new problem sets and new areas where I can go deep on and invest the next decade in.

Lenny Rachitsky (01:06:13):
I think it's going to take a long time for you to not feel like you're working on LinkedIn and to forget about all the things that you have been worrying about for so many years.

Tomer Cohen (01:06:20):
After you build something for such a long time, and I think you and I talked about it at one point, that I think one of the best traits for a builder is to become very passionate with what they're building. Really care. Not about the job. It's really care about the product. When you feel the pain when somebody complains and you kind of have this continuous discontent, and it's like for me, it's the notion of raising a baby. So yeah, it's hard. It will be hard. I will always think of LinkedIn as one of the babies I helped grow.

Lenny Rachitsky (01:06:53):
Well, I'm excited to have you back someday when you figure out what you want to do next and or start whatever you're doing. I love that this was an excuse to get to know you. Tomer, thank you so much for being here.

Tomer Cohen (01:07:03):
It was great to be here. Thanks, Lenny.

Lenny Rachitsky (01:07:04):
Bye, everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

---

## Why most public speaking advice is wrong—and how to finally overcome anxiety | Tristan de Montebello
**Guest:** Tristan de Montebello  
**Published:** 2024-10-13  
**YouTube:** https://www.youtube.com/watch?v=BQM3Yq93nVc  
**Tags:** growth, a/b testing, experimentation, monetization, culture, management, vision, market, design, ui  

# Why most public speaking advice is wrong—and how to finally overcome anxiety | Tristan de Montebello

## Transcript

Tristan de Montebello (00:00:00):
People tend to get into a public speaking voice. We'll be in a class and they'll be chatting normally and look super normal. And then we'll say, "Okay, now just a timer, I'm just going to give you a speech. Just speak for 60 seconds so we get a baseline," and I click play, and suddenly I say, "The important part about doing this," and they enter into a different version of themselves, a professional version, whatever that would mean. It's so much more freeing, powerful, connecting, and effective to speak conversation. So the cue I often give people is-

Lenny Rachitsky (00:00:36):
Today my guest is Tristan de Montebello. Tristan is the co-Creator of Ultraspeaking, which is the best public speaking workshop I have ever come across. In 2017, Tristan became the fastest competitor to reach the finals of the world championship of public speaking. And based on that experience, built a very unique course that helps you quickly build the skills to become better and to become more comfortable speaking in public, and especially speaking on the spot.

(00:01:04):
I'd like to spend time on this topic on this podcast because becoming a better speaker is such an accelerant of your professional life. And in this episode, we delve into a bunch of tactics and also misconceptions about how to become a better speaker, and to make it even more fun and interesting, we go through a few of the exercises that Tristan and his team have developed live on the podcast. He goes through them, I go through them, it was a lot of fun. I'm excited to hear what you think. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. It's the best way to avoid missing future episodes and it helps the podcast tremendously. With that, I bring you, Tristan de Montebello.

(00:01:45):
Tristan, thank you so much for joining me and welcome to the podcast.

Tristan de Montebello (00:01:49):
Thanks so much for having me.

Lenny Rachitsky (00:01:51):
So I took an abridged version of this speaking course that you teach called Ultraspeaking, and it immediately made me feel more comfortable public speaking, which I've never felt doing any other course. Public speaking is something it's just is very scary to me as it is for a lot of people, but it's just something I really dread. Even doing these podcast episodes, every time I get nervous before doing these things, as much as it may not seem that way. So this is not my natural habitat speaking, being in public. It may not seem that way to people, but it's true.

(00:02:22):
And the way you approach this stuff is so unique and worked for me. And because of that, I thought it'd be awesome to just bring you on this podcast and basically try to teach people the stuff that you've learned about how to become a better public speaker. I know we're not going to do your course here, but just, what are some very tactical things people can immediately start to apply? And also, I want to make the super interactive, so we're actually going to do some of the exercises that you use in your class. So that's what we're here for. How does that sound?

Tristan de Montebello (00:02:54):
That sounds exciting. I'm in.

Lenny Rachitsky (00:02:56):
Great.

(00:02:59):
This episode is brought to you by Eppo. Eppo is a next-generation, A/B testing and feature management platform built by alums of Airbnb and Snowflake for modern growth teams. Companies like Twitch, Miro, ClickUp and DraftKings rely on Eppo to power their experiments. Experimentation is increasingly essential for driving growth and for understanding the performance of new features. And Eppo helps you increase experimentation velocity while unlocking rigorous, deep analysis in a way that no other commercial tool does. When I was at Airbnb, one of the things that I loved most was our experimentation platform, where I could set up experiments easily, troubleshoot issues, and analyze performance all on my own. Eppo does all that and more with advanced statistical methods that can help you shave weeks off experiment time and accessible UI for diving deeper into performance, and out-of-the-box reporting that helps you avoid annoying prolonged analytic cycles.

(00:03:52):
Eppo also makes it easy for you to share experiment insights with your team, sparking new ideas for the A/B testing flywheel. Eppo powers experimentation across every use case, including product, growth, machine learning, monetization, and email marketing. Check out Eppo at geteppo.com/lenny and 10X your experiment velocity. That's geteppo.com/lenny.

(00:04:18):
Today's episode is brought to you by Command AI. If you're like me and most users that I've built product for, you're probably used to chatbots at the bottom right of websites, where you ask a question and it says something like, " Check out these three helpful articles. Did that answer your question?" And then you click away and then a few seconds later you get bombarded with some other useless pop-ups. For those of us who work on software, no one wants their product to feel like this. Command AI is an AI power toolkit for support, product, growth and marketing teams that embeds in your company's product. The AI support agent can deflect upwards of 80% of support questions, providing actually useful answers, and it can magically co-browse with your users to show them around your interface. They do pop-ups too, but their nudges are based on in-product behaviors like confusion or intent classification, which makes them much less annoying and much more impactful.

(00:05:11):
Command AI works with web apps, mobile apps and websites, and they work with industry-leading companies like Gusto, Freshworks, HashiCorp, LaunchDarkly, and over 25 million end users interact with Command AI interfaces. To try out Command AI. You can sign up at command.ai/lenny and experience a custom demo of how it works in your app. That's command.ai/lenny.

(00:05:36):
Okay, so let me first ask just kind of a broad question. What do most people get wrong about public speaking? What are some of, what's maybe the biggest misconception about how to become a better public speaker and how to be good at it?

Tristan de Montebello (00:05:49):
I actually think that the biggest misconception with tackling your speaking is that people grossly underestimate just how transformative it could be to your life. And the reason it's so transformative is because speaking is not a specialized skill, it's a meta skill. That means that the better you get at speaking, the better your life gets.

(00:06:16):
So an example of a meta skill is fitness, for example. If you were to start saying, "Okay, I'm going to transform my fitness," and you start lifting weights and you start going on runs, obviously your muscles are going to get bigger, you're going to get more in shape, and your cardiovascular system is going to improve. But that's actually only a sliver of the impact it's going to have on your life because you're going to start feeling more energy, and you're going to start having these nice hormones, these endorphins flowing through your body and you're going to feel better about yourself. And when you walk in front of the mirror, suddenly you're going to have a boost in confidence. So naturally, everything else in your life is going to start to improve as a result of you focusing on your fitness. And for speaking, it's the same thing.

(00:07:01):
This blew my mind when I went on my own speaking journey, is when I started making breakthroughs in speaking, other things started to feel different. So as you get breakthroughs, how you feel at work feels different. How you feel in your group of friends feels different. How you feel in a group of strangers, especially, how you feel and your family can even be impacted. This seeps into everything else in your life. But the thing is, because there's so much self-consciousness that goes with speaking, we often feel kind of constraints under the layers of overthinking and anxiety that come with speaking. So it can be hard to realize that underneath these layers, you actually have this extraordinary superpower, because as humans we're evolved to speak, this is what we are. So you don't need to teach a baby how to speak, it will learn by itself with no formal education. So what that means is, we all have this incredible hardware.

(00:08:12):
The thing is, over the course of our life, because of all these little situations that happen, we start getting bugs in the software and we're not really upgrading our software. The moment you get the bugs and things start working, not working, we start avoiding, and suddenly it's like we're not upgrading our software anymore. So we're stuck on old, buggy software. But the reality is, let's not forget that we have incredible software that were evolved for this. So all we need to do is some debugging and some upgrading of the software and suddenly your entire life can change. So that's really one I want to impart on anybody listening. You have it in, you already have what it takes.

Lenny Rachitsky (00:08:56):
Okay. So kind of building on what you just talked about, some of this insight of, your life can improve and how you kind of always have to unlearn stuff. One of my favorite maybe core insights and tenets of the way you approach teaching people to speak, is you talk about how if you don't enjoy speaking, you're doing it wrong. And that really helped me because you kind of encourage, you kind of remind people, try to have fun as you're doing. Can you just talk about that insight and why that's important and how that helps people become better?

Tristan de Montebello (00:09:26):
Well, I think that's very tied to what you were saying. I see enjoyment as a barometer, if I'm doing things right, I'm probably enjoying myself. If I'm doing things wrong, particularly with speaking, because again, this is something we're naturally evolved to do. So if we're naturally evolved to do it, it's not something that we dislike doing. It has to be something that rewards us. So as soon as things start not feeling enjoyable, it's a sign, hey, I'm probably doing this wrong, guy. There's something here that I'm doing that is making this unenjoyable that's probably not helping me.

(00:10:03):
And I think you mentioned that in those people who can hold an audience who are really good communicators in business, it looks like they feel very comfortable, it looks like they feel like themselves. And if you think about speaking, when you're talking with your kids, or with your partner, or with your best friend, your childhood friend, your parents, ever, we all have environments where we feel completely like ourselves. And when we do, communication is extraordinarily enjoyable. It's just a means to connect with other people, a means to share what we have on our mind and it's very, very empowering and it feels very good.

(00:10:42):
Then I take the same person with the same skill set and the same ability and I bring them in a business setting, and suddenly I don't feel like myself anymore. And because of the pressure, I start trying to speak differently. So people start having, I'm going to try to think really hard of what I need to say and I want to control the words that are going to come out of my mouth before they come out of my mouth so I make sure I don't make a mistake. And you basically loop in this thing that is so counter what communication is, which is just a natural subconscious scale. So using speaking as a barometer of, hey, if this is not feeling good, I'm probably overthinking. I probably need to relax and try to just feel a little bit more like myself.

(00:11:27):
But this also applies to practice, where in your practice, because this is not an overnight thing, you can't just snap your fingers, read a book, and be a better speaker. Well, your practice has to be enjoyable as well because otherwise two weeks in, you're going to quit just like a shitty fitness journey or diet. Right? You have to find joy in it and it has to be structured in a way where it rewards you as well, so that you get more energy and you get more enjoyment while you do it.

Lenny Rachitsky (00:11:58):
Awesome, and we're going to show people how you do that. You do these games, they're games that you play that help you actually learn these skills. So before that, and also I want to get into actual tactics that we can just give people to become better public speakers. But right before we get there, are there any other core insights or principles or lessons that are fundamental to the way you found that it works to become a better public speaker, that kind of inform a lot of the stuff we're going to be talking about?

Tristan de Montebello (00:12:25):
The day I understood that speaking was a subconscious flow-oriented process and not a conscious process, completely changed the way I approached it. So instead of thinking tactics and frameworks and adding more to the outside of the things I need to think about, when I realized when I speak best, I'm actually not thinking about speaking. It's the last thing I think about is the speaking part. I'm completely in tune with whatever it is I'm trying to convey to my audience or the person in front of me. And the goal is to get into a flow state and stay in that flow state all the way through the finish line. That's what really, really changed my mindset about speaking, because then it changes all of the exercise, the exercises you want to do. It changes how you can think about speaking.

(00:13:24):
And one of the ways that changed how I practiced was, instead of focusing on the symptoms of speaking, I started to try and figure out, well, what are the root causes that create these symptoms, and can I address those? So instead of counting my filler words, if that's something that's annoying to me, I'm going to go back and try to figure out, well, what's the root cause of that? Well, the root cause of having lots of filler words or racing in your speaking, is that you probably struggle to feel comfortable slowing down, relaxing, or even pausing when your mind is racing and you feel pressure. Solve that, and not only do the filler words take care of themselves, but the racing takes care of itself and you suddenly have more mind space.

(00:14:11):
And if you feel super constrained in your speaking, very monotonous, then maybe you feel boxed in and you're struggling to allow yourself to feel to be all of what you are under pressure because there's probably a lack of certainty. A lack of trust in, hey, if I let myself be more intense or if I let some of these emotions pop out, or if I take a time to gather my thoughts, is everything going to unravel, or is that going to work for me? And if you haven't proven that to yourself, then you're just going to go for safety and so you're going to be very monotonous and constrained, and that's creates monotony. But if I can solve that, suddenly I have freedom. So thinking through this and understanding that the goal here is upgrading the software and it's really layering, taking all the bad habits away and putting in new habits that I can just stay in this flow state without getting pulled out, that really changes the game.

Lenny Rachitsky (00:15:15):
That is a really interesting insight, and I love that you actually demoed that in the way you answered this question, where you took time to get into that state and not just get, um... It's just like, pause.

Tristan de Montebello (00:15:28):
Pause.

Lenny Rachitsky (00:15:29):
Yeah, that was a really beautiful example of that. Okay, let's get into a few tactics just to give people something they can-

Tristan de Montebello (00:15:29):
Sure.

Lenny Rachitsky (00:15:34):
... actually change about the way they speak this week. What are two or three things that you can recommend people tweak in the way that they do public speaking, in the way they speak in meetings and presentations, whatever?

Tristan de Montebello (00:15:47):
I actually thought about this because once you think about speaking being much more about the root causes, like play the games that are going to change you at the root, don't focus on the symptoms, then you find yourself sharing much less purely tactical advice and frameworks because we're trying to get out of our brain into our subconscious.

(00:16:10):
So when I thought about it, I thought of three things I wanted to share. One makes you sound better or look better, one makes you sound better, and one makes you feel better. So the first makes you look better. Now this is super basic and very crunchy, but it's a bad habit that a lot of people have. That when I am trying to gather my thoughts or think, people tend to look down. And if you're looking down on Zoom, it's three times as bad because it looks like you're looking at your phone or looking at notes if you had any, but even when you're in person, it doesn't look very confident. And so you're suddenly giving off of that vibe of, oh, this person feels a little bit uncertain here, and maybe it's going to look like you stopped speaking and you might get more interrupted.

(00:16:56):
If instead you switch that up and you start thinking up. I think up into the right, but you can think in any direction you want, but as long as you're looking up, you actually look thoughtful by default. So suddenly you're looking thoughtful. That means you look more confident because anybody who'd be willing to pause in their speaking is somebody who's confident. And as a result, you're much less likely to get interrupted. So it's a small tweak but makes a real difference.

(00:17:24):
The only thing is if you're not used to doing this, if this is not your habit, then it's going to feel a little bit awkward the first time you do it and you probably won't think about doing it. So I recommend writing, think up, on a post-it and putting it on your computer so that it's there for you. And then once you've done it a few times, this will become the new normal and by default, you'll look more confident.

Lenny Rachitsky (00:17:46):
I'm going to do this as we talk. I have a poster right here. Think up.,

Tristan de Montebello (00:17:48):
Oh, nice. Think up.

Lenny Rachitsky (00:17:50):
Okay, great. What else?

Tristan de Montebello (00:17:53):
Look more confident. Now how to sound more confident. This is a really important one, and this concept is called end strong. And it's, we had to bring this up because most people tend to end weak. And why is that? They put freestyle rappers in an fMRI, and what they found out is freestyle rappers have to enter a deep flow state. If you're freestyle rapping, you have a beat, you don't have any lyrics, and you have to get into the beat and invent the lyrics and the melody and everything on the fly. So there's no choice but being completely present. What happens is you can see their brain and it's lit up in a very specific place that shows that they're in flow, and when they get to the very end, the brain just blows up. Before they finish, they start getting pulled out of flow. And this is the same feeling of you're running at school and you see the finish line and just a few yards before you start slowing down. It's just, I don't know, we're built that way.

(00:18:53):
And in speaking, it's the same thing. People tend to give a great answer and then either they kind of taper off at the end, which doesn't leave you with a good impression, or they'll actively say the doubts that are coming up in their mind of maybe they'll be giving a great answer and then suddenly they say, "I don't really know if that makes sense."

Lenny Rachitsky (00:19:10):
I do that all the time. That's very relatable.

Tristan de Montebello (00:19:13):
Yeah, but what the thing is, what happens when you do that? When you do that, it's like you're forcing this lens on your audience, where now even if they had the best of experiences with your answer, now they're looking at everything you said through the lens of, oh, this person was kind of uncertain. So it's like you had a very smooth flight across the Atlantic and your landing was absolutely horrible. You were bumpy when you were coming up, and then when you hit the landing, you bounced three times and you thought you were going to die. You're not going to remember the smooth flight, you're going to remember the ending. So a simple tactic here is, anticipate that as you get to the end of anything you're saying, you're going to naturally start regaining consciousness and you're going to start being a little bit more self-aware, and some of those uncertainties are going to pop up. Know that it's coming and make sure you land the plane.

(00:20:14):
So what that looks like is, either you just make your ending sound like an ending and then leave it at that, or you can prompt your brain. You can use summary prompts, this is incredibly powerful. It just means you say the beginning of a sentence or the beginning of, yeah, the beginning of a sentence, and your brain's going to fill in the gap. It's going to. You're prompting your brain and your brain will always deliver. So you get to the end, you're like, okay, I got to wrap up now. And so you'll say, "So to wrap up..." And your brain's going to fill in the gap. Or, "In summary, so my point here is, so what I want you to remember," and you just place those words and your brain's naturally going to do the work of closing it for you. But make sure you don't let go of the gas pedal at the very last moment, you need to land that plane.

Lenny Rachitsky (00:21:01):
Awesome. I could definitely get better at this, great tip.

Tristan de Montebello (00:21:04):
Yeah, thanks.

Lenny Rachitsky (00:21:06):
I'm going to try to do that as we talk.

Tristan de Montebello (00:21:07):
Yes.

Lenny Rachitsky (00:21:07):
And what else we got?

Tristan de Montebello (00:21:09):
I'll be paying attention to that.

Lenny Rachitsky (00:21:11):
Okay, pressure.

Tristan de Montebello (00:21:15):
Yeah. The third one is staying in character. And these go hand in hand. And what's really powerful is when you start doing these, there's a beautiful feedback loop that happens that gives you a lot of confidence. So staying in character I said is the one that's going to make you feel more confident.

(00:21:33):
What's staying in character? So it's related to end strong in some sense, in that people tend to self-sabotage a lot. I'm speaking, and obviously as I'm speaking, all of my senses are really, really heightened. So I'm aware of everything, if a word comes out a little bit weird or if it's not the word that I was expecting to hear come out of my mouth, I'm going to be very aware of that because I was expecting something and something different happens. But that happens all the time when speaking. I'm starting to not make as much sense or I feel like I'm rambling, going a little bit too long. All of these create insane noise in the back of my mind, the insecurities. And you have a choice there, because I can tell you right now, nobody can tell. People cannot see what you feel, even though it feels that way when you feel really, really strongly, but people can't see it. You're just looking like a normal speaker, competent and confident. But internally, it feels like everybody can see.

(00:22:34):
So you're feeling all this insecurity and it feels like there's an elephant in the room. And so what most people do is they start leaking and they break character. And they'll say, "Oh, man, I'm not making sense right now," or they'll laugh nervously after saying a word that came out weird, which is kind of saying like, "Oh, I also noticed that this word came out weird and it's okay." Right? Or they'll keep letting all of the insecurities and doubts come out when people didn't see it in the first place. So again, it's like I'm forcing these filters onto my audience and now they can only see me through that light.

(00:23:15):
And so one analogy I love for this is, again, a flying analogy. You're on the plane, everything's smooth, you're having a great time watching your movie, and suddenly you're interrupted by the pilot who picks up the intercom and says, "Oh, ladies and gentlemen, so I just had a red light start blinking here in the cockpit, and I'm not sure what this is. It could be really bad, honestly, but I don't know. So don't worry, please, I'll get back to you soon." First thing that's going to happen if you experience that is you're going to think, I wasn't worrying in the first place. But then you start thinking, wait, something probably is going wrong. And now the smallest noise, the tiny little bit of turbulence, a creak on the right, you're going to start thinking, oh no, we're going to die, every time.

(00:24:03):
So you're going to make any little mistake, any little imperfection, you're going to turn that into something big. That's what happens when you speak. If you start leaking and letting the insecurities come out, people are going to start thinking, this person doesn't really know what they're talking about. It's like a leader who isn't clear in their direction. Suddenly I'm thinking, wait, I think I have to second guess everything here because I'm not sure about this guy or this person.

(00:24:33):
And the good news is, the solution is very, very simple. The solution is that is just, don't share your insecurities. Put your best foot forward and stay in it the whole time. Stay in character from beginning all the way through past the ending, because you go all the way through your speech, then you got to end strong, which is a form of staying in character, and then let it be. And that's so important, just let it be and you're going to notice something incredible. If you're the type of person who would break character a lot, start staying in character, and the cue use for myself is, stay in it. And the worse it gets, the more I'll say, just stay in it. And what happens is, you stay in it.

(00:25:21):
And you expect everybody at the end to say, "Oh my God, you looked so uncomfortable, what was happening?" But people can't see that, that you look confident. So they're just going to give you the reaction that a confident person would get, and you're going to notice, oh wow, I am coming off as confident, and that's going to make you feel more confident. And so it's a very reinforcing cycle. If you start staying in character and ending strong, naturally, you're going to be reinforced by this behavior and you're going to realize, oh, I didn't need to break character. I didn't need to hedge every time I spoke, and that's going to give you much more confident, and you're going to start realizing, people just look confident by default. This is a crazy thing. I want everybody to walk around the world and look at people and think, most of the people I'm looking at are actually nervous right now. You're going to look at them and you're like, I can't tell. Most people speaking up in meetings are feeling a level of nervousness, but you can't tell unless it's through the roof.

Lenny Rachitsky (00:26:23):
I love this, and it's something I'm extremely guilty of. And I think the reason I do this and the reason I think a lot of people leak, which I love that term of just I don't leak, that you know, feel something's not going right. The reason I do it is I feel like me being upfront, I know this isn't great-

Tristan de Montebello (00:26:41):
Exactly.

Lenny Rachitsky (00:26:41):
... makes it okay, but in reality, that's hurting you because it's like when I watch standup comedy. When the comedian's like, "Oh, sorry, that bombed," if he didn't say that or she didn't say that, I'd just forget about it, and we'd move on to the next thing. And it brings all this attention to, oh, I see, okay, it's not going great. Otherwise, you're just like, all right, whatever, I didn't like that joke. And so, yeah, I guess any thoughts on just that, why people do this?

Tristan de Montebello (00:27:07):
Well, I think that's exactly that. It's because you're convinced that everybody can tell. And so two things will happen. Either they could tell because it was a big thing and everybody could tell, but you shining light on it is literally that. It's like, hey, everybody, you're driving a train, everybody's in the train, you're the driver as the speaker, everybody's going with you. So if there's a crash on the side of the road, you can keep going and they'll not be looking at the crash a second later and they'll be looking at the next landscape, or you can stop the train and tell everybody, "Hey, let's look at this crash here real quick. I'm so sorry about it." When you keep going, people will forget it in a second and they're not going to pay attention to you. And with the peak end rule, what we we're seeing, people remember the end of experiences more than they remember the beginning of experiences. So you're going to be left with that feeling at the end.

(00:27:58):
The other piece is, because most people won't notice it in the first place, they'll be in their own minds. So when you share this, you're popping their bubble. And so I see people speaking all the time where I'm super in tune with the feeling I'm getting when they're speaking. I'm listening to the energy, I'm listening to everything that's happening, so I can try to understand, what state are they in right now? So when I get woken up from that state of somebody saying, "Oh man, can I go again right now? That really sucked." It's even more visible for me.

(00:28:36):
And I'll often have to say, "Hey, man, I was so into what you were saying," and I'll poll the audience, "is anyone surprised?" And everybody every time is like, "No, I thought that you were doing great. I was completely with you." So that's the case most of the time, but because we're convinced that people can tell, we want to break that fourth wall or because something happened and we know people can tell, we want to acknowledge it so it doesn't feel like I'm the only one in the room who can't tell that something went wrong here. But this habit of saying, "No, I'm going to be confident, I'm leading, I'm going to keep us going in a certain direction," is extremely powerful and very self-reinforcing.

Lenny Rachitsky (00:29:18):
Okay, so let's actually show people what this looks like by actually doing some live games. I know one of your principles for Ultraspeaking is you can't learn to speak by not speaking. You need to practice speaking to get better at speaking, and these games are a way to actually do that in a really fun way. So maybe first of all, just why games? When I did this course, I was just like, huh, because it's a bunch of games. I thought this was a public speaking course. So maybe talk about just why you approach it through games, everything you do is a game in this course.

Tristan de Montebello (00:29:48):
Yeah. Well, the first piece of the puzzle is what you were saying, that you can't get better at speaking without speaking. And it's, intuitively you could think, everybody knows that if you want to become a great cook, you can't just read 100-

Tristan de Montebello (00:30:00):
Everybody knows that if you want to become a great cook, you can't just read a hundred cookbooks. You actually have to spend most of your time in the kitchen refining your intuition, testing things, experimenting, learning new recipes, and building your timing and everything that goes with it. But in speaking, we tend to do the opposite, probably because it's a little bit scary and because there aren't that many options out there to practice the speaking itself. There aren't that many environments where you can do it right now. So we're kind of left with nothing, so, "Okay, I'll just go read an article or watch a YouTube short and hope that's going to make a difference."

(00:30:38):
But maybe the bad news is, you have to do it. You have to ask yourself, "Am I going to be serious about taking on speaking and making a difference here?" And if you are, then you're going to have to do the thing. You have to practice speaking. But the good news is, it's only the outside that's scary. As soon as you get started, you're going to get rewarded. And then, the better you get at it, the more enjoyable it becomes.

(00:31:03):
So why games then? Well, games number one, are fun to play. And as I was saying earlier, if your practice is not fun, you're going to stop. So you need intrinsic reward with what you're doing. But what all of the Ultraspeaking games have in common is that it's short, deliberate practice, short reps followed by feedback, followed by another rep. So that was more important than the idea that it was a game at first.

(00:31:35):
When we started coaching with Michael Gendler, my co-founder, it was just him and me in my backyard with somebody in front of us testing things out. And we would say, we would give him a speech title just to get a baseline. "Okay, what's the most incredible invention in the world?" And we'd watch this person go into their mind and start freaking out. And they'd think, " The iPhone," and then, "I don't know the iPhone. That's pretty recent. So maybe it's fire. Is it fire though? Was there a bigger maybe communication? I don't know. Wait. Maybe we've evolved for communication."

(00:32:08):
And the longer they spent thinking, the worse their answer tended to be, and the more their confidence tended to go down as they were speaking. So then we said, "Well, we've got to get this person speaking right away." So we'd say, "I'm going to ask you another question, but just start speaking." And so, I'd ask them another question and they couldn't start speaking right away.

(00:32:27):
So we just tried to compress it more and more and more to turn it into something where then it was like, "I'm just going to say a word and you have to say something about it, so horses." "Horseback riding is fun because you can go places." "Cats." "Cats are crazy because if they were bigger, they would eat you." And I just, almost like word association. Let's get words out.

(00:32:46):
Then we started developing different games for everything. Every root cause we were seeing, every symptom we were seeing, we'd figure out the root cause and we'd create some sort of a way to get the person into it as quickly as possible. And it's just one day, six months in that we realized, "Hey, did we just create a game? This feels like a board game." And then we created, I have this, we created Speak Before You Think, the game for people who think too much, and this is a bunch of cards with all of our games. And then, Covid hit and we turned it into online games.

Lenny Rachitsky (00:33:21):
Oh, I didn't know that.

Tristan de Montebello (00:33:23):
Yeah. The magic of games is short reps, immediate feedback, practice feedback, practice feedback. And it's enjoyable, you get rewarded, you get to adjust as you go. And what's changing is your internal feeling as you're going. So you're learning lessons, but you're internalizing. All of the practice is happening through speaking.

Lenny Rachitsky (00:33:48):
To reinforce what you just shared, I haven't shared this with you, but after I took the course, the mini course, I went to see my family in L.A. We visited for a few days, and I was talking about this course and just how fun it was and interesting and how much I learned from it. And I pulled up the games because I have access to the things online. I was just like, "Hey, you guys want to try this?" and we started playing some of these games that we're about to get into. And it was just, we spent like an hour just doing this and everyone loved it.

Tristan de Montebello (00:34:15):
Wow.

Lenny Rachitsky (00:34:15):
Everyone just felt so much better about their public speaking. Afterwards, my mom was like, "Hey, how do I do that on my own later?"

Lenny Rachitsky (00:34:22):
Wow, that's cool.

Tristan de Montebello (00:34:23):
My sister's like, "I want to start doing open mic nights because that was really fun just to talk."

Lenny Rachitsky (00:34:27):
Nice.

Tristan de Montebello (00:34:28):
So were you actually coaching them? How were you walking them through the different games?

Lenny Rachitsky (00:34:34):
We just pulled them up and played them. And then, I shared some of the tips that I learned in the class that we took, just like, "Try it this way" or "Try not to focus on being correct. Just focus on confidence and not leaking that you're not doing great." All these things we're going to talk about. Yeah. So it was a lot of fun. So let's get into some of these games. So we're going to try two or three. Which one do you want to start with?

Tristan de Montebello (00:34:56):
Conductor maybe.

Lenny Rachitsky (00:34:57):
Sweet. I love Conductor. That one was really insightful to me.

Tristan de Montebello (00:35:00):
Okay, so I've got Conductor. The way this game works is that when I click "start training," I'm going to have a random title that's going to appear. And for those of you who are just listening and not watching this, Lenny will say the title out loud so you can hear. And then, what you won't see or what you'll see if you're watching is in front of me, all I'm going to see are a series of random numbers. It's going to start with five, and five is just my natural rate of speaking like I'm speaking right now. But then, I might see a number from one to 10, and each one of these numbers represents an intensity or a state that I have to tap into. So if I see a seven, I automatically have to raise my voice and get into that kind of an energy. And if I see a 10, you could only imagine what that is. But it's also true for the lower ones. If suddenly I see a three, I have to find a way to calm my energy and match the three and go all the way down to one.

(00:36:00):
And then, there might be a slide that says "breathe," which is just an indication to pause. And when I see that slide "breathe," if I just go silent, that's because I'm in front of the breathe slide and I'm not allowed to speak. And in that moment, my goal is just to relax myself and calm myself and then see what happens where I'm at when that slide moves on to the next one. And now we're going to do this. This is going to be 70 seconds, so it's going to be super quick. Ready?

Lenny Rachitsky (00:36:28):
Yeah. So I'll read the title as soon as it pops up.

Tristan de Montebello (00:36:31):
Perfect.

Lenny Rachitsky (00:36:33):
"When I grow up."

Tristan de Montebello (00:36:36):
When I grow up, I want to have taken on all of my weaknesses or all of the emotional things that are holding me back. Because kind of annoying for me that I'm 40 years old and there's still things that are holding me back that man, I've had these when I was a kid. I was like this when I was 10. And it drives me crazy, because aren't I supposed to be an adult? Aren't I supposed to be mature and have my life together? I have two kids. I have this incredible responsibility. And I have to teach them, I have to show them the way. So I've decided I'm going to hire a coach, and I talked to him just a couple of days ago, so this is perfect timing because I want to unwrap, unravel, and untwine every single one of these emotional blockers so that when I grow up, I'm completely free.

Lenny Rachitsky (00:37:45):
That was so fun to watch. I'm seeing the numbers. If you're on YouTube, you can see what's going on there. If you're not, basically there's different numbers that give Tristan the different energies to be at, and that was masterful.

Tristan de Montebello (00:37:56):
I think we saw, what did we see? We saw a six. It went up first, six, seven, then it went down to three. Then we saw, I think a two, a one, then a breathe, and then it went back to a five. How about you give it a go and then we chat.

Lenny Rachitsky (00:38:10):
Let's do it. What do you think?

Tristan de Montebello (00:38:11):
Ladies and gentlemen, let's see this. Here we go. The title is The Greatest Puzzle.

Lenny Rachitsky (00:38:19):
The greatest puzzle that I think that I've had in my life, and I think just for most people, is trying to figure out what to do with their life. And I just had to spend so much time thinking... Actually, no, let me change. I'm changing direction. I actually have known from very early on what I wanted to do with my life. I've actually found it to be not much of a puzzle. I knew from pretty early that I wanted to be a software engineer. And interestingly, I became a software. And as I think about the puzzle that created around my life, I ended up... So my life actually started to look like a puzzle instead of what I'd always thought I'd be. So I ended up having a bunch of different careers. And I look back at my life and it started with one piece, and each piece led to all these other careers. Nailed it.

Tristan de Montebello (00:39:33):
It's funny. At the end you were like, you didn't even see there was a six that came up and then when you looked up, it had already gone away. That's a good warm-up.

Lenny Rachitsky (00:39:42):
Yeah, yeah. Let's do it.

Tristan de Montebello (00:39:42):
It's funny, because what it looked like to me is that, well, you just didn't let yourself play the game. You wanted to... You were more focused on, "I want to make sure this works well, this looks good, or I don't make a fool of myself" than "Let me just play the game." So switch your mindset from that. Back in the Creator Cohort, you didn't really care, because if you failed, it didn't matter. So you just played the game. And this is the same idea. Just don't try. Just let yourself play the game.

Lenny Rachitsky (00:39:43):
Okay.

Tristan de Montebello (00:40:15):
The game will do good. But that was actually really interesting. I feel kind of similar, which is cool, except I didn't know where it was going. But that feeling of all of these puzzle pieces, and suddenly when I hit Ultraspeaking, it's like, "Oh wow, every single... There's no more. There are no more gaps." That's really cool. Okay.

Lenny Rachitsky (00:40:35):
Here we go.

Tristan de Montebello (00:40:36):
You ready?

Lenny Rachitsky (00:40:37):
Ready.

Tristan de Montebello (00:40:38):
Here we go. "Integrating new cultures."

Lenny Rachitsky (00:40:48):
It's interesting having a kid. So we just had a kid about a year ago, he is a year and a half. And there's an interesting new experience where there's my family and their culture, there's my wife and her culture. And it was never a big deal for us, these different backgrounds that we have because we could do our own thing, we have our families, they're doing their thing. But now that we have a kid, I have to really think about this. I have to constantly wonder, "Is he getting both experiences? Is he being pushed in one direction or another? Is he going to get the full benefits of both of these cultures?" And I find if I don't actually think about it too deeply and just let him have fun and hang out with our different family members, he gets everything that I want him to get; that he experiences my wife's family's culture, my family's culture, and then the combination of my wife and I's new kind of culture and family that we're building. And so, I'm really excited about the future for us all.

Tristan de Montebello (00:41:57):
Yeah, that was awesome.

Lenny Rachitsky (00:42:00):
I'm practicing not leaking. All I think about is how much better it could have been, but now I'm leaking as I say that. See?

Tristan de Montebello (00:42:01):
Yeah.

Lenny Rachitsky (00:42:01):
It's hard.

Tristan de Montebello (00:42:10):
Yeah. You're hedging.

Lenny Rachitsky (00:42:10):
Hedging.

Tristan de Montebello (00:42:13):
So the point of all of these games is to create turbulence. This is going to be the theme of this podcast. I'm going to share only flight analogies. But if you think about a pilot, a flight simulator, you can think about these games as the flight simulator. You don't put a pilot in a flight simulator and waste those precious hours having them just cruise at 30,000 feet in clear skies. You're going to say, "Okay, you're going and now hey, you've lost your captain and you have to do something" or "Hey, your motor just broke" or "You're going into crazy turbulence."

(00:42:46):
So the gain here is always, every one of these games have in common that we're creating turbulence for you. So it's on purpose that like, "Ooh, that's interesting how I tend to want to leak, to want to break character. Wow. It's interesting how at the end, the ending strong is not just an automatic habit that I've built for myself." So what we want with the turbulence is that it highlights areas that we want to work on. And you can go again and see immediately because you have that same pressure every time. There's no way you can prepare for Conductor. You can do just a ton of reps and get to become the person who can just navigate the turbulence really, really gracefully.

(00:43:29):
Which reminds me of a Kevin Kelly quote that I love where he says, "Pros are just amateurs who've learned to recover gracefully from their mistakes." And this is what we're trying to do here. If you know that you can recover from any mistake gracefully, then you're going to have confidence in any speaking scenario. And most of the scenarios you're going to be in are spontaneous, are ones you can't prepare for. So it's that much more important.

(00:43:57):
So tell me, what do you remember from going through Conductor and the Creator Cohort, or specifically here, what was coming up and what were some of the things that pop into your mind?

Lenny Rachitsky (00:44:10):
There's two things that I really took away from it, and it's different doing it now on camera with this whole podcast thing.

Tristan de Montebello (00:44:15):
Yeah.

Lenny Rachitsky (00:44:16):
But the things that I really took away that have stuck with me from this exercise is one, is that you have this kind of metaphor of these file folders that you have kind of in your head where every energy level, like a one when you go low and a 10 or even a five, when you're at that energy level, you access different insights and memories and stories. So it's not just like, "Now I'm going to say the same thing at a 10, or I'm going to say the same thing at a one." It's when you let your body just slow down and relax to a one, new thoughts come up, because making it up as you go along and you're just trying to figure it out as you go. And that really happens when you're forced to go from five to, "Okay," and you let your body settle into a one. You're like, "Oh, okay, here's a new thought that comes to mind." So that was really powerful for me because I never had realized that.

(00:45:12):
And then, the other is just this idea of doing these really hard things with very low stakes. It's higher stakes, so maybe that's why it's different, how it feels different doing it here where it's like, "Oh, this is-"

Tristan de Montebello (00:45:22):
Yeah. Yeah, this is extremely high stakes for you.

Lenny Rachitsky (00:45:26):
Yeah, relatively. But yeah, there it's a couple people and you're like, just don't worry about failing so you don't even have to worry about apologizing or fleaking. It's just like, "Yeah, I did what I did." So those are two really powerful ones. I just like practicing this. And knowing you'll be okay at low stakes builds confidence. I'm like, "Okay." It's making up a minute of talk about the most random thing on the spot, not something that I would feel I'd want to do, but then you realize, "Okay, it's fine. I can do that."

Tristan de Montebello (00:45:54):
The common theme for me, and I've been on this journey for seven years now, I still am blown away every week by the lessons I've learned over the course of the seven years, which all come down to your brain, your subconscious is so incredibly powerful. So your hardware is magical. And because I've spent seven years kind of getting rid of the bad habits, getting rid of the gunk and trusting myself more, I allow myself to take many more risks. So I'm jumping into these games still with the same doubts in some sense, but they've just, everything's tapered down way, way, way into the background. So I get to be much more present.

(00:46:43):
And I talked about the summary prompts earlier in the podcast, saying the beginning of a sentence and trusting that your brain's going to fill in the gap is something that's initially hard to do. But when you've done it 1,000, 2,000, 10,000 times, you start believing, "Hey, maybe my brain will deliver every single time." So you can start saying the beginning of sentences the direction you want to go into and your brain fills in the gap, and we're going to do a game on that in a second.

(00:47:12):
But the Conductor one is so beautiful because the way we describe it, so that folder one when it came into my mind was my favorite ever. But the original one was when you tap into a certain energy, that creates emotion. And if you tap into that emotion, the words come as a natural consequence. So it's energy leads, emotions follow, and words fill in the gap.

(00:47:44):
And when you experience this for yourself, if you go into Conductor and you play, you realize, "Okay, if I want more conviction, I can raise my energy or get into a state of conviction and the words that are going to come out, the ideas, the stories, the anecdotes, the examples, everything is going to fit into that. If I feel frustrated, I can dive into that state and stay in that state, and naturally the content is going to follow. It's a very, very powerful game. It's a very exciting game, and it's a game that, especially when you're playing with low stakes, you very quickly feel the effect of, "Oh, I can see the potential of what it could be if I could just be like this anywhere." Maybe you taper out a little bit of the extremes.

(00:48:42):
But you can access this for free on Ultraspeaking or the way we did this at first, you just go to Google and type in a random series of nine numbers and then just have a friend say each number, one after the next, and you just match it. I used to just put my hand out and go up and down. So in essence, it's very, very simple to apply it.

Lenny Rachitsky (00:49:03):
And it's just like a lot of fun to just get an excuse to just go wild and high and then just get low. I love that part of it. And let's get into the next theme. But just one other insight I had that you shared with me when I did it the first time is just people have a strength.

Tristan de Montebello (00:49:16):
Yes.

Lenny Rachitsky (00:49:16):
They're either, correct me if I'm wrong, they're strong at the highs and just very uncomfortable at the lows or the opposite. And for me, I thought I was going to, "Oh, obviously I'll be more natural at the lows, because like introvert world." And you're like, "No, you're actually super energized at this high end, and then it's hard for you to access the low." And I thought that was really insightful for me.

Tristan de Montebello (00:49:39):
Yeah. You'll notice it pretty quickly once you jump in, especially with a friend. It's cool because when you get to see, "Oh, I'm much more comfortable going up than I am going down or vice versa, or I'm stuck in the middle and I am only comfortable when I'm not in the extremes." It's just telling you something.

(00:49:59):
This is what we want. We want to a mirror in front of us so I can know, "Okay, what's happening here?" I'm not very much a fan of actually watching yourself on camera on video, because again, this is an inner game, not an outer game. So when I watch myself on video, I see the outside, which can be useful for certain things, but the fundamentals are inside. So getting a mirror of I play this game and I feel a certain way, "Oh, interesting. It was easy to go up." So I can muster energy pretty quickly, and I'm willing to take risks of jumping into a different energy stage, which might mean changing the direction of where I'm going.

(00:50:37):
But slowing down means I need to be willing to take up space. I need to be willing to just be while everybody's looking at me and I'm using up their time. But I'm going to take up space and I'm going to take a moment to go inside and be introspective and really ask myself, "Okay, what do I want to say here?" And so, that's a reflection of, "Well, what does that mean if I struggle to do that?" And that's why speaking such an interesting skill set.

Lenny Rachitsky (00:51:08):
All right, let's do another game.

Tristan de Montebello (00:51:10):
This next game is called Triple Step. And Triple step is a game for people who struggle to stay on a single thought or get very easily put off their game or distracted. If you're the type of person where you're speaking and suddenly somebody yawns and you just start freaking out thinking, "I'm so boring and things are horrible, I must be terrible." Not, they probably have a baby and they didn't sleep last night. A pen drops and you start losing your ability to stay on track, this is a game for you. Also, a very fun one.

(00:51:46):
The principle of the game is pretty simple. Similarly to Conductor, we're going to start with a random speech title. So I have no idea what's going to show up. Then as I'm speaking, in this setting here, I'm going to speak for a minute. There will six random words or series of words that are going to pop up as I'm going through my speech. And my goal is to integrate the words into the speech as seamlessly as I can, as if they were part of the speech the whole time. So in theory, if I do a perfect job, if you're listening, you should struggle to pick out which words were actually the words that were popped up. The likelihood in one minute of me being able to do that is low, but let's see if you can do it. So if you're listening, you're not going to see the words. We'll tell you afterwards what they were. See if you can pick up on them. But otherwise, my goal is just to choose a strong direction and stay on that direction as naturally as I can.

(00:52:43):
Here we go. The title is, How Would Your Friends Describe You? I've been described as a Labrador by my friends. And I think the reason people describe me as a Labrador is because I am so easy to excite. It's like if you give me a box of french fries, I'm going to go nuts and it's going to be the best french fries I've ever tasted in my life. But if the next day I get a massage, I'll be completely in that experience and the massage is going to be the best massage. And then, I'm going to think, "I need to get a massage every day." I'm going to start daydreaming about massage as my natural day to day.

(00:53:19):
But the problem with being a Labrador is that Labradors get kind of excited. So I may be doing cartwheels one second, and the next second I'm supposed to be working. And so, I'll be on my computer, but then I hear the microwave ding and I think, "Oh, maybe I should go get some food next." And so, there's a beautiful trait to being the Labrador that allows me to explore all of what it's like to be human. I always have access to the internet inside me, but there are definitely some drawbacks as well.

Lenny Rachitsky (00:53:50):
Okay. So the words that you had to integrate are french fries, getting a massage, daydreaming, cartwheels, a microwave, and the internet.

Tristan de Montebello (00:54:05):
Yeah. And so, you might notice that some of the words I'm integrating literally, and some I might integrate more metaphorically like the internet of my mind. It's like I have access to the internet. So you can give yourself as much leeway as possible. The whole point here with Triple Step is you want to be that tree in the storm that is not so rigid that if the wind is too strong it's going to break in half, but not so flexible that it's going to swing every which direction as soon as there's a gust. So you want that firm solid grounding, which is in choosing a clear direction, that one thing off the bat, and then you want to make the words work for you. So stay focused on that one thing. And as the words come in, the more focused you are on that groove you've created for yourself, the easier it will be to let the words work for you. Okay?

Lenny Rachitsky (00:55:03):
And again, the skill this builds is to be more comfortable with things not going perfectly and being distracted.

Tristan de Montebello (00:55:12):
Yeah. I would say this one can be used for two other things. Number one is resiliency, right? Because this one will make your brain go crazy. And if you can stay composed within it, with all of these things happening, it really builds this ability to say, "Well, man, if I can do Triple Step on hard mode, I can do anything. Why would anything else scary? Why would an interview question scare me when I can throw these kinds of things? I can always navigate my way through." Right? We're trying to lower the likelihood of a mistake really hurting you.

(00:55:48):
And then, the other piece is this is a game, this one and a game called Rapid Fire Analogies, are games that are really, really nice to use as a way to warm your brain up. So you could use it before a podcast. You could use it before a job interview, before a meeting. When you want to be on, do a few reps of this, and your brain's just going to be completely lit up because it's pulling on so many different parts of your brain that are necessary for communication.

Lenny Rachitsky (00:56:13):
One last thought just before we dive into it. I think it's just to zoom out again, the reason that you've found this is a better way to learn to become better at public speaking, my sense is just if you were to just do the standard thing of just give more talks, find more opportunities to do presentations, it's too broad of a brush to build these different skills, and which you've identified is there's these very specific skills that add up to a great presenter. And these games pick a specific skill and help you just focus on that again and again and again.

Tristan de Montebello (00:56:51):
If you're already practicing, you're already leagues ahead of everyone, because most people aren't practicing. They're you're trying to learn from a video or a YouTube short or an article. You can only go so far with that. But if you are practicing, there are kind of two suboptimal ways that might show up. One is what you're saying. You're doing talks and you're speaking up more, but you're not really practicing. It's kind of, as you were saying, it's broad, broad strokes.

(00:57:17):
The other one is you are in a choreography, so it's like learning how to dance, but you only learn choreography. Well, that's all you know how to do. So if I ask you to do, I say, "Okay, now I'm going to put music on. Just dance." You're kind of stuck because you only know how to do the moves you were doing. So we're trying to get people outside of, "I have to be in my mind, or I have to do things that I've memorized how to do" and come back to trusting your natural ability to communicate.

(00:57:51):
So that's what we're doing here. You can feel like when you don't speak, when you struggle with speaking, you're stuck in this box, and everything around you is tiny and you can feel the sides of the box. And we're expanding the range. We're playing around with all kinds of different things, different tools. And all of them have specific meaning, but even if they didn't that much, you still would be able to, "Oh wow," you're pushing back the sides of the box. And now suddenly, "Hey, I can move around. I feel comfortable moving my arms and moving my legs and going to the right and the left and up and down." And just that act of making you feel more comfortable and more at ease is going to unlock your ability to communicate, because you already know how to do a lot of this. So we're tapping into these different skill sets and we're doing both at the same time.

Lenny Rachitsky (00:58:42):
This episode is brought to you by Brave Search. Brave Search is the private, independent search engine that doesn't bias or censor results. Brave Search and its answers with AI feature are available for free to all users on desktop and mobile devices. With Brave Search, you get real answers faster, served from their own independent index of the web. Their AI search engine can give lightning fast, incredibly accurate results for almost any question.

(00:59:09):
But Brave isn't just AI answers. It's also a powerful traditional search engine with real innovations versus big tech options. It fights bias and SEO spam. It brings a cleaner results page with fewer ads, Reddit threads in the search engine results page, powerful local results, and even community-driven ranking options. Tired of big tech's same old list of links? It's time to try Brave Search. Visit brave.com/Lenny to get started. That's brave.com/Lenny.

(00:59:40):
All right, let's do this. I'm energized. I'm pumped.

Tristan de Montebello (00:59:43):
Let's do this.

Lenny Rachitsky (00:59:44):
No, I'm not going to... I was going to say I'm going to nail it, but no, let's just have fun. Let's have fun.

Tristan de Montebello (00:59:49):
Yeah.

Lenny Rachitsky (00:59:50):
It goes how it goes.

Tristan de Montebello (00:59:52):
Indeed. Here we go.

Lenny Rachitsky (00:59:53):
Okay. And I'll say the title. The best thing about pain. So this is something I recently shared in another talk is just this quote that I always think of.

Lenny Rachitsky (01:00:01):
In another talk is just this quote that I always think of, "The cave you fear contains the treasure you seek," that the thing that is hardest often points you in the direction you want to go. Like I hate blue cheese, but sometimes I find that if I eat the blue cheese and add it to a salad, it ends up being the best salad I've had. Having kids is another amazing example where just kids are... There's so much pain, but it's also, there's nothing that is more joyous than having a kid.

(01:00:29):
And sometimes even growing a beard. I grow this beard and I have to maintain this beard for the rest of my life. And I know people would look at me without a beard and be like, "What the hell? Well, you look so different now and so young." Sometimes I think about just having a sibling and the pain that if I had a brother, if he just hit me, the pain that would come from that, but just then having the brother would be so much worth it, even if he's hitting me all this time.

(01:00:58):
And there, I ran out of time, but that was solid.

Tristan de Montebello (01:01:04):
Okay, I realize this is your first time playing Triple Step. It's kind of mean of me if you [inaudible 01:01:09]-

Lenny Rachitsky (01:01:09):
I have to go faster.

Tristan de Montebello (01:01:10):
... Give you six words. So I'm going to give you four words.

Lenny Rachitsky (01:01:12):
Okay. Okay.

Tristan de Montebello (01:01:13):
But here's what I noticed. What I noticed is you were letting the word... The word was the beginning of a new thought. Right, so you say, "Another thing is beers. Another thing is...". So you're finishing your thought and then you're moving on to the next one. Try to hold onto one direction. The one direction is approach your fears head on. And then, so when you see a puzzle, it's like, look, this doesn't have to be a hard puzzle because now I know that if it's scary, I do it. And it's like having kids, which I thought was so scary, I just jumped in and now I'm moving forward. And so it's like I'm growing my beard without caring what other people think just because it might be scary, or maybe I cut my beard because that would be something scary. So you're holding onto the line.

(01:02:08):
With four, it's going to be a little bit easier to integrate them. Ready?

Lenny Rachitsky (01:02:16):
Let's do it.

Tristan de Montebello (01:02:18):
Social-

Lenny Rachitsky (01:02:18):
Social distancing. It's interesting that social distancing was such a thing that we all had to do for so long. And then all of a sudden we look back at that time we're like, "Was that actually necessary? Did we actually have to stay far from each other? Did that actually have any impact?".

(01:02:34):
There's all these things we have to learn, like sometimes we look at the stock market and we wonder, "Should I be paying attention to the stock market? Should I be distancing myself from it? Should I be investing more often? Should I be reading every newspaper that comes out every day to stay on top of what's happening in the world? Should I get closer to this information or should I distance myself? What's better for me?". And sometimes it feels like you're running this marathon where sometimes you go back and forth. Sometimes it's, "Let's all be together. Let's pay attention to all the news. Let's hang out." And it kind of feels like I just want to just want to go to the toilet and peace out.

Tristan de Montebello (01:03:24):
Amazing. That works. That's really good.

Lenny Rachitsky (01:03:27):
Okay.

Tristan de Montebello (01:03:27):
That's really good. Well, tell me what, because again, the games are meant to put you in a state of turbulence and find out what was easy, what was hard, what am I noticing? And now you know what you want to work on. If you did a rep and you got it and it went perfectly, then you're learning nothing. A really easy rep is not worth much. The only reps that are worth something are the ones where you feel an edge.

Lenny Rachitsky (01:03:57):
Yeah. And by the way, we should say the words right, that I had.

Tristan de Montebello (01:04:00):
Oh, yeah. The first one was the stock market, then a newspaper, which you brought in really, really well, then running a marathon, and then toilet.

Lenny Rachitsky (01:04:13):
Yeah. Okay, great. Yeah, just the fact that I'm okay doing this is a big milestone for me of just like, ah, whatever. Because before doing this thing I'm like, oh my God, I never want to sit there and come up with a talk for a minute on the most random subject, and there's a lot of power in just feeling comfortable just doing it, just like, sure, let's do it. Whatever. Something will come out that's interesting enough.

Tristan de Montebello (01:04:35):
That's why taking on this journey of speaking is so empowering because speaking is a high performance skill. So taking on a high performance skill, and starting to tackle it, and getting kind of good at it is very addictive. It feels really, really good. If you get good at tennis, if you get good at golf, if you get good at anything, product management, it's a addicting, it's exciting. And as soon as you get good, there's nuance to it, and it's energizing in and of itself. And because we have such awesome hardware as humans, we've been speaking all of our life, a lot of us have a pretty decent level to start out with. So you really quickly, you're getting to like, "Oh, I'm getting some results here. This actually feels good." So there's something really energizing about jumping into it. It's the thinking about doing the exercise that's scary, but as soon as you're in it, it's energizing and empowering.

Lenny Rachitsky (01:05:35):
And also just doing it, this is a very hard exercise. Just giving a made up talk for a minute with words you have to integrate, and concepts. And I think just doing that makes a regular talk so much easier also, because you don't have to do that. So there's something there about just doing it on hard mode, learning things, and then, oh, okay, I just have to talk about a thing that I already know about, that I have planned, much easier. Anything else around this game that is worth sharing before we do our final game?

Tristan de Montebello (01:06:06):
We have a whole series of games, and you could probably even invent other games, but some people will play Triple Step and will say, "Wow, that's so hard." And then they'll go and play Conductor and think, "Wow, this is my game. This is so easy." But other people will play Conductor and think it's impossible, and then come play Triple Step and they'll be like, "Man, this is my jam. I can get this one very, very easy."

(01:06:31):
So again, it's just a mirror of where you're at. And what's beautiful about this is you start playing around with these games, you're very, very quickly going to see, okay, this is my edge. And where your edge is, as you were saying with your quote, is often where the gold lies. So if you can spend some time there and learn what it is underneath the struggle, what's actually holding you back. When you unlock that, whatever's holding you back in Triple Step, or in Conductor, in any other game, is holding you back elsewhere in your life. So when you unlock it there, it kind of unlocks the other things, which is really nice, like a set of gears.

Lenny Rachitsky (01:07:12):
And it's interesting, as we were talking, where my mind keeps going is I just want to say how I didn't feel good about my performance, but I'm internalizing the lesson of don't leak how you feel. And that's a really powerful lesson. It's really hard not to just to be like, "Oh, that was not good." I really wanted to say that after every time I tried this and I am making myself not. And I imagine from your perspective you're like, "No, it's fine. It's like whatever."

Tristan de Montebello (01:07:40):
Yeah, absolutely. I was actually thinking, I bet a lot of people watching you do that would think, wow, I don't think I could do that. That would be their first thought.

(01:07:49):
So absolutely. And again, and this is a habit. And the noise doesn't completely disappear, but it goes down to being almost imperceptible. So what we're trying to do is we're trying to internalize all of these habits to the point where I don't need to consciously think about them.

(01:08:12):
So it's like a gymnast who's doing their tumbling routine and jumps into the air. As they're flipping, they're not consciously trying to think of how to do a flip. They've done it a thousand times. They know how to do a flip. The only thing they have that they may be thinking of, all of their attention is on being completely present to what's happening, relying on your body and your subconscious knowing what to do, is they have kind of like listeners, like in programming, keyboard listeners. You have something that's there that is just listening for anything out of the ordinary. And it's very, very fine-tuned.

(01:08:47):
So as I'm speaking, for example, I might think to myself, "Oh, I may be rambling right now. Maybe I'm going a little bit too long." And it's a little listener that's going to just gently, nicely, say, "Hey, warning, I don't know if you're aware of this." And as I hear that, I might say, "Oh, okay, let me wrap it up." Or maybe it's saying, "I'm not sure if you're being clear," or, "Can you be more precise here?". Whatever it is, it's just a gentle listener in the background.

(01:09:15):
So as you get into the habit of staying in character, and if you had an audience here, we could have asked them right away, "Well, how do you feel about this?". You probably would've gotten really good feedback, really positive, which would've kind of jarred that feeling of, wow, I didn't think I did it that good of a job. And people are saying, "Hey, I thought that was pretty good." So As you get that reinforcing pattern, the voice starts going down more and more.

Lenny Rachitsky (01:09:43):
Awesome. I need that voice to go down. That'd be great.

Tristan de Montebello (01:09:46):
[inaudible 01:09:46].

Lenny Rachitsky (01:09:46):
Okay, let's do another game.

Tristan de Montebello (01:09:48):
Always does.

(01:09:49):
Cool. Let's do last game. Last one of these practical games. So this is actually a game from one of our courses that I'm pulling out. It's not a standalone game, it's one that's inside of the courses. But again, if you wanted to replicate this yourself, you can very easily do it.

(01:10:09):
So what we're going to do here is we're going to work on conviction prompts. So this comes back to this idea of entering a state or changing your energy to impact the words that are coming out of your mouth. So what's going to happen here, is similarly to Triple Step, I'm also going to get a random topic that I just have to start speaking about. But now, instead of getting a word that I have to integrate into my speech naturally, I'm going to get a prompt. So it's going to be the beginning of a sentence that I have to say out loud, and I have to find a way for my brain to just complete the sentence. And the sentences are specifically chosen because they're going to put you in a state of more conviction. So it's going to force me to care more about what I'm saying basically.

(01:10:56):
And this is a game for executive presence. If you think about somebody who you feel has great gravitas or great executive presence, they usually have, there's something about them that's saying, this person really believes in what they're saying. And what this game is showing you is that, hey, there's a way to fast track myself to that place. If I want to have more executive presence, let me bring a little bit more conviction to what I'm saying.

(01:11:27):
There's a caveat, small caveat. Maybe 10% of people in the workforce need the opposite. They need, "Hey, you need to maybe question what you're saying here." But the reality is the vast majority of people actually are not truly standing behind their words and their ideas. And what that does is that the people who speak a lot and feel a lot of conviction, their ideas go through more often than the others. And you'd want ideas to stand for themselves, but that's just not reality. So for most people listening to this, if you can bring more conviction to your words, then your ideas are going to have a better chance of being seen equally to those who are already doing that. So this is what this game's about.

Lenny Rachitsky (01:12:14):
Awesome. Okay.

Tristan de Montebello (01:12:15):
Okay, here we go. The title is Saying No. I've had to learn this the hard way as an entrepreneur, that saying no is one of the most important things I can do. But saying no is not saying no to a meeting, because that can be easy. And what I'm going to say now matters a ton. This is saying no to doing all of the exciting projects that I want to do. So as I said earlier, I'm Labrador. I get excited about everything, and I genuinely believe that every idea is awesome, but that doesn't mean I can do every idea. I need to choose a very clear focus and stick to that focus.

(01:13:02):
And this is a game changer. When you start reducing the amount of things you're doing to a painful amount, a painful few amount, then when you get there, suddenly everything else changed. And it astonishes me when I do that, just how much more I can get done, even though I'm doing fewer things.

Lenny Rachitsky (01:13:22):
I love it. That was great. These words are tough.

Tristan de Montebello (01:13:27):
They were, yeah. This was not an easy one. This was not a... Good thing that I get a tough one. Well deserved.

Lenny Rachitsky (01:13:35):
Let me read the phrases real quick, just so folks know. So the phrases you had to integrate is, "This matters a ton. I genuinely believe that every idea is awesome. Game changer."

Tristan de Montebello (01:13:45):
It was just, "I genuinely believe that." Yeah.

Lenny Rachitsky (01:13:49):
Oh, got it. Okay. "I generally believe that." And then, "game changer". And then, "It astonishes me when."

Tristan de Montebello (01:13:55):
And I'm so eager for you to go through this, and for anybody listening to try this for themselves, even if you know what's coming. Like, if you want to do this for yourself right now, write the words, the prompts that Lenny just shared, and choose any title, and just speak for a minute, and see if you can integrate those in. Because you're going to notice how if you bring conviction, these words naturally bring that out of you. And it's so interesting to watch the content change as a result of the state you get into and what you say. So it's really powerful to discover just how incredible your brain is.

(01:14:36):
So same intention for you I think, is choose a strong direction from the beginning. This is always, in speaking in general, the stronger the direction you choose in the beginning, the more ideas you're going to have. Everything gets easier when you choose a strong direction.

Lenny Rachitsky (01:14:54):
Okay, let's try it.

Tristan de Montebello (01:14:55):
But the goal here, is as it says, advocate for an important idea related to the speech title. Ready?

Lenny Rachitsky (01:15:01):
Yeah, let's do it.

Tristan de Montebello (01:15:02):
Here we go.

Lenny Rachitsky (01:15:02):
YOLO.

Tristan de Montebello (01:15:06):
The title is Space Exploration.

Lenny Rachitsky (01:15:08):
I think it's hard to imagine anything more important to the human race than space exploration. I know there's a lot of talk about people wasting time trying to get us to Mars, or trying to not think about what is happening on earth, but I feel like there's nothing more powerful, and important, and inspiring. In fact, the entire world needs to focus more on the value of space exploration. There's so many things we can discover, so many things that can help us on earth, and we cannot forget how much potential exists outside of our little earth, that we think our whole existence and everything that's ever existed on this one planet, when really we're this tiny, pale blue dot. And it just astonishes me when people don't think about this, don't think it matters, don't think they should spend any time getting us into space, investing money in space. And just hearing stories, if nothing else, of people that have gone into space and how life-changing that was for them, should tell us that space exploration is incredibly powerful and important.

Tristan de Montebello (01:16:14):
Yes, that was awesome. That was so cool. So you had, the title was Space Exploration, and the words were, "in fact", "the entire world", then, "We cannot forget that," then, "It astonishes me when," and finally "life changing". So what was that like? What did it feel like getting...

Lenny Rachitsky (01:16:41):
Yeah, there's a lot of... It really helps, just like, "Here's the thing you're going to believe." And I don't know if I got lucky with stuff, but it just felt like, okay, I have, something comes up that I'm not going to leak. But anyway, it was like, oh yeah, cool, something interesting happens.

(01:16:57):
And that's one of my other actual, just going on a little quick tangent, insights from the lessons that you guys teach, is that as you are forced to talk, you have new insights emerge. And you almost figure out what you think and know by being forced to get out of your head, and these problems help you along that. But I think that's really interesting, of just like, this will help you develop things, and insights, and take them out of your head.

Tristan de Montebello (01:17:26):
Yeah. Well, hopefully we get to talk about the Accordion Method, one of the most powerful methods I have, which is very close to this.

(01:17:35):
But this is often a prompt I tell people when they're speaking. I say, because people tend to get into a public speaking voice, so we'll be in a class, and they'll be chatting normally, and look super normal. And then we'll say, "Okay, now just a timer. I'm just going to give you a speech. Just speak for 60 seconds so we get a baseline." And I click play, and suddenly I say, "The important part about doing this," and they enter into a different version of themselves, a very professional version, whatever that would mean. It's so much more freeing, powerful, connecting, and effective to speak conversationally.

(01:18:18):
And so the cue I often give people is don't think about us, just think out loud. And that's really what we're doing. We can, most people have a skill set that's up here and a mindset that's down here. And so if you can just change the mindset to match the skill set, you've already made a giant leap. And you do that by reducing the stakes in your mind and by just speaking. And as you do that, when you're thinking out loud, you have these moments of connecting things in your mind, and then naturally it pops out.

(01:18:59):
And if you're doing it well... And I love, there's a really cool Naval Ravikant interview on the Joe Rogan Podcast from many years ago that's phenomenal. And at one point he talks about communication, if I'm not mistaken. I think it's on that podcast. But he says something along the lines of, "One should discover the words they are saying at the same time their audience is." And this comes back to thinking out loud, like if I'm really in my mind, I'm making connections, and suddenly the words are the consequence of it.

(01:19:31):
So using prompts, poking your brain, giving these cues naturally creates things that you couldn't have anticipated otherwise. It's like putting constraints on a creative project.

Lenny Rachitsky (01:19:46):
I love that. Before we segue to a couple of these methods, the Accordion Method is one example, I want to ask about, when people hear this, they may feel like you're helping people more, just like make shit up, and why, why would we want that? Talk about just how this isn't just like, you're not going to actually give talks like this necessarily. This is... And I guess I'm answering the question, but I'm curious if that's how you think about it. This is building a skill so that when you actually want to give a real talk that you've prepared, you are better at it. But yeah, just thoughts on just that potential element.

Tristan de Montebello (01:20:23):
Yeah, I think that's an important question, and it's a question I hear a lot because we all know a bullshitter, and that's the person who masters the skill of communication but doesn't have anything to show for it.

(01:20:43):
And so this thing happens, is that I see bullshitter and I think to myself, I really, really don't want to become that person. And what happens is it becomes an immune response or like an immune response where the desire not to be that person and the feeling being around that person gives you is so strong that now if I take even the smallest step in that direction of speaking freely, sharing my thoughts out loud, bringing more conviction or confidence to what I'm saying, not leaking, then there's this immediate response like an immune response in my body that's just too strong, that's saying, "Uh oh, you're becoming the bullshitter. Alarm bells. Alarm bells. Go back to that safe little corner you were in."

(01:21:39):
But the reality is, if you're thinking that, then you have no chance of becoming a bullshitter. Because if that thought is even popping into your mind, then you're the type of person who has developed a very acute skill set of noticing when people bullshit. And you have that same skill set for yourself. So it's just going to be, now it's just too loud.

(01:22:05):
So as we go through this practice, we want to match, "Hey, I want to match that bullshitter's level of communication, except I'm going to have the ideas to back it up. I'm going to really put effort into my craft, but I'm going to be able to show them in the best possible light." And what we want to be able to do is notice, okay, if this is a big thing for you, the bullshitting, and you're noticing a big reaction, just even listening to us, not even playing the games yourself, then you definitely benefit from calming that voice down. So spending time learning these skill sets, because you're most likely atrophied because you're staying away from it. And you're going to have this very powerful listener in the back of your mind that's going to ping you, and it's like, "Hey, you're at the limit right now. Stay true to what you know." And it's going to be a very good compass for yourself. It's going to be there and you can trust it because you developed this capacity.

Lenny Rachitsky (01:23:02):
Awesome. That's really helpful.

(01:23:05):
Okay. So, so far we've shared a bunch of techniques, things that you could just start doing today. We've done all these fun games that you could play online. If nothing else, just learning from the techniques these games teach you I think is really helpful. You've shared a bunch of principles of just like, here's how you actually get better at public speaking, and not this way, but that way.

(01:23:27):
I know you have a couple also methods just like that people can implement that helps them develop talks that I found really helpful. So maybe just as a closing, we talk about these two methods, the Accordion Method, and I think it's the Bow and Arrow Method?

Tristan de Montebello (01:23:40):
Uh-huh.

Lenny Rachitsky (01:23:41):
Awesome. Let's talk about the Accordion Method. We did this in the class briefly, and it was really helpful, and I've been explaining it to people of just like a really cool way of making your talk better. So talk about how that works and how people might be able to implement it when they're trying to develop the talk.

Tristan de Montebello (01:23:55):
Now, I'm biased when I'm going to say this, so take this with a pinch of salt, but I think the Accordion Method, the Accordion Method might be one of the things I'm the most proud of in my entire life because it's almost revolutionizing the way I think we should prepare speaking.

(01:24:19):
So up until now, we've talked about spontaneous speaking mostly, and that's going to be the vast majority of your speaking. Probably 80% of your speaking is stuff that you can't prepare for. But there are going to be situations where you know you have a deadline and you're going to have to speak. And either you have to speak because it's a job interview, or you're talking to your CEO, or maybe you're presenting to your whole team or an audience of a thousand.

(01:24:45):
The old way I think is shitty. I think it's broken, and I haven't found anything out there that is innovating on this. And it drove us crazy with Michael, and that's what gave birth to the Accordion Method. What's the old way? The old way is I have a talk coming up, so I'm going to dump all of my ideas on a piece of paper or multiple pieces of paper. Then I'm going to try rearranging those ideas. And as I'm rearranging the ideas and trying to make them in a talk, I have more inspiration. And I'm thinking, oh, maybe I could say it this way, and I don't want to lose that other thing that I said in the beginning because maybe I would use it.

(01:25:22):
And you start just creating this alien stack of paper with all of your ideas of what your talk might be, and then you're left with 10, 15 pieces of paper. And now as the deadline comes closer, what do you have to do? Well, you have to go through the excruciating pain of turning 10 pages into a script so that you don't forget all of those brilliant lines that you spent so many hours editing. And they're still in writing mode. They're not in your mind.

(01:25:50):
So now that I've created that script that I spent a lot of time editing, now I have to memorize it. And memorization is pretty. We're not good at memorization. Robots are good at memorization, humans are not. And memorization is like a chain where you just have all of these links very linearly. And everybody knows the feeling of going through, reciting a poem as a kid, and suddenly you miss one verse and you're lost, and now you're a deer in the headlights.

(01:26:21):
So what we're doing with the Accordion Method is instead of preparing our talk by writing, we're going to prepare our talk by speaking, and we're going to do so in a very specific way where we're going down the accordion to create extreme clarity, and to understand what the essence of our talk is, and then back up the accordion to bring back in intentionally just the right pieces.

(01:26:48):
So I was thinking of an analogy for this, and one that I really like is imagine you're redecorating your living room. The old way, the writing 10 pages and memorizing it is I'm going to look at my living room and I'm going to rearrange things and put stuff in a corner that I might need later. And then I'm going to bring some new things that I thought could be really nice and I'm going to struggle to make something work.

(01:27:14):
The Accordion Method is saying, and imagine this were easy to do with furniture, I'm going to take everything out of my living room except the most essential pieces that make my living room. So I might be left with that one couch that I really love, a pillow, a beautiful light that I bought three years ago, and one or two other small things. And as I look at that, I'm going to have clarity on the vision I want for my living room. And then very slowly, very intentionally, I'm going to go take certain elements that were already there that I might want to bring back in, and I'm going to bring new elements that now I see make sense. And so by the time you finish with your beautiful living room, it's going to be this beautiful minimalistic room that has a very clear design choice, and every element there is there because you chose it. It's there because you did it very intentionally.

(01:28:15):
So how does that work with the Accordion Method? What we do is you can go through the first step. If you want, you can write all of those ideas on paper just to get them out of your head. That's totally fine. But from this moment on, there's no more script. And I'm just going to give an example of times, but you can change these time constraints slightly. We're going down the accordion by using time constraints. So for example, you would say, "I'm going to speak for three minutes." So you're going to put a timer, and you have two rules. I have to stay in character the whole time and I have to end strong. So you must make it to the end of the three minutes, and it doesn't matter how bad it sounds, how many mistakes you make. The only point here is I'm trying to get my ideas out into spoken word. So I'm starting to populate my mind with everything and seeing where am I actually at.

(01:29:13):
Then after the three minutes, you think of, okay, what did I like, what didn't I like? Then you go to two minutes. And you put a timer and you do two minutes again. And you're very strict with those two minutes, because we're just trying to learn something every time. It doesn't need to be perfect. So at the two-minute mark, you do the same thing, but now you had to shave a whole minute out of that content. And as you do that, well, that means getting rid of the noise, getting rid of anything that doesn't feel right.

(01:29:38):
Then you go down to one minute. And you're going to go down all way to 30 seconds. So you started at a three-minute speech and you make your way down to 30 seconds. By the time you make it to 30 seconds, you're going to have only the essential pieces like that couch and that lamp in the living room. When you have the essential pieces, you're going to have a clear sense of what your talk is about, and it might've changed as you-

Tristan de Montebello (01:30:00):
Sense of what your talk is about and it might've changed as you were going down the accordion. And then from that place on, we're going to do another 30 second rep and then we're going to go back up the accordion. So you do another 30 seconds and then you do one minute, two minute, and all the way back up to three minute. And every step of the way you go from 30 seconds to a minute. Initially, a minute felt hard. Now that's double the time you just had. So you can bring in something that's aligned with the talk you want to share, and then two minutes, same. And then when you get to three minutes, one of my clients once said that it felt like he had a football field in his mind. So much space. And now whatever talk you have left there is a very clear, intentional talk.

(01:30:45):
And not only that, and this is why this is such an incredible method, your talk is now internalized. So you're at the stage of I've written a script that I've painfully edited in the old way that you now still have to memorize and it's a written speech that you're going to have to pretend to give in a spoken way. In this case you're there, but it's already completely internalized, not even memorized. It's internalized. You have these pillars, you know where you're going and by the time you make it through the accordion method, you're basically ready to go give it on stage.

(01:31:22):
But you could give it now in one minutes, two minutes, three minutes, five minutes. It's very plastic. You're going to be able to navigate different time frames. It's not going to really matter if you make a mistake because you're going to have a deep sense of what your speech is. It's not memorized, it's internalized. So not only have you gotten clarity and built out your speech in a very intentional way, but by the time you get to the end of it, you also actually know it and you're ready to perform it.

Lenny Rachitsky (01:31:51):
That example of the three minute when you come back up the accordion, that's exactly how it felt when I did this is just like, "Wow, so much time now" because you essentially, the way I think about it is you concentrate it to the best, most important nuggets and then you have time to build on those nuggets and you cut out all the stuff that no one really cares about, which is usually a long introduction, just like now just get to the good stuff and then you expand the good stuff. And it really worked for me and it was a really illuminating experience.

(01:32:19):
For someone that wants to actually use this. Say they have a speech coming up, say they're doing an all hands presentation in a week. Do you do this a week ahead of time? Do you do this a few days before? I guess where do you fit this in the workflow so that you actually remember what you want to say when it comes time?

Tristan de Montebello (01:32:36):
I can't say do it exactly a week or two weeks or it really depends how well familiar you are with the content. If you have an all hands, and this is something that you've been hashing with your executive team over the past two months, you probably know it really, really well and you have a lot of clarity and now it's just about organizing it nicely. So in that case, maybe you want to do a rough go through the accordion a week ahead of time so you have a clear sense of, "What is it that I want my audience to remember and what are the pillars that I know I like to hit that feel really good?"

(01:33:15):
So you can think about these as the foundational pillars that support that one thing that you're sharing or bookmarks that I know I have to hit and then what I would like to do. And so that's what I would write down. I wouldn't write a script. I'd write those down. And then before the all hands, maybe the day before, maybe even the morning of, depending on how important this is or how comfortable you feel, then you might go through just one or two reps of it, but now you already know it, so it should come back very, very quickly in your mind.

Lenny Rachitsky (01:33:44):
And it sounds like it's okay to have some bullet points at the end. It's hard for me to imagine going on stage with a bunch of people watching, not have any slide, bullet point, speaker notes. Any problems just having a couple of the bullet points of core points next to me?

Tristan de Montebello (01:34:01):
Before a talk, I might have four things written down. My one thing, and we'll talk about this in the bow and arrow, my one thing, the one thing I want people to remember and then the three bookmarks or pillars that I want to hit. And these are kind of cues or reminders that are going to send me into that part of the speech. So for example, if I'm talking about the accordion method, like what I just said, if I go back and I think through the pillars of this one. Well, my one thing would be the accordion method is more powerful than memorizing and then doing it the old way.

(01:34:35):
And then my bookmarks might be number one, describe the old way or the old way. Number two, the new way or the accordion method. And then number three might be internalize, don't memorize, and that'll be kind of the takeaway.

(01:34:53):
And if I have that in my mind, if I have 30 seconds, I can say the old way sucks because you have to work so hard and memorize everything and you're memorizing written stuff, the accordion method is much more powerful because you are going to compress it and go down and then open it up and then I'll explain that in a second and then I'll say, so you're internalized not memorized. What I realized right now is actually, it's funny enough though, those were the bookmarks there, so that sent me down that path. But actually I would say bookmark number two is probably the living room analogy. So it would be the old way sucks, the living room analogy, and then describe the accordion method.

Lenny Rachitsky (01:35:36):
That's cool. That was an awesome example of just the insights that appear by forcing yourself through this exercise. And it sounds like maybe the best use of this method is if you have a talk all of a sudden short term it's coming, all of a sudden you have to give a talk somewhere. There's a really powerful method to come up with a great talk that's maybe tomorrow, which you didn't expect.

Tristan de Montebello (01:35:58):
When I say I love this, I use this for myself, I use this with every single client I work with regardless of if it's a five-minute talk, a 20-minute keynote, we're using the accordion method, and you can use this at the macro level or at the micro level, so you can use it for the whole talk, but you can also say, "Hey, let's hone in on this part one that you're struggling with or part two and let's use the accordion to get clarity there."

(01:36:26):
So you can use the accordion as almost like a brainstorming way. I just want to see where I end up here and it takes maybe 15 minutes or something to go through a full accordion. It depends the time constraints you give yourself. Sometimes I'll just do two minute, one minute 30 seconds, that's even shorter, but I'll go through it for one piece of the puzzle or it's like, "Hey, we're almost there. Let's really internalize it. Let's clarify this. Let's get it really, really tight." And then I might say, "Okay, now let's do the whole thing through the accordion. So your 20-minute talk, I want to hear it in three minutes." That gets really, really interesting.

Lenny Rachitsky (01:37:03):
Amazing. Okay. Anything else along the accordion method before we talk about the final technique before we wrap up?

Tristan de Montebello (01:37:10):
We have a full self-paced course on ultra speaking on the accordion. I think it costs like 30 bucks or something like that to access all of the games and all the platforms. A bunch of them are free, but I think this one's behind the paywall. But we also put together a resource where we go all the way, we describe all of the accordion method, the bow and arrow, staying character ending strong on a free email course that we put together. That's ultraspeaking.com/Lenny. So this is shameless self-promotion, but if you want it to go grab it there, you can grab it there and then the bow and arrow is going to tie into the accordion method as well.

Lenny Rachitsky (01:37:53):
Awesome. I'm glad you mentioned all that and we'll point people to that URL in the show notes. Okay, final topic is the bow and arrow technique. Let's talk about what that is and how folks can use that to give better talks.

Tristan de Montebello (01:38:05):
The bow and arrow starts with a, it's really a mindset shift that most of us are in the weeds, so we're very sensitive and familiar to all of the content that we're working on. If you're in data, then you have all of the data. If you're sharing ideas, you still have all of the ideas. And the mistake that most people do when they're preparing a talk, a presentation, an all hands a meeting, whatever it is we tend to focus more on what we want to say than what we want our audience to remember. So the mindset shift here is stop focusing as much on what you want to say and focus more on what you want your audience to remember.

(01:38:51):
What we found out is if you think about your last all hands, the last big meeting, the last talk you saw on YouTube or in person, you probably don't remember much. In fact, I wager you might only remember one thing from that talk. And that's what this is all based on. We call it the bow and arrow technique because we think you can only remember one thing out of a talk and that it's very powerful to go through that framework or that kind of thinking when you're building a talk. And the one thing is your arrow. And so when you have that one thing to me I say it's literally a single sentence that is the only sentence people would remember if they left your talk. Would you be satisfied with that sentence?

(01:39:37):
It takes some times to get to a good one, but if you have a good one, it unlocks everything. It's like you're having a north star or a compass in your pocket. You can always pull it out. You always know where you're going. It gives you a lot of clarity. It's also giving a lot of clarity to your audience obviously.

(01:39:54):
But you can't just throw an arrow at somebody's face. You need to notch it in the bow and pull the bow back. And so to pull the bow back, you need to add in weight to that sentence. And that often comes in the form of an interesting anecdote or a data point that's going to support that or a story that's going to add emotion or illustrate it. So you want to find ways in which you can give weight or pull back the bow so that your arrow has that much more impact. So usually the process of clarifying what your arrow is is a back and forth between the bow and the arrows. So if you're going down the accordion method after the first one you might write or before the first one, you might write a tentative arrow, "Here's my one thing", and then the next one you say, "Okay, actually my one thing might be a refined version of that."

(01:40:55):
And so you might rewrite it a little bit and then you might tentatively put in what you think the bow is. "I like the anecdote I used here. I like this data point that I thought was powerful and maybe I can end on this story or this call to action." Then you'll put that in and then you go back in and you give that a try and that's starting to simplify in your mind.

(01:41:17):
And as you go, usually one informs the other. By the time you finish the accordion for example, you should have a very clear arrow and those clear bookmarks, which is the bow. But really the thing to remember with the bow and arrow, if you can only remember one thing, is switch your mindset from what I want to say to what I want people to remember and limit whatever that is you want them to remember as much as possible and that's going to give you extreme clarity.

Lenny Rachitsky (01:41:48):
That is really helpful. I'm preparing my talk for the summit, and so I'm going to use both of these exercises and what I take away from this last piece is as much as you may want to say a lot of things, really all someone's going to remember, as you said is one thing, if anything, but hopefully they remember that one thing.

(01:42:06):
So it's essentially what's the one thing you want people to remember and then what are the pieces of support that will convince them that that's right and that's something that'll stick with them?

Tristan de Montebello (01:42:16):
Exactly. And again, similar to the accordion method, this works in the macro and the micro. So if you have a talk where you're using slides, use it for the whole talk. But then for every single slide, ask yourself what is my one thing? And you might have some support there as well, but if you don't have a one thing for each slide, either the slide shouldn't exist or it should be multiple slides.

(01:42:45):
The symptom of not having a one thing is usually having a slide that says way too many things. I don't know what data point I want you to remember, so I'm going to put all of it on that slide. I'm not sure which piece of information is more important. So I'm going to write down all of my thoughts and I'm going to go through all of them or hope that you go through all of them and extract what you think is interesting. But the reality is people are just going to zone out if you do that. So if you do that slide by slide, you're going to gain incredible clarity and again, you're going to need less preparation and less memorization.

Lenny Rachitsky (01:43:21):
And to build on that, a pro-tip is to make that title of that slide exactly that one thing you want them to take away. Just put it there and tell them exactly what you want them to learn.

Tristan de Montebello (01:43:31):
Yes. I love that.

Lenny Rachitsky (01:43:32):
Sweet. Tristan, we've been on a journey. This was a really unique experimental episode. I had a good time even though I did some hard things, you made me do hard things that are good for me. Is there anything else you want to share before we get to our very exciting lightning round? Is there anything else you want to leave listeners with or a nugget you want to?

Tristan de Montebello (01:43:50):
I hope people found value. I mean, we did. This was really a group effort and I really appreciate you working on the agenda, really bringing in the games and trying to make this as practical as possible. I think the only thing I want to leave people with is again, this idea of how transformational tackling speaking can be, and the more constrained you feel with your speaking, the more transformational it will be to your life. So I just want to give this encouragement. It's much, much, much more enjoyable than you think it will be. It can actually be exhilarating and energizing and you feel like you can take over the world once you're on this journey. It's beautiful. And so I just encourage everybody, take the first step and start practicing your speaking.

Lenny Rachitsky (01:44:45):
Awesome. And I definitely felt that after doing the workshop of just I feel energized, I want to just talk all time, but then I'm like, I need more work. I need more practice. Tristan, with that, we've reached our very exciting lightning round. Are you ready?

Tristan de Montebello (01:45:01):
Let's do this lightning round. Here we go.

Lenny Rachitsky (01:45:04):
Here we go. First question, what are two or three books that you have recommended most to other people?

Tristan de Montebello (01:45:10):
I was given a book by my first coach, Nathan Seward seven years ago called The Big Leap by Gay Hendricks that I've recommended so many times. And it's based on this idea that we tend to self-sabotage ourselves when we experience too much success or too much happiness. And that that's linked to I think five things that would happen to us when we're growing up. One of them is the... What is it, the wild poppy syndrome or something like that. Like the tallest poppy is the one that's cut first. So if you shine in a family of siblings, then anytime you shine too much we're going to say, "Hey, hey, hey, that's not cool for the others." So that's going to be internalized and hardwired in your body and as an adult, as soon as you start shining a little bit too much, you're going to do the same thing to yourself. So the idea is going from having this point above which you can't be happy to turning it into, he calls it an upward-facing spiral with no upper limit. It's a really exciting and empowering book.

Lenny Rachitsky (01:46:20):
Do you have a favorite recent movie or TV show you really enjoyed?

Tristan de Montebello (01:46:23):
I haven't watched much very recently, but I'll say one of my favorite TV shows of all time is the Peaky Blinders, English show with Cillian Murphy. I'm absolutely obsessed with that movie that show. I think it's a true masterpiece. And I've recently rewatched, so I'll qualify this as recent. I recently rewatched The Nice Guys with Ryan Gosling and Russell Crowe, and I think it's just a brilliant comedy. Brilliant. Another masterpiece, I thought.

Lenny Rachitsky (01:46:58):
Do you have a favorite recent product that you have discovered that you really love. Could be an app, it could be something physical.

Tristan de Montebello (01:47:05):
I have a physical product actually right in front of me that was gifted to me by my business partner Michael Gendler, co-founder of Ultraspeaking. This is called an Ember Mug, and this keeps whatever you have in it, warm and it's extraordinary, whether you are a coffee drinker or a tea drinker, you know the feeling of pouring this and sipping it and by the fifth sip, it's cold. This keeps it at whatever temperature you want it to for however long you want. And I absolutely love it. I've been using it basically every day.

Lenny Rachitsky (01:47:37):
I have one of those. I find myself, you could actually control it through the app. You can control the temperature through an app, which I love. I haven't been using mine, but I love the idea. I know a lot of friends love them. Two more questions. Do you have a favorite life motto that you often come back to, share with friends or family, find useful in work or in life?

Tristan de Montebello (01:47:56):
I think we are too future focused as a species or as a society and as a result, we're always looking for the next thing. So the motto I share with my friends and my business partners and my family the most I think is these are the good old days. And I remind myself, I'll tell you right now for you and for whoever's listening. I mean think about the podcast, it's never going to be this young, it's never going to feel like it feels right now. And it always feels like these things are eternal, but truly one day you're going to look back and you're think, "Man, those were really the good old days." And so I say it right now, enjoy because these are the good old days.

Lenny Rachitsky (01:48:40):
I love that. And it's so relevant with a young kid, you're always going to think about, "Oh, they're little." I love that. Final question. You were the fastest person to reach the finals of the world championship of public speaking. I imagine that was quite a journey. I'm curious if there's a story from that experience that comes to mind that's like a wild part of that journey or something that might surprise people.

Tristan de Montebello (01:49:09):
Well, the journey lasted almost seven months, and it was the craziest journey of my life. I went into that with no experience whatsoever speaking, so really just a random amateur, and I just climbed the ladder by outworking everybody. The story that came to mind right away was six days before the semifinals. So I'm six days before the semifinals and I've qualified for the semifinals two and a half months ago. So I'm nobody, now I'm going to the semifinals of the world championships of public speaking. So my mind really is struggling to compute, and I had finally unlocked a speech that I thought was worthy of giving on the final stage. You have to show up there for the semifinals with one speech, and then the next day, if ever you win, you're going to the finals and you have to have a brand new speech, a completely different speech that you're going to give on that stage.

(01:50:12):
So you need two speeches ready to go, and both of those speeches have to be in theory, world-class. I'm six days before. I was struggling at that, really, really struggling to get that speech together. I finally got something and Michael managed to get me. I was flying I think two days later to Vancouver for the semis, and Michael managed to unlock this one opportunity to speak in front of 50 people to give it a try. And so I ran there. I give the speech, and as usual, we film. I film every single speech. I gave more than a hundred speeches over seven months, and I filmed every single speech. And we'd get home, we'd ask everybody for feedback, and I get home and I'm thinking, "Man, something is wrong. Something is wrong." I was so pumped. I wept. I genuinely wept as I wrote the speech because it was so moving. It was all about my life. It was something that I was so connected to. I don't know, probably the emotion of the pressure as well, but that's how much I believed in that speech.

(01:51:14):
We get home, we put the speech on the computer, and as I get to the most important part of the speech, I see two things happen. So this is the moment where I'm expecting people to pull out their tissues. One person pulls up the agenda for the event that they're at and is starting to look at the agenda. Another person pulls out their phone, another person starts going through their purse, and I'm looking at this, and suddenly I realized, "Oh, this speech, nobody cares about this. This is not a good speech. This is terrible." And then I go through all of these feedbacks.

(01:51:53):
I have 50 pieces of feedback, and all I'm getting is, "Good luck for the semi-finals. It's going to go great. I thought it was good", and I'm like, "I'm going to humiliate myself. This is terrible." So I had waves of anxiety. I threw my speech away, and in five days from the ground up, I rebuilt a completely new speech that was basically the best of everything I'd explored, everything I'd experimented with over the course of the three months leading up to that, the jokes that worked the best, like a stand-up comic would. I built my special and I focused on different areas like all of the transitions.

(01:52:38):
And right before the semi-finals, I gave the speech to one person. I was in Vancouver trying to internalize my speech and memorizing it in a plaza where I delimited the size of the stage and I'm just giving my speech out loud to get over the nerves, so I'm ready for the pressure to see if my brain will remember it and everything.

(01:53:01):
Anyways, I gave it in front of one person who was our district director at Toastmasters, and this is a speech meant for 500 to a thousand people, not one person. So I was scared it would flop. But in the middle of the speech, which is a completely different one, I saw a tear roll down her cheek, and then she just hugged me and said, "You got it. You did it. You did it." I walked out on that stage and I made it, and I won the semi-finals with that speech.

(01:53:32):
I think to me, that was really the, it showed me that everything I'd done was worth something, that it actually worked. If I was able to build a speech in five days, that could get me a win at the semi-finals of the world championships. That was kind of the ultimate, "Wow, I won." So when I walked into the finals, to me, I felt like I had already won.

Lenny Rachitsky (01:53:57):
Wow, that is a story. What an arc. Amazing. I'm so happy you asked that question. Now I just want to watch that speech and I want to learn more about this whole championship of public speaking, which I have no insight into. That could be its own podcast interview.

(01:54:13):
But Tristan, thank you so much for being here. This was incredible. One of the most interesting episodes I've done. Two final questions. Where can folks learn more about Ultraspeaking? I know you built a page where they could experiment with some of this stuff, so share that. And then how can listeners be useful to you?

Tristan de Montebello (01:54:28):
If you go to ultraspeaking. com/Lenny, so ultra like U-L-T-R-A ultraspeaking.com/Lenny, we put together, you have five emails that go deep into a bunch of the things that we've talked here. You can also just go to Ultraspeaking.com where you'll get access to a bunch of the games for free, and you can check out everything else that we do. If you want to follow me or hit me up or ask me questions about this podcast, you can do that on Twitter @Montebello, M-O-N-T-E-B-E-L-L-O. And how can listeners be useful to me? Well, first of all, if you made it to here, then I really appreciate you. Thank you. Thank you for being here with us, and what I would love for you to do is to apply this. We said in the beginning, you can't get better at speaking without speaking, and another piece of that puzzle is you want to do the thing that you're trying to get better at. So if you're nervous speaking in front of people, you want to speak in front of people as part of your practice. So the way you could be useful to me is introduce these games to somebody else. Try them for yourself, practice them with somebody else. Go through the accordion method with a friend. Try conductor, and when you succeed and when you have an awesome experience, then you can tell the world that Ultraspeaking helped you do that, and that would be huge.

Lenny Rachitsky (01:55:56):
Awesome. Tristan, thank you so much for being here.

Tristan de Montebello (01:56:01):
Thanks, Lenny. It was an honor.

Lenny Rachitsky (01:56:03):
It was my honor, Tristan. Bye everyone.

(01:56:05):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review, as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at LennysPodcast.com. See you in the next episode.

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

## Building a magical AI code editor used by over 1m developers in 4 months: Inside Windsurf
**Guest:** Varun Mohan  
**Published:** 2025-04-20  
**YouTube:** https://www.youtube.com/watch?v=5Z0RCxDZdrE  
**Tags:** growth, okrs, roadmap, prioritization, revenue, hiring, culture, management, strategy, vision  

# Building a magical AI code editor used by over 1m developers in 4 months: Inside Windsurf

## Transcript

Varun Mohan (00:00:00):
A lot of the bets we're making inside the company are for things that are not three, four weeks away. We should be cannibalizing the existing state of our product every six to 12 months. Every six to 12 months, it should make our existing product look silly. It should almost make the form factor of existing product look dumb.

Lenny Rachitsky (00:00:13):
How do you know when it's time to hire someone?

Varun Mohan (00:00:16):
I want the company to almost be like this dehydrated entity. Every hire is like a little bit of water, and we only go back and hire someone when we're back to being dehydrated.

Lenny Rachitsky (00:00:24):
Any other there skills you think people should be investing more in with the rise of AI building more and more of our products?

Varun Mohan (00:00:29):
The engineers are now able to produce more technology. The ROI of building technology has actually gone up. This actually means you hire more. The best thing to do is just get your hands dirty with all of these products. You could be a force multiplier to your organization in ways in which they never even anticipated.

Lenny Rachitsky (00:00:47):
Today my guest is Varun Mohan. Varun is the co-founder and CEO of Windsurf, which has quickly become one of people's favorite AI coding tools, and is basically the main competitor to Cursor with over 1 million users four months in. In our conversation, Varun shares what makes Windsurf unique, why they decided to invest heavily in enterprise sales very early in their history, why agency is going to be the most important skill for engineers and product builders to build, also the story of how they started out as a GPU infrastructure company and realized there was a much bigger opportunity up the stack and the two pivots that got them to where they're today.

(00:01:20):
He also gives a live demo, advice for being successful at Windsurf, and so much more. There's so much to learn about where things are heading for engineers and product builders in general in this conversation. And I'm really excited to bring it to you.

(00:01:32):
Thank you to everyone on LinkedIn and Twitter and my newsletter community for suggesting great questions to dig into with Varun. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. Also, if you become a yearly subscriber of my newsletter, you get a year free of Perplexity Pro, Notion Plus, Linear, Granola, and Superhuman. Check it out at lennysnewsletter.com. With that, I bring you Varun Mohan.

(00:01:59):
This episode is brought to you by Brex, the financial stack used by one in every three US venture-backed startups. Brex knows that nearly 40% of startups fail because they run out of cash. So they built a banking experience that focuses on helping founders get more from every dollar. It's a stark difference from traditional banking options that leave a startup's cash sitting idle while chipping away at it with fees. To help founders protect cash and extend runway, Brex combined the best things about checking, treasury, and FDIC insurance in one powerhouse account. You can send and receive money worldwide at lightning speed. You can get 20X the standard FDIC protection through program banks. And you can earn industry-leading yield from your first dollar while still being able to access your funds anytime. To learn more, check out Brex at brex.com/banking-solutions. That's B-R-E-X, .com/banking-solutions.

(00:02:57):
This episode is brought to you by Productboard, the leading product management platform for the enterprise. For over 10 years, Productboard has helped customer-centric organizations like Zoom, Salesforce, and Autodesk build the right products faster. And as an end-end platform, Productboard seamlessly supports all stages of the product development lifecycle, from gathering customer insights to planning a roadmap, to aligning stakeholders, to earning customer buy-in, all with a single source of truth. And now, product leaders can get even more visibility into customer needs with Productboard Pulse, a new voice of customer solution. Built-in intelligence helps you analyze trends across all of your feedback and then dive deeper by asking AI your follow-up questions. See how Productboard can help your team deliver higher-impact products that solve real customer needs and advance your business goals. For special offer and free 15-day trial visit productboard.com/lenny. That's Productboard.com/L-E-N-N-Y.

(00:04:00):
Varun, thank you so much for being here and welcome to the podcast.

Varun Mohan (00:04:03):
Buddy, thanks for having me. A long time listener.

Lenny Rachitsky (00:04:05):
Oh, I really appreciate that. I'm so excited to have you here. I feel like just you guys have become this overnight success, which is definitely not an overnight success, but I feel like I've been hearing about Windsurf more and more as people's favorite AI tool. And I just don't think people know the story behind Windsurf, behind Codeium, the company that you built. So I thought it'd be good to maybe just start there and have you just briefly share the history of Codeium and how Windsurf emerged out of Codeium.

Varun Mohan (00:04:31):
Yeah. So the company was actually started close to four years ago. As you know, AI coding was not a thing four years ago. ChatGPT was not out four years ago. At the time, we actually started out building GPU virtualization and compiler software. Before this, I worked in autonomous vehicles. My co-founder, who I had known since middle school, worked on AR/VR at Meta. And for us, we believe deep learning would touch many, many industries. It wouldn't just touch autonomous vehicles. It would touch financial services, defense, healthcare. And we believe these applications were hard to build, these deep learning applications. So we made it possible for you to effectively run these complex applications on computers without GPUs, and we would handle all the complexity of being able to actually run the workload on the GPUs for you. And we were able to optimize these workloads a ton.

(00:05:20):
And in the middle of 2022 rolled around and we had a couple million in revenue and we were managing upwards of 10,000 sort of GPUs. We had eight people. At the time, we were free cash flow positive. But I think what we felt was once these generative models started to get very good, we sort of felt a lot of what we built was not as valuable. And this was a very, very hard moment for us at the company. We were only eight people at the time, but we felt, "Hey, would people be training these very bespoke sentiment classifier models anymore that were very, very custom models? Or would they just ask GPT-N, is this a positive or a negative sentiment?" Probably it's going to be the latter, right? And in a world in which everyone was going to run generative AI models, why would an infrastructure company be a differentiator? Because everyone is going to run the same kind of infrastructure down the line.

(00:06:06):
So instead what we decided to do was we believe generative AI was almost going to be like the next internet. And in that case, what we should go out and do is build the next great apps like Google, like Amazon. And we vertically integrated and actually took our infrastructure, our inference infrastructure to go out and build Codeium at the time. And at that time, we were early adopters of GitHub Copilot and we thought the coding space was going to get tremendously disrupted in the next coming years. So we actually took our infrastructure, we ran our own models in massive scale. We even trained our own models.

(00:06:35):
In the very beginning it was very, very simple. It was purely an autocomplete model, which basically means that as the user was typing, we'd complete the next one or two or three or four lines of code. But we provided the product entirely for free in all the IDEs that developers coded. That meant to VSCode, JetBrains, Eclipse, Visual Studio, Vim, Emacs. And the reason why we were able to build it for free was because of our infrastructure background. We were able to optimize these workloads a ton.

(00:07:04):
I guess very quickly after that, some large businesses also wanted to work with us. And we built out this enterprise motion to work with these large companies like Dell, JPMorgan Chase. And for them the bigger thing wasn't just, "Hey, could we autocomplete code or could we chat with the code base?" It was, "Could you offer us a secure offering that was also personalized to all the private data inside the company?" So we took our infrastructure and made it so that we invested a ton in making sure that we deeply understood these large companies code bases. And that's what we were working on until six months ago.

(00:07:33):
It's not that we've stopped working on that, but basically what we realized six months ago was we were getting limited by the IDEs that we were already working in. So VSCode, which is a very popular IDE, had a ceiling for the AI capabilities, we could showcase our users. And because of that, we decided to go out and fork VSCode and build our own IDE with some of these new agentic capabilities. And over time in the last couple of years, the model capabilities have also been growing exponentially year over year. And that's sort of where we are right now. I skipped a lot of pieces there, but that's what we're landed.

Lenny Rachitsky (00:08:05):
There's so many interesting threads there. One is just, there's always this question of just where value will accrue in AI. And it's so interesting, you guys started almost at the bottom layer of infrastructure GPUs and then you went to what people call a GPT wrapper, not actually. So I guess any just lessons there, just thoughts on just where you think value will end up in this world of AI and the stack of AI tools?

Varun Mohan (00:08:28):
Maybe I can start by just saying one thing about startups that I think are really true, it's very unlikely the first thing that you believe you should go work on is going to be the right thing, which is a very hard thing to kind of wrangle with being a startup founder, right? You need to kind of be irrationally optimistic that what you're going to do is going to be differentially important. Because otherwise, why would you go out and do what you're doing? And if it's obvious, then a bigger company would've already done it, right?

(00:08:56):
But then you also need to be really, really realistic because most ideas that are, I guess, non-conventional are usually bad ideas, right? So it's this weird tightrope you need to kind of balance on top of where you're pushing for a future that you believe is true, but all the while you're getting new information. You need to kill the beliefs that you had. And if I were to start with the infrastructure piece, we first went in with the assumption that model architectures were going to be really, really heterogeneous.

(00:09:27):
Working from an autonomous vehicle background, there were many different types of model architectures out there. There were convolutional neural networks, graph neural networks, recurrent neural networks, LSTMs, sort of lighter neural nets with frustrum point networks. And there were maybe tens of architectures we were dealing with. And at that point we were like, the complexity of this is so high that it's very clear if someone offloaded the complexity, there would be a lot of value.

(00:09:50):
Fast-forward to the middle of 2023, everything looks like it's going to be a transformer. So now our hypotheses are just wrong. So at this point then, most of the value is probably not going to accrue at purely the, at least this is our belief, at the infrastructure layer. It's going to accrue somewhere else. Where is the layer that you can actually differentiate on? And we believe the application layer is a very, very deep layer to go out and differentiate on, right? What are the number of ways we can build better user experiences and better workflows for developers? We think there's effectively no ceiling on that, on how much better we can make the lives of developers basically.

Lenny Rachitsky (00:10:22):
You touched on the second thread that I thought was really interesting here, is just how you guys pivoted from ideas that were working. You were making money, people loved it. You said you had millions of dollars of ARR revenue. And then you're just like, "No, we're going to completely change the business."

(00:10:36):
So the question there is, just like, what have you learned about knowing what to follow? And one thing I heard there that was really interesting is just once your assumptions change about that you built your idea on, it's time to think this idea and maybe try something else.

Varun Mohan (00:10:48):
I think the way we sort of think about this is even when we're working right now, we just accept that we're going to get a lot of things wrong. We're just going to get a lot of things wrong. Obviously that's a very big moment because that was a bet the company moment in the sense that we basically said, told our investors, "Hey, we're making money on this." We had already raised 28 million of capital and we were just like, "Hey, we're just going to pivot entirely from this." And we did that overnight. This wasn't this thing where we just said, "Hey, maybe a quarter, one or two quarters." Because one of the things we knew that's very important for startups is focus.

(00:11:20):
If you're trying to do another thing that you think is big and you're focused on something that you don't believe is valuable, you're guaranteed going to fail at the thing you think is going to be big. So that's a very obvious thing there. But I think once you go in with the assumption that a lot of your hypotheses are going to be wrong, but you will do the most concentrated work possible to go out and validate these hypotheses and you won't be in love with your ideas.

(00:11:41):
I think ideas, it's awesome when you have a great idea, but you should never be too in love with your ideas. And you have an organization that is very truth-seeking. I think a lot of people at the company have had their ideas tested over and over again. Even just building Windsurf. That is not a complete company pivot, but that's a big decision that we made at the company. You kind of need to make some bets. And sometimes you're wrong and sometimes you're right. But if you have an organization that comes out and you feel like morale is not going to be low if you made the wrong decision, that's the best, right? That means you have optionality for the rest of time.

(00:12:14):
And Lenny, one thing that I try to tell the company about this is, this year the total amount of engineering output we'll have is much larger than the engineering output we've had since the beginning of the company's creation 'till now. So that almost means every year is a new lease on life for us, right? It's almost a new way for us to test out an entirely new set of hypotheses. And maybe we were wrong about our original hypotheses in the first place. What makes us more smart than everyone else to be right more times than that?

Lenny Rachitsky (00:12:46):
That's so empowering. It makes me think about... Uri Levine was on the podcast, co-founder of Waze, and he has this phrase that he wears on his shirt. His book is called this Fall in Love with the Problem, Not the Solution. And that feels like that's exactly what you're describing.

(00:12:59):
Okay, so let's talk about Windsurf. What's the simplest way for people to understand what is Windsurf?

Varun Mohan (00:13:04):
Yeah. So Windsurf is an IDE, right? It's an application to go out and build software and build applications. The crazy thing is a lot of people who use the product don't even probably know what an IDE is, which is crazy. And we'll get into that in a second.

(00:13:22):
But why did we go out and build Windsurf and what is Windsurf maybe? Why couldn't we have just done this on top of conventional IDEs like Visual Studio Code? So maybe just to get into this a little bit, as we saw that AI was getting more and more powerful, the way people go out and build technology, we thought the interface for that was going to change remarkably. It was not going to be a conventional pure text editor where the user is writing a handful of lines of code or most of the code and the IDE provides maybe some basic feedback on what the user is doing right or wrong. And the basic feedback could be, "Hey, there's a bug in your software or compiler error in your software." It could do much more, right? It could actually go out and modify large chunks of code.

(00:14:04):
One of the key pieces that we recognized was, with this new paradigm with AI, AI was probably going to write well over 90% of the software, in which case the role of a developer and what they're doing in the IDE is maybe reviewing code. Maybe it's actually a little bit different than what it is in the past. And we'll see this very soon with Windsurf. Maybe when you're using the product, actually a good chunk of the user's time is that you're reviewing what the AI is outputting. So we needed to build custom-review flows into the IDE to actually make it so that it was easier to actually go out and do that, right? Because the developer is not spending all their time writing code.

(00:14:38):
And this is the fundamental premise on why we built the product. We thought we were going to get limited a ton if we had very, very basic UI out there. And I'll give you even a simple example here. We have this auto-complete product that completes a handful of lines of code. Now we've actually launched this offering called Windsurf Tab that basically shows you refactors as well. And these refactors are almost inline refactors. And we were able to build a custom UI for that in Windsurf.

(00:15:03):
But in VSCode, because of the access to the APIs, we needed to dynamically generate images right alongside the user's cursor because we just didn't have access to the capabilities to showcase and edit properly. And what we realized is immediately by porting over to Windsurf, our acceptance rate tripled. Same ML models, it just tripled. So what that, I guess, gave us confidence in is yeah, you could argue technology is very important. And I think technology is very important. But if our users are getting very little value from the technology we're sort of building, you need to really clarify, "Maybe we do need to build a new surface and interface." And that's what Windsurf is.

Lenny Rachitsky (00:15:39):
So the big bet you took there just to make this super clear, is you were initially working within existing IDEs that everyone was familiar with. And then it was like, "This isn't going to get us where we need to go. We're going to try to convince people to switch to something completely new because it's going to be so much better. It's our own IDE."

(00:15:56):
I think maybe people may not recognize just how risky that is, convincing engineers to use something completely new. That's a huge deal.

Varun Mohan (00:16:02):
Yeah, no, of course. And one of the key pieces, maybe Lenny, that would be important to share is a lot of our developers do use Visual Studio Code. But there are lots of people that write in languages like Java, sort of C++ and so on and so forth, and they might use the JetBrains family of IDEs that like IntelliJ. And for us, we are actually still committed to building on those platforms, right? We just felt though that one of the dominant IDEs, which was Visual Studio Code, was limiting the sort of user interface that we could give to our actual customers.

Lenny Rachitsky (00:16:35):
What is the current state of traction for Windsurf? You hear all these crazy numbers about all the competitors in your space. What can you share there for folks just to know?

Varun Mohan (00:16:43):
Yeah, so maybe a handful. We launched the product a bit over four months ago. And in that period of time, over a million developers have tried the product. And obviously we have many hundreds of thousands of monthly active users right now.

Lenny Rachitsky (00:16:54):
I love how these days like, "oh, a million. Oh, no big deal." It's just the numbers are absurd these days. We're just getting used to just 100 million ARR here, million users in four months there. It's just like, "Oh, of course. How could you not have that?" But that's absurd. It's just like an insane time right now.

(00:17:12):
You touched on something that I wanted to get to later, but I may as well bring it up now, the question of just how engineering will change in the future. You throw out the stat that 90% of code is going to be written by AI in the future. Dario from Anthropic recently said the same thing. You guys have a really interesting glimpse into just how things will look in the future.

(00:17:31):
So I guess the question is just, how do you think coding specifically will look in the next few years, how different will it be from today?

Varun Mohan (00:17:39):
I think when we think about what is an engineer actually doing, it probably falls into three buckets, right? What should I solve for? How should I solve it? And then solving it. I guess everyone who's working in this space is probably increasingly convinced that solving it, which is just the pure, "I know how I'm going to do it" and just going and doing it. AI is going to handle vast majority, if not all of it. In fact, it probably actually, with some of the work that we've done in terms of deeply understanding code bases, how should I solve it is also going to get closer and closer to getting done. If you deeply understand the environment inside an organization, if you deeply understand the code base, how you should solve it, given best practices when the company also gets solved.

(00:18:19):
So I think what engineering kind of goes to is actually what you wanted engineers to do in the first place, which is, what are the most important business problems that we do need to solve? What are the most important capabilities that we need our application, our product to have? And actually going and prioritizing those and actually going and making the right technical decisions to go out and doing it. And I think that's where engineering is probably heading towards.

(00:18:40):
Now, does that mean that no one needs a CS degree? I think that's maybe a little bit overplayed a little bit just because maybe here's my argument for that. A lot of developers nowadays that build full stack applications, at least until a handful of years ago, they probably went to college and took an operating system course. And in theory, they're not really playing around with the operating system, like the kernel scheduler very frequently. But do those principles help them in understanding why their applications are slow? Do they help them in understanding why some design decisions are better than the other? Yeah, that makes them a much better engineer than another engineer. And I think that idea and the understanding of what's going on at the bottom will make a good engineer even better. But also at the same time, it empowers a bunch of people that never understood all of those things, how to actually build as well, which is another remarkable sort of thing that fell out through this whole process.

Lenny Rachitsky (00:19:33):
I don't know if you have kids, but just say you had kids or you had niece or nephew going into college, let's say, would you suggest they do do computer science or would you suggest you're not going to have a good time if that's the career you choose right now?

Varun Mohan (00:19:47):
Yeah. Maybe I think back a little bit. So I went to MIT. A lot of us at the company went to MIT together on the engineering team. I think when I think about what we learned the most for engineering or computer science, it was not exactly like how do you write code. That is almost a given that you can write code after going to college. It's more like the principles of how you think about a problem and how you break it down and how you solve it in an interesting way.

(00:20:15):
So an example of a class that I really enjoyed was our distributed systems class. And there, you're kind of reading through literature and understanding how some design decisions were kind of made. And I think it's more like a problem solving kind of course and a major. It's a major of how you solve problems given some constraints of how computers today function, right? Like, here's the speed at which memory sort of operates. Here's the speed at which... Here's how much computation you can do in one cycle or one second. And based on that, you can make some trade-offs and solve a problem.

(00:20:45):
So I don't know if I would say that you shouldn't go get a computer science degree. I think computer science is almost synonymous with problem solving. In that case, I think it's pretty valuable. Is everything you learn in your computer science degree useful? I'd say a lot of things that I learned in my computer science degree are not useful. I'll give you an example. I took a parallel computing class in Julia. I don't think Julia is a very popular programming language anymore. Am I very sad that I took the class? No. The principles of parallel computing are still very useful, I would say, today.

Lenny Rachitsky (00:21:12):
So what I'm hearing is, skills that you still want to build, whether it's computer science or maybe some version of computer science, is kind of building the mental model of how computers and systems work.

Varun Mohan (00:21:12):
That's right.

Lenny Rachitsky (00:21:23):
Parallel processing, memory, hard drives, internet, things like that. And then there's just problem solving skills, being able to solve interesting problems. Is there any other skills you think people should be investing more in with the rise of AI building more and more of our products?

Varun Mohan (00:21:37):
I think one of the things that's maybe a little bit undervalued is this kind of agency piece. And I think about this a lot, which is, you have a lot of people that could go through college and go through school and they're basically told exactly what to do on a P-set. They're given these very, very, I would say, well-defined paths that they need to take. I think maybe in society and just school, we don't prioritize how do you make sure you get people with real agency that want to build something, right? Their goal is not just to maybe graduate from college and then get a job at a big tech company where they're told exactly what to do or where to put the pixel for this one website. I think that's maybe a skill set that is undervalued just right now, probably in the last maybe 10 years or so. And I think that's going to be really, really important.

(00:22:27):
For a startup, obviously these are skills that we just look for. We look for people that are really high agency because we just recognize that by default, if we don't innovate and do crazy things, we're going to die. The company is just going to die. So we just look for this, right? But I would say for most software engineering jobs, that's probably not the case. Just think about big company X and what they're hiring for on the average software engineering interview. It probably doesn't look like that.

Lenny Rachitsky (00:22:52):
I love how you phrased that. If we don't do crazy things and innovate, we're going to die. That would be a great title for this podcast episode. And I think, I know, it's 100% true. There's just a lot of crazy things happening and a lot of innovation happening. And if you can't keep up, you'll die.

(00:23:07):
So let's talk about hiring. You have a really interesting approach to hiring. There's a few questions I have here. One is just how do you... I know you try to stay really lean. That's a common theme across all the AI startups these days. How do you know when it's time to hire someone?

Varun Mohan (00:23:22):
I love the idea of being a lean company, but I don't idolize it in the way that, "Hey, it is a dream to be a 10% or 20% company that's making 50, 100, 200 million in revenue." That's not, I think, what we idolize inside the company.

(00:23:36):
I think what we idolize is, be the smallest company we can be to satisfy our ambitions. That's what the goal is. And maybe, Lenny, the way I would sort of put that out there is, if I told you, "Hey, I'm going to build an autonomous vehicle," and I said our team is 10 people, you should rightfully say, "Hey Varun, you're not serious. And you'd be right. I'm not serious at that point. So I think the answer is, what is the minimum number of people to go out and build the crazy ambition project that you have?

(00:24:04):
And I think the project we are trying to go out and do, which is completely transform the way software gets built, we've mentioned this [inaudible 00:24:11] the company, our goal is to reduce the time it takes to build apps and technology by 99%, right? It is a tremendously sort of ambitious goal. And it's not possible for us to be a 10, 20, 30, 40 person engineering team in the long term and actually satisfy that goal. We think there's a very, very high ceiling. So that's maybe the first key piece there. It's like, if we can crack actually being a fairly sizable company but still operate as if we're a startup, that's the dream. That's the dream.

(00:24:40):
In terms of hiring philosophy, the way we sort of think about things is, we only hire for a role if we're actually underwater for that function. So let's say we're going out and building inference technology. Unless we're underwater there, we will not go out and hire someone to go out and work for that. And the reason for that is, I actually think this is a feature. When you hire for a role and you already have enough people there, you get a lot of weird politics that ultimately ends up happening. And it's not because people are bad people. I think most people are really well-intentioned. But what happens when you have people that join a company and in reality you didn't really need them? They will go out and manufacture some other thing that they should go work on. They will go out and figure out something else to work on. And realistically, it's not that important, but they will go out and try to convince the rest of the organization that it is important.

(00:25:30):
I just think as a startup, we don't have the bandwidth to go out and deal with that, right? For me, I would like to see everyone just almost be raising their hands up being like, "I'm dying. We need one more person." And that's when we go out and hire someone. And one of the analogies I like to give is, I want the company to almost be this dehydrated entity and every hire is like a little bit of water. And we only go back and hire someone when we're back to being dehydrated.

Lenny Rachitsky (00:25:57):
I love this metaphor so much. And it sounds painful. It sounds painful that you need to be underwater and raising your hand, "I'm about to die and dehydrated." But I also know that it's a really exciting way to work. It sounds hard, but if you're in it, it's just like... I guess talk about just that side of it because I think it could sound like, "This is terrible. I don't want to work this way."

Varun Mohan (00:26:19):
You know what I actually think, Lenny? It's really good for a handful of reasons, which is that a lot of the... We respect and trust the people that work at the company. So this forces ruthless prioritization. You have a team that's going out and doing something. They will never ask to work on something that's not important. In fact, if there are two things that they're working on, they're just going to just tell me, "Hey, there are two things on my plate. I just don't have the ability to do two. I can only do one." And they will pick the one that's most important.

(00:26:45):
And this actually goes back to one thing that I think is true about startups and just companies in general. You don't win by doing 10 things well. You win by doing one thing really well and maybe you fail nine things. This is the thing that I've told the company, "This is very different than school," right? In school you optimize for your total GPA. But for companies, I just need to get an A+ on the one class that matters. And then I can get an F in all the other classes. And an F in all the other classes doesn't mean just doing illegal things. That basically means you just deprioritize things that don't matter. That actually forces this organizational prioritization that is just really, really good.

(00:27:22):
And Douglas and I, Douglas being my co-founder, we can tell the company, "These are the two things that are the most important." But if we go out and tell these are the two things that are the most important to the company and then we put the company has 20% more people than necessary, what's going to ultimately happen? It's almost a forcing function for ruthless prioritization to have fewer people or people that are just underwater internally at the company.

Lenny Rachitsky (00:27:46):
Everyone listening that works at a big company knows exactly what you mean when you described when there's just too many people, they will all find work to do and they will all be pitching ideas. They all want to show impact, they want to do well in their performance reviews. That's just the nature of too many people at a company. And so I think this all really resonates.

(00:28:04):
To even getting even deeper on just what it looks like when someone's underwater to tell you it's time to hire, is it just someone coming to you, "Varun, I need someone on this team. This is just not possible"? What does that look like even more practically?

Varun Mohan (00:28:16):
Yeah, I think it's basically along those lines. It's that, "Hey, there's some pressure to get something done in a short period of time." By the way, one of the things that we do believe though for software, if you want to do great things, it's not possible to just say, "Hey, I want to get it done in one month" if it is like... Because you have to think about it from this perspective. If a software project could get built in two to three weeks, what does that really mean about the true complexity and differentiation of what you built? It's probably not very high, unless you believe you are way smarter than everyone else. But I think that's hubris, right? I think we actually have a very exceptional engineering team. But also at the same time, I don't think our engineering team is so exceptional that we can do things in three weeks that the rest of the world can't do in six to nine months. That's kind of stupid to believe that.

(00:28:57):
So I think basically it comes down to that person coming out and being like, "Hey, look, I don't have enough time to do X." Us having a conversation to be like, "Okay, what can you do then?" And if the answer is, "I can only do less than that," then maybe we make a decision actually, "Oh wow, that's great. Maybe we actually should deprioritize Y." Because this is actually also another thing that's very hard even for people like me and my co-founder. It's that we also want to do a lot of things. There's an urge to do a lot of things. But if we are forced to make a decision constantly on like, "We cannot do X," it's very clarifying. It's very clarifying because our engineering interview process is also extremely low acceptance rate. So it's not very easy for us to very quickly spin up people and have them join the company really, really quickly either.

(00:29:43):
So I think it's clarifying for everyone. It's clarifying for the person that wants more people. We can just tell them, "Hey look, we don't believe you should be doing this other thing." And it's also clarifying for us because we can also get on the same page with them. And sometimes we just kind of agree, "Hey..." Our teams are very flexible that, "Hey, actually we do need to get something done." And one of the things that we've kind of tried to make sure is true on our engineering team is, people's value to the company does not have anything to do with the size of their team. There are projects inside the company, there are directly responsible individuals for these projects inside the company. And if we feel like one project is very important, then people can move from one project to the next.

(00:30:21):
There's no notion of someone owning people at the company. That is a very bad and gnarly idea. In fact, the person that is the most valuable at the company is the person that can do the most crazy sort of project out there with as few people as possible. And that's what you should be rewarding internally.

Lenny Rachitsky (00:30:35):
How many people do you have at coding at this point?

Varun Mohan (00:30:37):
So we have close to 160 people and the engineering team is over 50 people right now.

Lenny Rachitsky (00:30:42):
Awesome. Oh, what's the other bigger functions? So [inaudible 00:30:46]-

Varun Mohan (00:30:46):
We have go-to-market. We have a... Yeah.

Lenny Rachitsky (00:30:48):
Oh, right. Okay. I want to talk about that, the sales learning that you guys had. Okay. But let's close out this hiring conversation. So we talked about what you look for... To tell you it's the time to hire, what do you look for in the people that you interview and hire?

Varun Mohan (00:31:01):
One of the key pieces that we look for, we have a very high technical bar. So assuming that they actually meet the technical bar, I think we sort of look for people that are really, really passionate about the mission of what we're actually trying to solve and people that are willing to work very hard. I think one of the things that we don't try to do is convince people, "Hey look, we are a very chill company and it's great to work here." I think, no, this is a very exciting space. It's very competitive. You should expect us to lose if the people at the company are not kind of... They're not working very hard. And I think one of the biggest dog whistles I hear is, when I ask people how hard are you willing to work, some people actually ultimately say, "Hey, I work very smart." And I basically ask them a question, "If we have many smart people at our company that also work hard, what's the differentiator going to be? Are you just going to pull them down?"

(00:31:48):
Because I think one of the things that's true about companies is it's like this massive group project. And I think the thing about a person that is not pulling their weight that's bad. It's not the productivity, right? At some point when the company becomes many hundreds of engineers, I'm not going to be thinking about the one engineer that's not pulling their weight. It's the team of people they work with that are almost basically saying, "Is this the bar internally at the company? Is this the expectation?" And I guess, Lenny, if I told you you have a team of five people and the four other people you're working with just don't care, how much are you going to feel like you should care?

Lenny Rachitsky (00:32:21):
Not too much.

Varun Mohan (00:32:22):
Exactly. So for us, I think that's what we more care about. We have a culture where it's very collaborative. It's not an individual sport, but people feel like they can rely on other people to get complex sort of tasks done.

Lenny Rachitsky (00:32:35):
So the question you asked there just basically is, how hard are you willing to work? How hard do you want to work? And I know some people, there's this whole group of folks that are just like work-life balance, "How dare you ask me to work crazy hours?" And I love just the filter upfront of, "If you work here, you will work really hard. You'll work a lot of hours. It's a crazy space to be in. And we will win by working smart and also really hard."

Varun Mohan (00:33:02):
Yeah.

Lenny Rachitsky (00:33:03):
You said at some point earlier that your engineering pass rate, as you said, it was like 0.6% of candidates, something like that.

Varun Mohan (00:33:10):
Yeah, it's probably post or take home. It's probably that actually. So the take home itself filters probably another 10, 15X on top of that.

Lenny Rachitsky (00:33:19):
Here's a question that I've been hearing more and more, is just, how do you do interviews these days with tools like Windsurf out there that solve all your problems?

Varun Mohan (00:33:25):
We are okay with people using the tools because I think one of the worst things is like, if someone comes here and doesn't like using these tools, we believe there are massive productivity improvements. We do bring people into the company on site so we can actually see how they think through problems on a whiteboard and all these other pieces. So we do want to see how they think on their feet and hopefully they're not just taking what we're saying, putting it in a voice translator and sticking it into ChatGPT and getting the answer out.

(00:33:51):
So there is a way to do this. My viewpoint on this is the tools are really, really important, but I do think we still look for some problem solving ability. If the only way you can solve a hard problem is put it into ChatGPT, I think that's a concern to us.

Lenny Rachitsky (00:34:07):
Today's episode is brought to you by Coda. I personally use Coda every single day to manage my podcast and also to manage my community. It's where I put the questions that I plan to ask every guest that's coming on the podcast. It's where I put my community resources, it's how I manage my workflows.

(00:34:22):
Here's how Coda can help you. Imagine starting a project at work and your vision is clear, you know exactly who's doing what and where to find the data that you need to do your part. In fact, you don't have to waste time searching for anything because everything your team needs from project trackers and OKRs to documents and spreadsheets lives in one tab all in Coda. With Coda's collaborative all in one workspace, you get the flexibility of docs, the structure of spreadsheets, the power of applications, and the intelligence of AI all in one easy to organize tab.

(00:34:54):
Like I mentioned earlier, I use Coda every single day. And more than 50,000 teams trust Coda to keep them more aligned and focused. If you're a startup team looking to increase alignment and agility, Coda can help you move from planning to execution in record time. To try it for yourself, go to coda.io/lenny today and get six months free of the team plan for startups. That's C-O-D-A, .io/lenny to get started for free and get six months of the team plan. coda.io/lenny.

(00:35:24):
Okay. Let's talk about this go-to-market sales experience that you guys had. So you started obviously like most people, started building without sales team. And then you realized, from what I hear, that that was a huge miss and a big opportunity to talk about there because that's really unique, I think, that you guys have a large sales team and go-to-market team.

Varun Mohan (00:35:40):
Yeah, we actually made this decision pretty early in the company's history, I would say. We hired our VP of sales over a year ago actually. And the go-to-market team is now over 80 people inside the company. So it's a pretty sizable function inside the company.

(00:35:55):
Yeah. Maybe a little bit of a backstory here. So when we started the company, actually we had a handful of angels that actually were operators, go-to-market operators. So an example of one was Carlos Delatorre who used to be the CRO of MongoDB. And I think for us, we never viewed enterprise sales and sales as a very negative thing. I think this is a interesting thing that technical founders sometimes don't really like. They think sales is a very negative part of the process. Everything should be product-led growth. I think it's not that black and white. I think enterprise sales is really valuable. But maybe when we were a GPU virtualization company and we were an infrastructure company, the reason why we never hired a salesperson is, I didn't know how to scale the function. I was the one who was selling the product.

(00:36:37):
So ultimately speaking, if it was hard for me to sell the product incrementally, I didn't know how we could make that into a process that we could then go and scale. I didn't know how we could take the revenue of the business from a couple million to hundreds of millions and let alone even tenths. So if I didn't know how to do that, how could I go out and hire someone and make them scale it out?

(00:36:58):
On the other hand, for Codeium, very quickly, a lot of large enterprises reached out to us. And from that alone in the middle of 2023, we started, I guess, me and a handful of other folks at the company started selling the product and we were doing tens of pilots concurrently with large enterprises and we were very quickly able to understand that there was a large enterprise motion that needed to be built in this space. So by the end of 2023, we actually hired our VP of sales. And very quickly after that, scaled our sales team. Yeah, I mean look, if you want to sell to the Fortune 500, it is very hard to do that purely by swiping a credit card.

Lenny Rachitsky (00:37:35):
Let's talk about Cursor. I don't want to spend too much time with competitors, but that's what everyone's always thinking about when they think of you guys. You guys are kind of the leading players, I think, in the space also. There's Copilot, but that's different.

(00:37:46):
So what's the simplest way to understand how you guys are different from Cursor and also just how you think you win in the space long-term?

Varun Mohan (00:37:53):
So I think maybe a handful of things that I could share. So on the product side, I think we've invested a lot in making sure code-based understanding for very large code bases is really high quality. And that's just because of where we started. We worked with some of the worlds are just companies like Dell, JPMorgan Chase. Companies like Dell have singular code bases that are over 100 million lines of code. So being able to understand that really, really quickly to make large scale changes is something that we've spent a lot of time doing. And that requires us actually building our own models that can consume large chunks of their code base in parallel across thousands of GPUs and almost rank them to be able to find out what the most important snippets of code are for any question that are asked about the code base. So we've gone out and built large distributed systems based on our infrastructure background to go ahead and do that. That's maybe one.

Lenny Rachitsky (00:38:38):
Let me actually follow that thread because I think people may underestimate just how big of a deal that is. So when we talk about, we had the founders of Bolt and Lovable on the podcast, so those products, they build something from scratch, they built, they write the code for you. So that versus just loading, say, Windsurf on your million line code base, say, at Airbnb or Uber. Like, understanding what the hell you have and how it works and where to go change things without breaking it is insanely hard. And so what I'm hearing is that's kind of a big differentiator as you guys started there actually. And then Windsurf is now building up that advantage.

Varun Mohan (00:39:15):
That's right. Yeah. So that's a big thing that we spent a lot of time on, which is just understanding what the code base is doing. And actually one of the other things is, what are all the user interactions with respect to the code base? And happy to show that also in a bit here.

Lenny Rachitsky (00:39:31):
Awesome.

Varun Mohan (00:39:31):
The second key piece probably is we're not only tied to Windsurf actually. This is probably a weird statement given even we are talking about Windsurf, which is that actually we're pretty focused on supporting IDEs like JetBrains. JetBrains or IntelliJ has over 70 to 80% of all Java developers coding in JetBrains based IDEs, right? The reason why we don't feel as big a need to almost build a competing product to JetBrains is JetBrains is actually a very sort of extensible product in a way that VSCode is not. VSCode is not very extensible.

(00:40:05):
So I think for us, our goal here is not only just to satisfy a subset of users that can actually switch onto our IDE, but we want to give this agentic sort of experience to every sort of developer out there. And if that means there are Java developers that write in JetBrains, that's fine. We work with a lot of large enterprises that have 10 plus thousand developers where over 50% of the developers are on JetBrains. It's a very large product. And by the way, that company itself is a privately held company that makes many hundreds of millions of dollars a year. So it's a very, very large company. So for us, that's another key piece. We actually want to meet developers sort of where they are. And if they use a different platform, we'll work on that too.

(00:40:42):
The third key piece, and this probably sounds another key piece for enterprises, is we work in a lot of very secure environments. We have FedRAMP compliance, which means we can sell to very large government entities. We have a hybrid mode of actually using the product, which means that all the code that lives that is indexed, it actually lives on the tenant of the user, right? Code is one of the most important pieces of IP for the company. So I think just if you were to look at it from a big company perspective, there are many reasons why over the years of just building an enterprise product, we've handled a lot of complexities that large companies want to see. But that's part of it is because of the history of how we got here in the first place.

Lenny Rachitsky (00:41:21):
Okay, Varun, enough teasing. Let's do a live demo of Windsurf so folks can see what it's like. And then I'm just going to ask you a bunch of questions as we're going through it. So I'll let you pull up a little shared screen where you have Windsurf pulled up.

Varun Mohan (00:41:33):
Great. So some context, this is a very basic React project. There's nothing in it right now. So if you were to open any sort of file, it's the default React app project. I have this basic image here. You can pass Windsurf images of what you'd like the project to look like, of what I would like an Airbnb for dog's website to kind of look like.

Lenny Rachitsky (00:41:55):
Beautiful. Beautiful mock-up by the way. I love that this is like all you need.

Varun Mohan (00:41:59):
This is all you need. This is all you need. So basically what we're going to do is we're going to say, "Hey..." One of the cool parts about Windsurf is it can actually work in an existing project already. So I can basically say, "Hey, change this React app to show an Airbnb for dog's website based on this image and preview it."

(00:42:25):
So now it'll just go out and start executing code, reading through the repository. Obviously, it doesn't know what the current code base actually looks like. And it'll go out and analyze the code base to actually find out the set of changes necessary. So we'll go out and wait and see what it's going to do. But while we're doing that, let's continue the conversation.

Lenny Rachitsky (00:42:45):
Awesome. Okay, so first of all, so you open up Windsurf. You had a boilerplate React project ready to go. And Windsurf had never really seen this code before. You ask it to do stuff on your code base, which is just like, "Change this to Airbnb for dogs using this design." Amazing.

Varun Mohan (00:43:03):
That's right. That's exactly right.

Lenny Rachitsky (00:43:04):
Yeah. Okay, cool. So we'll let it run and we'll talk. Let me ask you this question that I've been asking everyone that comes on that is building a product that helps engineers build products and product managers build products and designers.

(00:43:15):
Say you could sit next to every single new user that opens up Windsurf and whisper a couple tips in their ear to help them be successful with the product. What would be a couple tips you'd share?

Varun Mohan (00:43:25):
Tip number one is just be a little bit patient and both patient and explicit. When you ask the application to go out and make some changes, it could actually go out and make many irrelevant changes. One of the things that I think prevents this the most is just be really, really explicit or as explicit as possible. And one of the things I ask people to do is in the beginning, start by making smaller changes. If there's a very large directory, don't go out and make it refactor the entire directory because then if it's wrong, it's going to basically it destroy 20 files.

(00:44:00):
And I think from there, one of the key pieces I think that comes from the users that use the product is they sort of learn what the hills and valleys of the product are. The analogy I like to give are kind of similar to autocomplete. When you use a product like autocomplete, you would think a product that is suggesting things but only getting accepted 30% of the time would be really, really annoying. But the reason why it's not very annoying is actually because you've actually learned that, hey, 70% of the time, I don't need to accept this. And the times that I do, I know to get value from it. And you also know beforehand if a sort of command that you write is very complex, you just expect, "Hey, the autocomplete is not going to work for it." So I think it's almost like a, understand what the hills and valleys of the product are.

(00:44:45):
The crazy thing is, every three months that kind of gets changed and reevaluated. It almost becomes the case that it becomes materially better than it was in the past. So I think maybe patience and being explicit are maybe the two important key pieces I would tell users.

Lenny Rachitsky (00:45:00):
And I think something that was kind of between the lines there is get a gut feeling of what the model is capable of, like how specific to be versus how abstract it can be. And there's kind of this gut feeling you start to build over time.

Varun Mohan (00:45:12):
That's right. Yeah. And with that, it feels like we have an actual preview. Guess what? We have a nice-

Lenny Rachitsky (00:45:20):
Cute dogs.

Varun Mohan (00:45:21):
A nice dog app. And one of the cool parts is that we've also done beyond just modifying code is actually being able to point to different pieces. And I guess I could just kind of say... I could point to different elements and say, "Hey, make the background..." This is not great design, but I could basically say, if I took this element, "Make this background red and just take a particular element and just change it and make it red." And it should go out and be able to go out and do this.

(00:45:52):
The preview aspect of the product of being able to showcase the app while it's getting built helps in that, now actually you can live entirely in app world. You don't even maybe even need to look at the code. Granted this looks hideous, but in some ways if I wanted to, I could go out and do that, right?

Lenny Rachitsky (00:46:09):
This is what happens when there's no more designers. Like, [inaudible 00:46:11].

Varun Mohan (00:46:11):
Yeah. When there's no more designers. Sure. Maybe the answer is like, when you ask me what should people be doing, they should study great taste. Having great taste. Because I think taste is also a very, very hard, right?

(00:46:22):
But maybe the other key piece, Lenny, that I wanted to showcase here is obviously you could keep going here. I could take different components and kind of change them. We have a lot of plans here that are beyond just point and click changing components. But one of the cool pieces is the AI. There's an AI review flow as well, which is kind of like what I was saying. The goal of AI has now changed a lot in that it is now modifying large chunks of code for you. And the job of a developer now is to actually review a lot of the code that the AI has generated. And granted right now during this podcast, I'm not going to review all the code that's getting generated.

(00:46:57):
But let's say I want to go out and modify some of this code. And this is where if you're an actual developer that actually wants to go modify, maybe I don't like my variable name being called title. I want it to be called Title String instead, like this. And if I wanted to go out and make that change and change to go out and say Title String and that's what I'm going to do, I'm just going to tell the AI to continue.

(00:47:18):
The cool part about this is Windsurf not only knows about what the agent has done. It also knows everything that the user has done. Our goal here is to have this almost flow-like state where everything the user has done, the AI also knows. And it is able to predict the intent. And as you can see, it said, "I noticed that the interface property title was changed to Title String." And then it now has gone out and modified all the locations within the app from title to Title String. And now it no longer says that.

(00:47:45):
So this is where even if I'm writing software and I want to go and make point changes, the AI can go out and quickly make these changes on the user's path. Imagine doing a refactor or a migration and you just change one part of the code. You can just tell the AI to continue the rest. And because it deeply understands the code base, it should go out and find all the corresponding places to go out and make the change. And obviously now when I reload my app, there's no bug in the app. It still loads properly. I could obviously tell it to do even cooler things like make the app retro. I don't know what that means, but I guess I could do that. And it should go out and make the change correspondingly for me.

(00:48:23):
But yeah, that's maybe the high level parts there where the AI is not only able to operate entirely in app space but also on the code space of the users going out and modifying code and to bridge the gap between the two. So it should add leverage not only non-developers that are just purely building apps, but also developers that are just hands-on keyboard too.

Lenny Rachitsky (00:48:44):
Amazing. By the way, if you're not on YouTube, you can't see, but you can just select any element of the page and then reference that in your ask of, "Here's what I want changed." I didn't know that was a feature. And that is extremely cool.

(00:48:57):
So interestingly, so having just looked at Lovable and Bolt and Replit and apps like that, it's basically doing all the things those apps do. Oh, wow. There's the retro version. That's good. I like that it built on your red and made it really nice actually.

Varun Mohan (00:49:11):
Actually the red looks way better now.

Lenny Rachitsky (00:49:12):
Yeah, a little green button. This is great. Okay.

Varun Mohan (00:49:14):
Cool.

Lenny Rachitsky (00:49:16):
So I don't think people realize this, but apps like Windsurf, that it could actually do a lot of agentic work for you where you just tell it, "Here. I want you to do this" versus it's auto completing code for you.

(00:49:25):
The big difference is you need to start it with some code base so you have this kind of boilerplate React project. Is there a reason you guys aren't taking that step and just doing that automatically for you? Is it because you're targeting engineers and they don't need that or is there other reasons?

Varun Mohan (00:49:39):
Lenny, the interesting thing is the base app that you saw for this was also generated by Windsurf. The reason why we sort of didn't generate it is installing all the dependencies takes like three or four minutes. And for the demo, I didn't want to wait. But totally, actually most of the users of the product, probably zero-to-one build these apps.

(00:49:57):
And if I can say one interesting thing is, when we launched Windsurf, actually we tasked everyone at our company to go out and build an app with Windsurf. That included our go-to market team and our sales team. There was a crazy stat that I think people would find surprising, but we've saved over half a million dollars of SaaS products we were going to buy because our go-to-market team has now built apps instead of buying them. Our head of partnerships, instead of buying a partner portal product, has actually built its own partner portal. He had never built software in the past. We've actually come up with ways inside the company to deploy these apps easily in a secure way. And we're actually now building very, very custom software for our company to operate more efficiently, which is, I would not have expected this probably six months ago.

Lenny Rachitsky (00:50:44):
That is incredibly interesting. You don't need to name company names, but I guess what's a space you're least bullish on that you think is going to have the most problem here with people building their own version of these sorts of products?

Varun Mohan (00:50:56):
I think maybe my viewpoint are these very, very verticalized niche products I think are going to get... They're going to get competed down a ton. And I think sales products are an example of one of these things. And maybe this is a... I don't want to be very negative, but it's very hard inside a company like ours to task our best engineers to build a best in class sales product. There's not enough interest to do that. Or to build a best in class legal software product or finance software product. It's very, very hard for us to. And actually that's a very big moat for these companies that built these products that they were able to come out, have an opinionated stance on how to do this, hire good enough engineers to go out and build the software. Our company is unwilling to do that. So previously, we would go out and buy the technology because there would be no alternative.

(00:51:48):
But now one of the crazy things is that the domain specialists now have access to build the tools that they ultimately wanted, which is actually crazy. If you think about why were these software companies able to exist these vertical software companies, the reason is because they had many features. The kitchen sink of features worked for a lot of companies, but each individual company only wanted 10% of the features. But the problem is, each individual company was not capable of maintaining a piece of software or building the custom piece of software for 10% of the features, but that has now changed entirely. Now they can.

Lenny Rachitsky (00:52:22):
Yeah. There's always been a story of like, "Why would I spend any time building my own software if I could just..." But now it's like five minutes of time.

Varun Mohan (00:52:29):
Five minutes and maybe even more custom to your system. How many times have you bought a software and you're almost like, "Why is there no integration to X? And I actually use X." How annoying is that? That actually makes the software less useful to you.

Lenny Rachitsky (00:52:43):
So I think what's cool is when you go back, if someone zooms back to the beginning of when you started the demo, it's basically a PM talking to an engineer, "Hey, build me a Airbnb for dogs. Here's a stupid mock that I made with some boxes." That's almost like a bad PM talking to an engineer and it just actually works. That's what's insane about this. And so that's why this example you're sharing of go-to-market folks, building their own things, it's like they don't need to know anything about product building. It's just describe it in some ridiculous way and draw a couple boxes of what you want it to look like and it makes something for you.

Varun Mohan (00:53:20):
Which shows that agency is what matters. If you have a product manager that has an idea, there's no reason for why that idea cannot be more well fleshed out. How many times do you have a product manager that just continualize ideas, but it just feels like they are extremely unsure on how to execute on it? They just want to say things for sake of saying things? But for the people that have ideas and a lot of, I guess, agency, they can go out and prove out what they want without any sort of external resources.

Lenny Rachitsky (00:53:47):
I think even more acutely for product folks listening to this, it's the salesperson coming to you being like, "Hey, I want this thing. It's going to help me with my sales team." And you're like, "I don't have a million things to build. I don't have time for this." And so that problem goes away, which I think will make a lot of product leaders really happy.

(00:54:04):
The model that this is sitting on, is it Sonnet?

Varun Mohan (00:54:08):
Yeah. So just to break down how it ultimately works, we have a model that does planning. And I would say right now Sonnet is a really, really good planning model. I think OpenAI's GPT-4o is also good. But the crazy thing is what we try to do is we try to make the Anthropic based model or Sonnet model try to do as much of the high level planning as possible. And then what we try to do internally is run all the models necessary to do high quality retrieval for the agent. As you could see, the agent needed to understand what the rest of the code base ultimately did. We actually make sure we run models to actually chunk up the entire code base and understand the code base so that obviously it would not be a good idea if we had a 100 million line code base to send that entire code base to Anthropic.

(00:54:49):
First of all, you couldn't do that. That's over 1.5 billion tokens of code. So obviously that would be three or four orders of my actually larger than the largest context lens right now.

(00:54:58):
But you also wouldn't want to do that from a cost and latency standpoint too. So that's one. And the second piece that you saw was the model is able to very quickly make edits to the software as well. We have custom models that we built that are post trained on top of popular open source models that can make these edits really, really quickly to the code base. And the reason why you would want to do that is it's A, faster, and B, also that model can actually have more of the code base in context too. So it can be better at applying changes than even Anthropics model too.

(00:55:28):
So I think the way we like to think about it is, our only goal is how do we build the best product possible? How do we build the best product possible and how do we make the ceiling as high as possible? And we will go out and build models and train models wherever necessary. But if we're not going to be good at a task and we think the open source is better or Anthropic's better, we'll go and just use the open source or Anthropic.

Lenny Rachitsky (00:55:47):
And so the models you guys are building, those are built on open source models that people are releasing?

Varun Mohan (00:55:51):
Yeah. Interestingly, the one that does retrieval is actually completely pre-trained in-house that actually does that. But yeah, for a lot of different pieces, it's based on open source. Interestingly for the one that does the edits and auto-complete, that is also in-house. As you're typing, we actually do some auto-complete related stuff. I'm happy to show that, but I think a lot of users are familiar with that capability. So I think the way we like to look at it is like, what could we be best at and we will go out and trade. But if we're not going to be best at it, we should not just, for the sake of ego, go out and trade something.

Lenny Rachitsky (00:56:23):
This may be getting too technical, but just, is there anything interesting around what you train on?

Varun Mohan (00:56:27):
Yeah, so one of the interesting things that we have from our users, and this is where we try to think like, "Why would we be any better?" is that, actually every hour, we get probably tens of millions of pieces of feedback from our users. We get a lot of feedback on what they like and what they don't like. For something like autocomplete, we get a lot of preference data, a lot of preference data. And the preference data is weird. It doesn't look like data that you find on the internet. It's like data as the user is typing. Imagine you're typing some code in a code base, the code's going to be incomplete as you're typing it, right? It's not going to be in a full-fledged form. It's not like it is on GitHub. But we have a lot of data that looks like this.

(00:57:06):
So we are uniquely well-positioned to actually build a good model that can complete code even when it's in an incomplete state when the models that are out there, the frontier models have consumed very little code that looks like this. So for that case we're like, "Hey, we can go out and do a much better job potentially." And we'll go out and train models on all the preference data we have.

(00:57:25):
The same is kind of true on retrieval, right? There's a way to find out, are we retrieving the right data? Did the user accept the code change after that? Was the retrieval actually a good retrieval a signal that we can get? So basically the way we like to look at it is, if something is just purely code planning, there's not a great reason why we would be the best at that. I can't come up with a coherent argument for that. But for something that looks more along the lines of, "Hey, here's an intermediate code base that is very gnarly and here are some changes that need to get made" and we know the evolution of the code or we've seen the evolution of code across millions of users, we feel like we can do a great job of that.

Lenny Rachitsky (00:58:03):
I think what's interesting about this is another differentiator/moat for companies that end up winning in this space, is you just have more and more of that data than other companies if you're ahead.

Varun Mohan (00:58:14):
Yeah. This is sort of why maybe at a high level we like the zero-to-one app building product space. I think it's really... It's a good product space. But ultimately I think it needs to boil down to you understanding the code, because otherwise, you're living at too high a plane where it's not clear why you would be able to be the best at that compared to everyone else. It's not really clear.

Lenny Rachitsky (00:58:35):
As a company, you mean?

Varun Mohan (00:58:36):
As a company.

Lenny Rachitsky (00:58:36):
Versus as a user.

Varun Mohan (00:58:37):
It feels like it might get competitive in a way that it's not clear where you would continue to differentiate over and over with time.

Lenny Rachitsky (00:58:45):
I see. Because if they're just sitting on top of Sonnet and just doing what every other Sonnet wrapper is doing, there's not a lot of differentiation or moat.

Varun Mohan (00:58:54):
It depends on how you do it. But maybe if I was to say this, if the inputs you're consuming are just web elements, extremely high level web elements, then the interface might be high level enough that it's hard to maybe get better than maybe what the frontier models are doing just across the board. You are just better off just plugging in Sonnet for everything.

Lenny Rachitsky (00:59:14):
Got it. Awesome. One thing I wanted to come back to that I wrote down that I think is really important for people to understand, you talked about how with Windsurf it's not necessarily... There's a boilerplate code base that you want to start with because it's actually... Because it's not an abstracted zero-to-one app builder. It's an actual IDE you're coding in. And you talked about how has to install dependencies, which is kind this painful thing. And the reason it has to do that is because running locally on your machine versus in the cloud, like, say, Lovable and Replit and all these guys, although I think Bolt runs in your browser in this really cool way.

(00:59:47):
So that's an important distinction. This is like you're running this locally in your machine and has all the libraries you need to actually run it.

Varun Mohan (00:59:54):
No, I think that's important. I think we believe a lot of people sort of build software in what are called code spaces and things in a remote machine. I just think it's that a lot of developers like building locally for what you said. Like if you're doing things that are more than just full stack applications, you might have dependencies on your machine that are just system dependencies that are just gnarly to install. Let's imagine you're building a GPU-based application and the Nvidia drivers, they're necessary. You just want to give people the flexibility to build where they can build. And I think the IDE and building locally has been a thing that people have done for decades, so probably it's not going to go away in the next couple of years.

Lenny Rachitsky (01:00:29):
I love that your sales folks now are running local host servers.

Varun Mohan (01:00:34):
Well, with the browser previews, it's easier, right? You kind of just open it up on the side.

Lenny Rachitsky (01:00:37):
Yeah. Yeah. Oh my god. Okay. I have a few more questions just about how you think and operate at Codeium. So you guys are kind of at the forefront of how product teams are going to operate. You're seeing the future every day. And so I'm curious if there's ways you guys have structured your teams, engineers, product design that might be different from how other companies are doing it or have tried stuff that has worked really well or tried stuff that's a huge disaster?

Varun Mohan (01:01:02):
One interesting decision that we kind of have for core engineering is that we don't have pure product managers for the core engineering side of the company. And by the way, that's purely because we build for developers and our product is built by developers. So I think the intuition from our own developers is hopefully valuable. If not, we might be hiring the wrong type of people. So I think our developers are, in some sense, flexing to be more product conventional product managers.

(01:01:32):
Now on the other hand, if we were building something that looked more like Uber or the persona was very different and we didn't ourselves understand it, I think the organization wouldn't look the way it looks.

(01:01:42):
For the enterprise side of the company, because we do work with a lot of large enterprises where the requirements are not something that our engineers would automatically understand, I don't think our engineers wake up and they're like, "We need FedRAMP." This is probably something that a lot of customers come to us with and tell us. We have people that flex in this product strategy role that understand what the customer wants and understands the technical capabilities that we have to best build a product that would help them at scale.

(01:02:12):
So I think we have an interesting organization in this regard, but mostly I would say because we are a developer-based product, I would say that's true.

(01:02:21):
And then also kind of like what you said for the engineering team itself, the team structure is, it's fairly flat. We try to go with two pizza teams, teams that are fairly small just because I think the problem is when a team gets too big, the person leading the team is no longer able to get in the weeds of the technology itself. And I think in a space that's moving this quickly, I think it's dangerous to have leaders that don't understand the technology deeply and are not building. It's very, very dangerous because there's too much armchair quarterbacking. And so I think that's maybe one other decision we made.

(01:02:56):
And then teams are very, very flexible. So if we decide something is a new priority, we're very quick to change the way a team looks. And it's very centrally planned in this regard.

Lenny Rachitsky (01:03:08):
The two pizza team concept, I saw a tweet long ago where someone from India, was like, there's always talk about two pizza teams, but pizzas in India are much smaller. And so the teams end up being smaller and they're like, "Why can't we build as much of these teams in the US?"

Varun Mohan (01:03:22):
Oh man.

Lenny Rachitsky (01:03:23):
Okay. So how many PMs do you have? So you said you have 150 employees, something like that?

Varun Mohan (01:03:28):
Yeah. So in terms of the product strategy function, we have three people in that role right now.

Lenny Rachitsky (01:03:34):
I see. So it's like product... They're in their titles is product strategy, not necessarily product management?

Varun Mohan (01:03:41):
That's right.

Lenny Rachitsky (01:03:41):
Interesting. And then 50 engineers, you said 80-ish sales folks?

Varun Mohan (01:03:45):
Yes, that's right. And then obviously we have functions like recruiting parts of G&A, like finance. We have marketing at the company. So some other functions internally as well.

Lenny Rachitsky (01:03:56):
It's interesting. And this is something that you hear all the time with companies like Dario for example, from Anthropic talking about how 90% of code is going to be written by AI. But all at the same time, all you guys are hiring engineers like crazy.

Varun Mohan (01:04:08):
Yeah. Is that contradictory?

Lenny Rachitsky (01:04:10):
It's that contradictory, will there be an inflection point of like, "All right. Now we don't need them anymore."

Varun Mohan (01:04:15):
I think it really comes down to, do you get incremental value by adding more engineers internally? I'm going to take... First of all, maybe just to set the record straight, if AI is writing over 90% of the code, that doesn't mean engineers are 10X as productive. Engineers spend more time than just writing code. The review code, test code, debug code, design code, deploy code, right? Navigate code. There's probably a lot of different things that engineers do. There's this one famous law in parallel computing, it's called Amdahl's Law. I don't know if you've heard about it. But it basically says if you have a graph of tasks and you have this critical path and you take any one task and parallelize it a ton, which is make it almost take zero amount of time, there's still a limit of the amount of how much faster it made the whole process go.

(01:04:56):
So maybe put simply, let's say you have 100 units of time and only 30 units of time is being spent writing software and I took the 30 and made it three, I only took the 100 and made it 73. It's only a 27% improvement in the grand scheme of things.

(01:05:09):
So I think look, we are definitely seeing over 30, maybe close to 40% productivity improvements. But I think for the vision that we're solving for, even if I were to say the company in the long tail had 200 engineers, it'd probably be too low still at that point. So the question is, how much more productivity do you get per person? Actually, maybe just to even say one of those thing for some of these large companies, let's say you took the CIO of a company like JPMorgan Chase, right? Her budget on software every year is $17 billion and there's over 50,000 engineers inside the company and you told her, "Hey, each of these engineers are now able to produce more technology." That's effectively what you've done, right? The right calculus that JPMorgan Chase or any of these companies will make is the ROI of building technology has actually gone up. So the opportunity cost of not investing more into technology has gone up, which means that you should just invest even more. And maybe in the short term you have even more engineers, right?

(01:06:08):
Now, that's not true across the board. There are some companies that are happy with the amount of technology they're building and there's a ceiling on the amount of technology they want to build. But for companies that actually have a very high technology ceiling, this doesn't mean you stop. This actually means you hire more.

Lenny Rachitsky (01:06:22):
This is a great bull case for engineers. I feel like the canary in the coal mine for the engineering profession is when companies like yours slow down on hiring engineers.

Varun Mohan (01:06:30):
Yep.

Lenny Rachitsky (01:06:31):
That's not happening.

Varun Mohan (01:06:32):
[inaudible 01:06:32]. It seems like Anthropic is also hiring a lot to get it done.

Lenny Rachitsky (01:06:35):
Yeah. Everyone is. So I think that's really promising. I think if you're in college still, makes sense to get into engineering at this point.

(01:06:40):
Okay. Let me ask you this question as kind of a final question maybe. What's maybe the most counterintuitive thing you've learned about building AI products, building Windsurf and just being in a space?

Varun Mohan (01:06:54):
I think one of the weird things is online, everyone is very excited about the short-term wins that we are making, right? Like what we're putting out maybe weekly. We do these waves every couple of weeks. But actually a lot of the bets we're making inside the company are for things that are not three, four weeks, maybe three, six months, nine months away. That's what we're working on internally. Because I think this is kind of, Lenny, what I was mentioning to you before. One of the goals that I tell everyone at our company is we should be cannibalizing the existing state of our product every six to 12 months. Every six to 12 months, it should make our existing product look silly. It should almost make the form factor of our existing product look dumb.

(01:07:31):
So there's this weird tension where you want to have a product in market and you want to incrementally iterate and listen to users and keep making it better and better. But I would say we were the first identical IDE product out there. That's what we landed with. And I think the value of that is going to depreciate very quickly unless we continue to re-prove ourselves. And we will need to re-prove ourselves in ways in which our users are not even asking. So there's this tension here, where incremental feels very safe, right? Add this one more button. Users say, "Hey, I would like to be able to have this drop down to do X." But that is not the reason why we're going to win. That's almost table sticks. Yeah, we'll decide to do some of these. We might not decide to do a lot of these things. But it's these longer term efforts inside the company that almost disrupt the existing product that are ultimately the reason why we're going to succeed.

(01:08:21):
It's this weird tension that you need to have in your head of, you can't also not listen to your users at all because they're the reason you exist.

Lenny Rachitsky (01:08:29):
This reminds me of a recent podcast guest. We had Gara from captions on the podcast and he told us that he has two roadmaps. They have two roadmaps at the company. They have the real roadmap, like the typical roadmap based on feature requests and user feedback and data and things like that. And then they have the secret roadmap, which is completely not informed by users or data/ it's just them making bets on where they think the world is going.

Varun Mohan (01:08:52):
That's right.

Lenny Rachitsky (01:08:52):
And I love that he calls it the secret roadmap just to make it very mysterious and-

Varun Mohan (01:08:56):
That's smarts. That's very smart.

Lenny Rachitsky (01:08:57):
Okay. I have one more question. I apologize. What's one thing that you wish he had known before starting Codeium?

Varun Mohan (01:09:04):
Honestly, I wish I had... Maybe humility is the wrong term, but this idea of just being okay with being wrong faster. I always think about things on when we make decisions. Me and my co-founder, we always talk about it. We're almost like, "Hey, I wish we had made the decision to do this a couple months earlier." We always talk about this. And the weird thing is outside looking and everyone's like, "Wow, actually the decision was made at the right time." But in my head I'm always banging my head being like, "What if we had made it a couple months earlier?" I think part of that is I waxed poetically about like, "Oh, you need to be irrationally optimistic and uncompromisingly realistic." But it's very hard to do this in practice because you drink your own Kool-Aid too. Because if you're not drinking your own, you won't get up out of bed. The answer is already solved. It's not actually any of these startups. The answer is Microsoft is going to be the winner in any software category. Isn't that the answer? Just because of distribution, resources and capital, they're going to commoditize every space.

(01:10:06):
So I think in some ways this amount of just understanding that, hey, re-evaluate your hypotheses and get into an uncomfortable space way more frequently is something I need to remind myself even to this day. And probably something that I didn't know coming in and starting the company. We started the company at peak zero time. At that time, probably everything seemed like it was going to moon. And there was probably a lot of irrational confidence, I would say, that we shouldn't have had.

Lenny Rachitsky (01:10:36):
Varun, we covered so much ground. What an incredible conversation. I learned so much just sitting here listening and asking you questions. Is there anything else that you wanted to share I leave listeners with, any last piece of nuggets or wisdom before I let you go?

Varun Mohan (01:10:51):
To be honest, I could give predictions about the space. Probably most of them are going to be wrong. I think the best thing to do is just get your hands dirty with all of these products. And I think one of the most obvious things that's going to happen is, in the next year, there will be a tremendous amount of alpha for anyone that is able to take maximum advantage of these tools. Just imagine how many of your coworkers just don't even know the existence of these tools, don't know what they can do and how much less productive they will be. And I would just say get your hands as dirty as possible, as quickly as possible.

Lenny Rachitsky (01:11:24):
And when you say get your hands dirty, basically it's like download Windsurf, start coding. Ask it to build things for you.

Varun Mohan (01:11:29):
Yeah, build apps. Build apps. Start using it for maybe even making mocks, modifying your existing code base. There's probably ways in which you could be a force multiplier to your organization and ways in which they never even anticipated, right? Imagine if you were a product manager that could actually very quickly make edits to the code base and just start pushing changes yourself. You probably get a tremendous amount of respect from your own engineering peers. You could probably get way more done because of that. I feel like there's no sort of ceiling at that point.

Lenny Rachitsky (01:12:00):
I think this is such an underestimated point you're making here. There's apps that can build things from scratch and then there's apps like this that can edit your existing code base if you're a PM at... What's the largest company you work with, people-wise?

Varun Mohan (01:12:15):
Publicly, let's just say JPMorgan Chase.

Lenny Rachitsky (01:12:16):
Okay.

Varun Mohan (01:12:19):
They have over 50,000 developers.

Lenny Rachitsky (01:12:20):
Okay. So you could be a PM at JPMorgan Chase and be like, "I have a problem I need to solve. I want to move this metric. I want to change the step in the signup flow." You just open up Windsurf and tell it to do the thing you want. And then can you push straight to GitHub and do a-

Varun Mohan (01:12:37):
Yeah. Actually, you could do that too.

Lenny Rachitsky (01:12:39):
... merge [inaudible 01:12:39]-

Varun Mohan (01:12:39):
Yeah.

Lenny Rachitsky (01:12:39):
Okay. PR?

Varun Mohan (01:12:40):
Yeah, it could make a PR for you.

Lenny Rachitsky (01:12:41):
Oh, my God. This is insane. Folks, future is out of control. Okay. Man, that was such an important point at the end there because I think people may not realize this. They see all these other apps, they're like, "Oh, [inaudible 01:12:51], prototypes," but this is legitimately something a PM can actually do work with.

Varun Mohan (01:12:55):
Yeah. When you think about the people, at least that, I don't know, Lenny, who you respect the most, they're the people that somehow, despite their title, their level of agency and just output just all the way down to the weeds to the highest level strategy is just perfection, right? They know when to go all the way down. And I think sometimes you see people that talk about roles and they irrationally feel like, "Oh, because I'm this role, I'm not allowed to touch this." Well now everything's open season, right? And I think this is an opportunity to almost go all the way down to the weeds and all the way up to the top and just be effective on every level.

Lenny Rachitsky (01:13:29):
Unbelievable. All right. Well with that, we'll leave folks. Varun, thank you so much for being here.

Varun Mohan (01:13:35):
Awesome. Thanks a lot, Lenny.

Lenny Rachitsky (01:13:36):
What an incredible conversation. Thanks, Varun. Bye everyone.

(01:13:42):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

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

## Persuasive communication and managing up | Wes Kao (Maven, altMBA, Section4)
**Guest:** Wes Kao  
**Published:** 2022-08-28  
**YouTube:** https://www.youtube.com/watch?v=4jtGsyz4jLs  
**Tags:** growth, retention, acquisition, okrs, conversion, revenue, leadership, management, strategy, vision  

# Persuasive communication and managing up | Wes Kao (Maven, altMBA, Section4)

## Transcript

Wes Kao (00:00:00):
I often see operators who explain things poorly and then are shocked and horrified when people are confused or there's skepticism, there's apathy. I'm a big proponent of asking myself, if I'm not getting the reaction that I'm looking for, how might I be contributing? How could I explain this more clearly? How can I be more compelling? How can I anticipate any questions that they might have?

Lenny Rachitsky (00:00:22):
You are one of the best teachers of communication I've ever come across. I made a list of people's favorite tactics and frameworks and approaches that you teach in writing. Any tactics you can share for someone to be a little more concise?

Wes Kao (00:00:35):
I think the blast radius of a poorly written memo is way bigger than most people think. If you are just shooting off a message in a Slack channel with 15 other people, and it's confusing, you didn't include information you should have included, there's going to be a bunch of back and forth. Whereas if you had just taken another look at it, those 15 people would be off to the races.

Lenny Rachitsky (00:00:52):
You have an awesome framework called MOO.

Wes Kao (00:00:54):
MOO stands for Most Obvious Objection. A lot of times we're surprised by the questions that we get especially in meetings, we feel blindsided. When really, if you thought for even two minutes about what are obvious objections that I'm likely to get, you often immediately come up with what some of those things are. Are you going to be able to anticipate every single objection? No. But can you anticipate the obvious ones? Absolutely.

Lenny Rachitsky (00:01:22):
Today my guest is Wes Kao. Wes co-created the Alt-MBA program with Seth Godin. She Co-Founded a company called Maven, which I often collaborate with, which makes it easy for people to host live cohort-based courses. She recently left Maven to launch her own course on Executive Communication and Influence. There's a quote that came to mind after I stopped recording this conversation with Wes by George Bernard Shaw, "The single biggest problem in communication is the illusion that it has taken place."

(00:01:51):
By the end of this podcast if you listen to what Wes suggests, you'll be a lot closer to becoming a world-class communicator. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. Also, if you become a yearly subscriber of my newsletter, you get a year free of Perplexity Pro, Superhuman, Notion, Linear and Granola. Check it out at lennysnewsletter.com. With that, I bring you Wes Kao.

(00:02:18):
This episode is brought to you by WorkOS. If you're building a SaaS app, at some point your customers will start asking for enterprise features like SAML authentication and SCIM provisioning. That's where WorkOS comes in, making it fast and painless to add enterprise features to your app. Their APIs are easy to understand so that you can ship quickly and get back to building other features. Today, hundreds of companies are already powered by WorkOS, including ones you probably know like Vercel, Webflow, and Loom.

(00:02:50):
WorkOS also recently acquired Warrant, the Fine Grained Authorization Service. Warrant's product is based on a groundbreaking authorization system called Zanzibar, which was originally designed for Google to power Google Docs and YouTube. This enables fast authorization checks at enormous scale while maintaining a flexible model that can be adapted to even the most complex use cases. If you're currently looking to build role-based access control or other enterprise features like single sign-on, SCIM or user management, you should consider WorkOS. It's a drop-in replacement for Auth0 and supports up to 1 million monthly active users for free. Check it out at workos.com to learn more. That's workos.com.

(00:03:36):
This episode is brought to you by Vanta. When it comes to ensuring your company has top-notch security practices, things get complicated fast. Now you can assess risk, secure the trust of your customers, and automate compliance for SOC 2, ISO 27001, HIPAA and more with a single platform, Vanta. Vanta's market-leading trust management platform helps you continuously monitor compliance alongside reporting and tracking risks. Plus, you can save hours by completing security questionnaires with Vanta AI. Join thousands of global companies that use Vanta to automate evidence collection, unify risk management, and streamline security reviews. Get $1,000 off Vanta when you go to vanta.com/lenny. That's V-A-N-T-A.com/lenny. Wes, thank you so much for being here and welcome back to the podcast.

Wes Kao (00:04:36):
Thanks, Lenny. I'm very honored to be a second-time guest.

Lenny Rachitsky (00:04:40):
Very rare honor. No pressure, but I think this is going to be one of the highest leverage episodes I've done and let me tell you why I think that's the case in the newsletter and on the podcast, I often talk about just how important and how high leverage the skill of communication is to product leaders, to leaders, just to people in general. There's this quote that Boz, the CTO of Meta, he's been on the podcast, he wrote this famous blog post, "Communication is the job." And I think that's true for product people, but it's true for basically any sort of leadership role. Anyone trying to get ahead. And you are one of the best communicators I've ever met. You are one of the best teachers of communication I've ever come across. You have one of the most popular courses on Maven, on executive communication, so I'm really excited to have you here and to help people become better communicators, better at influence and all these things. So thank you again for being here.

Wes Kao (00:05:32):
Absolutely.

Lenny Rachitsky (00:05:34):
Okay. So something that I often do with guests on the podcast, not even often, always, I ping people that the guests have worked with and ask them, "What should I ask Wes? What should I know about Wes?" Let me read a few quotes about you in regards to your communication skills from folks that have worked with you-

Wes Kao (00:05:34):
All right.

Lenny Rachitsky (00:05:51):
And these are three different people. Okay, so first, "Wes single handedly raised the quality of the entire company's writing by like two X across the board. I always say the best writing course I ever took was working with Wes for a year."

Wes Kao (00:06:07):
Wow.

Lenny Rachitsky (00:06:09):
Okay. That's one.

Wes Kao (00:06:10):
Great.

Lenny Rachitsky (00:06:10):
"Wes never just throws things out there, she's precise with her use of language, meticulous about examining her own ideas before bringing them in front of others and knows how to make her points in a way that people will understand them and buy into them." Okay. And third, "Wes includes a reasoning with every proposal in the context behind all of her recommendations so that everyone around her learns in order of magnitude faster. This also makes her an exceptional teacher because she can clearly define what excellence is and why something is the goal, and then break down the steps and principles involved." Okay, reactions.

Wes Kao (00:06:46):
Those are really nice things. That's amazing. Yeah, thank you so much.

Lenny Rachitsky (00:06:52):
And these are people across different companies, so.

Wes Kao (00:06:52):
Cool.

Lenny Rachitsky (00:06:55):
Okay, so that was just to highlight of how good you are at this stuff. And what we're going to be doing with our chat is going through a bunch of your tactics that you teach and that have helped people become better communicators, executive communicators, better at influence. Before we get into the specific tactics, is there anything that you think is important for people to understand just broadly around the skill of becoming a better communicator?

Wes Kao (00:07:17):
I often see operators who explain things poorly and then are shocked and horrified when people are confused or there's skepticism, there's apathy, there's a lot of avoidable questions, and I'm a big proponent of asking myself, "If I'm not getting the reaction that I'm looking for, how might I be contributing to that?" So, you know, instead of blaming other people for not understanding me, I think about how could I explain this more clearly? How can I be more compelling? How can I anticipate any questions that they might have? So I'm a big proponent of agency. And realizing that we can only control our own behavior. And so the best place to start, if you're not getting the reaction you're looking for, is reflecting on how can I get better at the skill of communicating? And it absolutely is a skill.

Lenny Rachitsky (00:08:11):
So what I'm hearing is if you're having a hard time people buying into what you're trying to convince them to do or you're finding people are doing not what you asked them to do, it's likely an issue with your ability to communicate, it's probably not their fault.

Wes Kao (00:08:28):
Yeah, I would say so. You can't solve everything with improving your communication, but you can increase the likelihood of getting what you want.

Lenny Rachitsky (00:08:39):
Cool. Okay. Anything else along these lines of just things that are important to understand just broadly around communication, executive communication?

Wes Kao (00:08:46):
I think another big one that I teach in my course and really kick off with is practicing like it's game day, playing like it's game day. So I see a lot of operators who save their best behavior for executives only. So you know, they want to shine when they're presenting to senior leadership, but with everyone else, they're kind of calling it. And I just don't think that you're going to be able to get enough reps to actually get good at executive communication if you are only doing it with executives. Because many of us only present to execs once a month, right? Or a couple of times a quarter. And that's just not a lot of chance to practice. So really treating every single stakeholder as if they are important because they are, and you shouldn't be if you don't want to waste your CEO's time, you also shouldn't waste your cross-functional team members' time or your manager's time or your direct reports' time. So that's something else that I ask to keep in mind.

Lenny Rachitsky (00:09:39):
And maybe a last question before we get into the tactics. When people think communication, they think email, they think meeting presentations, things like that. How do you think about, when you talk about executive communication and communication in general, what's kind of the umbrella of things that includes?

Wes Kao (00:09:53):
Yeah, I would say broadly the two mediums are verbal communication and written. So verbal being meetings, conversations, presentations. And written being emails, strategy docs, notion docs, Slack messages, text messages, those two categories broadly. And I also think about communication as more of a means to an end, which might be interesting for some people because I teach a course on communication. So you would think that's like the end in and of itself, but I really see it as a means to an end where the end is getting the ideal outcome you're looking for. So whether that is buy-in or making a good decision as a team or moving to the next step, whatever that might be, communication is really in service of that end goal.

Lenny Rachitsky (00:10:43):
Awesome. Okay. So I made a list of people's favorite tactics and frameworks and approaches that you teach, and talking to folks that you've taught and folks that you've worked with. So I'm just going to go through a bunch and let's just help people get better at these things.

Wes Kao (00:10:58):
All right, let's do it.

Lenny Rachitsky (00:11:00):
Okay. So the first is something you call sales, then logistics. What is that about?

Wes Kao (00:11:07):
Yes. So a common mistake that I see is overestimating the amount of buy-in that you have from your audience. So that looks like jumping straight into talking about the logistics, the details of the how to do something, of the process. When in reality your audience has not yet decided if they even want to do the thing. So what I see operators do in response then is go even deeper into the logistics and the how, thinking that, "Oh, if I just explain this more than that person will want to do it." When really a sales note is different than a logistics note. A sales note is meant to get people excited to do the thing you want them to do, and to agree to do it. And only then after they have bought in, does it make sense to share the logistics.

(00:11:57):
So there's an order of operations here. If you switch the order of operations, you will likely get a slow response or just no response, right? We've all put a Slack message in a channel and got crickets and tumbleweed. So really starting off with selling the person and making sure that they know why we're doing this, why this matters to the company, why now, and then sharing the logistics tends to be a lot more effective.

Lenny Rachitsky (00:12:22):
Is there an example of that that might help illustrate that point or that approach?

Wes Kao (00:12:27):
Yeah. So one of my clients is a head of operations and she was trying to get the rest of her executive team, which she was a part of, to fill in some wins for the week so that they could share this out with the whole company. And this was going to be motivating, it was going to shine a light on folks. And she led with the logistics of which document to send, to put the details in, what time to put it in by, the format that you should put these wins and didn't really get much of a response from the leadership team, which makes sense, right? Because this totally sounds like one of those things that's another item to check off on your list when you already have so many other things to do and here's this other process that like we're all supposed to do now, like yay, right? And so she wasn't really getting response. And that's because she dove straight into logistics.

(00:13:20):
Whereas what she could have done is start by selling folks, selling the other executives on why are we doing this? Well, we're doing this because this is a chance to shine a light on your team members who are doing amazing work, for them to feel motivated and to feel like the rest of the company really sees them and understands what they're doing. And this is all something that is going to motivate your team, right? So sharing why this is helpful and useful and how this is in service of you and your team versus like, "Oh, this is a favor that you're doing for me to fill out this form and fill it out this way and by this date," et cetera, et cetera.

Lenny Rachitsky (00:14:00):
I know that execs often want the opposite where they're just like, "Okay, I know, just tell me what you want to do. Just like, okay, just get to the point. I don't want time for all this context and background." Any advice on when to spend any time on the sales? Like what are signs that, okay, maybe you don't have them sold yet, or what are maybe contexts where you should probably still try to sell them first?

Wes Kao (00:14:20):
Yeah. So I actually think that you should always do a little bit of selling even for situations where people have generally bought in. Because most of us have a lot going on and we're not actively thinking about whatever you're talking about. So even though I agreed to something two weeks ago, by the time you're telling me about it again, like I thought about a billion other things since then, right? So reminding me of why are we talking about this? Why does this matter? And then getting into it and framing that conversation upfront is way more likely for us to not get stuck in a cold start and not kind of go two steps back one step forward.

(00:14:55):
The other thing is, you can frame a conversation and sell a bit at the beginning very concisely. So I'm not talking about spending 15 minutes out of a 30 minute meeting selling, I'm talking about one to two minutes, even a couple sentences, and then transitioning into the main thing you want to talk about. So I'm a huge proponent of doing that and basically reminding people, why are we doing this? Why are we here today? Why does this matter? And then getting into the meat.

Lenny Rachitsky (00:15:24):
I love that. So basically you can do this really briefly, it doesn't have to be a whole pitch for half an hour. It's just a reminder, "Here's why we think this is important." And I think that's such a good point because a lot of times it's like a leader is looking at this thing you're asking them to do and they're like, "Why are we even, why am I spending time on this?" And just a reminder of like, "Okay, I see, I forgot this was going to be, this a part of our strategy, this has this much impact potential or here's how it could help our team be more efficient."

Wes Kao (00:15:52):
Yeah. And you can really do that in like 30 seconds.

Lenny Rachitsky (00:15:56):
Is there like a, I don't know, structure to this? Is it just like why? Is there a kind of a template you like or some way you recommend of selling first? Is it like, "Here's why we're doing this." Starting like that? Anything along those lines?

Wes Kao (00:16:09):
Yeah. I think explaining why we're doing this, why this benefits the business, what problem this is solving. Again, you can do a lot of this in a couple of sentences. And then I also like asking or stating what I need from the other person upfront. So saying, "Hey, we're here today because two weeks ago we were reviewing the product flow and realized that there were a couple of parts that were kind of confusing. So I took a stab at fixing those areas, rewriting the microcopy, and I want to present them to you today, see if you agree with these changes, and then we're going to roll them out. What I'm looking for from you is feedback on the changes and if you agree." So like that was like 15 seconds, right? Super fast. And then now we're all on the same page about why we're here. And you can listen more intently knowing that I'm looking for a certain kind of feedback.

Lenny Rachitsky (00:17:01):
I would love to hear it that way. I think there's like an implication here that maybe is worth sharing of just, a lot of this is about communicating effectively to execs, which will make you communicate better to most people. But especially with folks up the ladder. They don't have a lot of time, they have a million things in their head. Maybe just share like why this is so important, like what the state of mind of a leader is that you need to kind of break through.

Wes Kao (00:17:25):
Yeah. So I call it the yes, yes, yes, next, next, next mindset where if I'm listening to direct reports present something to me, very often I find myself thinking, "Got it. All right, yes, let's keep going." Right? And you know, on the other side of that, I've often presented to executives where I had a 15 slide deck and execs would do that and I'd be like, whoa, whoa, whoa. Like I have a whole sequence, I have a whole order, you know? And sometimes they would give me buy or make the decision by slide four, you know? And I'd be like, "Okay, well you know, slide 13, I want to show you this great graph I put together." Right? And what was really helpful for me was realizing that I should take the win. Okay, if five seconds already agreed, take the win and keep it moving, move on.

Lenny Rachitsky (00:18:13):
Yeah. What's that quote like? "If you've sold them, stop talking."

Wes Kao (00:18:16):
Right. Yes. Yeah, you might talk them out of agreeing.

Lenny Rachitsky (00:18:20):
Yeah. Okay. You mentioned being concise. Let's talk about that. You have some really good advice on just how to effectively be concise and not too concise. What's your advice there?

Wes Kao (00:18:31):
Yes. One of my pet peeves is when people are too concise and they equate being concise with brief, being brief. And being concise is not about absolute word count, it's about economy of words. It's about the density of the insight that you're sharing. And so you can have a 300 word memo that's meandering and long-winded and a thousand word memo that is tight and concise. And so not equating concision with briefness I think is a really big one to understand.

(00:19:05):
The second thing is a lot of advice about being concise, I think misses an important point. So we've all heard, "Don't bury the lead, cut to the chase." Main point, put the main point at the top, bottom line up front, right? And all of these pithy aphorisms assume that you actually know what your core point is. So you can't cut to the chase unless you know what the chase is. You can't unbury the lead unless you know what the lead is. And so that I found is the bottleneck to being concise. It's actually not really being clear of what you are thinking, that's what's leading to being long-winded.

(00:19:49):
And you can kind of test this theory because most of us have a go-to story that we've told a bunch of times, right? We're like, you know exactly when people are going to laugh, you know when they're going to gasp or hold their breath, right? And why are you so good at telling that story and why are you so concise about it? Because you've told it a bunch of times, you know all of the beats. So in meetings though, at work, we are very rarely talking about the same thing that many times it's always something new. It's something that we are also probably likely processing ourselves and are in the midst of processing as we are in a quick turnaround time, telling someone else about it, telling our team about it. And so you are basically asking your brain to do a lot of different processes, especially in a real time conversation. You're listening to the other person absorbing, making sense of it, processing it, figuring out what you think and how you would react.

(00:20:39):
And then trying to say something cohesive that makes sense, right? And then trying to be concise about it. So it's just a lot of different processes. And so the only solution I found consistently to being concise is preparation. It's not a very glamorous solution by any means, but the clearer I am going into a meeting, going into a conversation, going into a pitch, the better I am at being concise and being able to bring the conversation back to the most important points at being able to stay flexible, but also firm and preparation. I don't mean spending hours and hours preparing for a weekly meeting, even a couple of minutes really makes a huge difference.

(00:21:25):
Most of us are so back to back in meetings that we're doing zero preparation. It's like the meeting has started 30 seconds in and you're still unwinding from the last Zoom call that you were on, right? So most of us are in that mental state. So if you even take 30 seconds to one minute to ground yourself on why am I in this meeting? What do I want to share and make sure I get across in the time that we have, you're going to go in there so much more focused and so much more able to be concise.

Lenny Rachitsky (00:21:51):
So the advice there, so this is for meetings and I want to talk about writing also, but for meetings, the advice here is before you get into a meeting, actually think about why am I in this meeting? What do I want to get out of it? Instead of in the meeting figuring out a lot as you go, which to your point, you're just going to ramble and be like, "Oh, okay, here's what I actually want to say."

Wes Kao (00:22:10):
Yeah. And what might I want to share in the meeting too? You know, especially for more introverted folks. Sometimes you need to decide beforehand that you want to speak and you want to make sure you get a certain point across. So even deciding that beforehand makes a huge difference.

Lenny Rachitsky (00:22:25):
Yeah, I found this extremely powerful just like five minutes before you get into a meeting. And it could happen earlier in the day, right? It doesn't have to happen right before the meeting, or worst case, it's right before the meeting. Just, "Okay, what do I want to get out of this? What am I here? What do I want to say?" And just like giving your brain a little bit of time to prepare. Super powerful. In writing, is there like any tactics you can share for someone to be a little more concise?

Wes Kao (00:22:50):
I think the main tactic is to remind yourself to be concise. And usually when I do that, I end up trimming 20% at least of what I wrote, tightening up some sentences. I also ask myself, how might I be adding cognitive load to whatever it is that I'm saying? So is there a tighter, clearer, cleaner way that I can ask what I'm asking or present the information I'm presenting or make the recommendation that I'm making? And usually if you even ask yourself that, your brain automatically comes up with stuff. You just see whatever you wrote differently and you're like, "Oh shit, I could trim this entire paragraph because that's secondary." And maybe you have your primary message in Slack, and then within the thread add some of the secondary stuff, right? So I find that most of us, it's reminding yourself to be concise. And once you think of it, your brain naturally will see places where you can trim.

Lenny Rachitsky (00:23:50):
There's a layer of advice under this that you're not saying that I'm going to say, which is actually look at the thing you wrote at least once before you share it. Because I used to be really bad at this. I just like, "Okay, I don't have time. I wrote this doc, send it, get feedback.

Lenny Rachitsky (00:24:00):
... really bad at this. I just like, "Okay, I don't have time. We wrote this doc, send it, get feedback. All right. Send this email. I don't have time to read this email." And I find just forcing yourself to look at it solves so much of this.

Wes Kao (00:24:10):
Oh, yes, yes, definitely. I was assuming before doing that, but you're right, some people might not be. And yes, definitely reading your own message first is huge. And yeah, I find that even doing that you can often spot a lot of low-hanging fruit.

Lenny Rachitsky (00:24:31):
Right. You'll find the typos and grammar issues and you'll be like, "Oh, I don't need this word." Along those lines, let me share two books. People always ask me, "How did you learn to write?" I'm like, "I'm not a writer, I don't know what I'm doing." But two books really helped me write more effectively. And one is specifically to help you write more concisely called On Writing Well. I don't know if you've read that.

Wes Kao (00:24:51):
Yeah.

Lenny Rachitsky (00:24:52):
Okay. And it's basically chapter after chapter of, "Here's what you can cut. And you can cut more. And look what more you can cut and cut this stuff." And he has screenshots of essays that students have written in his class and he's like, "Look at all those words you cut and nothing has changed. It's exactly the same message and even is better with 40% of the words cut."

Wes Kao (00:25:12):
Is this by Sol Stein or another author?

Lenny Rachitsky (00:25:16):
I don't have it... It's somewhere in my bookshelf. So we'll look it up.

Wes Kao (00:25:19):
Yeah, there's a writing book by Sol Stein that I absolutely love. And I feel like it might be called On Writing Well, but then also I could see there being multiple books called On Writing Well.

Lenny Rachitsky (00:25:29):
There's also Writing Well I think by Stephen King, that's another one that people love, but there On Writing Well is the one I really loved because it's very tactical.

Wes Kao (00:25:37):
Going back to something that you were saying earlier with rereading what you wrote, I think the blast radius of a poorly written memo is way bigger than most people think. So if you're just shooting off a message in a Slack channel with 15 other people and it's confusing and you didn't include information you should have included, there's going to be a bunch of back and forth. All 15 of these people are reading this being like, "Okay, what do I do with this?"

(00:26:05):
Whereas if you had just taken another look at it, those 15 people would be off to the races. They would've read your message and then known exactly what to do next or what their part was or what you were looking for from them. So I think about that a lot too. It's not just me writing this and sending it off. It's, "Who are all the people who are going to come in contact with this message who are going to refer to it and use it? And if I just take 30 more seconds to make sure that it's clean, how much can I unblock from their work?"

Lenny Rachitsky (00:26:34):
That's such a good point. I like that, I love that term blast radius. It's such a good point. Just like there's so much negative leverage in writing inefficiently and inconcisely. If you spend like... Inconcisely? I don't know the word is there, but if you just spend three minutes spending a little more time making it more clear just like the impact and leverage that has, that's such a good point. I looked up the books, it's so funny. Okay, so there's On Writing Well by William Zinsser. There's Stein On Writing by Sol Stein, which is what you said you were talking about. And then Stephen King has a book called On Writing. Everyone's got the same.

Wes Kao (00:27:09):
Yeah. Common title.

Lenny Rachitsky (00:27:12):
Not ideal for SEO but On Writing Well is the one that I love by William Zinsser. There's also one called A Series Of Short Sentences if you haven't seen that one. It's a really good rate too. It's just how to write short sentences and just the power of just keeping sentences short, which I struggle with.

Wes Kao (00:27:27):
Yeah. Yeah, I like that.

Lenny Rachitsky (00:27:28):
Okay. Back to our agenda. There's another framework/tactic that I've heard you recommend. It's called signposting. What is signposting?

Wes Kao (00:27:38):
Signposting is using certain words, phrases, formatting, and an overall structure in your writing that helps guide your reader and signals what is coming in the rest of the post. So, this is especially helpful if you have a long memo. It adds structure to where are we going and what certain sections of paragraphs are about. So some of my favorite signposting words are, "for example," shows that you're about to show an example because shows that you're about to share your logic and rationale behind something. "As a next step," is a great one. People's eyes automatically zoom to, "as a next step." Even "First, second, third," kicking off a paragraph with that, you're not needing to rely on rich text formatting with bolding, italics, underlines and all that craziness. If you kick off sentences with signposting words, you can often signal, "Here's what I'm about to talk about in this paragraph."

Lenny Rachitsky (00:28:41):
These are power words for clarity. There's this whole concept of power words like, "free."

Wes Kao (00:28:47):
Yeah. "A gift."

Lenny Rachitsky (00:28:48):
"Gift." Yeah. For copywriting and these are basically power words for helping your brain see the structure and get to the thing you want to pay attention to. So I'll read back the words you just used. "For example," " because," "as a next step," and then, "first, second, third."

Wes Kao (00:29:05):
Yeah. Yeah. You can use signposting in writing and verbally too. So if you're doing a product demo, you might say something like, "The most important part to pay attention to is, blank." Or, "The part that we were most surprised by is, blank." Or, "The part that customers are," et cetera. Right? So it's, you're signaling that whatever comes after this thing is something that you may want to pay attention to. So it's a great way not only to add structure, but to also grab people's attention back if it has strayed some time as they were either listening to you or reading.

Lenny Rachitsky (00:29:42):
Along those lines, I find I find formatting really helpful here, just bold and bullets. I know you have a pet peeve with too much formatting. How much is too much formatting?

Wes Kao (00:29:51):
I really hate excessive formatting. So, I've seen memos where 30% of the note was bolded. And that just negates the entire point of bolding because if everything is bolded then nothing is being highlighted, right? So I think using formatting in general more sparingly than you think you have to is probably a good rule of thumb. I also dislike when people overuse bullets and sentence fragments, phrases in bullets when they should use complete sentences that actually show the connected tissue between ideas, that show the logical flow of what it is that you're saying.

(00:30:33):
And it feels faster and more concise to put bullets and fragments, but a lot of times your reader on the other end of that is needing to decipher and interpret and guess what you actually meant. So it net, net takes longer. And I also think that it can be a little bit of a crutch, it can be a little bit lazy because you are telling yourself that you're being concise when really, if you had to turn your sentence fragment into a full sentence, a lot of times it actually is harder than you think because you realize that you actually didn't really know exactly what you meant. So as you're trying to turn it into a full sentence, you're actually needing to use brainpower.

(00:31:15):
So that's I think a great litmus test of, "Was that idea fully thought out?" Because if it was, you should be able to really quickly turn it into a complete sentence. And many times, you actually aren't. So I see people like basically think, "Oh, I want to make this easier to read, more skimmable. I'm just going to throw a bunch of formatting and bullets and turn everything into bullets." And it's not quite that easy of a solution.

Lenny Rachitsky (00:31:41):
This is very much along the lines of the whole Amazon six-page memo where Jeff Bezos just realized, "If you can't write it out as a long memo and explain yourself in prose, you don't actually know what you're saying." And it's a really good filter for helping people actually crystallize and know themselves, "Okay, I see. I don't actually know what I'm doing here." And I love this is a microcosm of that. Can you just make a bullet point a real sentence versus a fragment of a sentence?

(00:32:06):
I'm thinking about as a listener being like, "Okay, how do I actually get better at this?" So maybe let's take a tangent. I know that you teach a whole course, you do all this stuff hands-on with people to help them actually build these skills. For someone that hasn't taken the course or isn't taking it, what's a good way to start practicing these skills and know if what you're writing is getting better, is good. Is it find a mentor, find someone that you think is a great writer and have them review stuff? Any tips there?

Wes Kao (00:32:34):
Yeah. So I have a pretty first principles driven approach for this, which is to think about how long does it take me right now to get to the reaction I'm looking for from my recipient? If it takes a bunch of back and forth and a bunch of friction, then that's my baseline. And once you start practicing some of these communication skills, how does that speed up? If you would have had seven different touch points of back and forth, does that shrink to two to three?

(00:33:08):
Not every point of friction is going to be avoidable, but a lot of it is if you get better at communicating. So I like watching for the reaction and how quickly and how enthusiastically I'm able to get that reaction. And for the things that are working, do more of that. For things that are not working, adjust your execution because it might not be that the tactic doesn't work, it might be your execution of it wasn't great. And keep trying, basically.

Lenny Rachitsky (00:33:35):
So the advice here is just see how well you're writing/meeting/suggestion goes, how well it does. And if it's not like there's the ideal immediately, "Yes, let's do it." And then there's the, "I don't really understand." There's the spectrum of response. And what I'm hearing is just pay attention to if the speed to getting what you want is increasing in general.

Wes Kao (00:33:59):
Yeah, yeah. I don't think that there's any single shortcut on how to get better besides that. I do think that being fascinated by a topic and being excited about it makes it more likely that you're going to find it fun to try all these different things and try different ways to get through to people. So, I would approach it with a hypothesis-driven experimental mindset and almost like a game. Like, "When I do this, how does that other person react? If I frame it this way, do I get a different reaction? When I try this, am I able to cut through the noise more?"

(00:34:39):
Yeah. So I really think it's about practicing. And I will say that the way not to do it is to try to incorporate 30 different tactics at the same time and then beat yourself up when you don't remember to do them. It's really easy when you are learning a new field or function to get overwhelmed when you're learning a new skill. And the way to build a habit is usually not changing so many different things at once. It's picking one thing that you want to try and keeping that top of mind, trying it in a bunch of different settings in different ways. And getting it better at that thing before moving on to the next thing.

(00:35:19):
So that's like a really common thing I see in my course is people feeling overwhelmed. And I always remind folks that, "You are building a new habit here. And be patient with yourself, take it step by step."

Lenny Rachitsky (00:35:31):
There's a lot of stuff we're talking about here that a lot of people might be like, "This is so minor. What? I just bullet point sentences, be a little... Tell them the why at the beginning."

(00:35:41):
And I just want to share in my experience the biggest jump I made in my career was actually getting better at these very specific skills. I had this manager, Vlad, who's been on the podcast and I talk about him regularly, who was such a stickler about communicating well and being very clear and concise and thinking and just spending more time on documents and emails, on strategy docs. Just like, "No, this isn't ready. Spend more time, here's something that's not clear." And just doing that was such an accelerant for me.

(00:36:12):
And it's all these little things. That's what's interesting about it. It's like everything seems really minor but it all adds up to a lot of impact because to your point, people see it, "Okay, cool, I get it, let's go." Versus like, "I don't like this idea." And then it's like it all falls apart. So I guess any reactions to that?

Wes Kao (00:36:29):
Yeah. All these little things compound and make a big difference. I often hear people think, "Well, this individual instance, this individual email, the Slack message is not worth spending a couple more minutes on. It's just an email or it's just a Slack message." The problem with that line of thinking is that no one instance of something is ever going to feel important enough to spend a little bit more time on that. And then, but when you zoom out, that's like, "Well that's all your work then. This is literally everything you've touched. This is all your work output then." because any piece of that process you thought wasn't worth spending time on and now this is just the quality of your work and it's not as good as it could be.

(00:37:15):
So yes, these might seem minor but A, it compounds. And also B, all the "big things," everyone else is already doing. So, there's not a lot of alpha in that. Whereas if you are paying attention to skills that people think are boring or too basic and realizing that's a lever that you can pull, that someone else thought, "Oh, we're hitting diminishing returns on that. I'm not going to spend more time on that." But you realize that there's actually more juice left to squeeze there and you decide to squeeze that juice. Well, now, you have extra juice that the other person doesn't have.

(00:37:56):
So yeah, in my experience I find that people claim the point of diminishing returns way too early. And this isn't just for communication, this is for strategies, tactics, et cetera. They'll try something once, a mediocre attempt and be like, "This channel doesn't work. This tactic doesn't work." It's like, "Really? Because it's working for a lot of other people who are getting really creative with it."

(00:38:19):
I'm not saying that everything has to work for you but for you to claim, "This thing just doesn't work," feels a little bit intellectually dishonest. It's more likely that your skill level, your creativity, your execution ability was not good enough. And that's fine. Let's admit that to ourselves because if we admit that, then we can do the hard work of getting better at those things.

Lenny Rachitsky (00:38:42):
It feels like if you really boil this down, all the advice comes down to just spend a little more time on all these things you're putting out.

Wes Kao (00:38:51):
I like thinking about it as a little bit more upfront investment. And it is an investment. It's not just time. It's an investment because yes, it takes a little bit longer to make a Slack message a little bit better, but net, net if you save a bunch of questions and back and forth and people asking you things that you don't think they should be asking, then by investing a little bit of upfront effort, you've prevented all that from happening. So yeah, it is a little bit more time in the moment but reaps a lot of benefits down the line.

Lenny Rachitsky (00:39:25):
Today's episode is brought to you by Coda. I personally use Coda every single day to manage my podcast and also to manage my community. It's where I put the questions that I plan to ask every guest that's coming on the podcast. It's where I put my community resources, it's how I manage my workflows. Here's how Coda can help you. Imagine starting a project at work and your vision is clear. You know exactly who's doing what and where to find the data that you need to do your part. In fact, you don't have to waste time searching for anything because everything your team needs from project trackers and OKRs to documents and spreadsheets lives in one tab all in Coda. With Coda's collaborative all-in-one workspace, you get the flexibility of docs, the structure of spreadsheets, the power of applications, and the intelligence of AI all in one easy to organize tab. Like I mentioned earlier, I use Coda every single day. And more than 50,000 teams trust Coda to keep them more aligned and focused. If you're a startup team looking to increase alignment and agility, Coda can help you move from planning to execution in record time. To try it for yourself, go to coda.io/lenny today and get six months free of the team plan for startups. That's C-O-D-A.I-O/lenny to get started for free and get six months of the team plan, coda.io/lenny.

(00:40:42):
You mentioned Slack. I have a great quote also about you that I didn't read that I'm just going to read right now from someone that worked with you. She said she searched the Slack channel at the company you worked at for old posts from Wes for inspiration for what to ask you. And she said you had zero half-baked thoughts, 100% complete sentences, perfect punctuation, clear takeaways at the top of every message. It's the kind of thing you don't notice in isolation, but once you see everyone else's messages in a remote-first company, it's a stark contrast.

Wes Kao (00:41:14):
Yeah, thank you. I will also say that as someone who tries to walk the talk, I feel like I get a pretty good response rate pretty quickly for the things that I ask for, for the recommendations I'm making. It's not instant, it's not 100%, but over time I've realized that improving my communication has led to people receiving my ideas better. Ideas that used to be locked in my head that I would get frustrated that no one else understood. People were now understanding and that feels really good. That's very, very exciting and it made me want to do it more and pay more attention to that. So that's going back to what I said earlier about watching for what's working. There's momentum is really encouraging.

Lenny Rachitsky (00:42:01):
And I totally feel that. If you start getting the things you want, that feels great. I'd be like, "Okay, cool."

Wes Kao (00:42:08):
Yeah, more.

Lenny Rachitsky (00:42:09):
"Let's do more of that." Yeah, and again, it's like very minor things. It's like a couple more minutes on the Slack message, a couple more minutes on email.

Wes Kao (00:42:16):
Very doable.

Lenny Rachitsky (00:42:17):
Yeah, which everyone can do. There's no magic here, it's just spend a little more time and use some of these tactics that we're talking about. Speaking of that, let me talk about another tactic. Apparently you have some really good advice on finding the right level of confidence in what you're saying. There's always this question of, "I come to this leader. How confident should I be about, 'This is the answer,' versus, 'Here's a bunch of ideas'?" What do you think? What's your advice there?

Wes Kao (00:42:41):
I find that people tend to naturally be on the spectrum a little bit too confident as a baseline or not confident enough. So people who are too confident might state hypotheses as if they are fact. So that really bothers me. That's another one of my pet peeves, where if you say, "This is X," or, "This will X," that is different than saying, "This could X," or, "This might X," or, "This will increase the likelihood of X."

(00:43:12):
So I'm a big proponent of speaking accurately. You can avoid a lot of problems if you speak accurately about your level of conviction and about the actual amount of evidence that you have for something. It's okay for something to be an initial hunch. Say, "It's an initial hunch." Don't act like this is something that you are super sure about. You've proven out that this is absolutely this way because the rest of your team is listening to you at face value. And y'all might spend real headcount and dollars pursuing something that you have advocated for in a way where you overreached with your level of confidence.

(00:43:52):
So, that's for people who are overconfident. It's equally a problem if you're under-confident. So I have some clients who their CEO asked them to share some recommendations with another team because they've run something before and so they share all this amazing information and at the end they're like, "Oh, but you can ignore everything I just said. Obviously, make your own decision. Do what you think is best. And if you want to just ignore everything, that's totally cool too." And it's like you just didn't have to say that. You could say, "Make your own decision, take all this into account," but you don't have to diminish to that degree.

(00:44:31):
And so again, speaking accurately, if you have really strong reasons to recommend something to the cross-functional team, it's almost irresponsible to act like you are not really sure and it's just this random idea, "Hey, try it if you want to." We might lose a lot of money and time if we don't take this idea, right? So again, speaking accurately is so, so important.

Lenny Rachitsky (00:44:56):
Is a simple way to think about then the right balance is have a point of view, have a recommendation, present accurate facts, and be clear when you are not? "It's not actually 100% true, but here's a hunch I have, or here's a theory we have."

Wes Kao (00:45:11):
Yeah, I think sharing a point of view, sharing a recommendation, and then backing it up with evidence, with logic, with first principles, with examples, with data, if you have it. Not every situation you're going to have data for, especially if you're building something new. So this is where first principles comes in. Even explaining how you got to where you got to and why you think this is going to work, that all gives your team, your manager, something to push back on, to poke holes on or to align on and say, "Yeah, I agree here, but I disagree on this part."

(00:45:44):
So you can talk about ideas with a lot more specificity when you share your thought process. And you can frame it all kicking off saying, "My initial thinking is," or, "Based on what we know, my hunch is, blank." So speaking accurately and then still bringing up those facts so that we can all make as informed of a decision as we can make given what we know.

Lenny Rachitsky (00:46:07):
Advice I got that really helped here for me was to try not to be biased with how you frame everything. You have your suggestion for how to do something. It's easy to just bias all of the data to point in that direction. And if people notice that, they're like, "Oh, okay. Well, I can't really trust this because I see you're just like, you clearly have an agenda." So it's a little bit like having an agenda and a POV, but be clear about what is actually true. Be accurate.

Wes Kao (00:46:36):
Yeah. I think anytime people have to discount what you're saying because you are biased in this way is not great.

Lenny Rachitsky (00:46:45):
Is there an example by any chance that highlights what you're describing here?

Wes Kao (00:46:49):
Yeah, so in my course I talk about not being a single-minded martyr. So single-minded martyr is someone who very much has an agenda, who wants the recommendation to go through and is presenting a bunch of evidence, supporting that direction. And then gets really frustrated when other people are not seeing it or are skeptical. And so one of my clients was a single-minded martyr in a recommendation she was making. So she was on the growth acquisition side of her company. And was having trouble with cross-functional team members lending headcount to her project. And so everyone would say like, " Oh, yes, we believe in this, this is important," but wouldn't want to actually give her half of their engineer for two weeks.

(00:47:36):
And we were talking about it and as we were talking, she revealed that the CEO had at the beginning of the year said that the company-wide goal is retention that year. That their biggest challenges and areas of opportunity were in retention, not necessarily in growth. And once she zoomed out and realized this, she was able to put her recommendation in context. And realized that it's not just-

Wes Kao (00:48:00):
... recommendation in context. And realize that it's not just I'm the only one who cares about this company. Everyone is a hypocrite. They say they believe this, but don't actually want to work on it. Before that was kind of her narrative, but once she zoomed out and realized she was being a single [inaudible 00:48:16], she could better fit her proposal in the context of what else was happening in the organization. I think actually this is a really big difference between more junior people versus more senior people. More junior people are like, "I need to win. I need to get a yes for this proposal and I'm going to keep advocating for it until I get a yes." Whereas really sometimes the best decision for the company is not right now. This doesn't actually fit our priorities right now, right?

(00:48:42):
Or maybe yes, but let's right size the level of investment. So it might look like half whatever the size of what that recommendation actually was, and having the maturity to realize that, to put your idea into context is huge. That took me a really long time to learn and I think that goes under the umbrella of always do what's best for the company, not necessarily what's best for me, my career, my team, my wins. If you prioritize what's best for the company, that helps you have a more right-sized way of still advocating for your ideas, but doing it with a bit more equanimity.

Lenny Rachitsky (00:49:26):
And also just connecting to what the company is. Just this idea of if the thing you're pitching is not aligned with what is important to the company right now, it's unlikely to be prioritized. It makes sense. This is why leaders choose, here's what matters most. We got to do the things that are going to help us drive this thing right now, like retention or revenue. And so that's just, I think, a sub tactic there is just whenever you're pitching something, connect that to the goal of the person you're pitching to so that they're like, "Oh, I see how this is going to help me. That's great. Let's do it. Great advice."

(00:50:01):
And I think this is something a lot of people run into. It's just, "Why aren't they listening to me? Why don't they want... That's such a good idea. They hate me." It's something, "Oh, I bet they hate me. They don't trust me." When it's just like, okay, this isn't a priority right now. Let's come back to it another time. Okay. I'm going to get to a couple more tactics and then I'm going to shift directions to talk about managers and being manager. You have an awesome framework called MOO. What is MOO? What does it stand for and what is it all about?

Wes Kao (00:50:26):
MOO stands for Most Obvious Objection. M-O-O. And the thought there is that a lot of times we're surprised by the questions that we get, especially in meetings where we feel blindsided, that was unexpected, and then we're on our back foot. When really, if you thought for even two minutes about what are obvious objections that I'm likely to get when I share this, you often immediately come up with what some of those things are. So are you going to be able to anticipate every single objection? No. But can you anticipate the obvious ones? Absolutely. And so this is where knowing your own argument in and out, including counterarguments becomes so important. So knowing your counterarguments as well as you know the arguments for doing the thing. When you do that, when you have prepared in that way, you're less likely to feel caught off guard.

Lenny Rachitsky (00:51:23):
When you hear you talk about this, it's like, obviously I shouldn't do this, but very few people actually do this, actually spend a couple minutes, " Okay, here's what I'm going to pitch."

Wes Kao (00:51:31):
Even a couple seconds, really. Really, even a couple seconds, your brain will think of something.

Lenny Rachitsky (00:51:38):
Is there a story or an example of this that you share that highlights this idea of the power of MOO?

Wes Kao (00:51:43):
I use MOO multiple times a day, every day, every single day. Literally whatever I'm about to say I think how might someone disagree with this or what might an objection be? So whatever it is I'm writing, saying, it's a really good mental filter because it encourages you to think a couple steps ahead in kind of a structured way, right? If I'm about to say this, the person may then say this to me. Well, if I take that into account, I can volunteer that information upfront or I can frame it in a way where they're less likely to think that that's an issue.

(00:52:19):
And so it's muscle memory for me at this point, and this might be something we include at the end is something to start with. But putting MOO on a post-it, Most Obvious Objection, what is someone likely to object about? And then just keeping that top of mind. It's a great way to train yourself to empathize with your audience and with your recipient. We all say that and we all know we should do it, but for me this is a really tactical concrete way to do it.

Lenny Rachitsky (00:52:50):
I think what's great about a lot of the tactics you're sharing is not only is it going to help you communicate it better, but it helps you actually think and crystallize it better for yourself because you may realize, oh, that's a really good objection. Like, oh, the objection's probably going to be this. Will it drive enough impact for the business? Oh, that's a great point. Maybe I should not pitch this right now.

Wes Kao (00:53:10):
Yeah. It definitely helps shape your own thinking. I think communication and thinking are so much more interrelated than we think. I think people think there's a thinking as phase one and then communicating the thinking, and the reality is a lot more intertwined. And I loved your example there that thinking ahead to what might be the most obvious objection actually then prompts you to realize that maybe there was a gap in what you were planning to present and then you now have an opportunity to strengthen that pitch before you say it out loud.

Lenny Rachitsky (00:53:45):
There's a quote I have highlighted on this podcast a number of times that I love that is exactly along these lines by Joan Didion. "I don't know what I think until I write it down." I know exactly that feeling. Okay. So there's a couple more things that people have shared that you are amazing at helping them get better at. One is just keeping your cool and staying calm during very high stakes, real-time conversations when things maybe aren't going your way or if you disagree with someone, any advice on that, it feels like you're really good at this.

Wes Kao (00:54:17):
I think one thing that tends to throw people off is putting a lot of pressure on themselves to get the exact right answer. So if they are asked a question and they don't know the answer, a lot of people will then kind of freak out. And I was taught early in my career that if you don't know the answer, you should say, "Let me look into it, I'll get back to you." So that's a fine approach. It's definitely better than making something up, right? So definitely don't make something up. But if you are more experienced and have some confidence in your subject matter area, just saying I'll get back to you, is sometimes a missed opportunity. You can ask for a bit more information to be able to continue the conversation in that moment. So let's say that your exec says what percentage of users came from mobile last month and you don't have that number off the top of your head.

(00:55:20):
So person A says, "Let me look into it and I'll get back to you." Person B might say, "I don't have that number off the top of my head, but in the last quarter the number has been 60 to 70% and it's grown in the past year, so mobile is now a bigger part of our business, et cetera. Are you wondering if we are investing in mobile appropriately or where's that commission coming from, basically? Right? And so being able to answer a similar question in the direction you think the person is asking about and then validating why they're asking that question allows you to still continue that conversation in the moment. I call it the question behind the question, sometimes you get a question, but underneath there's a deeper underlying concern.

(00:56:10):
And many times people don't even know that it's there, right? Subconscious. So it's not nefarious, they're not withholding anything from you. But when you are explaining something and you're kind of getting multiple questions on the same thing, it's a good sign that there might be a deeper question behind the question and it's our responsibility to figure out what might that be. And so probing, asking for a bit more information, answering in that general direction and then validating these are all techniques you can use when you are in the moment without feeling like, oh, I must have every single thing prepared and the moment that I'm caught off guard, everything goes to shit.

Lenny Rachitsky (00:56:49):
Another tactic along these lines that's very similar to what you're describing, but I'll share that I learned that was really helpful is just if you're not sure what to say, basically just reflecting back their question and just being like, let me just make sure I understand what you're looking for. You want to understand monthly retention for, and then maybe clarify. And that one gives you time to think about it as you're talking. Two, it helps the person recognize, "Oh, he hears me. Great. Okay, this is good. He's thinking about this." And then at the end of that you could be like, "Okay. I don't actually have that specific number. Let me think about it." Or, "I have the quarterly number. Okay. That's what I know." So there's an interim step almost that I'll add into your piece of advice of just reflect back their question, just better understand what they're looking for.

Wes Kao (00:57:32):
Yeah, I love that. Mm-hmm. Mm-hmm.

Lenny Rachitsky (00:57:34):
Awesome. Okay, let's go back to what I said we do. Let's pick one tactic that you think people should try first, maybe one or two. So let me read the ones we've gone through and then see what you think would be a good first step. So one is starting with sales, before getting to logistics and giving people the why signposting using specific words to help people guide the doc and not get overwhelmed. Finding the right level of confidence, having a POV, that sort of thing. Getting better, being concise, MOO, not overusing formatting, something else you shared. And then this idea of when you don't know the answer, not saying I'll get back to you as the default, maybe giving them a different answer, maybe asking them more questions. Across those, which do you think someone should try to like, "Okay. Let me start here."

Wes Kao (00:58:25):
I would start with Most Obvious Objection and also framing your conversation up front. And that kind of relates to using signposting words if needed to help you frame that conversation.

Lenny Rachitsky (00:58:37):
Sweet. That's such an easy one to remember. Just MOO. Okay. So stick a post it somewhere when you're about to share something in Slack and ask someone for something, present in a meeting, send a strategy, and just think about for a few seconds what might be the most obvious objection to what I'm trying to ask them to do. Great. Okay. So let's talk about management. And there's kind of two sides to it. Being a manager and being a person reporting to a manager, you have a bunch of really good advice here. One is there around managing up. One of my most popular posts in the early days was advice for managing up and just how important it is. What advice do you have for someone to get better at managing up? Why is that even so important? Why do you think people may be under appreciating how important it is to manage your manager, let's say.

Wes Kao (00:59:18):
One of the most common myths about managing up that I definitely felt early on in my career was that I would have to manage up if I were more junior, but eventually I would outgrow it, that I would get senior enough that I would no longer have to do it. And it was a rude awakening that no matter how senior I got, managing up, I not only had to manage up, it actually became more important. So I think managing up is one of those skills that if you invest in learning it, it serves you now and for the rest of your career. And I realize that many senior people are actually the best at managing up. That's partially how they got to be so senior in the first place. But also, the more senior you get, the less likely that your manager is going to give you really well-defined tasks and problems on a silver platter and ask you to solve them.

(01:00:09):
You are going to be dealing with more ambiguity and you're going to be dealing with sometimes a mandate like make this number go up or create this division, right? Where you need to manage up and make sure that your leader, your manager, is in the loop about what you are about to try and what you're about to do and make sure that they're aligned. And so for me, realizing that managing up is something that is ongoing and that it shifts and evolves and looks different as you go in your career, that was a big unlock for me.

Lenny Rachitsky (01:00:44):
Just that even if you become even a VP, if you become a director and still something you want to invest in, any specific tactic or advice for how to manage up well.

Wes Kao (01:00:54):
The biggest one is to share your point of view. So this some people are surprised by because they think I'm going to say do a weekly recap of the tasks that you worked on or what you contributed. And that is a good idea, if you want to do it, you can do it. But I think the more highly leveraged way to contribute and manage up is by being more vocal about sharing your point of view. When you just ask your manager, "Hey manager, what should we do?" You're putting a lot of cognitive load on your manager to need to think about the problem, think about potential solutions, craft the solution, and then tell you what to do. Whereas if you instead said, "Hey manager, here's what I think we should do. How does that sound? Where do you see gaps? Am I thinking in the right direction?" You give them something to build off of and that reduces the amount of mental lift that they have to put forth.

(01:01:54):
And so sharing your point of view more readily, backing it up with evidence, that's a wonderful way of making your manager's life easier. And also showing that you are an active rigorous thinker who is thinking strategically about the business. You're not just waiting to be told what to do, you're not expecting them to figure things out and then tell you you are actively looking around the corner trying to solve problems, forming hypotheses in your mind, observing and noticing things. And again, sharing your point of view doesn't mean that you have the perfect answer. You can share that, "Hey, I've noticed this problem popping up in a couple of different places. Here's what I think might be happening."

(01:02:36):
Or when you share a report, don't only share the report and expect your manager to come up with insights and takeaways. You should look at the report too and point out insights and takeaways. So it's really changing that posture from more reactive and more waiting to be told what to do or kind of staying in this narrow box to being willing to share your recommendation, your point of view, share what you're noticing, and this is something that even junior people could do.

Lenny Rachitsky (01:03:04):
I was going to say exactly that. I think not only is it something junior people can do, this is a really good way to get promoted and to take on more leadership opportunities. You coming to your manager with, "Here's something I think we should do. Here's a perspective I have. Here's an opportunity." If you were in charge, you're like, how awesome would it be for people to come to me with amazing ideas and have clear recommendations? That sounds great. Everyone wants that. So if you can do that, amazing. Who wouldn't want that? But then what's interesting is similar to how writing helps you crystallize your thinking, you coming in with a recommendation forces you to really think deeply about it because that's putting your reputation on the line. So there's a second order effect of it makes you actually spend more time on the thing and be clear about why you think this is a good idea and do more research. So a lot of wins here.

Wes Kao (01:03:53):
There are a lot of situations where you might have the most visibility into a problem. You might have the most proximity into an issue. And so if you're not speaking up about it and sharing what you're observing, sharing what you're noticing, your manager doesn't necessarily have visibility into that. And so I've heard so many managers say that they want their junior people to speak up more because their junior people have often close contact with customers, with support tickets, with cleaning data, with a bunch of things where the manager would love to hear insights from that.

Lenny Rachitsky (01:04:32):
If you're not having success with this, if you're hearing this and be like, but it never worked, my manager doesn't listen to me, listen to the rest of this podcast we just did, which is basically advice on how to effectively convince someone of a thing. It's like, tell them why this is a problem, be really concise about it, sign post words, all these things. That's exactly what this whole conversation's been about. Okay. Let's see. We have a couple more really cool tactics that people have suggested we talk about. One is how to give feedback well, how to do better, how to be more effective at giving feedback. What's your advice there?

Wes Kao (01:05:05):
I have a framework called strategy, not self-expression. And so the idea here is that most of the time, by the time we are giving feedback to someone, we have been frustrated for a while. I used to be very conflict diverse, so I would wait and try to convince myself that I wasn't bothered by something until I really couldn't hold it in anymore. Then I would schedule a one-on-one with a coworker to tell them the feedback and it would inevitably turn into a venting session where I was in the name of sharing the impact of what they did would share all my frustrations and all the ways that they have basically harmed me and made my life difficult. And this would be very counterproductive because the person would either feel like and feel really demoralized or they'd get really defensive and they'd want to argue with me about how what they did actually was not that bad or it was partially my fault too or whatever.

(01:05:59):
And so I realized that a better way of giving feedback is thinking about motivating the person's behavior change. The goal is behavior change. So if that's the goal, trim everything else that you were about to say that does not actually contribute to that goal and only keep the part that will make the person want to change, help them understand the benefit to them as well as to the people around them. And so usually for me, that's trimming 90% of the initial stuff that I want to say and really keeping only that 10%. And that's made a really big difference. Whenever I am giving constructive feedback of any kind, I always keep that in mind. And when I don't do it, I almost always regret it.

Lenny Rachitsky (01:06:46):
Someone close to me in my life is working on the skill, which is there's just, "I want people to know how they messed up. Justice. I need this to be fair." And what I always recommend is just think about what you want to get out of this conversation, what do you want from them? And then, okay, what's the best way to get that? Versus just making sure they hear you and making sure they understand how screwed up this was. And that's basically what you're saying is focus on the outcome you want to achieve, not something that's useful, something that will make you just feel better.

Wes Kao (01:07:23):
Yeah. I definitely think that having a space to vent and to share those frustrations is important. So you want to get that out before you go into the conversation with your counterpart. So whether it's talking to your therapist or your partner or friend, you want to basically get all that energy out because otherwise you bring it into the conversation and it doesn't take much to set you off. You might have a whole script, you're controlled, you're calm, and then you start talking and the other person raises an eyebrow and is acting a little incredulous at what you're saying, and that's all it takes for you to snap and be like, "You're surprised? You're incredulous? Why are you incredulous?" Right? And then you're off, right? Yeah. Getting that energy out, I would say step one, so that you can go into the conversation clear, grounded, setting that emotional tone that is more positive and that allows you to stay focused on only the part that will get them to behave in the way you want them to behave.

Lenny Rachitsky (01:08:23):
Such good advice. And I think we come back to are you getting the outcomes you want? If you're not, this is another reason it might be the case is you just need them to hear your mind. I just need you to know. And I think a lesson here is that may not be the best path to getting what you want, but it may feel good. Maybe people are like, "Ah, but I really want them to know this."

Wes Kao (01:08:42):
There's that great Einstein quote about insanity being repeating things that you're doing expecting a different outcome. And I feel like that applies so much to the workplace and to communication. Most of us have certain patterns that we are used to and certain ways of responding, and if you believe that there is untapped upside that whatever you are at is kind of a local maximum and that there's better out there, then that's where switching things up could be useful and not just doing everything that you've been doing and getting the same result that you might be getting.

Lenny Rachitsky (01:09:19):
This resonates with Toby Lutke when he is doing the podcast, talked about how... He had this quote that I love that just "No human in history has come anywhere near their potential and everyone is way, way, way better than they think are," and these are really cool tactics and really effective ways to actually get closer to your potential. Okay. Two more things I want to talk about real quick. One is your advice on delegating, but also continuing to have high standards. This is something I spent a lot of time on because a lot of people don't delegate because they're afraid it's not going to be as great. I just want this to be really good. I don't trust that it's going to go as well. If I did it my way, it'd be great. So just advice on how to delegate effectively while maintaining high standards.

Wes Kao (01:10:04):
Yeah. I have a framework called CEDAF. C-E-D-A-F.

Lenny Rachitsky (01:10:08):
Mm-hmm. I love all these acronyms.

Wes Kao (01:10:09):
It's kind of like Cedar, but with an F at the end. I need acronyms for myself. All of these are really reminders for myself because I need a short way to remind myself. So CEDAF stands for the C is comprehension. So have I given this person that I'm delegating to everything that they need to understand what it is that I want them to do. That includes more simple things like logins to all the right software tools that they need to look up, whatever you need to look up. And understanding what the end result should look like, right? So that's all under C for comprehension. E is excitement. Am I explaining this in a way that is making this as exciting as it could be? There are a lot of tasks that aren't inherently that exciting, but by explaining the why behind we're doing this or why it's important to the project we're working on, that makes people more likely to understand and be excited about how this fits into everything.

(01:11:06):
So E is for excitement. D is for de-risk. Am I de-risking any obvious risks from delegating this? So usually when I ask clients this, they immediately think of something. They're like, "Oh yeah, I wouldn't want my direct report to spend a ton of time going in the wrong direction, filling out a hundred rows of the spreadsheet if actually it took longer than we expected." Okay, great. If that's a risk, then maybe you have them do 10 rows, see how long it takes, see if we need all the information that they're actually gathering, and then regroup, right? So what's an obvious risk? Another might be I can see this person misunderstanding and thinking I'm looking for this where I'm really looking for that. Okay, perfect. Just tell them, "When I explain this, you might think I mean this, but really I don't want that. I actually want this," right? So just vocalize it. The A is for align. So am I giving the other person a chance to-

Wes Kao (01:12:00):
The A is for align. So am I giving the other person a chance to speak up and make sure we are actually aligned, that they're picking up what I'm putting down? Because you might be explaining a bunch of stuff, but how much are they actually absorbing? You won't ever know if you wrap up your little spiel and then say, "Okay, go off. Come back to me when you're done." So give people a chance to ask questions to see what parts are resonating, what parts they might be a little bit confused on. Usually, when I do this, it's amazing. Because my team member will say, "What did you mean by this part? How does this part fit in?" I'm like, "Oh my God, I totally forgot to mention this thing." Or, "Oh yeah, I didn't even really explain that well." Okay, so let's go into that.

(01:12:42):
And then F is feedback. How can you have the shortest feedback loop possible? I am a huge fan of shorting the feedback loop as much as possible and then shortening it again. So even within that initial conversation where I'm delegating something, instead of waiting a week, what if we waited a day and checked in on the initial direction that person was going? And let's do it even more. What if after I finished explaining, at the end of that conversation, we brainstormed a couple things that, that person wants to do? So within this same conversation, I'm delegating, I'm already getting a sense of, where do you want to go with this? Once you start, do you see any bottlenecks?

(01:13:24):
And so just really keeping that feedback loop super tight. I found that when I run through the CDAP acronym, there's usually one letter that I could amp up a little bit more like, oh, I didn't really put much thought into making this exciting for the person. How can I connect this to their career goals or to the company's priorities this quarter or to something else? So it's a nice mental checklist.

Lenny Rachitsky (01:13:49):
So much of your advice comes back to this idea that we've touched on a couple of times. We just spend a little bit more time upfront. Is that how you described it, a little more time upfront?

Wes Kao (01:13:56):
Yeah, a little bit more time. A little bit more of an investment upfront.

Lenny Rachitsky (01:13:59):
Upfront to save you tons of time later. Okay. So as you described this, I don't know if you're realizing this, but you're basically just helping people work better with AI and agents. This framework is exactly I think what people need to effectively delegate to this future world of this agent world of society of agents doing work for us. Basically, you're going to be delegating to these agents in the future, and this framework is a really cool way to frame it. So think about it. Am I communicating this well, comprehension? So CDAP. Comprehension is, again, can I make this clear? Is that the way to think about that?

Wes Kao (01:14:41):
Yeah. Can I make this clear? Does this person have everything they need to be able to accomplish what I am asking them to do?

Lenny Rachitsky (01:14:47):
Okay. And then it's communicate why you're excited about this, basically the why. And it's interesting, there's this funny prompt technique I've learned, prompting engineering technique of just telling the AI, "This is very important to my job." Just using that sentence, it does it better.

Wes Kao (01:14:47):
Oh, interesting, yeah.

Lenny Rachitsky (01:15:04):
It takes it more seriously. It's just so weird. I have a post about this, and that's one of the pieces of advice, just tell me why this is important. I think people take it to the extreme as someone will die if you don't get this right. That actually works.

Wes Kao (01:15:16):
That is extreme. Cool.

Lenny Rachitsky (01:15:18):
It's wild. Okay, so CEDF, comprehension, excited, de-risk, think about ways you can de-risk, which is moot, basically. What's the most? It's a similar concept. Just think ahead to what might go wrong. Make sure you're aligned, which is quite important in the AI space. Make sure you're aligned. And feedback, get a quick feedback cycle. And it's interesting with deep research on some of these AI tools now, it's like, "I'm off for half an hour. See you." And I imagine more and more of them will check in with you as it's going and ask you questions. I used deep research recently and it's really good at just like, okay, let me have five questions for you before I go off and do this work just to clarify what you want.

Wes Kao (01:15:58):
Yeah, I found that AI will often shorten the feedback loop and align with you as well. When you prompt it, when it comes back, it will not do the entire task for me, sometimes. It'll say, "I've done the first part of this. Does this sound right? Is this what you're looking for? If so, I will complete the next section." And then sometimes I'm like, "Do the whole thing. Just stop trying to conserve energy and just do. I want you to do the whole thing." But that's what it's doing, it's breaking it into smaller chunks to de-risk that it's going to use all this bandwidth to process this thing and I'm going to say, "Oh, that's not what I was looking for."

Lenny Rachitsky (01:16:37):
I'm going to come back to AI real quick, but before I do that, I have one more question for you, but let me just say, I feel like we've discovered an AI version of your course now. Basically, how to delegate well to AI agents that I think people are going to find really valuable, planting a seed. Okay. Before we get back to AI, you have this other concept that I love that I actually learned from you years ago when I was working on my course called the swipe file. Swipe file, what is a swipe file? What is that about? What can it help you with? Why should people be doing this?

Wes Kao (01:17:03):
Yeah. So swipe files are really common for marketers, and I think other functions haven't caught on as much, but I think it is really, really useful. And basically a swipe file is collecting inspiration that you can refer back to later on. So some marketers will collect examples of copy, landing pages, ads, et cetera. For me, I have a file, an Apple Notes, file called Smart Things People Have Said, where I will basically paste in phrases, words, things people have said that I thought were well articulated or sounded really intelligent or sounded strategic. And I don't actually go back and look through my swipe file very often, I think other people do, but for me, even the act of adding it to my swipe file, I've already gotten value from it because it's training me to be more alert to noticing when something is working well.

(01:18:01):
I think there's so much happening around us all the time that your coworker says something smart and you're like, "Oh, that was nice," and then you keep moving on. But when you stop and pause and think, oh, that was really effective, let me add it to my file, and also think about, why was that effective and is that something I can borrow? So in my course, I encourage folks to create a work journal where they can jot down some of these observations, some of these phrases, and basically encourage yourself to be more alert to things you can borrow from other people all around you.

Lenny Rachitsky (01:18:38):
Something else about the swipe file, you use quotes. It could be screenshots of cool designs. It could be strategy docs you found to be really effective. It could be conversion flows that are really cool. It could be just whatever you're interested in.

Wes Kao (01:18:52):
Yeah. And the great thing about that is you can then go back and analyze it and break down the structure, break down the argument, break down why was this so effective? Whereas if you're not capturing it, it's easy to just move on to the next thing.

Lenny Rachitsky (01:19:09):
Yeah, cool. And I did this for a while. I stopped, to be honest, but I really want to be doing this. So this is maybe some homework or something, because I know a lot of people stick with it, is just start like a folder or a Notes, note, whatever you use for your note-taking, and just start throwing stuff in there. And it could be messy, right? It's just like, throw it in.

Wes Kao (01:19:27):
It can be super messy. I was going to say, my back end system is super messy and it's fine. It's not a problem I need to be solving. It works. I find things I need to find. So I like having as simple of a process as possible. So Apple Notes, I open it. It's just on my home screen, I just add something. I'm not tagging anything, I'm not putting it in certain rows and filling information out. I'm just including it in a file, and if I want to go back and look at it, it served its purpose.

Lenny Rachitsky (01:19:58):
Awesome. Okay, so last question. AI, I'm going to just come back to this briefly. We have this segment on the podcast called AI Corner, and we touched on this already, but I'm just curious how you have found AI to be useful in your work or your life, whether it's helped you become a better communicator? Is there anything you can share that might be helpful to folks?

Wes Kao (01:20:18):
Yeah. I love Claude. There are days when I talk to Claude for three or four hours prompting as a thought partner. So yeah, I think that AI is really helpful for an initial draft of something to bounce off of. Sometimes I'll paste in an email that I am not quite sure how to respond to and ask Claude, "Tell me draft reply." And I'll usually give it some direction. So I found that sharing my point of view makes the output way better. If I just give it something and say, "What would you say?" It's just not as good. Whereas if I say, "I am not sure about how to tell this person no, because I previously said yes and so I feel on the hook, but history has changed and so is there a nice way where I can be really respectful of our relationship and also make them feel seen and heard, but decline?"

(01:21:19):
So if I explain, "That's the problem I'm dealing with and here's what I would ideally like to be able to do," Claude comes back to something that's pretty good. And then from there I'll edit it to my voice because usually it's a little bit too formal sounding. And so I'll make some edits and then I'll share it back to Claude and say, "What do you think of this version? Would you make any improvements?" And then we go back and forth from there.

Lenny Rachitsky (01:21:41):
Wes, this is the most useful thing I've ever heard.

Wes Kao (01:21:44):
[inaudible 01:21:44].

Lenny Rachitsky (01:21:45):
I need this and I need this immediately, just nice ways to say no to stuff. This needs to be an extension that I can have in my browser, just, "Help me say no to this, please." Wow, such a great idea. Okay, good one. Okay, great. Wes, is there anything else? We've gone through a lot. I imagine the answer is no, but before we get to our very exciting lightning round, is there anything else that you wanted to share or leave listeners with?

Wes Kao (01:22:11):
No, I feel like we covered a bunch of great frameworks, principles, so lots for folks to get started.

Lenny Rachitsky (01:22:18):
All the things. And I love that so much of this will apply to being more effective with AI tools and I feel like people can go through this again and just through that lens of, how will this helped me get more out of Claude and ChatGPT? I bet so much of this will actually apply and I feel like there's an interesting course there. With that, Wes, we've reached our very exciting lightning round.

Wes Kao (01:22:39):
All right,

Lenny Rachitsky (01:22:40):
Are you ready?

Wes Kao (01:22:41):
Let's do it.

Lenny Rachitsky (01:22:42):
Okay. First question, what are a couple books that you recommend most to other people?

Wes Kao (01:22:46):
One is High Output Management by Andy Grove, which is a classic. Another one is Your Brain At Work by Dr. David Rock. And that one is all about better understanding your own brain and attention span so that you can allocate your mental resources appropriately. So that one's great. Ever since reading that, I hide my phone from view because there have been studies that show that even seeing your phone in the corner of your eye, it's distracting. And I do the hardest things earlier in the day when you have more cognitive resources available. So that one's really good. Yeah, those two.

Lenny Rachitsky (01:23:31):
These are great. I completely get that phone thing. I'm just looking at my phone, I'm like, "Dang, get out of here. Just go away."

Wes Kao (01:23:36):
I will stick it under my pillow on the couch or hide it under a notebook. It's huge. I'm always hiding my phone so it's not in my line of sight.

Lenny Rachitsky (01:23:47):
I think Arianna Huffington has a product you can buy that's a little bed for your phone that you put to bed before you go to bed in a different room and it has a charger attached.

Wes Kao (01:23:54):
Oh, that's cute.

Lenny Rachitsky (01:23:55):
So cute, so cute.

Wes Kao (01:23:57):
I don't know if I need a separate bed for my phone.

Lenny Rachitsky (01:24:01):
But it's like a ritual, I guess, and there's some theory behind it. Okay, next question. Favorite recent movie or TV show you really enjoyed?

Wes Kao (01:24:08):
I love Anything by Harlan Coben on Netflix. Basically, I don't even remember any specific movies or a TV series, but anything he puts out, he's an author and then they've turned a lot of his books into mystery thriller TV series, and anything he puts out becomes number one on Netflix. And I appreciate that he gives the people what they want, that he knows his craft, he knows his genre. And yeah, he just has so many bangers. And I don't remember any specific one, but if it's a Harlan Coben show, I know it's going to be good.

Lenny Rachitsky (01:24:46):
I'm looking at a list now I just Googled real quick. So it's all scary stuff, right?

Wes Kao (01:24:49):
Yeah, they're mystery thrillers, and I think he does a good job playing with time and revealing information over time. It's usually something about someone's past that is now coming to haunt them, and so he'll skip between present day to the past and then slowly reveal stuff. And there's always a twist at the end.

Lenny Rachitsky (01:25:11):
There's a page, the Harlan Coben Collection on Netflix. That we'll link to that has all this stuff. I've never heard of this, so this is great. Next question, do you have a favorite product you recently discovered that you really love?

Wes Kao (01:25:22):
I recently started using an electric toothbrush and it's been life-changing. So my husband got one and then a couple weeks later he gifted me one, and I was like, "Wow, this is actually really nice."

Lenny Rachitsky (01:25:34):
Are you a Sonicare person, Oral-B person, or something else?

Wes Kao (01:25:37):
It's Oral-B but I've not tried any other brand. That was one that our dentist gifted my husband this electric toothbrush because he did Invisalign. And I'm sure Invisalign is every dentist's dream.

Lenny Rachitsky (01:25:51):
Margins.

Wes Kao (01:25:52):
I feel like every time I get a cleaning, the dentist is like, "So have you thought about, are you interested in Invisalign?" I'm like, "No." And so when they get a yes, I'm sure they're really excited, and then they lock you in, the brand locks you in with these replacement toothbrush heads that are way more expensive than they should be. So it's a whole razor and blades, ink cartridge and printer model here. So I was horrified by how expensive these replacement heads were.

Lenny Rachitsky (01:26:18):
But you got a free toothbrush. I think the Oral-B is what I use, but I think that's what the Wirecutter recommended, but it's so loud. I don't know. One of them is just really loud. I think it's the Oral-B, but it's better, apparently. I went with Wirecutter, but it's so loud. I feel like there needs to be a Wirecutter for good design and experience...

Wes Kao (01:26:37):
Ooh.

Lenny Rachitsky (01:26:37):
... versus just the optimal efficient version. Anyway, let's keep going. Do you have a life motto that you often find useful in work or in life that you repeat yourself and share with folks?

Wes Kao (01:26:51):
Yes. I actually have many, but I'll share two. One is everything takes longer than you think. So this applies whether you are calling customer support for something or running an errand or building your career, building skills. I find it's useful to add buffers for yourself. This applies for launches too. Just assume it will take longer than you think and you'll be less stressed.

Lenny Rachitsky (01:27:18):
That connects to everything we've been talking about. Just spend a little more time upfront to make it. And maybe if you spend more time front, it'll take less time than you think.

Wes Kao (01:27:25):
The other one is a riff on always be closing, like Glengarry Ross. "It's always be selling." This does not mean pawning your wares, but rather putting forth effort into convincing the other person of whatever your recommendation is.

Lenny Rachitsky (01:27:42):
Love them. Okay, final question. So you've been a long time, I hate this word operator, but I guess that's the way people describe this, where you've just been working at companies, building companies, and you recently left that just to become creative person. Started a course on Maven. You do executive coaching, things like that. Any just lessons or a lesson from that jump that might be helpful to folks that are maybe thinking about that?

Wes Kao (01:28:07):
I think when you are an in-house operator, there's a lot about your role that you have a little bit less control over, basically. There's just certain things you have to do because it comes with the territory. Whereas when you are a solo operator running your own business, doing your own thing, you have a lot of freedom to craft your work around only your strengths, only the part that you are really good at, that adds a lot of value for other people where there's market demand. And so, for me, there was a bit of a shift where when I realized that I could craft my business, my work around only the part that I'm best at, and that can be a narrow-ass slice, that's actually really, really freeing.

(01:28:54):
And so I would encourage folks to think about, what is the thing that you are extremely good at that people find super valuable, the part that you love doing most, if you could not do all the other stuff you don't want to do, and how can you think about doubling down on that?

Lenny Rachitsky (01:29:12):
That's such an important point. And the Claude tip you shared of how to say no well is such an important ingredient into that, because so many things come at you and are interesting and enticing that it's hard to decline, that you realize, why the hell am I doing this? I can actually control where I spend time and why did I say yes to this?

Wes Kao (01:29:33):
I actually credit you with helping me come to this realization. I mentioned you on a podcast the other day about this because, do you remember when Maven was launching an important feature, I think it was our marketplace or something, and I had asked you if you wanted to go on Clubhouse to be part of the launch?

Lenny Rachitsky (01:29:56):
I remember that, but I am sure I said no.

Wes Kao (01:29:59):
Okay, yeah. You said no. You said no. And I was like, "Wow. Out of curiosity, what's the thought behind it?" And you said, I'm going to bastardize this, you could correct me, but you essentially said, "I don't really like doing live public speaking type things and I've been fortunate enough to build a career where I can write, I do my podcasts, and work only on the part that I love doing. And so I'm okay saying no to these other really interesting opportunities." And I remember at that time thinking it was so groundbreaking that you could say no to something that was legitimately a cool opportunity and be really confident about it because it wasn't your core competency. It wasn't the thing you are best at. And I've really kept that in mind when opportunities come my way of, am I excited about this? Is this what I'm really good at? Can I shine in this setting? Because when you are solo, you get to choose the settings that you want to be in.

Lenny Rachitsky (01:31:00):
That's such a cool story. I don't exactly remember that, but I am zero surprised at what I said. And the way I put it now, when folks invite me to stuff like this is I just find the ROI on my time is so not worth doing a talk, doing a fireside thing, doing another podcast. It's just like, if I can spend more time on this newsletter than the podcast, the leverage is so much higher than just doing a talk because that takes so much time. So I just have this template now that basically says what I sent you, that is, that it helps. But it's tough. It's so hard to say no. Sometimes these opportunities are so interesting and the person is like, "Wait, what?"

(01:31:37):
Because I don't think the people asking you for stuff know that I'm getting 10 of them a day, and they're like, "Oh, he said no to my talk. He doesn't want to be on my podcast. What a jerk." That's what I think. I don't know if that's what they think. But anyway. Okay, that's great. Yes, and I think I just had a post about reaching a million subscribers to the newsletter, and actually had this image of the Ikigai concept, which is exactly what you just described, which is you want to try to find the thing that you love doing, that people value, and that you can make money doing. That's the dream. And that's exactly what you have done as well. So thank you for being here, Wes. I actually think we delivered on what I thought we would. I think this is going to be one of the most highest leverage conversations we've had.

(01:32:21):
So two final questions. Where can folks find your course? I know you also do executive coaching. Where can folks learn more? And final question is just, how can folks be useful to you, Wes?

Wes Kao (01:32:33):
You can find out more at weskao.com. I linked my course to my coaching from my main page. I also post on LinkedIn as well, so you can follow me there. And I'm always looking to meet fellow operators who out about communication. So if you put any of these principles into practice, I would love to hear about it.

Lenny Rachitsky (01:32:53):
Awesome. We'll do that in the comments. They can DM you. I don't know, what's the best way to reach you on the website or Twitter?

Wes Kao (01:32:59):
Yeah, bunch of platforms.

Lenny Rachitsky (01:33:02):
All the places. Okay, cool.

Wes Kao (01:33:04):
Website, email, LinkedIn, DM me.

Lenny Rachitsky (01:33:05):
There we go. There we go. Wes, thank you so much for being here.

Wes Kao (01:33:08):
Yeah, thank you so much, Lenny.

Lenny Rachitsky (01:33:09):
Very cool.

Wes Kao (01:33:10):
This was fun.

Lenny Rachitsky (01:33:14):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

---

## Persuasive communication and managing up | Wes Kao (Maven, altMBA, Section4)
**Guest:** Wes Kao 2.0  
**Published:** 2022-08-28  
**YouTube:** https://www.youtube.com/watch?v=4jtGsyz4jLs  
**Tags:** growth, retention, acquisition, okrs, conversion, revenue, leadership, management, strategy, vision  

# Persuasive communication and managing up | Wes Kao (Maven, altMBA, Section4)

## Transcript

Wes Kao (00:00:00):
I often see operators who explain things poorly and then are shocked and horrified when people are confused or there's skepticism, there's apathy. I'm a big proponent of asking myself, if I'm not getting the reaction that I'm looking for, how might I be contributing? How could I explain this more clearly? How can I be more compelling? How can I anticipate any questions that they might have?

Lenny Rachitsky (00:00:22):
You are one of the best teachers of communication I've ever come across. I made a list of people's favorite tactics and frameworks and approaches that you teach in writing. Any tactics you can share for someone to be a little more concise?

Wes Kao (00:00:35):
I think the blast radius of a poorly written memo is way bigger than most people think. If you are just shooting off a message in a Slack channel with 15 other people, and it's confusing, you didn't include information you should have included, there's going to be a bunch of back and forth. Whereas if you had just taken another look at it, those 15 people would be off to the races.

Lenny Rachitsky (00:00:52):
You have an awesome framework called MOO.

Wes Kao (00:00:54):
MOO stands for Most Obvious Objection. A lot of times we're surprised by the questions that we get especially in meetings, we feel blindsided. When really, if you thought for even two minutes about what are obvious objections that I'm likely to get, you often immediately come up with what some of those things are. Are you going to be able to anticipate every single objection? No. But can you anticipate the obvious ones? Absolutely.

Lenny Rachitsky (00:01:22):
Today my guest is Wes Kao. Wes co-created the Alt-MBA program with Seth Godin. She Co-Founded a company called Maven, which I often collaborate with, which makes it easy for people to host live cohort-based courses. She recently left Maven to launch her own course on Executive Communication and Influence. There's a quote that came to mind after I stopped recording this conversation with Wes by George Bernard Shaw, "The single biggest problem in communication is the illusion that it has taken place."

(00:01:51):
By the end of this podcast if you listen to what Wes suggests, you'll be a lot closer to becoming a world-class communicator. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. Also, if you become a yearly subscriber of my newsletter, you get a year free of Perplexity Pro, Superhuman, Notion, Linear and Granola. Check it out at lennysnewsletter.com. With that, I bring you Wes Kao.

(00:02:18):
This episode is brought to you by WorkOS. If you're building a SaaS app, at some point your customers will start asking for enterprise features like SAML authentication and SCIM provisioning. That's where WorkOS comes in, making it fast and painless to add enterprise features to your app. Their APIs are easy to understand so that you can ship quickly and get back to building other features. Today, hundreds of companies are already powered by WorkOS, including ones you probably know like Vercel, Webflow, and Loom.

(00:02:50):
WorkOS also recently acquired Warrant, the Fine Grained Authorization Service. Warrant's product is based on a groundbreaking authorization system called Zanzibar, which was originally designed for Google to power Google Docs and YouTube. This enables fast authorization checks at enormous scale while maintaining a flexible model that can be adapted to even the most complex use cases. If you're currently looking to build role-based access control or other enterprise features like single sign-on, SCIM or user management, you should consider WorkOS. It's a drop-in replacement for Auth0 and supports up to 1 million monthly active users for free. Check it out at workos.com to learn more. That's workos.com.

(00:03:36):
This episode is brought to you by Vanta. When it comes to ensuring your company has top-notch security practices, things get complicated fast. Now you can assess risk, secure the trust of your customers, and automate compliance for SOC 2, ISO 27001, HIPAA and more with a single platform, Vanta. Vanta's market-leading trust management platform helps you continuously monitor compliance alongside reporting and tracking risks. Plus, you can save hours by completing security questionnaires with Vanta AI. Join thousands of global companies that use Vanta to automate evidence collection, unify risk management, and streamline security reviews. Get $1,000 off Vanta when you go to vanta.com/lenny. That's V-A-N-T-A.com/lenny. Wes, thank you so much for being here and welcome back to the podcast.

Wes Kao (00:04:36):
Thanks, Lenny. I'm very honored to be a second-time guest.

Lenny Rachitsky (00:04:40):
Very rare honor. No pressure, but I think this is going to be one of the highest leverage episodes I've done and let me tell you why I think that's the case in the newsletter and on the podcast, I often talk about just how important and how high leverage the skill of communication is to product leaders, to leaders, just to people in general. There's this quote that Boz, the CTO of Meta, he's been on the podcast, he wrote this famous blog post, "Communication is the job." And I think that's true for product people, but it's true for basically any sort of leadership role. Anyone trying to get ahead. And you are one of the best communicators I've ever met. You are one of the best teachers of communication I've ever come across. You have one of the most popular courses on Maven, on executive communication, so I'm really excited to have you here and to help people become better communicators, better at influence and all these things. So thank you again for being here.

Wes Kao (00:05:32):
Absolutely.

Lenny Rachitsky (00:05:34):
Okay. So something that I often do with guests on the podcast, not even often, always, I ping people that the guests have worked with and ask them, "What should I ask Wes? What should I know about Wes?" Let me read a few quotes about you in regards to your communication skills from folks that have worked with you-

Wes Kao (00:05:34):
All right.

Lenny Rachitsky (00:05:51):
And these are three different people. Okay, so first, "Wes single handedly raised the quality of the entire company's writing by like two X across the board. I always say the best writing course I ever took was working with Wes for a year."

Wes Kao (00:06:07):
Wow.

Lenny Rachitsky (00:06:09):
Okay. That's one.

Wes Kao (00:06:10):
Great.

Lenny Rachitsky (00:06:10):
"Wes never just throws things out there, she's precise with her use of language, meticulous about examining her own ideas before bringing them in front of others and knows how to make her points in a way that people will understand them and buy into them." Okay. And third, "Wes includes a reasoning with every proposal in the context behind all of her recommendations so that everyone around her learns in order of magnitude faster. This also makes her an exceptional teacher because she can clearly define what excellence is and why something is the goal, and then break down the steps and principles involved." Okay, reactions.

Wes Kao (00:06:46):
Those are really nice things. That's amazing. Yeah, thank you so much.

Lenny Rachitsky (00:06:52):
And these are people across different companies, so.

Wes Kao (00:06:52):
Cool.

Lenny Rachitsky (00:06:55):
Okay, so that was just to highlight of how good you are at this stuff. And what we're going to be doing with our chat is going through a bunch of your tactics that you teach and that have helped people become better communicators, executive communicators, better at influence. Before we get into the specific tactics, is there anything that you think is important for people to understand just broadly around the skill of becoming a better communicator?

Wes Kao (00:07:17):
I often see operators who explain things poorly and then are shocked and horrified when people are confused or there's skepticism, there's apathy, there's a lot of avoidable questions, and I'm a big proponent of asking myself, "If I'm not getting the reaction that I'm looking for, how might I be contributing to that?" So, you know, instead of blaming other people for not understanding me, I think about how could I explain this more clearly? How can I be more compelling? How can I anticipate any questions that they might have? So I'm a big proponent of agency. And realizing that we can only control our own behavior. And so the best place to start, if you're not getting the reaction you're looking for, is reflecting on how can I get better at the skill of communicating? And it absolutely is a skill.

Lenny Rachitsky (00:08:11):
So what I'm hearing is if you're having a hard time people buying into what you're trying to convince them to do or you're finding people are doing not what you asked them to do, it's likely an issue with your ability to communicate, it's probably not their fault.

Wes Kao (00:08:28):
Yeah, I would say so. You can't solve everything with improving your communication, but you can increase the likelihood of getting what you want.

Lenny Rachitsky (00:08:39):
Cool. Okay. Anything else along these lines of just things that are important to understand just broadly around communication, executive communication?

Wes Kao (00:08:46):
I think another big one that I teach in my course and really kick off with is practicing like it's game day, playing like it's game day. So I see a lot of operators who save their best behavior for executives only. So you know, they want to shine when they're presenting to senior leadership, but with everyone else, they're kind of calling it. And I just don't think that you're going to be able to get enough reps to actually get good at executive communication if you are only doing it with executives. Because many of us only present to execs once a month, right? Or a couple of times a quarter. And that's just not a lot of chance to practice. So really treating every single stakeholder as if they are important because they are, and you shouldn't be if you don't want to waste your CEO's time, you also shouldn't waste your cross-functional team members' time or your manager's time or your direct reports' time. So that's something else that I ask to keep in mind.

Lenny Rachitsky (00:09:39):
And maybe a last question before we get into the tactics. When people think communication, they think email, they think meeting presentations, things like that. How do you think about, when you talk about executive communication and communication in general, what's kind of the umbrella of things that includes?

Wes Kao (00:09:53):
Yeah, I would say broadly the two mediums are verbal communication and written. So verbal being meetings, conversations, presentations. And written being emails, strategy docs, notion docs, Slack messages, text messages, those two categories broadly. And I also think about communication as more of a means to an end, which might be interesting for some people because I teach a course on communication. So you would think that's like the end in and of itself, but I really see it as a means to an end where the end is getting the ideal outcome you're looking for. So whether that is buy-in or making a good decision as a team or moving to the next step, whatever that might be, communication is really in service of that end goal.

Lenny Rachitsky (00:10:43):
Awesome. Okay. So I made a list of people's favorite tactics and frameworks and approaches that you teach, and talking to folks that you've taught and folks that you've worked with. So I'm just going to go through a bunch and let's just help people get better at these things.

Wes Kao (00:10:58):
All right, let's do it.

Lenny Rachitsky (00:11:00):
Okay. So the first is something you call sales, then logistics. What is that about?

Wes Kao (00:11:07):
Yes. So a common mistake that I see is overestimating the amount of buy-in that you have from your audience. So that looks like jumping straight into talking about the logistics, the details of the how to do something, of the process. When in reality your audience has not yet decided if they even want to do the thing. So what I see operators do in response then is go even deeper into the logistics and the how, thinking that, "Oh, if I just explain this more than that person will want to do it." When really a sales note is different than a logistics note. A sales note is meant to get people excited to do the thing you want them to do, and to agree to do it. And only then after they have bought in, does it make sense to share the logistics.

(00:11:57):
So there's an order of operations here. If you switch the order of operations, you will likely get a slow response or just no response, right? We've all put a Slack message in a channel and got crickets and tumbleweed. So really starting off with selling the person and making sure that they know why we're doing this, why this matters to the company, why now, and then sharing the logistics tends to be a lot more effective.

Lenny Rachitsky (00:12:22):
Is there an example of that that might help illustrate that point or that approach?

Wes Kao (00:12:27):
Yeah. So one of my clients is a head of operations and she was trying to get the rest of her executive team, which she was a part of, to fill in some wins for the week so that they could share this out with the whole company. And this was going to be motivating, it was going to shine a light on folks. And she led with the logistics of which document to send, to put the details in, what time to put it in by, the format that you should put these wins and didn't really get much of a response from the leadership team, which makes sense, right? Because this totally sounds like one of those things that's another item to check off on your list when you already have so many other things to do and here's this other process that like we're all supposed to do now, like yay, right? And so she wasn't really getting response. And that's because she dove straight into logistics.

(00:13:20):
Whereas what she could have done is start by selling folks, selling the other executives on why are we doing this? Well, we're doing this because this is a chance to shine a light on your team members who are doing amazing work, for them to feel motivated and to feel like the rest of the company really sees them and understands what they're doing. And this is all something that is going to motivate your team, right? So sharing why this is helpful and useful and how this is in service of you and your team versus like, "Oh, this is a favor that you're doing for me to fill out this form and fill it out this way and by this date," et cetera, et cetera.

Lenny Rachitsky (00:14:00):
I know that execs often want the opposite where they're just like, "Okay, I know, just tell me what you want to do. Just like, okay, just get to the point. I don't want time for all this context and background." Any advice on when to spend any time on the sales? Like what are signs that, okay, maybe you don't have them sold yet, or what are maybe contexts where you should probably still try to sell them first?

Wes Kao (00:14:20):
Yeah. So I actually think that you should always do a little bit of selling even for situations where people have generally bought in. Because most of us have a lot going on and we're not actively thinking about whatever you're talking about. So even though I agreed to something two weeks ago, by the time you're telling me about it again, like I thought about a billion other things since then, right? So reminding me of why are we talking about this? Why does this matter? And then getting into it and framing that conversation upfront is way more likely for us to not get stuck in a cold start and not kind of go two steps back one step forward.

(00:14:55):
The other thing is, you can frame a conversation and sell a bit at the beginning very concisely. So I'm not talking about spending 15 minutes out of a 30 minute meeting selling, I'm talking about one to two minutes, even a couple sentences, and then transitioning into the main thing you want to talk about. So I'm a huge proponent of doing that and basically reminding people, why are we doing this? Why are we here today? Why does this matter? And then getting into the meat.

Lenny Rachitsky (00:15:24):
I love that. So basically you can do this really briefly, it doesn't have to be a whole pitch for half an hour. It's just a reminder, "Here's why we think this is important." And I think that's such a good point because a lot of times it's like a leader is looking at this thing you're asking them to do and they're like, "Why are we even, why am I spending time on this?" And just a reminder of like, "Okay, I see, I forgot this was going to be, this a part of our strategy, this has this much impact potential or here's how it could help our team be more efficient."

Wes Kao (00:15:52):
Yeah. And you can really do that in like 30 seconds.

Lenny Rachitsky (00:15:56):
Is there like a, I don't know, structure to this? Is it just like why? Is there a kind of a template you like or some way you recommend of selling first? Is it like, "Here's why we're doing this." Starting like that? Anything along those lines?

Wes Kao (00:16:09):
Yeah. I think explaining why we're doing this, why this benefits the business, what problem this is solving. Again, you can do a lot of this in a couple of sentences. And then I also like asking or stating what I need from the other person upfront. So saying, "Hey, we're here today because two weeks ago we were reviewing the product flow and realized that there were a couple of parts that were kind of confusing. So I took a stab at fixing those areas, rewriting the microcopy, and I want to present them to you today, see if you agree with these changes, and then we're going to roll them out. What I'm looking for from you is feedback on the changes and if you agree." So like that was like 15 seconds, right? Super fast. And then now we're all on the same page about why we're here. And you can listen more intently knowing that I'm looking for a certain kind of feedback.

Lenny Rachitsky (00:17:01):
I would love to hear it that way. I think there's like an implication here that maybe is worth sharing of just, a lot of this is about communicating effectively to execs, which will make you communicate better to most people. But especially with folks up the ladder. They don't have a lot of time, they have a million things in their head. Maybe just share like why this is so important, like what the state of mind of a leader is that you need to kind of break through.

Wes Kao (00:17:25):
Yeah. So I call it the yes, yes, yes, next, next, next mindset where if I'm listening to direct reports present something to me, very often I find myself thinking, "Got it. All right, yes, let's keep going." Right? And you know, on the other side of that, I've often presented to executives where I had a 15 slide deck and execs would do that and I'd be like, whoa, whoa, whoa. Like I have a whole sequence, I have a whole order, you know? And sometimes they would give me buy or make the decision by slide four, you know? And I'd be like, "Okay, well you know, slide 13, I want to show you this great graph I put together." Right? And what was really helpful for me was realizing that I should take the win. Okay, if five seconds already agreed, take the win and keep it moving, move on.

Lenny Rachitsky (00:18:13):
Yeah. What's that quote like? "If you've sold them, stop talking."

Wes Kao (00:18:16):
Right. Yes. Yeah, you might talk them out of agreeing.

Lenny Rachitsky (00:18:20):
Yeah. Okay. You mentioned being concise. Let's talk about that. You have some really good advice on just how to effectively be concise and not too concise. What's your advice there?

Wes Kao (00:18:31):
Yes. One of my pet peeves is when people are too concise and they equate being concise with brief, being brief. And being concise is not about absolute word count, it's about economy of words. It's about the density of the insight that you're sharing. And so you can have a 300 word memo that's meandering and long-winded and a thousand word memo that is tight and concise. And so not equating concision with briefness I think is a really big one to understand.

(00:19:05):
The second thing is a lot of advice about being concise, I think misses an important point. So we've all heard, "Don't bury the lead, cut to the chase." Main point, put the main point at the top, bottom line up front, right? And all of these pithy aphorisms assume that you actually know what your core point is. So you can't cut to the chase unless you know what the chase is. You can't unbury the lead unless you know what the lead is. And so that I found is the bottleneck to being concise. It's actually not really being clear of what you are thinking, that's what's leading to being long-winded.

(00:19:49):
And you can kind of test this theory because most of us have a go-to story that we've told a bunch of times, right? We're like, you know exactly when people are going to laugh, you know when they're going to gasp or hold their breath, right? And why are you so good at telling that story and why are you so concise about it? Because you've told it a bunch of times, you know all of the beats. So in meetings though, at work, we are very rarely talking about the same thing that many times it's always something new. It's something that we are also probably likely processing ourselves and are in the midst of processing as we are in a quick turnaround time, telling someone else about it, telling our team about it. And so you are basically asking your brain to do a lot of different processes, especially in a real time conversation. You're listening to the other person absorbing, making sense of it, processing it, figuring out what you think and how you would react.

(00:20:39):
And then trying to say something cohesive that makes sense, right? And then trying to be concise about it. So it's just a lot of different processes. And so the only solution I found consistently to being concise is preparation. It's not a very glamorous solution by any means, but the clearer I am going into a meeting, going into a conversation, going into a pitch, the better I am at being concise and being able to bring the conversation back to the most important points at being able to stay flexible, but also firm and preparation. I don't mean spending hours and hours preparing for a weekly meeting, even a couple of minutes really makes a huge difference.

(00:21:25):
Most of us are so back to back in meetings that we're doing zero preparation. It's like the meeting has started 30 seconds in and you're still unwinding from the last Zoom call that you were on, right? So most of us are in that mental state. So if you even take 30 seconds to one minute to ground yourself on why am I in this meeting? What do I want to share and make sure I get across in the time that we have, you're going to go in there so much more focused and so much more able to be concise.

Lenny Rachitsky (00:21:51):
So the advice there, so this is for meetings and I want to talk about writing also, but for meetings, the advice here is before you get into a meeting, actually think about why am I in this meeting? What do I want to get out of it? Instead of in the meeting figuring out a lot as you go, which to your point, you're just going to ramble and be like, "Oh, okay, here's what I actually want to say."

Wes Kao (00:22:10):
Yeah. And what might I want to share in the meeting too? You know, especially for more introverted folks. Sometimes you need to decide beforehand that you want to speak and you want to make sure you get a certain point across. So even deciding that beforehand makes a huge difference.

Lenny Rachitsky (00:22:25):
Yeah, I found this extremely powerful just like five minutes before you get into a meeting. And it could happen earlier in the day, right? It doesn't have to happen right before the meeting, or worst case, it's right before the meeting. Just, "Okay, what do I want to get out of this? What am I here? What do I want to say?" And just like giving your brain a little bit of time to prepare. Super powerful. In writing, is there like any tactics you can share for someone to be a little more concise?

Wes Kao (00:22:50):
I think the main tactic is to remind yourself to be concise. And usually when I do that, I end up trimming 20% at least of what I wrote, tightening up some sentences. I also ask myself, how might I be adding cognitive load to whatever it is that I'm saying? So is there a tighter, clearer, cleaner way that I can ask what I'm asking or present the information I'm presenting or make the recommendation that I'm making? And usually if you even ask yourself that, your brain automatically comes up with stuff. You just see whatever you wrote differently and you're like, "Oh shit, I could trim this entire paragraph because that's secondary." And maybe you have your primary message in Slack, and then within the thread add some of the secondary stuff, right? So I find that most of us, it's reminding yourself to be concise. And once you think of it, your brain naturally will see places where you can trim.

Lenny Rachitsky (00:23:50):
There's a layer of advice under this that you're not saying that I'm going to say, which is actually look at the thing you wrote at least once before you share it. Because I used to be really bad at this. I just like, "Okay, I don't have time. I wrote this doc, send it, get feedback.

Lenny Rachitsky (00:24:00):
... really bad at this. I just like, "Okay, I don't have time. We wrote this doc, send it, get feedback. All right. Send this email. I don't have time to read this email." And I find just forcing yourself to look at it solves so much of this.

Wes Kao (00:24:10):
Oh, yes, yes, definitely. I was assuming before doing that, but you're right, some people might not be. And yes, definitely reading your own message first is huge. And yeah, I find that even doing that you can often spot a lot of low-hanging fruit.

Lenny Rachitsky (00:24:31):
Right. You'll find the typos and grammar issues and you'll be like, "Oh, I don't need this word." Along those lines, let me share two books. People always ask me, "How did you learn to write?" I'm like, "I'm not a writer, I don't know what I'm doing." But two books really helped me write more effectively. And one is specifically to help you write more concisely called On Writing Well. I don't know if you've read that.

Wes Kao (00:24:51):
Yeah.

Lenny Rachitsky (00:24:52):
Okay. And it's basically chapter after chapter of, "Here's what you can cut. And you can cut more. And look what more you can cut and cut this stuff." And he has screenshots of essays that students have written in his class and he's like, "Look at all those words you cut and nothing has changed. It's exactly the same message and even is better with 40% of the words cut."

Wes Kao (00:25:12):
Is this by Sol Stein or another author?

Lenny Rachitsky (00:25:16):
I don't have it... It's somewhere in my bookshelf. So we'll look it up.

Wes Kao (00:25:19):
Yeah, there's a writing book by Sol Stein that I absolutely love. And I feel like it might be called On Writing Well, but then also I could see there being multiple books called On Writing Well.

Lenny Rachitsky (00:25:29):
There's also Writing Well I think by Stephen King, that's another one that people love, but there On Writing Well is the one I really loved because it's very tactical.

Wes Kao (00:25:37):
Going back to something that you were saying earlier with rereading what you wrote, I think the blast radius of a poorly written memo is way bigger than most people think. So if you're just shooting off a message in a Slack channel with 15 other people and it's confusing and you didn't include information you should have included, there's going to be a bunch of back and forth. All 15 of these people are reading this being like, "Okay, what do I do with this?"

(00:26:05):
Whereas if you had just taken another look at it, those 15 people would be off to the races. They would've read your message and then known exactly what to do next or what their part was or what you were looking for from them. So I think about that a lot too. It's not just me writing this and sending it off. It's, "Who are all the people who are going to come in contact with this message who are going to refer to it and use it? And if I just take 30 more seconds to make sure that it's clean, how much can I unblock from their work?"

Lenny Rachitsky (00:26:34):
That's such a good point. I like that, I love that term blast radius. It's such a good point. Just like there's so much negative leverage in writing inefficiently and inconcisely. If you spend like... Inconcisely? I don't know the word is there, but if you just spend three minutes spending a little more time making it more clear just like the impact and leverage that has, that's such a good point. I looked up the books, it's so funny. Okay, so there's On Writing Well by William Zinsser. There's Stein On Writing by Sol Stein, which is what you said you were talking about. And then Stephen King has a book called On Writing. Everyone's got the same.

Wes Kao (00:27:09):
Yeah. Common title.

Lenny Rachitsky (00:27:12):
Not ideal for SEO but On Writing Well is the one that I love by William Zinsser. There's also one called A Series Of Short Sentences if you haven't seen that one. It's a really good rate too. It's just how to write short sentences and just the power of just keeping sentences short, which I struggle with.

Wes Kao (00:27:27):
Yeah. Yeah, I like that.

Lenny Rachitsky (00:27:28):
Okay. Back to our agenda. There's another framework/tactic that I've heard you recommend. It's called signposting. What is signposting?

Wes Kao (00:27:38):
Signposting is using certain words, phrases, formatting, and an overall structure in your writing that helps guide your reader and signals what is coming in the rest of the post. So, this is especially helpful if you have a long memo. It adds structure to where are we going and what certain sections of paragraphs are about. So some of my favorite signposting words are, "for example," shows that you're about to show an example because shows that you're about to share your logic and rationale behind something. "As a next step," is a great one. People's eyes automatically zoom to, "as a next step." Even "First, second, third," kicking off a paragraph with that, you're not needing to rely on rich text formatting with bolding, italics, underlines and all that craziness. If you kick off sentences with signposting words, you can often signal, "Here's what I'm about to talk about in this paragraph."

Lenny Rachitsky (00:28:41):
These are power words for clarity. There's this whole concept of power words like, "free."

Wes Kao (00:28:47):
Yeah. "A gift."

Lenny Rachitsky (00:28:48):
"Gift." Yeah. For copywriting and these are basically power words for helping your brain see the structure and get to the thing you want to pay attention to. So I'll read back the words you just used. "For example," " because," "as a next step," and then, "first, second, third."

Wes Kao (00:29:05):
Yeah. Yeah. You can use signposting in writing and verbally too. So if you're doing a product demo, you might say something like, "The most important part to pay attention to is, blank." Or, "The part that we were most surprised by is, blank." Or, "The part that customers are," et cetera. Right? So it's, you're signaling that whatever comes after this thing is something that you may want to pay attention to. So it's a great way not only to add structure, but to also grab people's attention back if it has strayed some time as they were either listening to you or reading.

Lenny Rachitsky (00:29:42):
Along those lines, I find I find formatting really helpful here, just bold and bullets. I know you have a pet peeve with too much formatting. How much is too much formatting?

Wes Kao (00:29:51):
I really hate excessive formatting. So, I've seen memos where 30% of the note was bolded. And that just negates the entire point of bolding because if everything is bolded then nothing is being highlighted, right? So I think using formatting in general more sparingly than you think you have to is probably a good rule of thumb. I also dislike when people overuse bullets and sentence fragments, phrases in bullets when they should use complete sentences that actually show the connected tissue between ideas, that show the logical flow of what it is that you're saying.

(00:30:33):
And it feels faster and more concise to put bullets and fragments, but a lot of times your reader on the other end of that is needing to decipher and interpret and guess what you actually meant. So it net, net takes longer. And I also think that it can be a little bit of a crutch, it can be a little bit lazy because you are telling yourself that you're being concise when really, if you had to turn your sentence fragment into a full sentence, a lot of times it actually is harder than you think because you realize that you actually didn't really know exactly what you meant. So as you're trying to turn it into a full sentence, you're actually needing to use brainpower.

(00:31:15):
So that's I think a great litmus test of, "Was that idea fully thought out?" Because if it was, you should be able to really quickly turn it into a complete sentence. And many times, you actually aren't. So I see people like basically think, "Oh, I want to make this easier to read, more skimmable. I'm just going to throw a bunch of formatting and bullets and turn everything into bullets." And it's not quite that easy of a solution.

Lenny Rachitsky (00:31:41):
This is very much along the lines of the whole Amazon six-page memo where Jeff Bezos just realized, "If you can't write it out as a long memo and explain yourself in prose, you don't actually know what you're saying." And it's a really good filter for helping people actually crystallize and know themselves, "Okay, I see. I don't actually know what I'm doing here." And I love this is a microcosm of that. Can you just make a bullet point a real sentence versus a fragment of a sentence?

(00:32:06):
I'm thinking about as a listener being like, "Okay, how do I actually get better at this?" So maybe let's take a tangent. I know that you teach a whole course, you do all this stuff hands-on with people to help them actually build these skills. For someone that hasn't taken the course or isn't taking it, what's a good way to start practicing these skills and know if what you're writing is getting better, is good. Is it find a mentor, find someone that you think is a great writer and have them review stuff? Any tips there?

Wes Kao (00:32:34):
Yeah. So I have a pretty first principles driven approach for this, which is to think about how long does it take me right now to get to the reaction I'm looking for from my recipient? If it takes a bunch of back and forth and a bunch of friction, then that's my baseline. And once you start practicing some of these communication skills, how does that speed up? If you would have had seven different touch points of back and forth, does that shrink to two to three?

(00:33:08):
Not every point of friction is going to be avoidable, but a lot of it is if you get better at communicating. So I like watching for the reaction and how quickly and how enthusiastically I'm able to get that reaction. And for the things that are working, do more of that. For things that are not working, adjust your execution because it might not be that the tactic doesn't work, it might be your execution of it wasn't great. And keep trying, basically.

Lenny Rachitsky (00:33:35):
So the advice here is just see how well you're writing/meeting/suggestion goes, how well it does. And if it's not like there's the ideal immediately, "Yes, let's do it." And then there's the, "I don't really understand." There's the spectrum of response. And what I'm hearing is just pay attention to if the speed to getting what you want is increasing in general.

Wes Kao (00:33:59):
Yeah, yeah. I don't think that there's any single shortcut on how to get better besides that. I do think that being fascinated by a topic and being excited about it makes it more likely that you're going to find it fun to try all these different things and try different ways to get through to people. So, I would approach it with a hypothesis-driven experimental mindset and almost like a game. Like, "When I do this, how does that other person react? If I frame it this way, do I get a different reaction? When I try this, am I able to cut through the noise more?"

(00:34:39):
Yeah. So I really think it's about practicing. And I will say that the way not to do it is to try to incorporate 30 different tactics at the same time and then beat yourself up when you don't remember to do them. It's really easy when you are learning a new field or function to get overwhelmed when you're learning a new skill. And the way to build a habit is usually not changing so many different things at once. It's picking one thing that you want to try and keeping that top of mind, trying it in a bunch of different settings in different ways. And getting it better at that thing before moving on to the next thing.

(00:35:19):
So that's like a really common thing I see in my course is people feeling overwhelmed. And I always remind folks that, "You are building a new habit here. And be patient with yourself, take it step by step."

Lenny Rachitsky (00:35:31):
There's a lot of stuff we're talking about here that a lot of people might be like, "This is so minor. What? I just bullet point sentences, be a little... Tell them the why at the beginning."

(00:35:41):
And I just want to share in my experience the biggest jump I made in my career was actually getting better at these very specific skills. I had this manager, Vlad, who's been on the podcast and I talk about him regularly, who was such a stickler about communicating well and being very clear and concise and thinking and just spending more time on documents and emails, on strategy docs. Just like, "No, this isn't ready. Spend more time, here's something that's not clear." And just doing that was such an accelerant for me.

(00:36:12):
And it's all these little things. That's what's interesting about it. It's like everything seems really minor but it all adds up to a lot of impact because to your point, people see it, "Okay, cool, I get it, let's go." Versus like, "I don't like this idea." And then it's like it all falls apart. So I guess any reactions to that?

Wes Kao (00:36:29):
Yeah. All these little things compound and make a big difference. I often hear people think, "Well, this individual instance, this individual email, the Slack message is not worth spending a couple more minutes on. It's just an email or it's just a Slack message." The problem with that line of thinking is that no one instance of something is ever going to feel important enough to spend a little bit more time on that. And then, but when you zoom out, that's like, "Well that's all your work then. This is literally everything you've touched. This is all your work output then." because any piece of that process you thought wasn't worth spending time on and now this is just the quality of your work and it's not as good as it could be.

(00:37:15):
So yes, these might seem minor but A, it compounds. And also B, all the "big things," everyone else is already doing. So, there's not a lot of alpha in that. Whereas if you are paying attention to skills that people think are boring or too basic and realizing that's a lever that you can pull, that someone else thought, "Oh, we're hitting diminishing returns on that. I'm not going to spend more time on that." But you realize that there's actually more juice left to squeeze there and you decide to squeeze that juice. Well, now, you have extra juice that the other person doesn't have.

(00:37:56):
So yeah, in my experience I find that people claim the point of diminishing returns way too early. And this isn't just for communication, this is for strategies, tactics, et cetera. They'll try something once, a mediocre attempt and be like, "This channel doesn't work. This tactic doesn't work." It's like, "Really? Because it's working for a lot of other people who are getting really creative with it."

(00:38:19):
I'm not saying that everything has to work for you but for you to claim, "This thing just doesn't work," feels a little bit intellectually dishonest. It's more likely that your skill level, your creativity, your execution ability was not good enough. And that's fine. Let's admit that to ourselves because if we admit that, then we can do the hard work of getting better at those things.

Lenny Rachitsky (00:38:42):
It feels like if you really boil this down, all the advice comes down to just spend a little more time on all these things you're putting out.

Wes Kao (00:38:51):
I like thinking about it as a little bit more upfront investment. And it is an investment. It's not just time. It's an investment because yes, it takes a little bit longer to make a Slack message a little bit better, but net, net if you save a bunch of questions and back and forth and people asking you things that you don't think they should be asking, then by investing a little bit of upfront effort, you've prevented all that from happening. So yeah, it is a little bit more time in the moment but reaps a lot of benefits down the line.

Lenny Rachitsky (00:39:25):
Today's episode is brought to you by Coda. I personally use Coda every single day to manage my podcast and also to manage my community. It's where I put the questions that I plan to ask every guest that's coming on the podcast. It's where I put my community resources, it's how I manage my workflows. Here's how Coda can help you. Imagine starting a project at work and your vision is clear. You know exactly who's doing what and where to find the data that you need to do your part. In fact, you don't have to waste time searching for anything because everything your team needs from project trackers and OKRs to documents and spreadsheets lives in one tab all in Coda. With Coda's collaborative all-in-one workspace, you get the flexibility of docs, the structure of spreadsheets, the power of applications, and the intelligence of AI all in one easy to organize tab. Like I mentioned earlier, I use Coda every single day. And more than 50,000 teams trust Coda to keep them more aligned and focused. If you're a startup team looking to increase alignment and agility, Coda can help you move from planning to execution in record time. To try it for yourself, go to coda.io/lenny today and get six months free of the team plan for startups. That's C-O-D-A.I-O/lenny to get started for free and get six months of the team plan, coda.io/lenny.

(00:40:42):
You mentioned Slack. I have a great quote also about you that I didn't read that I'm just going to read right now from someone that worked with you. She said she searched the Slack channel at the company you worked at for old posts from Wes for inspiration for what to ask you. And she said you had zero half-baked thoughts, 100% complete sentences, perfect punctuation, clear takeaways at the top of every message. It's the kind of thing you don't notice in isolation, but once you see everyone else's messages in a remote-first company, it's a stark contrast.

Wes Kao (00:41:14):
Yeah, thank you. I will also say that as someone who tries to walk the talk, I feel like I get a pretty good response rate pretty quickly for the things that I ask for, for the recommendations I'm making. It's not instant, it's not 100%, but over time I've realized that improving my communication has led to people receiving my ideas better. Ideas that used to be locked in my head that I would get frustrated that no one else understood. People were now understanding and that feels really good. That's very, very exciting and it made me want to do it more and pay more attention to that. So that's going back to what I said earlier about watching for what's working. There's momentum is really encouraging.

Lenny Rachitsky (00:42:01):
And I totally feel that. If you start getting the things you want, that feels great. I'd be like, "Okay, cool."

Wes Kao (00:42:08):
Yeah, more.

Lenny Rachitsky (00:42:09):
"Let's do more of that." Yeah, and again, it's like very minor things. It's like a couple more minutes on the Slack message, a couple more minutes on email.

Wes Kao (00:42:16):
Very doable.

Lenny Rachitsky (00:42:17):
Yeah, which everyone can do. There's no magic here, it's just spend a little more time and use some of these tactics that we're talking about. Speaking of that, let me talk about another tactic. Apparently you have some really good advice on finding the right level of confidence in what you're saying. There's always this question of, "I come to this leader. How confident should I be about, 'This is the answer,' versus, 'Here's a bunch of ideas'?" What do you think? What's your advice there?

Wes Kao (00:42:41):
I find that people tend to naturally be on the spectrum a little bit too confident as a baseline or not confident enough. So people who are too confident might state hypotheses as if they are fact. So that really bothers me. That's another one of my pet peeves, where if you say, "This is X," or, "This will X," that is different than saying, "This could X," or, "This might X," or, "This will increase the likelihood of X."

(00:43:12):
So I'm a big proponent of speaking accurately. You can avoid a lot of problems if you speak accurately about your level of conviction and about the actual amount of evidence that you have for something. It's okay for something to be an initial hunch. Say, "It's an initial hunch." Don't act like this is something that you are super sure about. You've proven out that this is absolutely this way because the rest of your team is listening to you at face value. And y'all might spend real headcount and dollars pursuing something that you have advocated for in a way where you overreached with your level of confidence.

(00:43:52):
So, that's for people who are overconfident. It's equally a problem if you're under-confident. So I have some clients who their CEO asked them to share some recommendations with another team because they've run something before and so they share all this amazing information and at the end they're like, "Oh, but you can ignore everything I just said. Obviously, make your own decision. Do what you think is best. And if you want to just ignore everything, that's totally cool too." And it's like you just didn't have to say that. You could say, "Make your own decision, take all this into account," but you don't have to diminish to that degree.

(00:44:31):
And so again, speaking accurately, if you have really strong reasons to recommend something to the cross-functional team, it's almost irresponsible to act like you are not really sure and it's just this random idea, "Hey, try it if you want to." We might lose a lot of money and time if we don't take this idea, right? So again, speaking accurately is so, so important.

Lenny Rachitsky (00:44:56):
Is a simple way to think about then the right balance is have a point of view, have a recommendation, present accurate facts, and be clear when you are not? "It's not actually 100% true, but here's a hunch I have, or here's a theory we have."

Wes Kao (00:45:11):
Yeah, I think sharing a point of view, sharing a recommendation, and then backing it up with evidence, with logic, with first principles, with examples, with data, if you have it. Not every situation you're going to have data for, especially if you're building something new. So this is where first principles comes in. Even explaining how you got to where you got to and why you think this is going to work, that all gives your team, your manager, something to push back on, to poke holes on or to align on and say, "Yeah, I agree here, but I disagree on this part."

(00:45:44):
So you can talk about ideas with a lot more specificity when you share your thought process. And you can frame it all kicking off saying, "My initial thinking is," or, "Based on what we know, my hunch is, blank." So speaking accurately and then still bringing up those facts so that we can all make as informed of a decision as we can make given what we know.

Lenny Rachitsky (00:46:07):
Advice I got that really helped here for me was to try not to be biased with how you frame everything. You have your suggestion for how to do something. It's easy to just bias all of the data to point in that direction. And if people notice that, they're like, "Oh, okay. Well, I can't really trust this because I see you're just like, you clearly have an agenda." So it's a little bit like having an agenda and a POV, but be clear about what is actually true. Be accurate.

Wes Kao (00:46:36):
Yeah. I think anytime people have to discount what you're saying because you are biased in this way is not great.

Lenny Rachitsky (00:46:45):
Is there an example by any chance that highlights what you're describing here?

Wes Kao (00:46:49):
Yeah, so in my course I talk about not being a single-minded martyr. So single-minded martyr is someone who very much has an agenda, who wants the recommendation to go through and is presenting a bunch of evidence, supporting that direction. And then gets really frustrated when other people are not seeing it or are skeptical. And so one of my clients was a single-minded martyr in a recommendation she was making. So she was on the growth acquisition side of her company. And was having trouble with cross-functional team members lending headcount to her project. And so everyone would say like, " Oh, yes, we believe in this, this is important," but wouldn't want to actually give her half of their engineer for two weeks.

(00:47:36):
And we were talking about it and as we were talking, she revealed that the CEO had at the beginning of the year said that the company-wide goal is retention that year. That their biggest challenges and areas of opportunity were in retention, not necessarily in growth. And once she zoomed out and realized this, she was able to put her recommendation in context. And realized that it's not just-

Wes Kao (00:48:00):
... recommendation in context. And realize that it's not just I'm the only one who cares about this company. Everyone is a hypocrite. They say they believe this, but don't actually want to work on it. Before that was kind of her narrative, but once she zoomed out and realized she was being a single [inaudible 00:48:16], she could better fit her proposal in the context of what else was happening in the organization. I think actually this is a really big difference between more junior people versus more senior people. More junior people are like, "I need to win. I need to get a yes for this proposal and I'm going to keep advocating for it until I get a yes." Whereas really sometimes the best decision for the company is not right now. This doesn't actually fit our priorities right now, right?

(00:48:42):
Or maybe yes, but let's right size the level of investment. So it might look like half whatever the size of what that recommendation actually was, and having the maturity to realize that, to put your idea into context is huge. That took me a really long time to learn and I think that goes under the umbrella of always do what's best for the company, not necessarily what's best for me, my career, my team, my wins. If you prioritize what's best for the company, that helps you have a more right-sized way of still advocating for your ideas, but doing it with a bit more equanimity.

Lenny Rachitsky (00:49:26):
And also just connecting to what the company is. Just this idea of if the thing you're pitching is not aligned with what is important to the company right now, it's unlikely to be prioritized. It makes sense. This is why leaders choose, here's what matters most. We got to do the things that are going to help us drive this thing right now, like retention or revenue. And so that's just, I think, a sub tactic there is just whenever you're pitching something, connect that to the goal of the person you're pitching to so that they're like, "Oh, I see how this is going to help me. That's great. Let's do it. Great advice."

(00:50:01):
And I think this is something a lot of people run into. It's just, "Why aren't they listening to me? Why don't they want... That's such a good idea. They hate me." It's something, "Oh, I bet they hate me. They don't trust me." When it's just like, okay, this isn't a priority right now. Let's come back to it another time. Okay. I'm going to get to a couple more tactics and then I'm going to shift directions to talk about managers and being manager. You have an awesome framework called MOO. What is MOO? What does it stand for and what is it all about?

Wes Kao (00:50:26):
MOO stands for Most Obvious Objection. M-O-O. And the thought there is that a lot of times we're surprised by the questions that we get, especially in meetings where we feel blindsided, that was unexpected, and then we're on our back foot. When really, if you thought for even two minutes about what are obvious objections that I'm likely to get when I share this, you often immediately come up with what some of those things are. So are you going to be able to anticipate every single objection? No. But can you anticipate the obvious ones? Absolutely. And so this is where knowing your own argument in and out, including counterarguments becomes so important. So knowing your counterarguments as well as you know the arguments for doing the thing. When you do that, when you have prepared in that way, you're less likely to feel caught off guard.

Lenny Rachitsky (00:51:23):
When you hear you talk about this, it's like, obviously I shouldn't do this, but very few people actually do this, actually spend a couple minutes, " Okay, here's what I'm going to pitch."

Wes Kao (00:51:31):
Even a couple seconds, really. Really, even a couple seconds, your brain will think of something.

Lenny Rachitsky (00:51:38):
Is there a story or an example of this that you share that highlights this idea of the power of MOO?

Wes Kao (00:51:43):
I use MOO multiple times a day, every day, every single day. Literally whatever I'm about to say I think how might someone disagree with this or what might an objection be? So whatever it is I'm writing, saying, it's a really good mental filter because it encourages you to think a couple steps ahead in kind of a structured way, right? If I'm about to say this, the person may then say this to me. Well, if I take that into account, I can volunteer that information upfront or I can frame it in a way where they're less likely to think that that's an issue.

(00:52:19):
And so it's muscle memory for me at this point, and this might be something we include at the end is something to start with. But putting MOO on a post-it, Most Obvious Objection, what is someone likely to object about? And then just keeping that top of mind. It's a great way to train yourself to empathize with your audience and with your recipient. We all say that and we all know we should do it, but for me this is a really tactical concrete way to do it.

Lenny Rachitsky (00:52:50):
I think what's great about a lot of the tactics you're sharing is not only is it going to help you communicate it better, but it helps you actually think and crystallize it better for yourself because you may realize, oh, that's a really good objection. Like, oh, the objection's probably going to be this. Will it drive enough impact for the business? Oh, that's a great point. Maybe I should not pitch this right now.

Wes Kao (00:53:10):
Yeah. It definitely helps shape your own thinking. I think communication and thinking are so much more interrelated than we think. I think people think there's a thinking as phase one and then communicating the thinking, and the reality is a lot more intertwined. And I loved your example there that thinking ahead to what might be the most obvious objection actually then prompts you to realize that maybe there was a gap in what you were planning to present and then you now have an opportunity to strengthen that pitch before you say it out loud.

Lenny Rachitsky (00:53:45):
There's a quote I have highlighted on this podcast a number of times that I love that is exactly along these lines by Joan Didion. "I don't know what I think until I write it down." I know exactly that feeling. Okay. So there's a couple more things that people have shared that you are amazing at helping them get better at. One is just keeping your cool and staying calm during very high stakes, real-time conversations when things maybe aren't going your way or if you disagree with someone, any advice on that, it feels like you're really good at this.

Wes Kao (00:54:17):
I think one thing that tends to throw people off is putting a lot of pressure on themselves to get the exact right answer. So if they are asked a question and they don't know the answer, a lot of people will then kind of freak out. And I was taught early in my career that if you don't know the answer, you should say, "Let me look into it, I'll get back to you." So that's a fine approach. It's definitely better than making something up, right? So definitely don't make something up. But if you are more experienced and have some confidence in your subject matter area, just saying I'll get back to you, is sometimes a missed opportunity. You can ask for a bit more information to be able to continue the conversation in that moment. So let's say that your exec says what percentage of users came from mobile last month and you don't have that number off the top of your head.

(00:55:20):
So person A says, "Let me look into it and I'll get back to you." Person B might say, "I don't have that number off the top of my head, but in the last quarter the number has been 60 to 70% and it's grown in the past year, so mobile is now a bigger part of our business, et cetera. Are you wondering if we are investing in mobile appropriately or where's that commission coming from, basically? Right? And so being able to answer a similar question in the direction you think the person is asking about and then validating why they're asking that question allows you to still continue that conversation in the moment. I call it the question behind the question, sometimes you get a question, but underneath there's a deeper underlying concern.

(00:56:10):
And many times people don't even know that it's there, right? Subconscious. So it's not nefarious, they're not withholding anything from you. But when you are explaining something and you're kind of getting multiple questions on the same thing, it's a good sign that there might be a deeper question behind the question and it's our responsibility to figure out what might that be. And so probing, asking for a bit more information, answering in that general direction and then validating these are all techniques you can use when you are in the moment without feeling like, oh, I must have every single thing prepared and the moment that I'm caught off guard, everything goes to shit.

Lenny Rachitsky (00:56:49):
Another tactic along these lines that's very similar to what you're describing, but I'll share that I learned that was really helpful is just if you're not sure what to say, basically just reflecting back their question and just being like, let me just make sure I understand what you're looking for. You want to understand monthly retention for, and then maybe clarify. And that one gives you time to think about it as you're talking. Two, it helps the person recognize, "Oh, he hears me. Great. Okay, this is good. He's thinking about this." And then at the end of that you could be like, "Okay. I don't actually have that specific number. Let me think about it." Or, "I have the quarterly number. Okay. That's what I know." So there's an interim step almost that I'll add into your piece of advice of just reflect back their question, just better understand what they're looking for.

Wes Kao (00:57:32):
Yeah, I love that. Mm-hmm. Mm-hmm.

Lenny Rachitsky (00:57:34):
Awesome. Okay, let's go back to what I said we do. Let's pick one tactic that you think people should try first, maybe one or two. So let me read the ones we've gone through and then see what you think would be a good first step. So one is starting with sales, before getting to logistics and giving people the why signposting using specific words to help people guide the doc and not get overwhelmed. Finding the right level of confidence, having a POV, that sort of thing. Getting better, being concise, MOO, not overusing formatting, something else you shared. And then this idea of when you don't know the answer, not saying I'll get back to you as the default, maybe giving them a different answer, maybe asking them more questions. Across those, which do you think someone should try to like, "Okay. Let me start here."

Wes Kao (00:58:25):
I would start with Most Obvious Objection and also framing your conversation up front. And that kind of relates to using signposting words if needed to help you frame that conversation.

Lenny Rachitsky (00:58:37):
Sweet. That's such an easy one to remember. Just MOO. Okay. So stick a post it somewhere when you're about to share something in Slack and ask someone for something, present in a meeting, send a strategy, and just think about for a few seconds what might be the most obvious objection to what I'm trying to ask them to do. Great. Okay. So let's talk about management. And there's kind of two sides to it. Being a manager and being a person reporting to a manager, you have a bunch of really good advice here. One is there around managing up. One of my most popular posts in the early days was advice for managing up and just how important it is. What advice do you have for someone to get better at managing up? Why is that even so important? Why do you think people may be under appreciating how important it is to manage your manager, let's say.

Wes Kao (00:59:18):
One of the most common myths about managing up that I definitely felt early on in my career was that I would have to manage up if I were more junior, but eventually I would outgrow it, that I would get senior enough that I would no longer have to do it. And it was a rude awakening that no matter how senior I got, managing up, I not only had to manage up, it actually became more important. So I think managing up is one of those skills that if you invest in learning it, it serves you now and for the rest of your career. And I realize that many senior people are actually the best at managing up. That's partially how they got to be so senior in the first place. But also, the more senior you get, the less likely that your manager is going to give you really well-defined tasks and problems on a silver platter and ask you to solve them.

(01:00:09):
You are going to be dealing with more ambiguity and you're going to be dealing with sometimes a mandate like make this number go up or create this division, right? Where you need to manage up and make sure that your leader, your manager, is in the loop about what you are about to try and what you're about to do and make sure that they're aligned. And so for me, realizing that managing up is something that is ongoing and that it shifts and evolves and looks different as you go in your career, that was a big unlock for me.

Lenny Rachitsky (01:00:44):
Just that even if you become even a VP, if you become a director and still something you want to invest in, any specific tactic or advice for how to manage up well.

Wes Kao (01:00:54):
The biggest one is to share your point of view. So this some people are surprised by because they think I'm going to say do a weekly recap of the tasks that you worked on or what you contributed. And that is a good idea, if you want to do it, you can do it. But I think the more highly leveraged way to contribute and manage up is by being more vocal about sharing your point of view. When you just ask your manager, "Hey manager, what should we do?" You're putting a lot of cognitive load on your manager to need to think about the problem, think about potential solutions, craft the solution, and then tell you what to do. Whereas if you instead said, "Hey manager, here's what I think we should do. How does that sound? Where do you see gaps? Am I thinking in the right direction?" You give them something to build off of and that reduces the amount of mental lift that they have to put forth.

(01:01:54):
And so sharing your point of view more readily, backing it up with evidence, that's a wonderful way of making your manager's life easier. And also showing that you are an active rigorous thinker who is thinking strategically about the business. You're not just waiting to be told what to do, you're not expecting them to figure things out and then tell you you are actively looking around the corner trying to solve problems, forming hypotheses in your mind, observing and noticing things. And again, sharing your point of view doesn't mean that you have the perfect answer. You can share that, "Hey, I've noticed this problem popping up in a couple of different places. Here's what I think might be happening."

(01:02:36):
Or when you share a report, don't only share the report and expect your manager to come up with insights and takeaways. You should look at the report too and point out insights and takeaways. So it's really changing that posture from more reactive and more waiting to be told what to do or kind of staying in this narrow box to being willing to share your recommendation, your point of view, share what you're noticing, and this is something that even junior people could do.

Lenny Rachitsky (01:03:04):
I was going to say exactly that. I think not only is it something junior people can do, this is a really good way to get promoted and to take on more leadership opportunities. You coming to your manager with, "Here's something I think we should do. Here's a perspective I have. Here's an opportunity." If you were in charge, you're like, how awesome would it be for people to come to me with amazing ideas and have clear recommendations? That sounds great. Everyone wants that. So if you can do that, amazing. Who wouldn't want that? But then what's interesting is similar to how writing helps you crystallize your thinking, you coming in with a recommendation forces you to really think deeply about it because that's putting your reputation on the line. So there's a second order effect of it makes you actually spend more time on the thing and be clear about why you think this is a good idea and do more research. So a lot of wins here.

Wes Kao (01:03:53):
There are a lot of situations where you might have the most visibility into a problem. You might have the most proximity into an issue. And so if you're not speaking up about it and sharing what you're observing, sharing what you're noticing, your manager doesn't necessarily have visibility into that. And so I've heard so many managers say that they want their junior people to speak up more because their junior people have often close contact with customers, with support tickets, with cleaning data, with a bunch of things where the manager would love to hear insights from that.

Lenny Rachitsky (01:04:32):
If you're not having success with this, if you're hearing this and be like, but it never worked, my manager doesn't listen to me, listen to the rest of this podcast we just did, which is basically advice on how to effectively convince someone of a thing. It's like, tell them why this is a problem, be really concise about it, sign post words, all these things. That's exactly what this whole conversation's been about. Okay. Let's see. We have a couple more really cool tactics that people have suggested we talk about. One is how to give feedback well, how to do better, how to be more effective at giving feedback. What's your advice there?

Wes Kao (01:05:05):
I have a framework called strategy, not self-expression. And so the idea here is that most of the time, by the time we are giving feedback to someone, we have been frustrated for a while. I used to be very conflict diverse, so I would wait and try to convince myself that I wasn't bothered by something until I really couldn't hold it in anymore. Then I would schedule a one-on-one with a coworker to tell them the feedback and it would inevitably turn into a venting session where I was in the name of sharing the impact of what they did would share all my frustrations and all the ways that they have basically harmed me and made my life difficult. And this would be very counterproductive because the person would either feel like and feel really demoralized or they'd get really defensive and they'd want to argue with me about how what they did actually was not that bad or it was partially my fault too or whatever.

(01:05:59):
And so I realized that a better way of giving feedback is thinking about motivating the person's behavior change. The goal is behavior change. So if that's the goal, trim everything else that you were about to say that does not actually contribute to that goal and only keep the part that will make the person want to change, help them understand the benefit to them as well as to the people around them. And so usually for me, that's trimming 90% of the initial stuff that I want to say and really keeping only that 10%. And that's made a really big difference. Whenever I am giving constructive feedback of any kind, I always keep that in mind. And when I don't do it, I almost always regret it.

Lenny Rachitsky (01:06:46):
Someone close to me in my life is working on the skill, which is there's just, "I want people to know how they messed up. Justice. I need this to be fair." And what I always recommend is just think about what you want to get out of this conversation, what do you want from them? And then, okay, what's the best way to get that? Versus just making sure they hear you and making sure they understand how screwed up this was. And that's basically what you're saying is focus on the outcome you want to achieve, not something that's useful, something that will make you just feel better.

Wes Kao (01:07:23):
Yeah. I definitely think that having a space to vent and to share those frustrations is important. So you want to get that out before you go into the conversation with your counterpart. So whether it's talking to your therapist or your partner or friend, you want to basically get all that energy out because otherwise you bring it into the conversation and it doesn't take much to set you off. You might have a whole script, you're controlled, you're calm, and then you start talking and the other person raises an eyebrow and is acting a little incredulous at what you're saying, and that's all it takes for you to snap and be like, "You're surprised? You're incredulous? Why are you incredulous?" Right? And then you're off, right? Yeah. Getting that energy out, I would say step one, so that you can go into the conversation clear, grounded, setting that emotional tone that is more positive and that allows you to stay focused on only the part that will get them to behave in the way you want them to behave.

Lenny Rachitsky (01:08:23):
Such good advice. And I think we come back to are you getting the outcomes you want? If you're not, this is another reason it might be the case is you just need them to hear your mind. I just need you to know. And I think a lesson here is that may not be the best path to getting what you want, but it may feel good. Maybe people are like, "Ah, but I really want them to know this."

Wes Kao (01:08:42):
There's that great Einstein quote about insanity being repeating things that you're doing expecting a different outcome. And I feel like that applies so much to the workplace and to communication. Most of us have certain patterns that we are used to and certain ways of responding, and if you believe that there is untapped upside that whatever you are at is kind of a local maximum and that there's better out there, then that's where switching things up could be useful and not just doing everything that you've been doing and getting the same result that you might be getting.

Lenny Rachitsky (01:09:19):
This resonates with Toby Lutke when he is doing the podcast, talked about how... He had this quote that I love that just "No human in history has come anywhere near their potential and everyone is way, way, way better than they think are," and these are really cool tactics and really effective ways to actually get closer to your potential. Okay. Two more things I want to talk about real quick. One is your advice on delegating, but also continuing to have high standards. This is something I spent a lot of time on because a lot of people don't delegate because they're afraid it's not going to be as great. I just want this to be really good. I don't trust that it's going to go as well. If I did it my way, it'd be great. So just advice on how to delegate effectively while maintaining high standards.

Wes Kao (01:10:04):
Yeah. I have a framework called CEDAF. C-E-D-A-F.

Lenny Rachitsky (01:10:08):
Mm-hmm. I love all these acronyms.

Wes Kao (01:10:09):
It's kind of like Cedar, but with an F at the end. I need acronyms for myself. All of these are really reminders for myself because I need a short way to remind myself. So CEDAF stands for the C is comprehension. So have I given this person that I'm delegating to everything that they need to understand what it is that I want them to do. That includes more simple things like logins to all the right software tools that they need to look up, whatever you need to look up. And understanding what the end result should look like, right? So that's all under C for comprehension. E is excitement. Am I explaining this in a way that is making this as exciting as it could be? There are a lot of tasks that aren't inherently that exciting, but by explaining the why behind we're doing this or why it's important to the project we're working on, that makes people more likely to understand and be excited about how this fits into everything.

(01:11:06):
So E is for excitement. D is for de-risk. Am I de-risking any obvious risks from delegating this? So usually when I ask clients this, they immediately think of something. They're like, "Oh yeah, I wouldn't want my direct report to spend a ton of time going in the wrong direction, filling out a hundred rows of the spreadsheet if actually it took longer than we expected." Okay, great. If that's a risk, then maybe you have them do 10 rows, see how long it takes, see if we need all the information that they're actually gathering, and then regroup, right? So what's an obvious risk? Another might be I can see this person misunderstanding and thinking I'm looking for this where I'm really looking for that. Okay, perfect. Just tell them, "When I explain this, you might think I mean this, but really I don't want that. I actually want this," right? So just vocalize it. The A is for align. So am I giving the other person a chance to-

Wes Kao (01:12:00):
The A is for align. So am I giving the other person a chance to speak up and make sure we are actually aligned, that they're picking up what I'm putting down? Because you might be explaining a bunch of stuff, but how much are they actually absorbing? You won't ever know if you wrap up your little spiel and then say, "Okay, go off. Come back to me when you're done." So give people a chance to ask questions to see what parts are resonating, what parts they might be a little bit confused on. Usually, when I do this, it's amazing. Because my team member will say, "What did you mean by this part? How does this part fit in?" I'm like, "Oh my God, I totally forgot to mention this thing." Or, "Oh yeah, I didn't even really explain that well." Okay, so let's go into that.

(01:12:42):
And then F is feedback. How can you have the shortest feedback loop possible? I am a huge fan of shorting the feedback loop as much as possible and then shortening it again. So even within that initial conversation where I'm delegating something, instead of waiting a week, what if we waited a day and checked in on the initial direction that person was going? And let's do it even more. What if after I finished explaining, at the end of that conversation, we brainstormed a couple things that, that person wants to do? So within this same conversation, I'm delegating, I'm already getting a sense of, where do you want to go with this? Once you start, do you see any bottlenecks?

(01:13:24):
And so just really keeping that feedback loop super tight. I found that when I run through the CDAP acronym, there's usually one letter that I could amp up a little bit more like, oh, I didn't really put much thought into making this exciting for the person. How can I connect this to their career goals or to the company's priorities this quarter or to something else? So it's a nice mental checklist.

Lenny Rachitsky (01:13:49):
So much of your advice comes back to this idea that we've touched on a couple of times. We just spend a little bit more time upfront. Is that how you described it, a little more time upfront?

Wes Kao (01:13:56):
Yeah, a little bit more time. A little bit more of an investment upfront.

Lenny Rachitsky (01:13:59):
Upfront to save you tons of time later. Okay. So as you described this, I don't know if you're realizing this, but you're basically just helping people work better with AI and agents. This framework is exactly I think what people need to effectively delegate to this future world of this agent world of society of agents doing work for us. Basically, you're going to be delegating to these agents in the future, and this framework is a really cool way to frame it. So think about it. Am I communicating this well, comprehension? So CDAP. Comprehension is, again, can I make this clear? Is that the way to think about that?

Wes Kao (01:14:41):
Yeah. Can I make this clear? Does this person have everything they need to be able to accomplish what I am asking them to do?

Lenny Rachitsky (01:14:47):
Okay. And then it's communicate why you're excited about this, basically the why. And it's interesting, there's this funny prompt technique I've learned, prompting engineering technique of just telling the AI, "This is very important to my job." Just using that sentence, it does it better.

Wes Kao (01:14:47):
Oh, interesting, yeah.

Lenny Rachitsky (01:15:04):
It takes it more seriously. It's just so weird. I have a post about this, and that's one of the pieces of advice, just tell me why this is important. I think people take it to the extreme as someone will die if you don't get this right. That actually works.

Wes Kao (01:15:16):
That is extreme. Cool.

Lenny Rachitsky (01:15:18):
It's wild. Okay, so CEDF, comprehension, excited, de-risk, think about ways you can de-risk, which is moot, basically. What's the most? It's a similar concept. Just think ahead to what might go wrong. Make sure you're aligned, which is quite important in the AI space. Make sure you're aligned. And feedback, get a quick feedback cycle. And it's interesting with deep research on some of these AI tools now, it's like, "I'm off for half an hour. See you." And I imagine more and more of them will check in with you as it's going and ask you questions. I used deep research recently and it's really good at just like, okay, let me have five questions for you before I go off and do this work just to clarify what you want.

Wes Kao (01:15:58):
Yeah, I found that AI will often shorten the feedback loop and align with you as well. When you prompt it, when it comes back, it will not do the entire task for me, sometimes. It'll say, "I've done the first part of this. Does this sound right? Is this what you're looking for? If so, I will complete the next section." And then sometimes I'm like, "Do the whole thing. Just stop trying to conserve energy and just do. I want you to do the whole thing." But that's what it's doing, it's breaking it into smaller chunks to de-risk that it's going to use all this bandwidth to process this thing and I'm going to say, "Oh, that's not what I was looking for."

Lenny Rachitsky (01:16:37):
I'm going to come back to AI real quick, but before I do that, I have one more question for you, but let me just say, I feel like we've discovered an AI version of your course now. Basically, how to delegate well to AI agents that I think people are going to find really valuable, planting a seed. Okay. Before we get back to AI, you have this other concept that I love that I actually learned from you years ago when I was working on my course called the swipe file. Swipe file, what is a swipe file? What is that about? What can it help you with? Why should people be doing this?

Wes Kao (01:17:03):
Yeah. So swipe files are really common for marketers, and I think other functions haven't caught on as much, but I think it is really, really useful. And basically a swipe file is collecting inspiration that you can refer back to later on. So some marketers will collect examples of copy, landing pages, ads, et cetera. For me, I have a file, an Apple Notes, file called Smart Things People Have Said, where I will basically paste in phrases, words, things people have said that I thought were well articulated or sounded really intelligent or sounded strategic. And I don't actually go back and look through my swipe file very often, I think other people do, but for me, even the act of adding it to my swipe file, I've already gotten value from it because it's training me to be more alert to noticing when something is working well.

(01:18:01):
I think there's so much happening around us all the time that your coworker says something smart and you're like, "Oh, that was nice," and then you keep moving on. But when you stop and pause and think, oh, that was really effective, let me add it to my file, and also think about, why was that effective and is that something I can borrow? So in my course, I encourage folks to create a work journal where they can jot down some of these observations, some of these phrases, and basically encourage yourself to be more alert to things you can borrow from other people all around you.

Lenny Rachitsky (01:18:38):
Something else about the swipe file, you use quotes. It could be screenshots of cool designs. It could be strategy docs you found to be really effective. It could be conversion flows that are really cool. It could be just whatever you're interested in.

Wes Kao (01:18:52):
Yeah. And the great thing about that is you can then go back and analyze it and break down the structure, break down the argument, break down why was this so effective? Whereas if you're not capturing it, it's easy to just move on to the next thing.

Lenny Rachitsky (01:19:09):
Yeah, cool. And I did this for a while. I stopped, to be honest, but I really want to be doing this. So this is maybe some homework or something, because I know a lot of people stick with it, is just start like a folder or a Notes, note, whatever you use for your note-taking, and just start throwing stuff in there. And it could be messy, right? It's just like, throw it in.

Wes Kao (01:19:27):
It can be super messy. I was going to say, my back end system is super messy and it's fine. It's not a problem I need to be solving. It works. I find things I need to find. So I like having as simple of a process as possible. So Apple Notes, I open it. It's just on my home screen, I just add something. I'm not tagging anything, I'm not putting it in certain rows and filling information out. I'm just including it in a file, and if I want to go back and look at it, it served its purpose.

Lenny Rachitsky (01:19:58):
Awesome. Okay, so last question. AI, I'm going to just come back to this briefly. We have this segment on the podcast called AI Corner, and we touched on this already, but I'm just curious how you have found AI to be useful in your work or your life, whether it's helped you become a better communicator? Is there anything you can share that might be helpful to folks?

Wes Kao (01:20:18):
Yeah. I love Claude. There are days when I talk to Claude for three or four hours prompting as a thought partner. So yeah, I think that AI is really helpful for an initial draft of something to bounce off of. Sometimes I'll paste in an email that I am not quite sure how to respond to and ask Claude, "Tell me draft reply." And I'll usually give it some direction. So I found that sharing my point of view makes the output way better. If I just give it something and say, "What would you say?" It's just not as good. Whereas if I say, "I am not sure about how to tell this person no, because I previously said yes and so I feel on the hook, but history has changed and so is there a nice way where I can be really respectful of our relationship and also make them feel seen and heard, but decline?"

(01:21:19):
So if I explain, "That's the problem I'm dealing with and here's what I would ideally like to be able to do," Claude comes back to something that's pretty good. And then from there I'll edit it to my voice because usually it's a little bit too formal sounding. And so I'll make some edits and then I'll share it back to Claude and say, "What do you think of this version? Would you make any improvements?" And then we go back and forth from there.

Lenny Rachitsky (01:21:41):
Wes, this is the most useful thing I've ever heard.

Wes Kao (01:21:44):
[inaudible 01:21:44].

Lenny Rachitsky (01:21:45):
I need this and I need this immediately, just nice ways to say no to stuff. This needs to be an extension that I can have in my browser, just, "Help me say no to this, please." Wow, such a great idea. Okay, good one. Okay, great. Wes, is there anything else? We've gone through a lot. I imagine the answer is no, but before we get to our very exciting lightning round, is there anything else that you wanted to share or leave listeners with?

Wes Kao (01:22:11):
No, I feel like we covered a bunch of great frameworks, principles, so lots for folks to get started.

Lenny Rachitsky (01:22:18):
All the things. And I love that so much of this will apply to being more effective with AI tools and I feel like people can go through this again and just through that lens of, how will this helped me get more out of Claude and ChatGPT? I bet so much of this will actually apply and I feel like there's an interesting course there. With that, Wes, we've reached our very exciting lightning round.

Wes Kao (01:22:39):
All right,

Lenny Rachitsky (01:22:40):
Are you ready?

Wes Kao (01:22:41):
Let's do it.

Lenny Rachitsky (01:22:42):
Okay. First question, what are a couple books that you recommend most to other people?

Wes Kao (01:22:46):
One is High Output Management by Andy Grove, which is a classic. Another one is Your Brain At Work by Dr. David Rock. And that one is all about better understanding your own brain and attention span so that you can allocate your mental resources appropriately. So that one's great. Ever since reading that, I hide my phone from view because there have been studies that show that even seeing your phone in the corner of your eye, it's distracting. And I do the hardest things earlier in the day when you have more cognitive resources available. So that one's really good. Yeah, those two.

Lenny Rachitsky (01:23:31):
These are great. I completely get that phone thing. I'm just looking at my phone, I'm like, "Dang, get out of here. Just go away."

Wes Kao (01:23:36):
I will stick it under my pillow on the couch or hide it under a notebook. It's huge. I'm always hiding my phone so it's not in my line of sight.

Lenny Rachitsky (01:23:47):
I think Arianna Huffington has a product you can buy that's a little bed for your phone that you put to bed before you go to bed in a different room and it has a charger attached.

Wes Kao (01:23:54):
Oh, that's cute.

Lenny Rachitsky (01:23:55):
So cute, so cute.

Wes Kao (01:23:57):
I don't know if I need a separate bed for my phone.

Lenny Rachitsky (01:24:01):
But it's like a ritual, I guess, and there's some theory behind it. Okay, next question. Favorite recent movie or TV show you really enjoyed?

Wes Kao (01:24:08):
I love Anything by Harlan Coben on Netflix. Basically, I don't even remember any specific movies or a TV series, but anything he puts out, he's an author and then they've turned a lot of his books into mystery thriller TV series, and anything he puts out becomes number one on Netflix. And I appreciate that he gives the people what they want, that he knows his craft, he knows his genre. And yeah, he just has so many bangers. And I don't remember any specific one, but if it's a Harlan Coben show, I know it's going to be good.

Lenny Rachitsky (01:24:46):
I'm looking at a list now I just Googled real quick. So it's all scary stuff, right?

Wes Kao (01:24:49):
Yeah, they're mystery thrillers, and I think he does a good job playing with time and revealing information over time. It's usually something about someone's past that is now coming to haunt them, and so he'll skip between present day to the past and then slowly reveal stuff. And there's always a twist at the end.

Lenny Rachitsky (01:25:11):
There's a page, the Harlan Coben Collection on Netflix. That we'll link to that has all this stuff. I've never heard of this, so this is great. Next question, do you have a favorite product you recently discovered that you really love?

Wes Kao (01:25:22):
I recently started using an electric toothbrush and it's been life-changing. So my husband got one and then a couple weeks later he gifted me one, and I was like, "Wow, this is actually really nice."

Lenny Rachitsky (01:25:34):
Are you a Sonicare person, Oral-B person, or something else?

Wes Kao (01:25:37):
It's Oral-B but I've not tried any other brand. That was one that our dentist gifted my husband this electric toothbrush because he did Invisalign. And I'm sure Invisalign is every dentist's dream.

Lenny Rachitsky (01:25:51):
Margins.

Wes Kao (01:25:52):
I feel like every time I get a cleaning, the dentist is like, "So have you thought about, are you interested in Invisalign?" I'm like, "No." And so when they get a yes, I'm sure they're really excited, and then they lock you in, the brand locks you in with these replacement toothbrush heads that are way more expensive than they should be. So it's a whole razor and blades, ink cartridge and printer model here. So I was horrified by how expensive these replacement heads were.

Lenny Rachitsky (01:26:18):
But you got a free toothbrush. I think the Oral-B is what I use, but I think that's what the Wirecutter recommended, but it's so loud. I don't know. One of them is just really loud. I think it's the Oral-B, but it's better, apparently. I went with Wirecutter, but it's so loud. I feel like there needs to be a Wirecutter for good design and experience...

Wes Kao (01:26:37):
Ooh.

Lenny Rachitsky (01:26:37):
... versus just the optimal efficient version. Anyway, let's keep going. Do you have a life motto that you often find useful in work or in life that you repeat yourself and share with folks?

Wes Kao (01:26:51):
Yes. I actually have many, but I'll share two. One is everything takes longer than you think. So this applies whether you are calling customer support for something or running an errand or building your career, building skills. I find it's useful to add buffers for yourself. This applies for launches too. Just assume it will take longer than you think and you'll be less stressed.

Lenny Rachitsky (01:27:18):
That connects to everything we've been talking about. Just spend a little more time upfront to make it. And maybe if you spend more time front, it'll take less time than you think.

Wes Kao (01:27:25):
The other one is a riff on always be closing, like Glengarry Ross. "It's always be selling." This does not mean pawning your wares, but rather putting forth effort into convincing the other person of whatever your recommendation is.

Lenny Rachitsky (01:27:42):
Love them. Okay, final question. So you've been a long time, I hate this word operator, but I guess that's the way people describe this, where you've just been working at companies, building companies, and you recently left that just to become creative person. Started a course on Maven. You do executive coaching, things like that. Any just lessons or a lesson from that jump that might be helpful to folks that are maybe thinking about that?

Wes Kao (01:28:07):
I think when you are an in-house operator, there's a lot about your role that you have a little bit less control over, basically. There's just certain things you have to do because it comes with the territory. Whereas when you are a solo operator running your own business, doing your own thing, you have a lot of freedom to craft your work around only your strengths, only the part that you are really good at, that adds a lot of value for other people where there's market demand. And so, for me, there was a bit of a shift where when I realized that I could craft my business, my work around only the part that I'm best at, and that can be a narrow-ass slice, that's actually really, really freeing.

(01:28:54):
And so I would encourage folks to think about, what is the thing that you are extremely good at that people find super valuable, the part that you love doing most, if you could not do all the other stuff you don't want to do, and how can you think about doubling down on that?

Lenny Rachitsky (01:29:12):
That's such an important point. And the Claude tip you shared of how to say no well is such an important ingredient into that, because so many things come at you and are interesting and enticing that it's hard to decline, that you realize, why the hell am I doing this? I can actually control where I spend time and why did I say yes to this?

Wes Kao (01:29:33):
I actually credit you with helping me come to this realization. I mentioned you on a podcast the other day about this because, do you remember when Maven was launching an important feature, I think it was our marketplace or something, and I had asked you if you wanted to go on Clubhouse to be part of the launch?

Lenny Rachitsky (01:29:56):
I remember that, but I am sure I said no.

Wes Kao (01:29:59):
Okay, yeah. You said no. You said no. And I was like, "Wow. Out of curiosity, what's the thought behind it?" And you said, I'm going to bastardize this, you could correct me, but you essentially said, "I don't really like doing live public speaking type things and I've been fortunate enough to build a career where I can write, I do my podcasts, and work only on the part that I love doing. And so I'm okay saying no to these other really interesting opportunities." And I remember at that time thinking it was so groundbreaking that you could say no to something that was legitimately a cool opportunity and be really confident about it because it wasn't your core competency. It wasn't the thing you are best at. And I've really kept that in mind when opportunities come my way of, am I excited about this? Is this what I'm really good at? Can I shine in this setting? Because when you are solo, you get to choose the settings that you want to be in.

Lenny Rachitsky (01:31:00):
That's such a cool story. I don't exactly remember that, but I am zero surprised at what I said. And the way I put it now, when folks invite me to stuff like this is I just find the ROI on my time is so not worth doing a talk, doing a fireside thing, doing another podcast. It's just like, if I can spend more time on this newsletter than the podcast, the leverage is so much higher than just doing a talk because that takes so much time. So I just have this template now that basically says what I sent you, that is, that it helps. But it's tough. It's so hard to say no. Sometimes these opportunities are so interesting and the person is like, "Wait, what?"

(01:31:37):
Because I don't think the people asking you for stuff know that I'm getting 10 of them a day, and they're like, "Oh, he said no to my talk. He doesn't want to be on my podcast. What a jerk." That's what I think. I don't know if that's what they think. But anyway. Okay, that's great. Yes, and I think I just had a post about reaching a million subscribers to the newsletter, and actually had this image of the Ikigai concept, which is exactly what you just described, which is you want to try to find the thing that you love doing, that people value, and that you can make money doing. That's the dream. And that's exactly what you have done as well. So thank you for being here, Wes. I actually think we delivered on what I thought we would. I think this is going to be one of the most highest leverage conversations we've had.

(01:32:21):
So two final questions. Where can folks find your course? I know you also do executive coaching. Where can folks learn more? And final question is just, how can folks be useful to you, Wes?

Wes Kao (01:32:33):
You can find out more at weskao.com. I linked my course to my coaching from my main page. I also post on LinkedIn as well, so you can follow me there. And I'm always looking to meet fellow operators who out about communication. So if you put any of these principles into practice, I would love to hear about it.

Lenny Rachitsky (01:32:53):
Awesome. We'll do that in the comments. They can DM you. I don't know, what's the best way to reach you on the website or Twitter?

Wes Kao (01:32:59):
Yeah, bunch of platforms.

Lenny Rachitsky (01:33:02):
All the places. Okay, cool.

Wes Kao (01:33:04):
Website, email, LinkedIn, DM me.

Lenny Rachitsky (01:33:05):
There we go. There we go. Wes, thank you so much for being here.

Wes Kao (01:33:08):
Yeah, thank you so much, Lenny.

Lenny Rachitsky (01:33:09):
Very cool.

Wes Kao (01:33:10):
This was fun.

Lenny Rachitsky (01:33:14):
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

