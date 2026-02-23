# BYL Brain: Data, Analytics & Experimentation — Part 2 of 2
_See Part 1 for topic index | Updated: 2026-02-23 01:10 UTC_

---

## TRANSCRIPTS (continued)

### Product management theater | Marty Cagan (Silicon Valley Product Group)
**Guest:** Ray Cao | **Date:** 2024-03-10 | [YouTube](https://www.youtube.com/watch?v=9N4ZgNaWvI0)  

# Product management theater | Marty Cagan (Silicon Valley Product Group)

## Transcript

Lenny (00:00:00):
We rarely get a peek into what it's like to work at TikTok. What are some core principles or values or just how TikTok operates?

Ray Cao (00:00:07):
The number one thing is context, no control. That's the reason why we're always encouraging people to see themselves as a business owner.

Lenny (00:00:14):
You give them all the information they need and then let them just do things without specific instructions.

Ray Cao (00:00:18):
How do you actually solve the puzzle by connecting all the dots together? Just like how I see some of my friends, their kids playing Legos, if you don't really see the full picture, you won't be able to make the Lego as one thing at the end of the day. You have to see the other pieces.

Lenny (00:00:31):
What else are important cultural values of TikTok, of how TikTok operates that everyone always has in mind when they're building?

Ray Cao (00:00:36):
We always have this mentality we are a startup, we're a young company, we're always hungry for growth. And a very wacky way is like, "How can I run my second half of my marathon faster than the first half?"

Lenny (00:00:49):
Today my guest is Ray Cao. Ray is the global Head of Monetization Product Strategy & Operations at the Global at TikTok where he has been for over four years. Prior to TikTok, Ray spent six years at Google helping scale Google shopping globally.

(00:01:05):
TikTok is interesting for two big reasons. One, it's one of the most successful businesses in history, last valued at over $80 billion. And its parent company is the most valuable private company in the world, last valued at over $200 billion.

(00:01:19):
Two, TikTok is quickly becoming one of the biggest advertising platforms alongside Meta and Google, and generated nearly $10 billion in advertising revenue just a couple of years ago. So for both these reasons, TikTok is a really interesting business and team to learn from. And I've seen very few podcasts and even media get a peek inside how TikTok operates.

(00:01:39):
In our conversation, we discuss TikTok's culture, their core principles and values, how they hire, how they move so fast, their emphasis on working hard, how they do OKRs and planning. We also get into how to succeed on TikTok's ad network, why you want to be testing at least 10 videos a week, how it's different from running ads on Instagram, how to make content that does well on TikTok, and so much more. This episode has a lot of interesting lessons and insights. Obviously TikTok is at the center of a lot of debate globally. Some people love it, some people hate it. But no matter your opinion of TikTok, there's a lot that we can learn from their success.

(00:02:14):
If you enjoy this podcast, don't forget to subscribe and follow the podcast on your favorite podcasting app or YouTube. It's the best way to avoid missing future episodes and it helps the podcast tremendously. With that, I bring you Ray Cao after a short word from our sponsors.

(00:02:29):
This episode is brought to you by WorkOS. If you're building a SaaS app, at some point your customers will start asking for enterprise features like SAML authentication and SCIM provisioning. That's where WorkOS comes in, making it fast and painless to add enterprise features to your app. Their APIs are easy to understand, so that you can ship quickly and get back to building other features. And 100s of other companies are already powered by WorkOS, including ones you probably know like Vercel, Webflow and Loom.

(00:02:59):
WorkOS also recently launched AuthKit, a complete authentication and user management service. It's essentially a modern alternative to Auth0, but with better pricing and more flexible APIs. AuthKit's design is stunning out of the box and you can also fully customize it to fit your app's brand. It's an effortless experience from your first user all the way to your largest enterprise customer. Best of all, AuthKit is free for any developer up to 1 million users. Check it out at workos.com/lenny to learn more. That's workos.com/lenny.

(00:03:35):
This episode is brought to you by Eppo. Eppo is a next generation A/B testing and feature management platform built by alums of Airbnb and Snowflake for modern growth teams. Companies like Twitch, Miro, ClickUp and DraftKings rely on Eppo to power their experiments. Experimentation is increasingly essential for driving growth and for understanding the performance of new features. And Eppo helps you increase experimentation velocity while unlocking rigorous deep analysis in a way that no other commercial tool does.

(00:04:05):
When I was at Airbnb, one of the things that I loved most was our experimentation platform where I could set up experiments easily, troubleshoot issues, and analyze performance all on my own. Eppo does all that and more, with advanced statistical methods that can help you shave weeks off experiment time and accessible UI for diving deeper into performance, and out-of-the-box reporting that helps you avoid annoying prolonged analytic cycles. Eppo also makes it easy for you to share experiment insights with your team, sparking new ideas for the A/B testing flywheel. Eppo powers experimentation across every use case, including product, growth, machine learning, monetization and email marketing. Check out Eppo at getEppo.com/lenny and 10X your experiment velocity. That's getEppo.com/lenny.

(00:04:55):
Ray, thank you so much for being here and welcome to the podcast.

Ray Cao (00:05:00):
Thank you Lenny for having me. It's a pleasure.

Lenny (00:05:02):
It's my pleasure. I am really excited to have you here because it feels like we rarely get a peek into what it's like to work at TikTok, how TikTok builds product and operates, also how to be successful in TikTok as a business, as an advertiser. So I have all these kinds of questions for you, and so I'm really happy to be chatting. I wanted to start with a little bit about your time before TikTok, which was at Google and comparing that to TikTok. So, you're at Google for six years, I believe. Now you're at TikTok. I'm curious on what stood out to you about the cultural differences between how Google operates and TikTok operates.

Ray Cao (00:05:37):
Three major things, I would say. Number one is really how these two company thinking about innovation. So, I think Google has a very strong philosophy of we're engineering lab and that there's a lot of technology-driven, and a lot of pieces. They are not necessarily always trying to, I would say, cope with the market even, right? However, I think at the TikTok, I think besides the technology part, we do have a very keen, I would say, appetite to really understand what the markets really want and also how can we really service our clients in a better way and the clients here is not necessarily only for advertisers including our user and also creator altogether. So that's one of the things I think it's very different in terms of TikTok way of work. It's very customer-centric in a way, and again, the customer here is not necessarily only for the business partner but also for our regular user and creators on the platform.

(00:06:39):
And the second one is really thinking about how we take approach on product development. So a lot of times that we take a very rigid approach in terms of product development and oftentimes you see us that experimenting a lot of different things all the same time. And also we do have a lot of engineering and [inaudible 00:07:04] project in the backend to really understand how can we optimize better for the platform. So a lot of time, these are the things that I think TikTok is doing really, really well.

(00:07:14):
The last piece I have to say is the approach for global prioritization. A lot of times that you see a US-born company go global and oftentimes still they are really rooted with the US market and there's nothing wrong with it to be honest, because this is the biggest market for them as I would say for East-born company. I think a lot of times that we can take approach with truly how do we think about globalization and for example, we launched a lot of product not necessarily first in North America. We launched it in South Asia for example, for our shopping, really very big initiative internally for shopping and we launched our really creator fund here in North America. We launched our gaming approach, really serviced our EUI gaming advertisers. Really, really strong over there. So there are a lot of different approach in terms of how do we prioritize our go-to-market and also product development. So that's the part I feel like we're very unique in the market or unique to some of that was the tech company born in the US.

Lenny (00:08:24):
It reminds me there's this piece by this smart guy, Eugene Wei who wrote a few things about TikTok over the years and just why it's been so successful and one of his really big points is that TikTok can work really well in other markets 'cause it's basically... you don't need to know a ton about the market because it's this algorithm that figures out what people in each market want. Is there anything along those lines you've seen that just has been really fundamental to it working so well in many different markets?

Ray Cao (00:08:51):
The algorithm is definitely helping because it is basically the machine is doing a lot of heavy lifting. That's actually I think across the board on a technology company today. The difference is actually how much you are willing to take the heavy lifting over there in the market. By that I mean really sending your troops into the market, hiring your local talent, understanding the culture and really understanding the behavior from those users. I understand the machine can do things, but also at the same time that we need to actually get local talent to fine tune the machine. So there are a lot of conversations about how I would say technology is able to change our life, but I do think that at the end of the day, I do believe technology is a tool.

(00:09:34):
So if we do have a ambition to go global, you have to do one more thing is actually take your step into global. Rather than having the machine do the heavy lifting, you have to really understand in local culture. I had a fun background for my first job is to really doing go-to market research in the Southeast Asia area. I think there was only one thing opened my eyes after a year and a half in this career path is different market have totally different, I would say, culture and these market behaviors are actually coming out of this culture. One of the fun example I always been using was I was doing market research for one of the suppliers for toner and also these ink cartridges for Thailand as a go-to market research. One of the things is always concern to my, at that point, the client was they cannot figure out why their premium product cannot sell in Thailand and then we just figure out because the quality of their printing machine and also their ink cartridges are premium and the quality of the paper and everything is very good.

(00:10:51):
But when you actually do talk to those consumers in those market, the answer is very eye-opening. They literally told me at that time is I don't care. I don't care if your ink cartridges or your printer is at the premium quality, maybe the printer I can use, but I can use compatible ink cartridges or toner for that because my consumer won't care about your printing quality or the majority of my consumer won't care. So in that case you should not necessarily worried about if you are a premium product, it's actually more about how durable, how reliable you're able to print things and people can read.

(00:11:30):
So I think these are the insights I think a lot of times it will be neglected from some of clients or the manufacturers or even the owner of the business because they think that we want to serve this segmentation, but, however, this segmentation is that big in this area. So that's reason why the culture is really the key part from the market. If you don't understand the culture, you won't be able to understand the behavior over there. It's more about that, I think, when we say about globalization or take the product go to market in a global scheme or even build it apart, you have to get your hands dirty and to really understand the local culture so that you can understand local behavior.

Lenny (00:12:16):
I love that advice, the way you described it, which I love also is that you kind of have to fine-tune the algorithm and the product to work in different cultures. Is there an example of how that was done with TikTok, like a tweak that had to be made or some kind of fine-tuning that happened for it to work in a different market?

Ray Cao (00:12:32):
Yeah. I think we did a lot of fine-tuning on our user product side to really think about content. So that's the number one thing going to be super different coming from each of the market and also from each of the culture. For example in Japan, how do you actually get more content that relevant for the culture? A lot of people may think, okay, are you guys only doing dancing or doing singing for Japan? The answer is not. It is actually more food on the TikTok side, like how do you actually introducing new food restaurant or new recipes and also sometimes that you're introducing a new technology. I would say 3C like consumer electronics product over there. So these are the content get really popular sometimes in Southeast Asia or even Japan area and versus in the US as everybody knows that we're starting from really lip-syncing at a very early stage but now really we're expanding to shopping behaviors and also a lot of people using us as a main platform to acquire new discovery for the product.

(00:13:40):
So these are the things I think different market definitely deserves and demand different kind of treatment and if you are able to do this a lot, you're able to find success over there.

Lenny (00:13:53):
That's really interesting because you could think it's just this algorithm that figures everything out for you, but I think what you're pointing out is you have to seed it with the right sorts of use cases that that culture is most excited about.

Ray Cao (00:14:04):
Another good example will be creative, so it's a very good example how human can work with technology together. We have a ton of creatives and we have a ton of content so, of course, we use machine to label those content use metadata to analyze those content. However, a lot of times you can find that when we're really thinking about how creative can help advertisers? Humans actually make a more interesting or more, I would say, influencing decisions over there. For some of the verticals we can say that, "Oh, you know what, maybe we can try a coupon image with a new product like a sticker on the top?" This maybe actually work better compared to some of the price promotion even. So a lot of things really depends on how do you actually interpreting the numbers and interpreting the data points but also at the same time your business acumen is going to be very important here to make a judgmental call for some of the situation like that. I think we're still rely a lot on both machine and also our own experts to analyzing those trends and give it the recommendations.

Lenny (00:15:11):
Awesome. Okay, so there's a few threads I'm going to follow later. You talked about the product development process, so I'm going to want to spend time there, also about how to be successful in TikTok both as a creator also as a business, I'm excited to hear your advice there. But I want to spend a little more time first on just what it's like to work within TikTok and the culture of TikTok. What are some core principles or values or just how TikTok operates if you had to identify, here's the ways that we all think about what we want to do and the most important to your day-to-day work, what words and concepts come to mind?

Ray Cao (00:15:43):
The number one thing resonating really, really well with me is context, no control. Oftentimes when we are looking around companies different sizes, we're looking at how to collaborate. Oftentimes we see the behavior that a lot of people just working on a smaller piece based off their job description. So hey, you're working on go-to-market and you're working on data analytics, and you're working on this book of business and commerce, and you're working on auto industry for example. A lot of times that these human-made silos is actually slowing things down because humans are not, or our talent, they're not supposed to be categorized into different basket. They may have their own majority responsibility for sure, but we don't want to cap them into this kind of a box we created. That's really why we're always encouraging people to think out of the box and think more and think themselves as a business owner rather than a piece of machine that keep the machine running.

(00:16:49):
Oftentimes that will say context, no control. That means you actually can go above and beyond to really think about your whole business problem as your own problem and your piece is maybe one part of it to solve the puzzle, but how do you actually solve the puzzle by connecting all the dots together, we're encouraging all the people to think like that way and by that I think we kind of mentally break out those walls. So encouraging our team members to do a little bit more thinking is very important. It's a little bit more thinking because the think part is very important.

(00:17:23):
And then, now in terms of getting things into behavior or changes or getting to action, then you need to really collaborate with other teams because we don't want to necessarily creating, hey, you're on other people's working group now you're actually stepping on other people's toes now. It is not the situation we're trying to encourage in, but where it's encouraging more is context, no control, think more about how you can change it and then we you do really actually take some actions, be active. You reach out to who's supposed to be the owner of that and then have a discussion so then you you're able to connecting the dots altogether.

(00:18:00):
So that's one thing I think it's very unique to our culture. I think it's very, very important for us to continue to grow at this speed because everybody have a, I would say, full visibility towards our full ownership to their mindset, how they can contribute.

Lenny (00:18:16):
And the key there is context implying you give them all the information they need and then let them just do things without giving them specific instructions, "Hey, I need you to hit this goal, work on this project, launch this thing. Here is what we know, do the things you think are best, roughly." Right now, I know it's not just like anyone does anything, but I imagine that's kind of the implication there.

Ray Cao (00:18:35):
Yeah, I think it's context, no control plus proactive thinking and reactive doing so you have to do more proactive thinking with these contexts. Now reactive doing means that you need to collaborate, but when everybody has this kind of mindset, the collaboration should be very smooth because people have the context altogether. The part that I see maybe some of the other company are facing challenges is actually there's too many IOs in between and you have people that are just protecting their own thing and working their own thing and then I'm delivering. But just like how I see some of my friends, their kids playing Legos, if you don't really see the full picture, you won't be able to make the Lego as a one thing at the end of the day. You have to see the other pieces. So that's the part I think it's really powerful and reasoning really, really well when we're really thinking about product development and also product go-to-market. So it's a pretty full cycle. People have to see this and then they have the context.

Lenny (00:19:35):
I love this, and this has come up actually a few times recently when I was talking to the CTO of Netflix and also OpenAI. They're very similar in culture where it's give people a lot of autonomy and freedom and not a lot of do this, do this, do this. The key there is to hire very high quality people and very high caliber people because if not, then things won't work out too great. Is there anything along those lines that you can share just like yeah, the kinds of people you end up hiring and how you hire people that can work well in that environment?

Ray Cao (00:20:05):
I agree with you. So the caliber of these people is actually pretty important to support the structure I just talked about, and oftentimes I can see some people that with the quality of always curious. Curiosity is a very important quality when I'm actually talking to my interviewers because I want to see that they are naturally curious to new things. They want to learn more about the new things and don't really get stuck with their own things. That's one thing. And the other thing is the discipline because like I said, it is actually a double-edged sword in this case. So it could potentially introducing some of the chaotic situation in a company because everybody is thinking everything. The discipline here is actually how you are really following the guidance on reactive doing, be always thinking about how to collaborating, and the discipline here and also the rigorous approach here is also going to be very important.

(00:21:07):
One of the good example that is the ability to prioritize because I don't believe one thing is everybody can do everything. You have to prioritize properly so that you're able to push the right agenda. So I think that's more of the quality of the people we're looking for is... it is hard, don't get me wrong. It is really hard to say that we can find everyone like that, but we would love to believe that we can train our employees like that so that they're able to even do better in their longer-term career.

Lenny (00:21:38):
Essentially what you look for when you're hiring people is making sure they're always curious, they have high discipline, and that they prioritize well. Coming back to the cultural pieces of TikTok, so the main one you've shared so far is this idea of context, not control. What else are important cultural values of TikTok, of how TikTok operates that everyone always has in mind when they're building and new meetings, making decisions?

Ray Cao (00:22:04):
Yeah, another internal thing that we always say is always day one, we want to make sure that we always have this mentality we are a startup. We are a young company. We're always hungry for growth. We don't want to fall into the trap that people may think, "Oh, you guys are very successful in the market and then you are not necessarily need to worry about your existence anymore." I think it is actually something we're trying to avoid. We always want to make sure that in our team members always think like, "Okay, if this is actually a new day for you, I know what other things that you always want to keep in your mind you want to do." And also to keep that spirit is very important.

(00:22:42):
A lot of times that I can see some of the mature company, they're not necessarily losing the edge of, I would say this competition or losing the edge of being innovative. I think it's more about some of the culture has been shifted because you have a lot of new employees that live in your culture. So not necessarily it's not going to be like the old days that the co-founder is sitting among you, but I do think this company has a very interesting behavior. I see there is I can talk to anyone at any time via our internal communication system. I can ping Shuo right now. I can ping the co-founder if I want to tomorrow.

(00:23:24):
We always keep this kind of mentality internal is that we're still a young company, we want to grow and you can feel free to talk to anyone. We don't have a limitation for that as long as you have a good opinion, I would love to hear from you. Is that creating some of the, I would say chaotic situation? It might be, but I do think that this keeps the company very energetic. People are willing to share, people are willing to engage. That's very important.

(00:23:50):
I want add one more thing. We just talked about, you asked me what is actually the uniqueness of TikTok versus the other company. It's very tied up to that is I have never seen a company, the engineering team and the product team and the sales team are so close. That's definitely one of aha moments I had because if you're thinking about if your engineer does not really know what the market wants and if your PM doesn't really know what is actually the client's feedback, they won't be able to get a right product in the market. They just won't be. And they won't even tell a good go-to-market story to advertisers or even to our users because they just don't know what the end users are thinking.

(00:24:39):
So I think it's a very secret sauce for us is that our sellers and our engineering team and our product team and also data scientist team, we're all collaborating really, really closely and that's very much, I would say a such big advantage for us compared to when a company becomes too big and nobody talks to each other. So I do hope that it is the thing that we're going to continue reinforce along the years where we'll continue to grow the company.

Lenny (00:25:09):
What does that actually look like? I imagine people hearing this are like, "Yeah, we're going to make sales and product and hinge very close." I imagine many people don't actually do this too well. How do you actually execute that? Is it they report to the same leader, they sit next to each other or I don't know, zoom next to each other? What actually makes that work?

Ray Cao (00:25:28):
Yeah, I think a couple of things. Number one is a structure. Everything has to go at a structure. So we do have a meeting structure that we called it... it used to be by month and now it's actually a quarterly level. We get everybody together, engineering leader, product leader, and also not necessarily only the leader level. Some of the team members, we're joining the force together to have a big meeting. That meeting is 180 people-ish. It's crazy to have a meeting at that size, especially that there are different kind of functionality there. But one thing we keep really well is actually we are using a reading format of meeting. So it's a doc reading. We just read in comments and understanding the context again. It is the doc, bring everybody together, and then we discuss the things that we want to make a decision with or the things that we feel is a blocker or things that we need to celebrate.

(00:26:24):
So that meeting structure keep everybody together and consensus, again, not necessarily only for the top leaders. It's normal for the engineering leader and product leader and sales leader at the company level, they talk to each other, but we made that happen for their core team members. And the very beginning of my time here, that was literally getting to the IC level. So it is pretty eye-opening for me to join that meeting first time because I was get so used to their level of different meetings at Google, but here it's like, okay, everybody read one documentation and then you just understand what are people talking about or thinking about. It is intentional. But I do think that that structure is a very big secret sauce, I would say, not necessarily we invented it, right? We also learned from the other companies. So it is actually one of the things that we actually deployed pretty well today here to keep that structure running.

(00:27:22):
And the other thing is really feed those, I would say, first-hand market information to our PMs and RDs. That means we took them out with us. We're just inviting them together to join the force together to meet the clients and a lot of the company, if you want to meet APMs, if you want to meet the engineering leaders, it's literally once a year maybe, and also if you're investing a ton with some of the platforms. For us, I think it's always on to junior PMs, senior PMs and engineering leaders. We invited them together to these immersion trips recorded to really get face time with our clients, to really feel the heat. They are actually really facing a challenge by using our own product.

(00:28:07):
So that kind of, I would say, the aha moment is bringing a lot of, I would say, insights to them and also get them to feel the heat of the pains the sellers may feel. So that worked really well, too. I think oftentimes it is a battle. It is not necessarily the general, you have to stay in the back, you sometimes have to go to the front, but we just make sure that the general go to the front quite often in our company to do that.

Lenny (00:28:36):
I love that concept of having them feel the heat. An interesting trend I've noticed is there's a lot of Amazon influence on the way you all operate. It's always day one idea. There's the memo culture you just described. Any idea where that comes from? Is there like a senior Amazon person that came in and helped influence those sorts of things? Is it just hey, Amazon's killing in there? I've noticed interestingly, Amazon has influenced the most companies in all of their ways of working, so it's not a surprise. I'm just curious if there's anything else there that's interesting.

Ray Cao (00:29:04):
I think we have the benefits to standing on the shoulder of all the giants. So we learned definitely always there when the culture that Amazon was always championing, I think we learned from them. So this is something that we, I would say, always trying to listen and trying to learn from industry. The dark fashion is also learned from Amazon, so we kind of studied, oh, this is maybe one of the best practices we can employ here, how we deploy here. So we tried it, not even mentioned we have the OKR system, so it is actually a very good learning from our early stage from Google. So all these, I think definitely we do have some of the, I would say, benefits being the newcomer to the market and then learn a lot of the best practices coming from our industry peers and really deployed here hopefully successfully.

(00:29:53):
And some of the things that we just tweaked. So for example our culture always day one is definitely very similar to Amazon, but the implementation of that could be different. And also the context, no control piece is, I believe other companies may have the similar idea, but for us I think we just really need to implement it in a way that's going to be fitting to us. I happened to listen to your podcast with the Airbnb co-founder the other day. He also mentioned that how he break out the IOs. I think it is very similar approach among industry right now trying to really make sure the team is able to talk to each other because I think a quote from him, "If your PM doesn't know how to sell the product they're creating, you won't be able to do your job better." So this is literally how we're thinking about it, too, in a lot of way.

Lenny (00:30:40):
I know that you all move very fast and I want to actually talk about that next. And with that it feels like your value should be, it's always the first half of the day instead of it's always day one. It's always the morning of the first day.

Ray Cao (00:30:53):
I think the value, if I put it in a very reactive way is, "How can I run my second half of my marathon faster than the first half?" So that's how I think about it and how do we really continue pushing for it.

Lenny (00:31:09):
Wow, that sounds very hard and painful, but I like that metaphor. Okay, so let's talk about how you set up the product org to move as fast as you move. I think there's this idea of just running fast. I don't know if that's a phrase you use, but just how is the product org set up, especially different from other teams that you've seen that allows it to move as quickly as you move and innovate as often as you all innovate?

Ray Cao (00:31:34):
Our product teams are setting, I would say, very importantly is global. So we want to actually, like I said, the number one step is if we really want to do global business, we have to go global. So we set up teams really across the board in the global locations to really acquire global talent who knows the market and who knows the competition, too. So we're able to really getting the, let's say jumpstart, in the local market. So for example, we have the majority of the engineer and also PMs currently located in the west coast of North America, so Los Angeles and also San Jose. These are the key hubs we have for our tech folks and also for North America wise we do have our majority of the go-to-market leads sitting in New York to get closer with our seller and also with our clients at the same time.

(00:32:27):
Also, it is not necessarily only for North America. Like I said, we heavily invested in Southeast Asia, so you can see that a lot of our engineering and also PM resources are deployed over there in Singapore to enable them to get closer to our clients over there as well. So really deploy your resources globally and also focusing on the key markets you want to penetrate. That's the commitment. I think we're doing pretty good in this case. And the second one is to really, again, I think the PMs and the product team of settings are oftentimes I would say because we're growing so fast, oftentimes we have to do a lot of minor team adjustment to catering for that. So it is very usual or common for teams to do a little bit of work on an annual basis or even on a two years or three year cycle. The stability is important, don't get me wrong, but I do think that as a faster growing company, we need to consistently to reiterate not only the product but also our teams.

(00:33:33):
So how can we do reiteration on the PM side, on the go-to-market side, it is actually something that I have seen this company doing really, really well. Not necessarily we're bonding to one team structure. We're actually bonding to the market need and we're bounding to the growth we're looking for. So we're not afraid to break our seams. And actually I literally break out my team last year to make sure that my team having more go-to-market mindset to actually embedded them with seller directly. So these are the things that very, I would say conventional to a size of this company, but I do think that's necessary and also that's a good mentality for the team to really run faster with this kind of a rigid approach. So yeah, these are the two things I think very unique to us, I think could also be continuously helping us in the next phase of the growth.

Lenny (00:34:33):
Today's episode is brought to you by OneSchema, the embeddable CSV Importer for SaaS. Customers always seem to want to give you their data in the messiest possible CSV file. And building a spreadsheet importer becomes a never-ending sink for your engineering and support resources. You keep adding features to your spreadsheet importer, the customers keep running into issues. Six months later you're fixing yet another date conversion edge case bug. Most tools aren't built for handling messy data, but OneSchema is. Companies like Scale AI and Pave are using OneSchema to make it fast and easy to launch delightful spreadsheet import experiences, from embeddable CSV Import to importing CSVs from an SFTP folder on a recurring basis. Spreadsheet import is such an awful experience in so many products. Customers get frustrated by useless messages like, "Error on line 53," and never end up getting started with your product. OneSchema intelligently corrects messy data so that your customers don't have to spend hours in Excel just to get started with your product. For listeners of this podcast, OneSchema is offering a $1,000 discount. Learn more at oneschema.co/lenny.

(00:35:38):
I know you mentioned earlier when we were chatting offline is when you were trying to build the go-to-market org for this stuff, you failed in some ways and there's some things you learned from that experience. What went wrong when you first tried to approach this?

Ray Cao (00:35:51):
Yeah, when I joined the company, there were only two people on the go-to-market side.

Lenny (00:35:57):
For the advertising business.

Ray Cao (00:36:00):
There are only two people and by that time the US and plus, I would say, Europe business together, we're having less than 80 people, but the business needs to grow and we need to hire really fast. The first mistake I made was... By the way, the goal is to hiring 100 people in a six month to support the go-to-market. That is the speed we're into. So that is early 2020 to middle of 2020. So within six months I need to hire, I would say, 100 people to supporting the global go-to-market structure and build everything. Then the first mistake I made just at the right point because we're trying to grow too fast and sometimes as a hiring manager I have to compromise the standard we're trying to hire. So that's the mistakes I think I made first and I think nobody should repeat that mistake is you need to always run for the quality rather than the quantity. So it's a easy mistake. You can fall into the trap because the business demands you to go faster. If you don't have the manpower, you won't be able to.

(00:37:11):
But I would say, believe me when I say this, this is a pain, right, when you have the wrong people on the team, it's not necessarily going to make you move faster, it's going to actually slow you down. So that's one of the biggest mistake I made for my first year when I created the team and not necessarily myself only. So also the managers reporting to me, they're facing the same pressure and then it's cascading down. So it's definitely the mistakes we made at early stage.

(00:37:43):
The second thing I can think about is really on the context, no control. It is not necessarily I'm born into, to be honest, because I was trained really like, "Hey, this is your box, finish your work here and then you're good." But the reason why I value that really the attitude more today is literally I failed at the very early stage of my time here because I was trying to creating that kind of a very black and white discipline for my team, "You can do this, you cannot do that." But technically speaking, that's literally slowing things down because a lot of times you can see that, "Hey, we're delivering our go-to-market strategy and we're good." But literally what you don't know is your goal is not to deliver the go-to-market strategy. Your goal is to land your go-to-market strategy with sales together. So if your job only is delivering, no, you're failed oftentimes because you're not really getting the market context, you're not even talking to your clients. So that was literally another mistake I think taught me how to really embrace the culture. Here is context, no control.

(00:38:52):
And the third piece, I think, it's also a mistake, really a hard moment for me as well is, for the past couple of years now, I've been managing a such big global organization, oftentimes even not myself, my managers, they don't have time to go detail and to go talk to the clients, which is very scary because again, if you don't know, you don't hear what is happening in the market, you won't know the details in the market, you won't be able to take the right movement or take the right approach to go to market or even give the feedback to the engineering team.

(00:39:32):
So it's very important that the leader at any level needs to be situational. You cannot always down to the wheat and you cannot really distance yourself from the reality. So you need to find the balance to really get engaged and also see yourself out there to getting, I would say, getting deeper into the problems, to identify the problems, and then you're able to perform even better. Because I don't believe one thing is you are the pure, I was the people manager. You cannot do that because when you do that, you're very, very at the very, I would say, position to really thinking about your career because you're losing your competitive edge from the other, I would say equivalent talents in the market.

Lenny (00:40:18):
I love these stories. I love stories of things not working out, so I appreciate you sharing these things. When someone doesn't work out at TikTok and they have a bad time and they get let go or they leave, what's the most common reason other than just they're not good enough? Is there something that just doesn't stick with people that often leads to this is not the place for me?

Ray Cao (00:40:36):
Yeah, I would try to really thinking about this in a different way. I can tell how people can be more successful here. So I definitely can see we're just talking about people being very curious and people are very, being nimble. They can be more successful here. At the same time, I think we have to admit one thing, join a start-up and join a rocket ship is a lifestyle. It is not necessarily a job you are working on from 9 to 5. So it is a different lifestyle and it is not built for everyone. So if you are not able to adjust your mentality towards some of the work that we are here to do and it's maybe not right fit for you. I'm not saying that that candidates is incapable. I think they could be capable in the other scenario for sure, but is the right fit? I think that is, I would say very much towards the situation or the company status in the market.

(00:41:33):
I can see a lot of people that they left and become very successful, too. So it is not necessarily that, "Oh, we think you're not good and then you're going to be not good for every single other company." That's not the case.

(00:41:46):
And one thing, and also this is my team culture I try to create is, I'm happy to say that when an employee reach out to me, say, "Hey Ray, I'm actually leaving the company," as long as they're telling me that they're going to a better place or a place that they can continue to grow their career, I'm happy for them because oftentimes my last question during my interview is, "What is actually your goal in the next three to five years?" And also I'd be really honest with them, say, "Hey, I don't think this is the job for you forever. Nobody going to work in this forever. If you can, great. But what is really your North Star?" I think that's the part that I would love to co-partner with you because I always believe one thing is it is not only about achieving the company goal, it's also achieving really the career goal or your employee's career goal together.

(00:42:41):
So I want to creating that culture here as well. So yeah, I think I'm doing so far so good. Most of my team members when they actually are moving on internally or externally, I'm able to say that, "Okay, that's a good choice. If I were you, I may probably do the same thing." It is actually a very good culture, I think, I would love to champion across.

Lenny (00:43:03):
On that first point, I'm also a huge advocate of just, "You'll be successful if you work very hard." I know there's a bit of a backlash at working along and thinking too much about work-life balance. And I feel like it's actually really important to work a lot and work long hours often to be successful, especially at a company that's going through this 'cause that's not going to last forever.

Ray Cao (00:43:22):
I think at the end of the day it's a personal choice. It's very much like a personal choice. If you are excited about this, if you want to grow together, yeah, this maybe is a good thing for you. And also depends on the life stage. So some of the people they want to actually getting more family time, I think that's also the right choice, too. But it just depends on your, I would say, your personal choice rather than if the company demands that. I mean, I cannot force my team to working long hours. I don't want them to working long hours. I think it's more about if you are able to deliver, right? If it requires a bit, a longer time to contribute, I think it's okay, but you'll also get rewarded very well too. So what's get in, what's get out. So I think it's, again, I do believe that this is the quality and also the value we're evaluating here as well.

Lenny (00:44:19):
And even though it's hard in the moment, I find that those are the times you remember most and most fondly in your career, when you just go all in, "I'm going to work really hard and do the best possible job I can do." Assuming that doesn't last forever, those end up being the most impactful, helpful to your career. Most proud moments when you're just like, "Look what I had accomplished." And so I'm on the same page. I want to talk about being successful on TikTok as a creator, as a business, as an advertiser. But a couple more questions real quick on how TikTok operates. You mentioned you do OKRs just briefly, is there anything that you've learned about being successful doing OKRs within TikTok? Maybe is there anything different that you all do versus how other companies think about OKRs?

Ray Cao (00:44:59):
It is definitely a company alignment that we are using OKR as our basically the system to make sure that everybody is working towards the same goal. I think definitely we have a lot of room to improve. So how often do you actually see your team able to go to OKR at the end of a quarter and also putting OKR really two weeks or one week before the beginning of a quarter? I have to say that shame on me. I sometimes delay it a little bit, but I think the goal is always there to using OKR system as our North Star to drive the behavior and also to align. Again, it's very important to align on the OKRs because I can see a lot of times the OKRs are putting in, but they are very siloed and that is not really necessarily helpful for the company want achieving really high growth. So I think it's very important that we know we don't take OKR as a shell, but we take OKR as its core is cross-functional alignment, cross-functional goal silo. So these are the things we're still continuing improving.

Lenny (00:46:06):
Is the way that OKRs work at TikTok, is there an OKR per team and they all kind of trickle up to a company level OKR? Is it less structured that way and teams decide if they want to use OKRs or not? How does that roughly work?

Ray Cao (00:46:17):
The structure is, basically the guidance is, using the key result to evaluating and then you put the steps in between. So that's how at least my team has been using this. I think the things that we can improve is the input and output. So the output is very clear, but what is actually the input sometimes is debatable, sometimes I have to say. And also oftentimes your output is other people's input. Are you able to connect the dots over there, too? Then that's actually the part that requires a lot of, I would say reinforcement alignment. Definitely we're getting better, don't get me wrong. We're totally not perfect, for sure. But I do see there is a lot of, I say momentum, to leveraging the system better. If you know other companies doing this really, really good, please shoot them my way. I would love to learn from them.

Lenny (00:47:07):
One last question here. You do planning, you have OKRs. Just briefly, how often do you all do planning? Is there a yearly plan that you put together and then a quarterly detailed plan?

Ray Cao (00:47:16):
Yeah, we do have annual planning cycle, but I have to say that our annual planning cycle is the baseline. We often do a lot of iterations in the middle of the year and also on a quarterly basis that we're able to pivoting really nimbly to really catering to the things that we see in the market. Some of the longer term strategy won't change, just like the platform we want to always creating, inspiring and also frictionless and immersive experiences for users. This won't change, but anything into the core of how do we realizing that you're always a consistent experiment over there. I cannot speak for the user product side, but at least from advertising product side that this is always the approach we're taking. And for the go-to-market part, that's also creating a very different behavior for us because oftentimes if we have a solid and kind of a static product roadmap, you can do go-to-market relatively easy, I would say, because everything is planned. But with a environment like that that basically make the go-to-market and also the product feedback loop much more short and faster.

(00:48:23):
So there's a lot of, I would say, pressure or actually put it nicely, there was a lot of innovative things that on the go-to-market side. Also on the sales side, the company or the teams need to actually do to make sure that we're able to catering for that. But again, this is a teamwork rather than only one side of the work. So far so good, I would say. A lot of things that we've been able to achieve within the past couple of years has been already proven that this approach has been working for us, but not necessarily they're always is perfect already, always room to improve, to make sure that we have more structural approach as well so that the market able to keep the pacing with us. We don't want to overwhelm our advertisers or our users either. So that's also the other part that we need to continue optimizing, too.

Lenny (00:49:12):
Okay. Let's talk about a different topic which is being successful on TikTok. So the way I think about it in my head is, there's how to be successful is just a regular human creator person. How to be successful as a business, trying to just create viral content and then being successful as an advertiser, which I know is where you spend a lot of time. So let me just ask, is there a tip you could share for someone to be successful, say aka go viral on TikTok? I imagine your answer will be just produce something people love and want to share and like. But I guess is there anything that could be tactically useful when you're creating content in TikTok to help you go viral?

Ray Cao (00:49:47):
I think if I know that I definitely will already become a very successful creator, I have to say. Our system is very much smarter than I am. I cannot trick the system, but I have seen a couple of good cases. So number one thing is that you have to really be unfiltered. I mean, you don't really need to be perfect on this platform. I mean that's the beauty of it. You can be yourself, you can really share the things that you like. And if you're really master at one thing that you're really, really good at and you want to showcase, this is the platform for you to shine because not necessarily that we are fully saturated and also all algorithm distributing the content in a very different way. Some of the other platforms they are, I would say like a people-based or friend-based.

(00:50:32):
I think for us it's purely based on actually you're creating something that everybody want to see. So let's see if we can distribute it more. So I think continuously to bring new content to this platform and testing and finding your own competitive edge going to be very important as a successful creator. And most of our creators have been doing that. And I can see some of our biggest TikTok stars, they're literally practicing this every single day. And I do think that creativity and that part of, I would say, getting the nuances is the key part that to be more successful on the T TikTok community.

(00:51:11):
And the second thing is it's including also for brands as well, because I consider brands as our creator as well. They really need to embrace the culture and the community here to really listen and understand what are the user behaviors on the platform to understand what do they like to see. And also the messages or the presence could be very different from your other media channels, or as a creator, it could be very different from your other, I would say, platforms.

(00:51:40):
So that's the other thing that it's going to be challenging because for them to shift in the mindset. But I do think that definitely was trial. Some of the, I would say, our early adopters has already been proven that when you do embrace the culture here, you're able to acquire a ton of different kind of a user or the audience to your channel and you can show a different side of yourself as well. So yeah, I've been trying to do that. I have not really finding my competitive edge I have to say, but I'll keep trying.

Lenny (00:52:14):
Is there an example you could share of someone that has done that really well, either be really authentic and also embrace the community of a business specifically that has done this really well and has taken off not as an advertiser?

Ray Cao (00:52:25):
There was one creator I remember called Sheba. She's a singer and she is able to caught my eyes because she was able to basically rap and also during some of the songs cover in a very different way because she's a minority and she was able to basically using her minority identity as actually everybody was thinking, "I'm supposed to be doing Bollywood music, but actually, you know what I'm not. I'm doing a lot of very just hip hop and also the music that people may think like I'm not good at."

(00:52:59):
So it is pretty fun to watch that kind of a comparison or the contrast between a creator and also she's able to put a lot of original music on the platform to really inspire more people to do the same thing. There's another music, I would say TikTok creator. So he was pretty big on the other platforms, but the total approach from him is he's basically changing the lyrics, make it very relatable as a personal life. Because for example, he can totally change the lyrics from a old Backstreet Boys song or Nsync song to make it related with his daily communication with his wife. Make it really relatable and fun. So these are the things I think is very unique to us. If you are able to test and find something new like that, you're able to find a new batch of audience and even go viral on the platform.

Lenny (00:53:49):
So then switching to the advertising network, a lot of listeners here are thinking about, I imagine, advertising on TikTok. There's kind of classically been Facebook and Google are the two places to do run paid ads. Paid ads are a huge growth driver for tons of companies. It's one of the easiest you could say, or one of the most traditional way to grow. TikTok obviously is emerging and has already emerged as one of the newer advertising networks. So there's a lot of people thinking about how do I succeed as an advertiser on TikTok. So what advice do you have for people? One, who's it best for? I imagine TikTok isn't the best place to advertise for every sort of business. So what sort of businesses are best aligned to be successful on TikTok? And then just what advice can you share to do well as an advertiser on TikTok?

Ray Cao (00:54:37):
Yeah, I see a lot of really different type of advertisers already find their success on the platform. One thing that they actually can do that is really due to a couple of things that they're doing. Number one is, like I said, they're embracing this platform. They actually do a lot of things is TikTok first. I have a couple of advertisers. They have actually creating their own internal creative team just dedicated for TikTok. So they actually produce a ton of creative every single day to actually test and learn to understand the platform and understand the community they are engaging with. So I would say leaning in is the first part. It's harder, but it is not that hard. As long as you try it, you'll feel that every single day is getting easier. And also we make a lot of tools to make things easier for them as well. Like creative, we have also a lot of resources on the platform, the creative hub and also we have creative analytics to help you. So these are the things that we're able to basically help the advertiser to leaning in more.

(00:55:42):
The other angle to leaning in more is test and learn. A lot of times that people don't know how to really run ads on this platform. Google is very much search, like search fronts. They are really leading on the intent graph. And Meta is really on the people graph they're making. I mean TikTok is the content graph. It's very different, I would say machine compared to the other two. And it requires different way to optimizing and to leveraging the tools we have. So if you're applying the same logic from Meta or Google into TikTok, not necessarily you'll be able to see a great success, I have to say.

(00:56:27):
So you have to really get to the detail and to learn how you're operating this platform at the very beginning. Of course, like I said, we're trying to make things as simple as possible because we strongly believe that an advertiser's job is to taking care of their own business and our job is to service them. So we definitely make things a bit easier and along the way, but still it's a little bit learning for advertisers to change their mindset when they engage with us the first time. And I can see that again, for example, last Q4, I can see a lot of advertisers taking this approach to really listen to us and understanding what is our best practices. They actually see a very successful Q4 on the platform. So I do think that if you want to do more, just do more test and learn with us and to really understand the impact from TikTok.

Lenny (00:57:17):
Just to understand this point about versus Instagram, I think a lot of people probably run on them on both platforms and try to see which one's working better. Your point is the same content won't work as well on one versus the other. So just so people understand what the main difference there is. I know you talk about there's the friend graph versus TikTok just spreads it all over and anyone can see it. You don't have to be friends and it's really good at getting content out. So what is it that you would do differently if you're making an ad video for Instagram versus TikTok?

Ray Cao (00:57:44):
I think the TikTok video, it's more about the backend settings, right? So how often do you actually changing creatives? I think for us it is actually pretty... you want to actually test more creatives on this platform and see which one is actually working. And then we also have really detailed guidance on how do you set up your campaign structure to make sure that you're able to be more successful on the platform. So these are, I would say, the basic hydrangeas we talked about. You can see these guidance are very different from what Meta has today or even Google has today because we're just basically different platforms. And oftentimes you can also hear that we requires a bit more real time react on the platform due to some of the trends we have seen.

(00:58:30):
So that is the part I feel like if advertiser wants to engage more with really the sales team and they're able to provide more guidance to you and you're able to see more success there. But a lot of things will be counterintuitive I would say, because the intuitive you have learned is coming from the other platforms, but technically we're not. So a lot of things that, "Oh, this doesn't make sense to me, but why don't you try it?" And we make actually that really easy because we are sharing a lot of, I would say added credit to intensify incentivizing our advertisers to try it at the end of the day that hopefully they can see the result is proven itself.

_[123 additional lines trimmed for context budget]_

---

### The art of product management | Shreyas Doshi (Stripe, Twitter, Google, Yahoo)
**Guest:** Shreyas Doshi | **Date:** 2022-08-25 | [YouTube](https://www.youtube.com/watch?v=YP_QghPLG-8)  

# The art of product management | Shreyas Doshi (Stripe, Twitter, Google, Yahoo)

## Transcript

Lenny (00:00:03):
There's no one out there today who shares more wisdom, more consistently on the art of product management than Shreyas Doshi. Shreyas came out of nowhere a few years ago and started tweeting gems of insight about building product and the role of product management, and rightfully so, has built a huge following on Twitter. What I love about Shreyas is that his insights are often framed in really memorable and interesting ways and they're often contrarian and not ideas that you've heard elsewhere. Shreyas has worked at some of today's most important tech companies, including Yahoo, Twitter, Google, and most recently Stripe, both as an IC and a manager. And his advice is always rooted in his real life experiences at these companies.

(00:00:48):
In our chat, we focus on five topics and go deep on them. We talk about the power of pre-mortems. We talk about how to best use your time as a product manager. We look into the three levels of product work and how getting them wrong often leads to tension on your team. We dig into why most execution problems are really strategy problems. And we talk about a common pitfall in prioritization. And if you listen to the end, we actually throw in a bonus topic. I really appreciate that Shreyas made the time for our chat and I cannot wait for you to hear it.

(00:01:29):
This episode is brought to you by Coda. Coda is an all in one doc that combines the best documents, spreadsheets, and apps in one place. I actually use Coda every single day. It's my home base for organizing my newsletter writing, it's where I plan my content calendar, capture my research and write the first drafts of each and every post. It's also where I curate my private knowledge repository for paid newsletter subscribers. And it's also how I manage the workflow for this very podcast. Over the years, I've seen Coda evolve from being a tool that makes teams more productive to one that also helps bring the best practices across the tech industry to life with an incredibly rich collection of templates and guides in the Coda Doc Gallery, including resources for many guests on this podcast, including Shreyas, Gokul, and Shishir, the CEO of Coda. Some of the best teams out there like Pinterest, Spotify, Square, and Uber use Coda to run effectively and have published their templates for anyone to use.

(00:02:23):
If you're ping ponging between lots of documents and spreadsheets, make your life better and start using Coda. You can take advantage of a special limited time offer just for startups, head over to coda.io/lenny to sign up and get a thousand dollars credit on your first statement. That's C-O-D-A.io/lenny to sign up and get $1 in credit on your account.

(00:02:49):
This episode is brought to you by Productboard. Product leaders trust Productboard to help their teams build products that matter, from startups to Industry Titans. Over 6,000 companies rely on Productboard to get the right products to market faster, including companies like Zoom, Volkswagen, UiPath and Vanguard. Productboard can help you create a scalable, transparent and standardized process so your PMs understand what their customers really need and then prioritize the right features to build next. Stakeholders feel the left too with an easy to view roadmap that automatically updates so everyone knows what you're building and why. Make data-driven product decisions that result in higher revenue and user adoption and empower your product teams to create delightful customer experiences. Visit productboard.com to learn more.

(00:03:42):
Shreyas, the man, the myth, the legend, thank you so much for joining me and for having this conversation.

Shreyas Doshi (00:03:48):
It's great to be here, Lenny.

Lenny (00:03:49):
So we strategized about how to make this podcast as concretely useful and actionable for as many people as possible. And so, we decided to do is instead of a regular interview where we talk about a lot of stuff, instead we're going to go deep on five of your ideas, teachings, lessons that you've shared on Twitter that have stuck with me, and I know have resonated with a lot of other people and we're going to call it the five big ideas from Shreyas Doshi. Does that sound about right?

Shreyas Doshi (00:04:14):
Sounds great.

Lenny (00:04:15):
Okay, cool. So before we get into that, before we get into the meat of all this stuff, you share a lot of wisdom on Twitter, but you don't share a ton of about yourself and your background, where you grew up, where you're born and things like that. So I'd love to learn a little bit more about the human that is Shreyas. And so, maybe we start there, where were you born, where'd you grow up, what'd your parents do for work, what did you want to be when you grew up?

Shreyas Doshi (00:04:36):
So I was born in Mumbai, Bombay, India, and I lived there for the first 21 years of my life. I actually did not really even get to see many parts of India while I grew up in India and basically just was in Mumbai the whole time. And then I moved here to the United States for graduate studies at age 21. My parents, my father was a businessman, and so, he started his own business. He manufactured spices and marketed them. So growing up, I saw him work on packaging and pricing. And when he was short on staff, I used to be packaging the spices into the little box or creating some marketing material for him, not the creative part, but the grunt work. So I grew up in that environment where the lines between what was my dad's business and our personal lives were very blurred.

(00:05:32):
My mother just growing up as a homemaker, and so, my dad was largely just busy and all consumed in his business. And I ended up spending a lot of time growing up with my mother. And so, both of them have had a pretty significant influence in different ways, but both significant influence on who I am. When I grew up, I changed that a lot. I think when I was very young, one of my uncle is a doctor, so I saw him and I was like, "Oh, maybe I should be a doctor." And at some point later, I changed that. In high school, I took French and I ended up being really good at it, surprisingly good at it, and I was very passionate about it.

(00:06:10):
So for a while, I was thinking, "Oh, I'll maybe teach French after graduate from college. Maybe I'll go to France, learn the language a little more. And maybe I'll teach French." That lasted for a few years and turned out that I ended up not pursuing that, and instead, got a degree in computer engineering. Partly, I think because in India back then, if you were good at science and mathematics, you would usually take up engineering. And so, that's what I ended up doing. I was also quite passionate about computers, so maybe that was part of it. But once I started on that path, it became much clearer what I wanted to do.

Lenny (00:06:50):
How's your French these days?

Shreyas Doshi (00:06:51):
Very bad. Sad to say, my son is now taking French and I am just embarrassed at my inability to assist him in any way, other than to point out some conjugation errors.

Lenny (00:07:04):
So you said you studied computer engineering, that's what you moved to the US for, how did you move from that to product?

Shreyas Doshi (00:07:11):
So, I started my career as an engineer, or well, backtracking, so I completed my undergrad in India, came here to the United States to pursue a PhD in computer science. About one month in, I realized that PhD in academia wasn't for me, so I decided that I was going to drop out of the PhD program. And once I dropped out, this was like 2001, 2002 so the climate was very different, there were basically no jobs for tech people. Certainly there were no jobs for people who required a visa, which I did. So it was very difficult, but I ended up working as an engineer at a couple of startups and that started my career in tech. I was an engineer for about four or five years. And when I moved here to the San Francisco Bay Area, I got a little taste of product management.

(00:08:00):
So, I was part of this team that used to be Loudcloud, and they were acquired by a larger company EDS at that time, so it was a startup team within a larger organization. And I was an engineer there and I just started doing some product work. And I found that my managers over the time would send me to customer meetings. We had an internal product, so these were internal customers. And I thought it was a little surprising because I was fairly junior and I was an engineer, but I was like, "Okay, I'll just go to the customer meetings." And I really enjoyed that. I really enjoyed understanding what our customers were trying to do, helping them out. I also enjoyed thinking about creative ways to solve their needs and whatnot. So, that was my taste of product management.

(00:08:40):
For about a year, I was doing the product job without having the title and I was also the engineer. So I was in this great state where I'd figure out what needed to be built and I would just build it myself. So, that's how I started. And at some point during that one year, I realized that while I was a good engineer, I was perhaps a top 20% engineer. I realized that I would never be a great engineer, that I would never be a top 10% engineer because I saw those engineers, the fortune of working with them, and I just could tell that I couldn't be that. And I increasingly got interested in this product thing, so I said, "Okay, let's try out this product thing." And so, that's really what started my product career. And I think what I have to be really thankful and grateful for there is the people who gave me a chance to do the product work and there were many people involved. And so, I think without their support, it would've been much harder for me to become a product manager.

Lenny (00:09:34):
I didn't know that you moved from engineering to product and your journey is very similar to mine where I was also an engineer. And once I got to Airbnb, I was like, "Okay, I am not good. And I will not last as an engineer at a company like this. And I should think about what other options exist." And it worked out great. And so, I wonder how often that happens of PMs moving into PM because they aren't going to make it as an engineer.

Shreyas Doshi (00:09:57):
I think it might be a common occurrence because engineering is a really great job, particularly on empowered teams, as an engineer, you can do a lot. You don't have to just write code, but you can do a lot. And so, I also think it's a great place for people to start their career if they have a technical background and if they enjoy the part about building software. Because sometimes people will ask me, "Hey, I'm doing this technical degree, whether it's computer science or something else, but I want my first job to be product management." And I often respond with, "Tryout engineering because, again, in many companies, fortunately these days you can do a lot more than just the core engineering job. And so you get exposure to many different things. And once you do that, you can decide what path to pick."

Lenny (00:10:44):
It's such a bonus to have that background as a PM. I wanted to go back, so you mentioned that you worked at Loudcloud. I had no idea. That was Marc Andreessen's second company, right?

Shreyas Doshi (00:10:53):
Yes. I joined that team. Again, this was a time when there were very scared jobs in the valley and I was interviewing with them for nine months or something like that, and they had just been acquired by EDS. So they split into two companies. One got acquired by EDS and the other became Opsware, which was the product company. And so, I joined the Loudcloud part of that organization.

Lenny (00:11:17):
Got it. Is there something that you took away from that company? Was Marc Andreessen still working there? And I think Ben Horowitz also.

Shreyas Doshi (00:11:24):
Yeah, they were still there, they were working on the Opsware side. Again, because even though I was hired as an engineer, the non-engineer task I was given was to manage a relationship with Opsware because the way that split worked is EDS would use Opswares data center automation technology, and my team was responsible for deploying and supporting that technology for EDS. And so, I was given this role of managing the vendor relationship and I have no idea. I'm in my early 20s, I have no idea how to manage vendor relationships, but I ended up doing that.

(00:11:59):
And as part of that, I got an opportunity to work with many folks over at Opsware, including folks on the leadership team there. And that was my first experience of what a really highly talented and energetic team looks like, both on the Opsware side, like I said, I worked with a number of people there, but also on the former Loudcloud side who were my team members. And that magic, a very high caliber team, people who really great at their job and brought high degree of energy and collaboration to their work. I was just lucky to have been part of that team early on.

Lenny (00:12:32):
And then following that, you worked at a bunch of really important well run successful companies, Stripe, Twitter, Google, Yahoo, what's one thing you took away from each of these companies that you've worked at that has stuck with you? You share a lot of this on Twitter, but if you just think about somebody took away from each of these companies or even the founders that ran these companies, what might those be?

Shreyas Doshi (00:12:53):
Yeah, let's do this rapid fire style because you know me, I could spend an hour just talking about this topic. But just starting with Yahoo, I think I learned the importance of building multiple services under a single account. I think that was the one Yahoo ID was such a powerful thing. It wasn't easy to pull off back in the day and Yahoo was perhaps the first company that pulled it off really well. And so, that idea of bundling under a single account, which then Google really did extremely well later on was something that I got to experience very first hand because I was working on the identity team at Yahoo. Google taught me the.

Lenny (00:13:33):
Real quick on Yahoo because it makes me think about it. I remember they tried to do that with Flickr and they had a bunch of trouble with that, people on Flickr didn't want to log in with Yahoo, is that right?

Shreyas Doshi (00:13:42):
Yes. That's the story of every acquisition that are some raving fans of the service that are perhaps not entirely happy about their beloved service being acquired by a large company. In fact, we encountered this at Google as well. If you remember YouTube accounts used to be separate from Google accounts or Gmail accounts. And at some point, Google decided that you should be able to use your Google account to log into YouTube, and also over time, that everybody who uses YouTube should have a Google account. So they went through a multi-year migration of accounts, and they had similar backlash. The interesting part though, is nobody remembers that now, people happily use YouTube. So this is one of those things where sometimes it's painful in the short-term, even though it might actually be the right answer over the long-term.

Lenny (00:14:36):
Great advice. Okay. Sorry I cut you off. Google.

Shreyas Doshi (00:14:38):
Yes. Google, I think the main thing I learned was the power of thinking really big. And I know it sounds like a platitude, but really big. And I only actually realized that when I left Google and I started working with the other teams and these were all capable teams and I was struck by how many teams just limited the potential of what they could achieve. And I think Google helped people think big by default. And so, I think the six years I spent at Google really helped me understand that really well and just make it a normal part of how I operated. So that was really useful for me.

Lenny (00:15:18):
Is there an example at Google that some of you worked on that was like, "Holy shit. This was going to be big or let's think bigger about this"?

Shreyas Doshi (00:15:25):
Well, as with anything, there's pluses and minuses. So I worked on the ads team at Google for a number of years and there was this unwritten rule of thumb that, hey, if it's not going to generate more than $100 million in revenue, it's not worth talking about it. Because the ads business was growing so fast and was so large that we would regularly not pursue opportunities that were just quote $100 million. So why do that? That's because Google had access to billion dollar opportunities for it as business. So they were very clear on pursuing the big opportunities. And in some cases, these opportunities were not obvious, so we had to create those opportunities. If you think about some of the innovations Google brought over the years in monetization, including things like video ads and whatnot, those were not obvious opportunities, but Google decided that it wanted to pursue those big opportunities.

(00:16:22):
And in order to do that, it had to sometimes just let go of these seemingly smaller opportunities. So that tendency to think about, well, yes, there is $10 million business here, but can we make it $100 million business? Or there is a $1 million business here, can we make it a $10 million business? What does it take to make it bigger is a habit, I think, that got ingrained for me at Google. Now, of course, there's the other side of it, which is, I think, Google missed out on some trends simply because of this filter or this high bar where sometimes it's not clear if something is $100 million opportunity or $1 billion opportunity. So that is a downside of this. What I mainly took away is for instance, even at Stripe, when I joined, I was just thinking a lot bigger about the business. I was responsible for Stripe Connect and that helped us make different decisions about what to prioritize and at what pace to go after it. So, that was Google.

(00:17:21):
Moving on to Twitter. I think at Twitter, the main thing that struck me with all the challenges, they had infrastructure challenges and also some challenges around leadership and culture is just the stickiness that comes with combining network effects with core product differentiation, because Twitter had both. We talk about network effects all the time and I don't have much more interesting things to add beyond what's already added. But this combination of core product differentiation, because if you think about it, there's still no product like Twitter, despite now being a long time since the product was launched. And that core product differentiation combined with network effects has what enabled Twitter to have the staying power it's had. And I think unless something terrible happens, I think Twitter will be around for a really long time. So, that's something I got to observe very closely when I worked at Twitter.

(00:18:13):
And then at Stripe, I think the main thing I took away was that when you combine high energy sound judgment, low ego and small teams, you just get magic. And so, Stripe wasn't by any means flawless, but I saw that combination of high energy sound judgment, low ego and small teams more at Stripe than any other place I've been at. And so, that was very impactful and my growth and thinking as a leader. And I can go on with the founders, because I know you had asked that question.

Lenny (00:18:45):
Let's do it.

Shreyas Doshi (00:18:46):
Okay. With regards to the founders and what I learned from the founders, Yahoo, I didn't work much with the founders. At Google, I had some interactions. I was in meetings with Larry, Sergey, Eric Schmidt. And I think particularly if I were to pick one thing, I really appreciated Larry's strategic insight and particularly his ability to simulate the future to make better decisions. And so Twitter, I just overlapped very briefly with Jack's comeback as CEO back when he came back. And I think I was struck by his ability to listen and ask great questions in a few meetings that I was with him. And so, I was really impressed like he would just listen a lot more than you would expect, say, the CEO to listen. And then he would just ask one vital question and that's something I've tried to use in my leadership style ever since I saw that.

Lenny (00:19:38):
Is there an example of that or a story of that happening that you think about?

Shreyas Doshi (00:19:42):
I forget the details and they're not that important anyway. But there was a time when we were discussing a potential acquisition and I was on the fence on that acquisition, it would be something that my team would acquire, Jack was in the room. And I remember we went through as is common in many corporate settings. We went through all the pros and cons and all the intellectual arguments and the strategic arguments and the metrics arguments and all of that. And Jack was just listening through all of that. And then I remember very distinctly, he asked me one question which was something to the effect of, how does this make our users love Twitter more? Simple question. But then at that point I realized, yeah, we never really talked about that because we were so engrossed in all the other stuff. And we talked about it as a proxy because we were talking about metrics and impact and integration and those sorts of things.

(00:20:40):
So I still remember that. I still remember him asking a simple question. Frankly at the time I did not have a good answer to that question. So that was a lesson for me to get more rigorous about my own thinking.

Lenny (00:20:52):
That's a question that a lot of PMs would hear and be like, "Oh my God. Come on, man. We're trying to move some metrics here." But I love that you took that as like, okay, I really find this really important. And this is a really important question to think about and as a lesson of how to approach this kind of stuff. So I love that. I think you were going to talk about Stripe too, right?

Shreyas Doshi (00:21:08):
Yes. Stripe, I worked a lot with Patrick and John. John was my manager for a while. And from John, I learned a lot about marketing. John is a master marketer. Among many other things that he's absolutely great at, he's just a great marketer. And I just learned a lot about how to think about talking about the product in terms that, again, obvious stuff, but talking about product in terms that customers really understand. And then sometimes emphasizing things that we as product people might not think are really important, because maybe we didn't spend much time on building it, and we want to talk about things that we spent a lot of time that are truly innovative, etc., etc. And John would often make, again, these observations about, well, if we just talked about the product in this manner, that will likely resonate a lot more with customers.

(00:22:00):
And that got me thinking a lot about how I need to reframe my approach to basically separate the effort involved in building something with the effort you want to put behind talking about said thing. And that doesn't have to be the same features that you talk about. So, that's something I learned a lot working with John. From Patrick, I think the main thing I learned was just how to think and communicate more clearly. Patrick did that extremely well. And then overall from both, I learned the importance of setting the culture you want, simply by consistently being an example of the behaviors you want to replicate in the organization. So instead of talking about values, I saw both of them just live the values that they wanted the company to replicate, especially as the company was scaling. So, whether it's a culture of being user centric or it's a value around humility, they just lived those values so consistently. And I think that consistency spoke louder than anything that you might write on a poster on the office walls.

Lenny (00:23:08):
It's just hearing you describe all these companies and all these founders that you've worked with, it's pretty incredible to set of experiences that you've had and the primordial soup in which you became a PM. And it explains a lot about how you're able to squeeze so much wisdom and insights about the role of product management and the art and skill of product management, because you've seen so many ways of doing it and so many companies that have done in different ways. And so, it's a good segue to shifting to talk about the five big ideas. The first is around this concept of pre-mortems, this is something that stuck with me when you tweeted it. I think it was a couple years ago at this point and I see it come up occasionally in your tweets and amongst people chatting your super follower threads. And so, I also like that there's something you can actually implement and act on pretty quickly and see impact. And so, curious to hear your thoughts on this idea of pre-mortem just unpack this idea for folks.

Shreyas Doshi (00:23:58):
We're all familiar with a post-mortem or as they call it in the military, I think, after action reviews. So every company I've worked at, we've had some form of post-mortem when a launch had problems or an initiative did not go as planned or we suffered an unacceptable system downtime. Somebody would say, "Oh, we need to post-mortem that." And over the years, I really saw the effectiveness of a post-mortem. Some really great insights came out of a post-mortem about what went wrong and what we could have done better. And as I saw the effectiveness of a post-mortem, that's what made me wonder, why do we need to wait until after things go wrong? Because why can't we extract some of these insights before they go wrong? And it was around that time that I discovered the idea of a pre-mortem. I learned about it from an Harvard business review article written by Gary Cline.

(00:24:50):
And the idea is simple, which is when you are working on an important project or initiative, you get together with your team early on in the products or the projects' life to see in advance what could go wrong. And the way I describe a pre-mortem is that if you do a pre-mortem right, you will not have to do an ugly post-mortem. You might still do a post-mortem to learn, but odds are very high that it is not going to be a bad post-mortem. And the genius of the pre-mortem ritual is the initial prompt. So it's not just about like, well, what could go wrong? The initial prompt is the genius, which is the prompt starts with, imagine this project that we are working on has failed six months from now, or this launch we are doing has miserably failed. Let's just all imagine that. Now, let's work backwards from there and ask ourselves what went wrong, what could have contributed to this utter failure.

(00:25:47):
And that's how a pre-mortem meeting will start. The leader will start with this prompt. And then the way the meeting goes is you ask your team members to share what could have caused this utter failure, and the magic of this type of approach where you work backwards from a failed outcome. A hypothetical failed outcome is that it just somehow enables two things. One is much greater psychological safety for team members to talk about things they're concerned about, but that they were just hesitant to bring up because nobody likes to be negative in modern organizations, everybody wants to be optimistic and positive. So a pre-mortem setting gives everybody the license to actually think about what can go wrong. So, that psychological safety is a big, big factor in why a pre-mortem works.

(00:26:40):
And what I've found is at Stripe, I did this regularly with launches that my team was involved in. Sometimes some teams or some people were just surprised or skeptical like, how is it really going to work? And then we go through the pre-mortem meeting and there's a whole process that we can talk about. But as we complete the meeting, I ask everybody, so how did that go? And just everybody is smiling, even though we've spent say 30 minutes or an hour, just talking about terrible scenarios of things that could go wrong, but everybody's feeling a little lighter because its great catharsis for them. So that becomes really important.

(00:27:14):
And the last kind of thing I found with pre-mortems now that I've done them with various other companies as well, that I advise and whatnot is the shared vocabulary and the shared vocabulary that you get about being able to talk about things that will fail. So I have a specific approach, which is I ask the team to talk about three things. Each member on the team should bring up three things. One is a tiger. So you can bring up tigers in the shared doc that we create. And a tiger is a threat that will actually kill us, just like a tiger would. So these are actual problematic things that could be really harmful to the product or the project. So, that's a tiger.

(00:27:51):
The other is paper tiger. So this is a seeming threat that others might be worried about, but you're not worried about. So that's the paper tiger. And then the last one, and I think this one was also used at Airbnb in other ways is elephant. And the elephant in the room that nobody is talking about. So it might not be a tiger, it won't kill us, but you're still worried that we are not seeing reality as it is that. And so, an elephant could be like, well, we are assuming that just because we launch this and do a bunch of PR that we'll get users, but are we sure we're going to get users? That's the elephant in the room that nobody is talking about that, again, this gives you that psychological safety to bring it up.

(00:28:28):
And then what I noticed as I ran pre-mortems is that in future meetings that the team had where I wasn't even present, people started talking about, "Oh, I have this tiger. Can I bring up this tiger?" And all of a sudden it became okay for people to bring those things up, which I think is perhaps the best part about a pre-mortem is that shared vocabulary.

Lenny (00:28:45):
Such a simple idea that is clearly going to benefit you and your team. And it's interesting that people don't often do this, or haven't even thought about doing this. And so, just to get a little bit deeper, how do you actually execute this meeting? Who do you invite? What are the questions you ask? When exactly do you do this, that kind of stuff?

Shreyas Doshi (00:29:02):
And so, as I started doing pre-mortem, they got more and more popular at Stripe, other teams started doing them, and then afterwards I helped some startups also do pre-mortems. And at some point, I decided I should just write down my template for pre-mortems. So I worked with the folks at Coda to create a Coda doc, which you can find, and we can put in the show notes if possible, basically that's an entire template for how to run pre-mortems using this method that I talked about, including tigers, paper tigers, elephants, all of that. The main thing about a pre-mortem is to include people from every function that is going to be involved in, say, if you're doing a launch. And so, if it's a really large launch, sometimes I will separate it into two groups. One is everything related to the engineering side of things. Usually the engineering team is fairly large, so you can bring in every engineer. So, that's really important. Every engineer needs to be in the meeting, and so, it might be a meeting of 10, 15, 20, whatever engineers, and maybe a PM, maybe a design counterpart, and so on.

(00:30:07):
That's just focused on the product engineering side of things like what could go wrong. And then again, for a large launch, I like doing a separate pre-mortem for the go-to-market side. And so that will involve sales team, support team, marketing team, involve design team. Some of the core engineering leads will also need to be at that meeting. Over there, we'll talk about more of the go-to-market risks. So that's what I like to do for a very large launch.

(00:30:35):
For a smaller launch, I just like to do one meeting where everybody is present. And like I said, start with the prompt of, imagine this has failed. So as the pre-mortem meeting leader, it's my responsibility to share the prompt. And then I like doing these pre-mortems where we alternate between speaking and quiet time. So I'll share the prompt and then I'll say, okay, now the next five minutes or the next 10 minutes is quiet time where I already have that template, like the quarter doc where people start entering their own tigers and paper tigers, and elephants in a way that nobody else sees. And so, people do that, and then we go around the room and share.

(00:31:11):
And the one other innovation I added as I did this often was also, after people shared, I ask people to pick the tiger that they find more scary, but that somebody else mentioned, so not their own tiger, but some other tiger that somebody else mentioned that they found more scary. So, that ends up being people basically are voting. And then as the pre-mortem leader, it's my responsibility to take all of that output that the team has generated in this document and then prioritize. Because again, the point is not to solve every problem, the point is to identify threats that we are not talking about openly or that we might just be missing, or we might be assuming that somebody else is going to deal with it only to find nobody was thinking about it. So then I like to create a pre-mortem action plan and then share that with the team and keep myself as the leader accountable for actually making progress on it.

Lenny (00:32:04):
Having started doing this, have you noticed a less need for post-mortems, basically projects failing less than having less problems? What impact have you seen executing on this idea?

Shreyas Doshi (00:32:13):
Absolutely, I've seen us identify certain issues that just wouldn't have come up and likely you can't really run a simulation and see what that actually looked like in real life. But those likely would have resulted in a problematic situation afterwards. A great example is sometimes you'll see a company announce something and they have massive backlash. And then one reasonable observer might say, "Well, how did this company miss this?" because what happens is they have the backlash, then the company realizes, "Oh, we have this backlash." Then they start doing damage control. They sometimes might even backtrack and undo whatever they did. They'll say, "Sorry, we didn't think about these issues. Give us some more time and we'll come back, and we'll perhaps relaunch the feature, but in a better way."

(00:33:00):
To the casual observer, it may seem like that it should have been obvious and sometimes it's not, but oftentimes I agree, it should be obvious to these teams what issues these things are going to cause. In fact, it is obvious to some team members, but the problem is that they perhaps haven't created that psychological safety and that vocabulary to be able to talk about it in an objective way and to decide with intent, are we going to solve for this or not? So I do see a lot of those scenarios in our industry, which end up just actually wasting a lot of time. Whereas pre-mortem is a very inexpensive way to see these things because all it is is one meeting followed by some work that the leader needs to do to prioritize, followed by some mitigating actions, which you would've had to take anyway. So that's why I'm a huge fan of pre-mortems is, it's one of those very low downside, but very high upside things that I've experienced.

Lenny (00:33:54):
I'm excited to see those template, I haven't seen yet. I don't know that you put one together, so that's awesome. And we'll link it in the notes of this episode. I want to move to our second big idea, which is about something you've called LNO framework, which is all around prioritizing your finite time as a PM and as a team. And so, I'll just kind of turn that over to you to share what that's all about.

Shreyas Doshi (00:34:15):
Yes. And so, I'm going to share a short personal anecdote related to the LNO framework, which is that when I just joined Google as a relatively new PM, this is back in 2008, for the first three years, I was overwhelmed and stressed. And that was because, one, I was a new PM in this really high performance environment. I was working on some important products and launches and I just had too much to do. And I looked back at that time and it was perhaps the most stressful time of my career, where I would long hours, etc. But even at the end of the day, I'd feel highly dissatisfied because my to-do list was endless and I wasn't able to make a dent on it, and I was also a little bit of a perfectionist, so I was like, "No, no, no, I need to do this well."

(00:35:02):
It was just constantly I would come home and talk to my wife and basically just complained to her about how I'm not able to make progress or as much progress as I want, then that was accompanied with not being able to sleep very well because I was concerned about how much output I was producing and whatnot. And so, again, very stressful time in my career. And then things changed when I discovered the ideas related to this LNO framework in a block post. Unfortunately, I can't even find that block post somewhere, but it had some ideas that I took and then created this LNO framework on myself, which is essentially that as a product manager or as anybody in a creative high impact high leverage role, all your tasks are not created equal, there are actually three type of tasks that you end up doing in such a role.

(00:35:56):
So there are L tasks which are leverage tasks. And the L tasks are such that when you put in a certain amount of effort, you get 10X or 100X in return in terms of impact. So those are L task, leverage tasks. Then there are neutral tasks, so that's N. And those are tasks where you basically get what you put in, or just a little more than that. So you put in 1X and you get 1.1 X, those are neutral tasks. And then there are overhead tasks where, again, in terms of impact, you get back a lot less than you actually put in. And it turns out that many people who are ambitious or are perfectionists like myself by default treat each of these types of tasks the same way, and therein lies the problem. So this was the epiphany for me back at Google when I discovered some of these ideas.

(00:36:47):
And what I realized is that among the things in my to-do list that are actually only very few L tasks, and so, it made sense for me to focus a lot on those L tasks, to take on those L tasks when I was feeling most productive, most energetic during a certain time of the day.And for the L tasks, let my inner perfectionist shine because I'm going to get so much more in return. It makes sense for me to spend that time on that PRD, for instance, related to an important feature that will meaningfully impact our revenue. I'm going to spend more time on that than I ordinarily would. So now, where does that more time come from because it cannot come from just working more hours? Well, it comes from spending less time on N tasks and O tasks. And so, there are some tasks that you do. Classic example of an O task is say an expense report. Sounds silly, but I used to try to make my expense report really good.

(00:37:47):
And sometimes that made no sense like, "No, no, no. I need to do that." And again, this is the silliest example, but there are many examples. And something I realized is that the same type of activity can actually be either an L task or an N task or an O task. So what's an example? So say a classic PM task activity of filing a bug report. And so, many companies have these bug templates, etc., etc. that you use to file a bug report. Well, it turns out that filing a bug report depending on the situation, depending on what type of bug it is can actually be an L task high leverage task, and over there you want to file a very detailed explicit bug report. And in other cases, might actually be an O task where you don't fill out the template that diligently and you don't add 15 screenshots with annotations, instead, you just have one screenshot and you hit submit on the bug report.

(00:38:43):
So that shift. Usually for the same type of activity, we provide the same type of engagement. The last example I'll use to illustrate this is taking notes. It turns out even taking notes, taking notes synthesizing them, and then sharing them can actually be an L task, an N task or an O task, depending on what type of notes they are. So, after I understood this, previously, I would just send all notes. I tried to make them really good, which took a lot of time. But then I realized, well, this is a meeting where, yes, I need to send notes, but again, it's like, it's just standard stuff, I just need to quickly list out. People need to really know is the three action items that came out of the meetings who owns them, that's it.

(00:39:23):
And it is not about something highly strategic or controversial. Well, in that case, I'm just going to send the notes out the moment the meeting is over, I'm just going to hit send because I've already taken the action item. I'm not going to try to make my notes look great so that others can appreciate, "Oh, Shreyas always sends great notes." On the other hand, if it was a product review with the CEO about a very contentious topic that you have gone back and forth multiple times, and now you made a decision about something, you want to perfect those notes before you send them out, you want to get the language right, you want to be very clear on what the decision is, so there's no room for misinterpretation, so you don't backtrack afterwards or people say, "Well, but I thought we'd said this." That's a case where it's an L task. And I would say just spend an hour or even two hours perfecting those notes because it's an L task. So, hopefully that helps illustrate some of the ideas behind the LNO framework.

Lenny (00:40:18):
Yeah. And that last piece is a really good segue to the next big idea around optics and the important optics.

(00:40:25):
This episode is brought to you by Sprigg. If you've been a member of my community for a while, you know my user fan and investor in Sprigg. Sprigg is a user research platform that makes getting user insights from your product as easy and fast as getting analytics. The best product and research teams at companies like Loom, Opendoor and Dropbox use Spriggs in product surveys to target specific users, start collecting insights and identify issues and opportunities related to activation, onboarding, engagement [inaudible 00:40:54]. Talk about a platform that pays for itself. But I'm perhaps most excited about Sprigg's newest launch, which extends the power of the platform pre-launch and makes it possible to test mockups and prototypes with your own users in minutes.

(00:41:06):
The testing interface is super slick and doesn't require any of the typical plugins that make testing with your own users an appealing. And with unlimited seats, you're able to invite anyone from your company to view and use insights generated by Sprigg. If you want to get started, head over to sprigg.com/lenny and mention that I sent.

(00:41:26):
But before we get to that, I wanted to have one follow-up question. What are some classic examples of high leverage tasks that PM should try to do more often and think about? What's in that bucket, generally? Even though you pointed out a lot of times they could be in any of the buckets, depending on how you execute them. Are there things that are just like, you should probably spend a lot of your time doing X, Y, Z?

Shreyas Doshi (00:41:43):
Yeah. So, turns out that the L tasks, PMs implicitly just deep down they know what their L tasks are, because those are the tasks that are bothering them the most because they are not doing them or because they're not doing them as well as they know they should. So, the classic example of this is the case where a PM will say, "I know I need to work on getting our strategy right, but I don't have time because I'm busy firefighting. I'm busy just dealing with all these execution issues. And I just don't have time to work on the strategy piece." Sometimes we console ourselves by saying, "Yeah. That's because we have all these things going on this month, but trust me, next month, we're going to have ample time and I'm going to just spend a whole week working on strategy." Well, the next month rolls around and it's the same thing, you've got other issues.

(00:42:38):
The reason we procrastinate on these tasks are, one, because we know that they're L tasks, we know the impact they'll have, and we are a little scared. That's one. The second is they require dedicated attention. And again, we are afraid about whether we'll have anything interesting to say. That's the deep fear. Why many people procrastinate on strategy? Because deep down, they don't know if they can formulate a good strategy. So time becomes a convenient excuse for us where we say, "Well, it's not me. It's just, I don't have time to work on it." And by the way, everything I say here, I have been that person. So I have been that person who's procrastinated on an L task, whether it's the strategy or whether it's writing the PRD for this really difficult feature, or it is working on aligning two teams where that alignment would create a lot of impact, but it's hard, it's an L task, but I don't do it because I don't want to deal with this other person, this manager I love to collaborate with to make it happen.

(00:43:46):
And perhaps, I don't know if we'll get along. I don't know if I can have that tough conversation. And so again, it's an L task, but I'll try to apply bandaids instead of just tackling it head on. So, this is tough stuff. And what I've found useful there is two things, two tactics make a huge difference in helping us target L tasks better. One is the idea of placebo productivity. So, what I do is before I have to tackle an L task, that couple of days leading up to it, I do all these placebo productivity tasks. Basically, I intentionally do N tasks and O tasks. I fill up my day with N and O tasks.

(00:44:26):
And I keep reminding myself, "Yeah, you're just doing neutral and overhead tasks." Because then that just tricks me into thinking, "Okay, if I've been doing this placebo productivity task for the last two days, now, it's the right time for me to do this L task." So that's one tactic. The other is change of location. Nothing, for me, at least fights my procrastination for L tasks better than changing the place from which I'm working. So if I normally work from this desk, the appointed day I did my couple of days of placebo productivity tasks, and on that appointed day, when I'm slated to do an L task, I will actually go out and work from somewhere else, whether it's a coffee shop or a co-working space or some other space. And I find that change of place just forces a focus and a shift in mindset that helps me bang out that L task very quickly and do it really well.

Lenny (00:45:16):
That are some great advice. There's so many layers of advice in that answer. Your point about the high leverage tasks being the task that you know you should do, but don't want to do, makes me think of a quote that I always come back to that the cave you fear contains the treasure that you seek. And I often find that to be true. And it's this reminder to just wherever the compass is pointing where it's most difficult, it's probably where the biggest opportunity lies. And so, that's a really good reminder of all that.

Shreyas Doshi (00:45:40):
So wise. Yeah, pay attention to your fears because they're telling you something.

Lenny (00:45:44):
Speaking of fears, our third big idea is around the three levels of product work. Basically the three things that a PM should be focused on and how often when you're not aligned on what is most important to you and your team, it often leads to conflict. And so, I'm excited for you to unpack this idea of these three levels of product. We can all share what they are impact, execution and optics. And when I saw this for the first time, I always come back to these three things, because it's so simple and so accurate. And so, I'm excited for you to unpack all this.

Shreyas Doshi (00:46:12):
This idea that there are three levels of product work, impact, execution, and optics. Once you understand it, it explains a lot of what you see on product teams and organizations in general. And so, perhaps start with an example that most product people, product leaders and founders are used to seeing, and something I've seen dozens of times in my career that there's a product review, say, where you as a PM are presenting to the CEO. And as you're presenting what the plan is, obviously since this is a real world product, there's going to be some compromises that you're taking. And so, the CEO perhaps asks about, "Okay, well, why is our customer service response time going to be so high in this case?" And you've thought about it, it's like you did not think about that issue, but that is a good reason why. You talk to the VP of customer support and they don't have the funding this quarter to support your product fully, which will then result in a poor customer service experience for this kind of new product that you're launching.

(00:47:16):
But then you've agreed. You've used your skills of influence to agree that, okay, next quarter, they're going to allocate a lot more people to your product so that the customer service experience will get better next quarter. And so, the CEO asks, "Why is the customer service experience going to be poor here? Or they make a remark like that." And then you reply with all these good reasons. Again, good reasons. And needless to say the rest of the product review doesn't go as well. And after the product review, you wonder what happened. Maybe you ask your manager what happened and particularly you're wondering why couldn't the CEO see a very rational argument about why you can't do this at launch.

Lenny (00:47:57):
Never happened to me. Never happened.

Shreyas Doshi (00:47:58):
And so, it's like, why doesn't he or she see that? And the reason is that you are thinking at different levels. So you as a PM perhaps are fixated as you are dealing with this launch or this project, you are fixated on the execution level, which is what does it take to get something done? And how can I do it? How can I hit the next milestone? Those are all the things we tend to think about when we are thinking at the execution level. The CEO on the other hand is approaching it from the impact level. And particularly perhaps in this case, what is the impact to the customer experience? And often CEOs are the ones, or founders are the ones that are thinking about, what is the impact to our brand? And so the CEO is thinking at the impact level, you're thinking at the execution level, there is that mismatch.

(00:48:46):
We litigate the minutiae of whatever issue we are discussing, but we never really recognize that it's because we are default thinking at different levels. And so, this realization helped me better understand why there were conflicts between two very smart and well intentioned people or groups within a company. I was myself guilty of this as well earlier on in my career, time and again, I noticed that we can, again, keep litigating the specific issue without understanding that, "Oh no, there's actually just a fundamental mismatch." And it's not like people are stuck at one level and can never think at a different level, it's just that we tend to default to certain levels, and that's like sometimes our preferred level. We can switch levels, but that requires a nudge sometimes. And so, that observation helped explain a lot of things, including what kind of people an organization will promote? Does it promote people who default operate at the impact level? Does it promote people more who default operate at the execution level or at the optics level? So, it has very wide ranging impacts on just overall how an organization functions.

Lenny (00:49:59):
What's an example of optics? And when optics matters, when you might not be thinking about the importance of that? Just impacting that one a little bit.

Shreyas Doshi (00:50:06):
Yes. So, optics is about creating awareness of the impact and the execution that you're doing or your team is doing. That is the most compact definition I can come up with for optics. And optics is a good thing. So I'm not saying don't think about optics whatsoever, I think it's actually important to think about optics. And now I'm talking about just internal optics. External optics is an entirely different thing and that's like marketing PR and that's definitely highly important. But even when we talk about simply we limit scope to internal optics, I'll make the observation that you should be spending some time on internal optics because it creates energy, it creates awareness, it creates excitement, it creates opportunities for feedback. Those are all really great things and they will enable greater impact and better execution for you.

(00:50:57):
The challenge with optics is that in certain organizations that balance gets thrown off, where optics sometimes becomes the goal where somehow implicitly the organization or its culture has indicated to it's people that as long as you do the optics well, you are going to be fine, you are going to be appreciated here, you're going to be rewarded here as long as you do the optics fine.

(00:51:22):
And it's not like the organization woke up in the morning and said, 'This is the culture we want to create." It just happens again through little actions that occur every day, it happens through who you hire, who you fire, who you promote and what kinds of things do you appreciate at all hands as the CEO or the founder. Do you appreciate a launch? Do you appreciate results? Do you appreciate, I don't know, an awesome status update that somebody sent? So a status update doesn't on its own accomplish anything. I mean, they are important, but a status update is an optics activity. Now, it is a necessary optics activity, but if you start appreciating the necessary optics activities, constantly, the signal you are sending to people is, 'Oh, you got to focus on this optics activity." So then, that becomes the goal and that can be really harmful.

Lenny (00:52:09):
So there's these three levels of product work. Do you have advice for, should I just default to one of these normally based on just as a PM, I should always be thinking about impact or is it more, just make sure you're aligned with your leader with your team? Is that the more important takeaway?

Shreyas Doshi (00:52:23):
Yes. I think that's the more important takeaway is again, it's about now we have a vocabulary that we can talk about in an objective manner without pointing fingers. It's like, 'Oh, you tend to be fixated on all these execution details and that's not the right thing." That's the type of feedback sometimes that gets shared. So now you have vocabulary to talk about this and once you have that, you can, as a team, decide what is most important given your context. I'll give you an example. For early stage teams, of course, they need to be thinking about the eventual impact, but what they should actually, I think, most early stage teams should actually optimize for execution. Assuming that they have come up with a reasonable hypothesis about what's going to win, their main emphasis needs to be on execution because you will not see impact readily on a one week horizon or a one month horizon or perhaps even on a quarterly horizon.

(00:53:20):
So that's an example of a situation where let's be explicit, we need to get great at execution. We have a set of core insights that were informed by our desire to make an impact. But now that we are responsible for converting these insights into a product, let's be largely operating at the execution level, as an example. Say there is a platform team and that platform team has had some issues lately with availability that has disrupted some other teams within the company and their products. Perhaps that platform team should have a conversation that, 'You know what, yes, we need to focus on impact obviously to avoid this negative impact, but also let's pay some more attention to optics because we haven't been communicating with teams as much teams that rely on us. So let's create a better communication channel with them. Let's create better status updates for them," and whatnot. So again, the point is not so much like, "Oh, this is the right level and all other levels are wrong," it's about being sensitive to what's right in this situation.

Lenny (00:54:21):
So you talked about execution and how maybe for early stage startups that might be default the most important type of work to be focused on. And that's actually a really good lead way to our fourth big idea, which is a provocative tweet that you put out a while ago that you said, "The most execution problems are actually strategy problems or culture problems." And so, I'm excited to hear a little bit more about how you discovered that and what that means and maybe how to address those problems.

Shreyas Doshi (00:54:49):
And so, I realized this somewhat late in my career as a leader, most execution problems that I encounter in a high performing environment where everybody has the right intentions are actually not execution problems, they are either strategy problems or interpersonal problems or cultural problems. And so, just to illustrate it, I'll make the observation that many leaders are extremely busy in such environments, whether it's a fast growth startup or a fast growth larger company, they're extremely busy, they're usually overwhelmed. Like I said earlier, I was one of those people. Take a deeper look at what they're engaged in. And I got a chance to look at it with my peers that I was mentoring or coaching or people on my team, PMs or PM leaders were extremely busy and usually overwhelmed.

(00:55:36):
I noticed two things, that what made them busy is two things. One is that somehow the organization had imposed very high optics requirements. So they had to do a lot of optics related work, show up at certain status meetings and blah, blah, blah. So we talked about that. So let's leave that aside. But the other reason they're so overwhelmed is that they're constantly solving execution problems. So they solve the most important ones, the new ones come up and they solve those. And then there are two new ones to solve and on and on, it's a classic guacamole. And as I noticed that, and I'll share a concrete example of where this might happen, where an execution, a seemingly execution problem surfaces, so say two teams are misaligned. They need to work together where they're misaligned. Everybody knows it. And that is affecting our execution. That misalignment is affecting our execution. It's affecting our ability to hit our OKRs, it's affecting their ability to hit their OKRs.

(00:56:32):
So as a leader or say, you are a director of product or VP of product responsible for one of these teams, you now charge with fixing this execution problem so we can move faster. So you do a dozen meetings to figure out what's going on, you try to diagnose the issue, how to better align. And then you talk to your peers on the other side, and then you decide, "Okay, here's what we're going to do to solve this execution problem. We are going to create a new review process." And so, we are going to create this process and we are going to review priorities on a regular basis across these two teams. And then we are going to also as the managers of these individual teams to do regular one-on-ones so they can stay in sync. So this type of scenario is extremely common, again, especially in high growth organizations that want to accomplish a lot.

(00:57:19):
You'll come up with this solution after many meetings and a lot of work, a lot of conversation. And so, as I grew as a leader, I got increasingly curious about this type of situation. And when I looked at it more closely, I started realizing that what looked like an execution problem, this misalignment and this causing execution issues wasn't usually an execution problem. Instead, it was a strategy problem in some cases, because the reason we are misaligned is because we are pursuing different strategies or that is more often the cases, the reason we are misaligned is because we don't know what the strategy is. So, we don't know what the strategy is. We craft some OKRs based on what makes sense. The OKRs are not very well aligned. We don't have a sense of priorities, and we also don't have a sense of what we do when reality changes.

(00:58:09):
This is all stuff that a clear correct strategy should help inform. But actually this lack of strategy is what's causing this misalignment, it's not because they're not meeting regularly. And what happens in these meetings is, again, you're arguing the minutiae of like, "Well, are you going to work on this feature? I depend on this. Or can you swap two engineers from this team?" All of this stuff that PMs are very familiar with. You're talking about all the small stuff, but nobody recognizes that like, "Can we fix that?" So, as I started seeing this often was a strategy problem, sometimes it was not a strategy problem, it was a culture problem. So, what is a culture problem in this situation where two teams are misaligned?

(00:58:49):
It's basically that you have a problem where you have set a culture that you are supposed to mainly optimize for your OKRs. In a culture like that, it becomes really hard to allow two teams to work better together because if one of the teams doesn't hit their OKRs, because they were helping rightly for the sake of the company, they were helping this other team that team's manager is going to get his or her wrist lap at the next performance review.

_[90 additional lines trimmed for context budget]_

---

### When to invest in new acquisition channels | Adam Grenier (Uber, MasterClass)
**Guest:** Adam Grenier | **Date:** 2022-09-15 | [YouTube](https://www.youtube.com/watch?v=-PDsvl2WCZU)  

# When to invest in new acquisition channels | Adam Grenier (Uber, MasterClass)

## Transcript

Adam Grenier (00:00:00):
One of the biggest pieces of advice I'm giving to people that are like, "How should we adjust our marketing with the economic changes and things like that?" I was like, "Start by assuming you no longer have product market fit, because you had product market fit in a different market." It's a different market now, so you have to start over. And hopefully you do, or it's pretty close to it and you just have to adjust a couple things, and you could be right back on track. But if you just assume you need to launch a new channel to fix this problem, you're going to be wrong, because your entire customer base changed, not just the next 10% of customers that you're looking for.

Lenny (00:00:34):
Welcome to Lenny's Podcast. I'm Lenny and my goal here is to help you get better at the craft of building and growing products. I interview world class product leaders and growth experts to learn from their hard won experiences building and scaling today's most successful companies. Today, my guest is Adam Grenier. Adam was head of Growth Marketing and Innovation at Uber where he basically built their growth marketing infrastructure and the team from the ground up. Then he went on to VP of Product and Marketing at Lambda School, and most recently he was VP of Marketing at Masterclass. These days, Adam advises companies, large and small, on growth and marketing strategy.

Lenny (00:01:10):
In our conversation, we cover how to decide when to try new and emerging acquisition channels like TikTok, VR, newsletter ads, and how to go about testing them out. We get into the growth CMO role, which is an emerging role that Adam has helped pioneer, and we get into some real talk about burnout and depression and mental health issues that often come with working in tech. This was a really powerful and insightful conversation and I learned a lot from Adam both as an operator and as a human. I can't wait for you to hear this episode. And so with that, I bring you Adam Grenier.

Lenny (00:01:48):
This episode is brought to you by Whimsical. When I ask product managers and designers on Twitter what software they use most, Whimsical is always one of the most mentioned products, and the users are fanatical. Whimsical is built for collaborative thinking combining visual, text and data canvases into one fluid medium. Distributed teams use Whimsical for workshops, white boarding, wire frames, user flows, and even feature specs, and that includes thousands of built-in icons and a rich library of templates. See why product teams at leading companies call Whimsical a game changer. Visit whimsical.com/lenny to have my own templates added to your account when you sign up. That's whimsical.com/lenny.

Lenny (00:02:34):
This episode is brought to you by Coda. Coda's an all-in-one doc that combines the best of documents, spreadsheets, and apps in one place. I actually use Coda every single day. It's my home base for organizing my newsletter writing, it's where I plan my content calendar, capture my research, and write the first drafts of each and every post. It's also where I curate my private knowledge repository for paid newsletter subscribers, and it's also how I manage the workflow for this very podcast. Over the years I've seen Coda evolve from being a tool that makes teams more productive, to one that also helps bring the best practices across the tech industry to life, with an incredibly rich collection of templates and guides in the Coda Dock Gallery, including resources from many guests on this podcast, including Shreyas, Gokul, and Shishir, the CEO of Coda.

Lenny (00:03:23):
Some of the best teams out there like Pinterest, Spotify, Square, and Uber use Coda to run effectively, and have published their templates for anyone to use. If you're ping ponging between lots of documents and spreadsheets, make your life better and start using Coda. You can take advantage of a special limited time offer just for startups. Head over to coda.io/lenny to sign up and get a $1,000 credit on your first statement. That's C-O-D-A.I-O/lenny to sign up and get a $1,000 in credit on your account.

Lenny (00:04:02):
Adam, welcome to the podcast.

Adam Grenier (00:04:04):
Thank you. Thanks for having me.

Lenny (00:04:06):
It's my pleasure. I'm really excited to chat. So, I'm going to give a very brief overview of your very impressive career, and just let me know if I missed anything.

Adam Grenier (00:04:15):
All right.

Lenny (00:04:15):
Sound good?

Adam Grenier (00:04:15):
Yeah.

Lenny (00:04:17):
Okay, so you were most recently VP of Marketing at Masterclass, which I'm actually a happy subscriber of and I've watched many a video. Before that, you were VP of Product and Marketing at Lambda School. I don't know if that's right before, but that was something you did. Also, you were head of Growth Marketing and Innovation at Uber, which is a really cool title. And I think you spent four years there and you basically built their growth marketing infrastructure and the team. And currently you're doing a bunch of advising and exploring to see what you want to do next. Is that about right?

Adam Grenier (00:04:50):
Yeah, you hit most of the key points. I think pre-Uber, the first chunk of my career was on the advertising side, so worked in agency world. So, I kind of think of this as phase three of my life. Ads world was phase one, startup and growth world phase two, and now really just spending time helping entrepreneurs and founders and built companies and that type of stuff.

Lenny (00:05:16):
What's been your favorite phase so far?

Adam Grenier (00:05:18):
I mean all of them. I just embrace what gets thrown at me and allow it to organically happen. So, each phase has had its pros and cons and ups and downs, and so I think they've all fit pretty well into where I was in my career.

Lenny (00:05:34):
Speaking of moving and adjusting and iterating, I know you're big into improv. How serious are you about improv?

Adam Grenier (00:05:44):
Good question. Serious in the sense that I've done it for a very long time and I still do it and I try to do it regularly. Serious as in am I aiming to make money off of it and have a career out of it? Unfortunately not. There was a point in my life that that is what I wanted to do. I lived in Chicago, did Second City ImprovOlympic, a variety of different places, did quite a bit of performing, but also got into corporate paychecks early as well.

Adam Grenier (00:06:12):
And so kind of built a lifestyle that made doing improv full time probably not the best path for me at the time. And so made a pretty conscious choice early on that it was more of a hobby and if something ever came of it, cool, but if not, that's okay. It's something I keep coming back to, because it's very grounding and fulfilling in ways that work and family life and things like that don't quite hit for me.

Lenny (00:06:34):
Actually at Airbnb we had an improv teacher come and work with the PM team. It was for months. We did improv games once a week.

Adam Grenier (00:06:42):
Nice.

Lenny (00:06:43):
And played all these fun things. And I'm curious what you've taken away from improv that has helped you become better at your work?

Adam Grenier (00:06:51):
So, I think generally the whole suite of skills that you develop in improv are pretty applicable, right? Because you are getting comfortable on your feet with change, with teamwork, building off of each other, experimenting, trying new things, a little bit of everything. I think a couple of the key rules or themes of improv that I really try to hammer home with people are obviously the "Yes, and..." side of improv, which everyone's probably heard, which is in a scene the worst thing you could do is deny somebody, because you're actually just stopping progress and you're not building off of anything.

Adam Grenier (00:07:27):
So, the appropriate approach is to say, "Yes, that is true, and..." and add to it. So, if someone's like, "Hey, you have a chicken on your head," not saying, "No, I don't." Just kind of ruins that scene. Versus saying, "Yes, I do, and it's name is Sally. What's your chicken's name?" Builds on that and gives it more opportunity. And so I think that in growth in business is super important to be able to say, "Yes, I do see your idea," or "Yes, we did accomplish this and this is what we want to do next and this is how it's going to build on it," I think is super important.

Adam Grenier (00:07:59):
The other one that I think is less known or talked about is the gift of details. So, in a scene, if you give somebody really specific details about something, it gives so much more meat to be able to work off of in terms of what's coming next. So, if someone's starting a scene and they're clearly watching television and clicking through the channels and I walk up and just say like, "Oh, you're watching TV, cool." That's a yes statement. I'm not denying what they did. But if I come up and say like, "Oh cool, you're watching TV. Is that an Alf episode? I haven't seen Alf since I was a kid. It reminds me this one time I actually ate my own cat."

Adam Grenier (00:08:39):
Just giving those specific details of Alf and me as a kid and I had a cat, which if people don't know Alf, he ate cats.

Lenny (00:08:48):
I don't remember that. I remember Alf, but I don't remember he ate cats.

Adam Grenier (00:08:51):
He was always trying to get the family cat. So, those kinds of details add a ton of value and you take that into the business world, to use Masterclass for instance, if I say, "Yeah, Masterclass, we've got this way to build content that is both entertainment and education," that's interesting. But if I say, "We create content that is both education and entertainment to solve people's deep curiosities in the way that maybe a biography would." That just opens up the exact problem that you're trying to solve. What are other alternatives to that problem? How are people consuming that? So, I think the gift of details in good improv and learning those skills is something that I really value and look for in every aspect of my business life as well.

Lenny (00:09:41):
It sounds like it's really helpful, one, in marketing, creativity and positioning, and things like that you just described. Have you found it also to be helpful in collaboration like this "Yes, and..." piece? I'm curious, is there an example or story where you like "Yes, and..." someone? Do you actually say "Yes, and..." in a meeting? How do you actually find that you use it?

Adam Grenier (00:09:58):
I hear it every now and then. I don't usually literally say it. I think one of the areas that I've found it to be valuable is when you've got cross-functional work. So, obviously at Uber we dealt with city teams a lot, and so a lot of the times the way that the central team would scope a problem versus a local team would scope a problem, would almost feel at odds with each other. And if you approach it with that "Yes, and...", it's often still true.

Adam Grenier (00:10:24):
It's like, oh, both of these things can be true at once. You could have a different goal than I have, or you have a system problem local to you that is important to you and it's not important to me. That's okay, both things can exist. So, now that we accept both and can work off of each other, we're more likely to build both a better rapport and energy among ourselves because we're not just saying, "No, no, no, no, you're wrong. That's not true, that's not important to the business. Why are you doing that?" That type of energy when cross-functional work, it just kills the scene, it kills that progress. And then you don't build relationships, you don't build the right solutions, all that type of stuff.

Lenny (00:11:06):
It sounds really good. Everyone in theory wants to be really good at this. And I imagine just doing a bunch of improv is a really good way to get better at not getting defensive and being like, "Yes. And how do we make this idea better?" Is there something you can advise folks to work on this skill, or is it just do a bunch of improv classes and it'll kind of help build that skill?

Adam Grenier (00:11:25):
That's one. I would say that I'll say that all the time to people, "Do some improv classes." And I get a lot of people like, "No, I'm not funny," or, "I don't want to do improv." And I think it's still a really great class to take, even if you have zero interest in doing improv, or public speaking, or any of that kind of stuff. Because, again, improv 101 is taught everywhere. Every city has it somewhere, and it's rarely ever people that are trying to do improv professionally. It's all games, like you said. The classes that you all did at Airbnb is what improv 101 is, right?

Adam Grenier (00:12:00):
It's just like, "Hey, let's just have fun. Let's just get out of our skin," and things like that. So, I do think everybody should take improv classes. I think it's also something with a lot of goals or skills that you want to develop, I think being really public and open about you wanting to develop that. So, if you are managing a team and you want to sharpen the skills, make it a team goal, or have accountability and just say, "Hey guys, I know that I've been pushing back on things lately. I want to really try to embrace and grow off of ideas better, hold me accountable, call me out and be like, 'Adam, "Yes, and..." this please."

Adam Grenier (00:12:32):
Or giving people permission to push back on that when it doesn't happen, I think also just opens the door for more productive conversations with people and the ability to hold yourself accountable and keep trying it.

Lenny (00:12:47):
I love that. And such a good team bonding activity. There's like all these reasons to do this as a team. My wife actually, she's a designer, artist, writer, illustrator kind of person, and she's been taking a lot of these sorts of classes to help inspire her creativity. She never wants to be an improv person, she did stand up classes.

Adam Grenier (00:13:03):
That's awesome.

Lenny (00:13:05):
As you said, it just helps you get the juices flowing along these lines. Okay, so we're not going to talk about improv the whole time.

Adam Grenier (00:13:13):
We could if you want to.

Lenny (00:13:15):
We could. Throw me word, let's go. No, we don't want to do that. So, there's basically three things I really wanted to chat about with you. One is how to decide when to invest in an emerging acquisition channel like TikTok, VR, Clubhouse was a big thing. You have some really interesting thoughts on how to decide and approach this thing. To the growth CMR role, which is kind of this, I think emerging role, something you're really good at, and I just want to get your thoughts on what's happening there. And then, three, some real talk on burnout and depression that often comes with working in tech and stuff that we go through. Does that sound good?

Adam Grenier (00:13:51):
Yeah.

Lenny (00:13:51):
Okay, great. So, to start with in the first topic, if you think about it just every company essentially goes through this kind of S-curve of growth. They start slow, they find something that's working, then hopefully it works out and things start to grow, grow, grow, and then eventually it flattens out and you see this S-curve that happens. And every company is always trying to find the next S-curve to add this layer on the cake that keeps overall growth up while this first growth channel slows.

Lenny (00:14:18):
And so people are always looking for what's the next thing? "Oh man, Clubhouse is coming out. We should get on Clubhouse." "Oh, TikTok is so hot, we've got to run some TikTok ads." And there's always something new, like newsletter ads, I don't know, podcast ads, if that's new. And you have a really interesting framework for how to think about this and make decisions and experiment. So, I'd love to hear insights there.

Adam Grenier (00:14:38):
So, the exploring emerging channels framework that I'll take, either my teams or companies that I'm advising through, has three core ingredients that I like to spend time with. So, the first is really understanding if there is an overlap between what the customers need is, what your company's goals are, and what the channel actually does really well. So, the example I've used in the past is Spotify in the moment of things like Clubhouse and Paparazzi and stuff like that becoming really popular.

Adam Grenier (00:15:14):
Well, for Spotify, they're trying to get more people to consume music and be entertained by music and things like that. And it's all audio driven. And so their growth goals are probably around new customers or deeper engagement with audio. The customer's needs are discovery and more ways to maybe have deeper relationships with their music. If you're a jazz fan, can you learn new jazz artists or more about the artists that you love? Things like that. And then take those two channels. If you take something like Clubhouse, it's audio first, it's almost like live podcast radio type feel to it.

Adam Grenier (00:15:57):
You can get into these rooms with just people with really amazing esoteric knowledge about something. And so its strengths have a really clean overlap to me with the goals of Spotify, the needs of the customer and the strengths of that. And so that to me is great. That is probably a green light in terms of is it even worth our time? Versus Paparazzi is very photo driven and nothing really to do with music or anything like that. And so it's like even though Paparazzi might have become the best biggest channel ever, is that the thing you should be putting your time into? It would be a yellow light for me at best.

Lenny (00:16:36):
And how did you describe that again? It's the medium matches?

Adam Grenier (00:16:40):
Yeah, the strengths of the medium. So, let's take influencer right now. Actually two of the channels that a lot of people are talking about right now are streaming TV or OTT and influencer marketing. And so to me, one of the strengths of influencer marketing is hyper targeted contextual marketing. And so I can go find the five influencers that are hardcore Alf fans, and if I'm marketing Alf something, great, I can go find that specific thing. Whereas OTTs a lot harder to get that specific.

Adam Grenier (00:17:16):
OTT strength is broad reach and video storytelling and that type of stuff. So, it's like, okay, well maybe my medium is if I'm Masterclass and I have a ton of video content and storytelling and things like that, that channel actually makes a ton of sense probably. So, it's like what are the strengths of that channel is something that... that is actually probably the piece I see people ignore the most, which is they just want to know if a channel is hot or not. And this gets especially hairy in this world of a lot of B2B doing more consumer-esque marketing. There's so many B2B companies that just don't apply to emerging consumer channels.

Adam Grenier (00:18:00):
And it's just like, please just stop. I don't need a Notion Clubhouse channel this week. And maybe there's a world to do that. But I think that's kind of number one, is making sure that there's even a reason that you should be there to put it on your radar right now.

Lenny (00:18:19):
Awesome. What does the OTT stand for by the way?

Adam Grenier (00:18:22):
Oh my gosh, you're putting it on the spot.

Lenny (00:18:24):
It's all good.

Adam Grenier (00:18:25):
I'm drawing a blank on it.

Lenny (00:18:26):
But essentially it's a streaming platform?

Adam Grenier (00:18:28):
Over the top. Over the top. So, instead of it being cable TV, it's coming from a box. So, it's primarily if you think of ads on Amazon or Hulu or even if you go to cnn.com and you start streaming and you get an ad first. it's basically video ads, but a lot of them now are happening on televisions and on streaming services rather than just on websites.

Lenny (00:18:55):
Got it. Okay, cool. So, the first is the strength of the channel. You should look at that.

Adam Grenier (00:18:59):
Yep. And how that overlaps with your customer and your business needs. The second is the channel DNA. And so this is looking at things like where are they in their trajectory? So, Clubhouse is actually a perfect example, because in a weird way, so Clubhouse got hot before Facebook got cold. And I was pretty amazed how many more people were trying to crack Clubhouse than TikTok, because TikTok hadn't really released their ads solution yet, but neither had Clubhouse. But everybody was talking about Clubhouse, and TikTok is very clearly not going away anytime soon, where Clubhouse hopefully won't. Like this is an amazing product.

Adam Grenier (00:19:41):
I really enjoyed it and loved it, but it was clearly very early, very quickly at that point of hotness where everyone was just kind of, "That's the reason I should be there." And part of this reason is to accept the risks of going into that channel. So, if I go and dedicate two quarters of work to Clubhouse, I need to accept that they are so early in this curve that there's a good chance this is a once in a lifetime opportunity and it'll be over. It's not a repeatable action. It also is important because if you get something to work on a channel that's earlier in their growth curve, the likelihood that they will change is very high.

Adam Grenier (00:20:23):
You're going to need to commit a lot of cycles to keep it going, because it's like, "Okay, well, their product is going to evolve drastically very quickly over the next two years." And so a really great example is Facebook early... I was at Zoosk. And so Zoozk and companies like Zynga got tons of their early growth because of notifications on Facebook, which was one of their early features, which allowed basically anybody that took any action on Zynga, it would post on everybody else's page that you got 10 carrots, and that was a huge growth lever.

Adam Grenier (00:20:59):
But then Facebook just pulled the plug on that. And so it's like, well, if you put all of your energy into that and that's it, it was pretty clear that that was still an area that's like this may not last forever. The last thing on the channel DNA that I like to look at that's a little bit more, I don't know if odd or unusual is the right term, is I like to spend a lot of time thinking about how they monetize. What is the monetization strategy of the channel? And the reason is because if you, as a business, can match or support their monetization strategy, it actually gives you a really interesting leg up with that channel.

Adam Grenier (00:21:37):
Because the likelihood of you being able to call them up and go do custom stuff with them, or partner with them, or that your solutions will actually stick around for a while, it'd go up pretty drastically. And so my key example of this was with when Facebook started exploring mobile ads, Hotel Tonight, we were one of the alpha testers of mobile ads, because I'd been sitting here buying ad inventory on networks for the last five or six years and just waiting for Facebook to work, because it just wasn't really working for mobile installs.

Adam Grenier (00:22:13):
And it's like, I know this is a huge channel because I can use it on my online marketing, my web marketing, but as a mobile acquisition it's nowhere near as efficient as a lot of these other networks. And so as soon as they were doing that, I was able to basically position and say, "Look it, you want to work with us. Let me into your alpha, because I have five years of experience already buying mobile ads. I know the space. I know it'll work. And if you get us to work, we're a killer case study, because we are a non-game and a lot of money is spent on gaming, but there's these whole other major categories that you're going to need other than gaming examples within that group. So, you're going to be able to use me as a case study and a lot of different scenarios than the gaming players."

Adam Grenier (00:22:59):
And so I was spending a lot less than the gaming players, but because of that understanding that your goal at Facebook is to make ads work for all of travel and for all of leisure and those kinds of things, that's the value of working with me. So, that's another piece of the channel DNA I like people to focus on.

Lenny (00:23:18):
Awesome. That's such a good one, because to your point, if your goals are aligned, they're going to be like, "Yes, let's make this happen." And it always feels like it's this behemoth that doesn't want to talk to any new startups, but if you can make the case of this is going to help you and the way you laid out is so clear, it's such a good idea.

Adam Grenier (00:23:35):
And especially with emerging channels, right? Because their whole thing is that make this work for a long time. It's part of the challenge you see with some new channels flipping to the other side of growing an ads business, will gravitate towards like, "I want to get Disney on here," but Disney is very campaign driven, or they have been traditionally, where it's like you may get one big paycheck from them, but that doesn't... The way that UA driven gaming works is you get that to work, that's a gift that keeps on giving forever, right? Because there's not one of those companies, there's thousands of them and they all do the same thing. So, being able to drive that conversation is really helpful.

Lenny (00:24:18):
Cool.

Adam Grenier (00:24:18):
And then the third main ingredient is just your own company DNA. And so I think risk profile is a big one. Do you actually have comfort in being a first mover, a true first mover? Nobody knows anything, tracking's not going to work, it's not going to be programmatic. You're probably going to show up on content that's offensive. You're probably going to ask for refunds that won't happen. It's going to be really painful to be a true first mover. Do you have that appetite? Do you have the staff to actually be able to put someone on that and it not distract from everything else?

Adam Grenier (00:24:53):
And then the other piece on the company side is just your current channel mix. There's very few companies that I recommend saying, "Yes, go put energy on this brand new channel that you don't know how to scale yet before you've figured out some type of volume on Google and Facebook." Every now and then there may be a perfect fit where it's like, absolutely, you should be the person doing this. But if you're not at least getting something out of the basic channels that everybody else is using, it's probably not the thing you should be putting your first energy into. It should be like, "Great, I've got a good foundation." Like you said, now we're at that stage of trying to add things, tends to be a better stage to do more risky exploration into new channels.

Lenny (00:25:40):
What advice do you have or can you give to founders teams that are trying to test one of these in terms of just how to run these tests? How much time should they spend, would you say? What do they look for? I know that this is a hard question and super dependent on the situation, but any advice there?

Adam Grenier (00:25:55):
So, I think going through those three ingredients should help shape that answer, right? Because if you're like, "Okay, well, the first one is super strong, the channel DNA is maybe really early and I've got a small to mid-size team and maybe only one channel working," then it may be like, "Great. Put half of one person into this, because it's maybe interesting. But don't put any more than that into it." Versus if it's like, "Man, this is a killer fit the channel's a little further along and I have a 20 person team, so I'm going to put three dedicated people to this, because we are in prime position to be the leaders in this new channel and really push it."

Adam Grenier (00:26:36):
So, I think it's figuring those pieces out, because it is a very it depends answer, but rarely ever is it like, "Hey, this should be your entire team's focus for the next three sprints or five sprints." I think that if you've got that half person working on it for a while and there starts to be some magic happening, sure, put a sprint or two against it as a whole team. But generally speaking, I think keeping it minimum at first is my typical recommendation.

Lenny (00:27:06):
I had another guest, Yuri, who I think from former Grammarly, and he made a really good point that it's often better not to try something than to do it badly and then take away the wrong lessons. I guess, in your experience, what's a timeframe you think people should put into this stuff? You said two sprints, maybe a couple weeks. I don't know, what's the range of just maybe don't spend more than X months on something new if it's not clearly working, just based on your experience.

Adam Grenier (00:27:33):
Generally I wouldn't let anything bleed past a quarter. You can probably get some good signal in a month or less, what I would call fishing. It wouldn't be like you're just putting bait in the water to figure out where the fish are, not necessarily getting statistically significant repeatable solutions. The big variables that can change that timing, so if I'm exploring a new video channel, the content I need to create is if I'm going to have to create something that takes three weeks to produce and $20,000 to make, I may want to give it a little more time, because I gave it more of an upfront investment.

Adam Grenier (00:28:16):
Versus if it's like I want to put text ads in podcasts listings or something like that. It's like, great, I can do that by myself at midnight and it's not distracting anybody or anything. And if it doesn't work in three weeks, let's move on. But generally ideally what you're working through, and we'll touch a little bit more on this with the Growth CMO, is that this should all be part of a roadmap. It shouldn't just be randomly chosen and thrown at. This should be part of your sprint process and you should have a backlog of other things that you want to try. And so you're actually weighing that decision of how long based on what other opportunities you're missing out on by investing in that.

Adam Grenier (00:28:57):
But I would say most channels, especially new ones, are going to take more than a couple cycles to kind of suss out. Because there's no rules, there's no playbooks yet on how to do them well. So, give it a little bit of time, but if you're going over a quarter and you don't feel like directionally it's getting better or it's interesting, I would put it back on ice for a while.

Lenny (00:29:18):
Cool. And to your point, you're not going to see any statistically significant answers. Is the thing you look for just like you know it when you see it? Oh wow, qualitatively feels like it's working kind of thing? Is that what you kind of look for?

Adam Grenier (00:29:30):
Yeah, and I think define that going into it. What am I looking for, for this? So, something like Clubhouse I'm probably not going to see clicks. It's more about are we able to start a room and increase the size of that room by 10% every time that we run it? Okay great, that means that we're at least getting better at this and there's more reach available to us. But if we're getting 20 people every time we start a room and then it goes down to 15, then we're either not doing this well, the channel's not doing well, or there's just not enough reach for us to actually expand. Versus TikTok you might be able to say, "Great, I can actually track clicks and conversion, so let's look at it the way we would any other channel."

Lenny (00:30:11):
Got it. So, kind of look for momentum and that you're getting better and that it's moving somewhere. Awesome.

Adam Grenier (00:30:16):
Yeah. Yep.

Lenny (00:30:17):
Cool. So, a question that I'm sure is on many people's minds that they would want to ask is, Adam, what are emerging platforms that are interesting right now that we should experiment with? What do you feel?

Adam Grenier (00:30:28):
So, I mean I mentioned OTT, or basically the key thing with OTT is that it's way more trackable than traditional television, but it has similar value that traditional TV does in terms of the ability to do more long form storytelling type content, and a lot of it's not skippable if you buy it. And so those are reasons to be exploring that right now. It's hard for me to call that emerging channel, because it's been around forever. It's there's more of it and the tools and services around it are way better now than they were four years ago. And so I think the sophistication and ability to scale OTT is much higher now than ever before. Influencers probably the one that I'm most intrigued by, because similar to OTT, the scale and services and the ability to go do it is still there.

Adam Grenier (00:31:19):
It's also got that hyper granularity that when I get into influencer tools, it feels to me like early Facebook when I used to go be able to target Lenny, or 10 people that have exactly the same likes as Lenny. And that type of stuff where it's like you can get so specific and find exactly who you need. It's incredibly tedious and manual and it's a lot of relationship management. So, I'm also keeping an eye on the technology being built around influencer, because I think that's a huge area of opportunity for entrepreneurs right now.

Adam Grenier (00:31:57):
But generally speaking, the scope and opportunity there is huge and it's not going away, but it feels very new and different right now. And it supplements the ability to do some hyper level targeting that you've not been able to do, that Facebook and Google are getting less open about at the same time. I think VR is really interesting in the way that mobile was interesting before iPhone Three, where it was if you've got a VR app, it's a really interesting space, but if you don't, it's not that interesting to me yet. Any that have come up for you that you're like... what are your thoughts on this?

Lenny (00:32:35):
No, these are great. All I think of is TikTok.

Adam Grenier (00:32:38):
I feel like TikTok's crossed a chasm, whereas they actually have a formalized ad platform now, people are finding scale. There's still a ton to do there and influencers is also weird, because it crosses all of these other worlds as well. But I think TikTok is actually hyper interesting and everyone should be doing that. But I think of that less as you should be doing it as should I do it, should I not? And it's more I need to figure out how to do Facebook if I'm at least mildly appropriately should be there.

Adam Grenier (00:33:05):
The podcast ads I think are great. I think that I bought podcast ads 15 years ago, so it doesn't feel like an emerging channel to me. I think there's way more volume now than there's ever been before. One of the guys that was on my team at Uber has a company that's doing programmatic buying and that type of stuff. And so I think there's more opportunities on podcast. I think people want to treat it like Facebook ads or direct response ads, immediate response ads. And actually what I keep seeing as the effective strategy with podcast ads is treating them more like radio where it's more about getting on the right program, making it personal and feel like it should be part of that program, and then repeating over and over and over again.

Adam Grenier (00:33:53):
So, I think podcast is super interesting. I think it's just hard to scale. It's likely not going to get people the same volumes as the Googles and Facebooks of the world.

Lenny (00:34:01):
Cue our mid-roll ad. I'm excited to chat with my friend John Cutler from Podcast sponsor, Amplitude. Hey John.

John Cutler (00:34:08):
Hey, Lenny. Excited to be here.

Lenny (00:34:10):
John, give us a behind the scenes at Amplitude. When most people think of Amplitude, they think of product analytics, but now you're getting into experimentation and even just launched a CDP. What's the thought process there?

John Cutler (00:34:21):
Well, we've always thought of Amplitude as being about supporting the full product loop. Think collect data, inform bets, ship experiments and learn. That's the heart of growth to us. So, the big aha was seen how many customers were using Amplitude to analyze experiments, use segments for outreach and send data to other destinations. Experiment and CDP came out of listening to and observing our customers.

Lenny (00:34:42):
And supporting growth and learning has always been Amplitude's core focus, right?

John Cutler (00:34:46):
Yeah. So, Amplitude tries to meet customers where they are. We just launched starter templates and have a great scholarship program for startups. There's never been a more important time for growth.

Lenny (00:34:55):
Absolutely agree. Thanks for joining us, John, and head to amplitude.com to get started.

Adam Grenier (00:35:01):
I also come from a very consumer perspective. I'm actually stronger on B2B companies using podcasting, because it has that exact same value I just described, but each one of their customers is substantially more valuable. So, they don't need the scale that a consumer application or product would need.

Lenny (00:35:20):
Yep. That's exactly who I work with usually. One last question on this topic. What percentage of the time do you find that an emerging channel works? Is it like 20% of the time, 10%, 5%? What should people estimate, it's probably not going to work but when it does it's going to be game changing?

Adam Grenier (00:35:34):
Like 5% of the time. There's new things popping up all the time. I think the area that I think of as emerging that I've found more success in is taking things that exist already and make them... so the two slices of it are either it's existed for a long... like podcasting. So, it existed for a long time and now we're finally getting to a spot where it feels scalable. The other is existing channels that introduce something brand new.

Adam Grenier (00:36:04):
So, at the mobile ads I described on Facebook, pre mobile install ads and post. Those first 18 months of mobile install felt like an emerging channel, right? Because they were changing the product every week and tracking didn't work, and there were all these funky problems with it even though Facebook had been around forever. But brand spanking new channels, I don't know, they rarely work or are worth the effort early that you hope that they will be.

_[249 additional lines trimmed for context budget]_

---

### Humanizing product development | Adriel Frederick (Reddit, Lyft, Facebook)
**Guest:** Adriel Frederick | **Date:** 2022-10-20 | [YouTube](https://www.youtube.com/watch?v=uMhBej6-Ey4)  

# Humanizing product development | Adriel Frederick (Reddit, Lyft, Facebook)

## Transcript

Adriel Frederick:
There are probably, I call them techno utopians who would say, feed all data to the algorithm, give it an objective, and it will do the right thing. And I was like yeah, the reason that falls down is the algorithms don't understand long term effects often, nor do they understand how people might respond to it, nor do they understand your intent for the product, and I think it's really important for product managers to play that role. That is our job. When you are working on algorithmic heavy products, your job is figuring out what the algorithm should be responsible for, what people are responsible for, and the framework for making decisions.

Lenny:
Welcome to Lenny's Podcast. I'm Lenny, and my goal here is to help you get better at the craft of building and growing products. Today my guest is Adriel Fredrick. Adriel is a VP product at Reddit where he focuses on incubating and scaling new products within Reddit. Before that, he was director of product at Lyft where he led the marketplace teams and the pricing teams over the course of five years, and before that, he was an early PM at Facebook where he spent four years leading the user acquisition team. Adriel is one of these incredible product leaders who's way too under the radar because he doesn't spend all day on Twitter and instead is executing and building great products. One of the goals of this podcast is to highlight incredible product leaders who you may not be aware of. And Adriel is a great example.

Lenny:
In our chat we talk about the origins of growth hacking, how to get better as a product leader, ways to increase diversity at your company, what it was like to work on Facebook's growth team early on, the future of AI and a lot more. It was such a joy chatting with Adriel and I am really excited to share this episode with you. With that, I bring you Adriel Frederick.

Lenny:
This episode is brought to you by Linear. Let's be honest, the issue tracker that you're using today isn't very helpful. Why is it that it always seems to be working against you instead of working for you? Why does it feel like such a chore to use? Well, Linear is different. It's incredibly fast, beautifully designed, and it comes with powerful workflows that streamline your entire product development process from issue tracking all the way to managing product roadmaps. Linear is designed for the way modern software teams work. What users love about Linear are the powerful keyboard shortcuts, efficient GitHub integrations, cycles that actually create progress and built in project updates that keep everyone in sync. In short, it just works. Linear is the default tool of choice among startups and it powers a wide range of large established companies such as Versal, Retool and CashApp. See for yourself why product teams describe using Linear as magical. Visit linear.app/lenny to try Linear for free with your team and get 25% off when you upgrade. That's linear.app/lenny.

Lenny:
Hey Ashley, head of marketing at Flatfile. How many B2B SaaS companies would you estimate need to import CSV files from their customers?

Ashley:
At least 40%.

Lenny:
And how many of them screw that up and what happens when they do?

Ashley:
Well based on our data, about a third of people will consider switching to another company after just one bad experience during onboarding. So if your CSV importer doesn't work right, which is super common considering customer files are chop full of unexpected data and formatting, they'll leave.

Lenny:
I am 0% surprised to hear that. I've consistently seen that improving onboarding is one of the highest leverage opportunities for both signup conversion and increasing long term retention. Getting people to your aha moment more quickly and reliably is so incredibly important.

Ashley:
Totally. It's incredible to see how our customers like Square, Spotify and Zoro are able to grow their businesses on top of Flatfile. It's because flawless data onboarding acts like a catalyst to get them and their customers where they need to go faster.

Lenny:
If you'd like to learn more, get started, check out Flatfile at flat file.com/lenny.

Lenny:
Adriel, welcome to the podcast.

Adriel Frederick:
It's good to be here, Lenny. Thanks for having me, man.

Lenny:
It's absolutely my pleasure. I actually found out about you through a guy named Jules Walter who we both know.

Adriel Frederick:
Yeah.

Lenny:
He's a PM at YouTube and I actually asked him, who should I have on this podcast that is maybe a little bit under the radar that is just amazing and immediately he suggested you. And so I'm really excited to be chatting.

Adriel Frederick:
Man, that is hype praise coming from Jules. Jules is my boy. I love him. He's such a great guy. Awesome product manager and dedicated to the craft that I just like being in his presence.

Lenny:
Yeah, and we're going to get him on this podcast at some point. He's busy with some kind of secretive project that we can't talk about. He's scheduled, I could talk about Jules all day, but he actually has the 10th most popular guest post on my newsletter still. How about that?

Adriel Frederick:
Wow. Yep, he's awesome.

Lenny:
Anyway, enough about Jules. So to give listeners a little bit of context on yourself, can you just give us a 55 second overview of all of the wonderful things that you've done in your career?

Adriel Frederick:
Ooh, we'll do real fast. So big highlight about me is I'm originally from Trinidad and Tobago, an island in the Caribbean. Came to the US for college, double E, got seduced by consulting and did that for a couple years, worked in oil and gas, electric power, heavy industries, loved that stuff, but also liked writing code on the weekends for fun. So I thought I should move into tech and I did. Worked at Intuit and helped develop their first iPhone app, which was a thing back in the day. Worked at a startup growth team at Facebook for four years working on user acquisition, which was really fun and a good kind of strong formative experience. I had. Quick stint in biotech and then worked on marketplace at Lyft. So rider pricing, realtime driver incentives, matching rider with drivers, and then a lot of the operational tools that we use to manage our marketplace. And so that's a bit of my journey in maybe 45 seconds.

Lenny:
That was great. I don't have a timer for these, but that sounded right. So we're going to talk about a lot of the things that you've learned along the way at all those places. Can you also share what you do now?

Adriel Frederick:
Awesome. Yes. So I'm the Vice President of Product Management for Reddit X, which sounds like we're out launching balloons into space, but that's not exactly what we're doing. We're more of a team at Reddit that's thinking about the evolving the modes of interaction with Reddit. So content, temporality, the audience that you're talking to, if you think about it, Reddit is primarily about asynchronous conversations between anonymous strangers about shared interests. Sometimes other people find answers to their questions on Reddit, but we're looking into and on the X team, evolving that to look at problems like helping people communicate fast during easier about shared interests, perhaps changing who they're having conversations with. Maybe it's about something other than a shared interest or maybe they have something else in common that brings them together. Maybe bringing video, audio, and other media into being a part of the product and playing with permanence and things like that.

Lenny:
Whoa, I felt like you were going to go into a metaverse direction. Is there metaverse angles to this?

Adriel Frederick:
Not really. I think we look at that as a potential technology, but our primary focus is a lot more on, I see modes of interaction and platforms that are a lot more at scale today.

Lenny:
Got it. Is there anything coming out in the near future we should be looking forward to? I imagine you can't talk about too much of what you're actually working on more concretely.

Adriel Frederick:
I think there's a few things that we've done recently that have been fun. We have an avatar marketplace that we've been working on recently where creators have been able to make art, put it up for sale on Reddit and make that available for other folks to buy and use. And that's been performing amazingly well. The underlying technology behind it is NFTs and we thought that technology was really important to use because it gives a creator a public way of acknowledging their rights to a piece of content. And so they have some form of IP protection, especially in a marketplace where you're doing something like selling digital art, we felt like that was incredibly important. I think the technology behind NFTs has been used for some really nefarious things, but I think we're still in the infancy of using these technologies appropriately. There's a lot of terrible use and a lot of uses that are wastes, but I think there's some gems in there and we're hoping to find some of those.

Lenny:
Sweet. I will avoid getting pulled into a web3 rabbit hole here, but that is very cool. Something I wasn't planning to ask about, but I'm curious because I was just talking to some other guest about this topic is the idea of these kind of R and D ish teams at larger companies and companies that have been around for a while. I know you're relatively new there and that's kind of maybe a new thing, but I'm curious, is there anything you've learned about how to set up teams like this and investments like this, these kind of long term horizon bets R and D teams?

Adriel Frederick:
Yeah, I think it's really good coming to this from being on the other side of it. If you think about where I've been, I've been on growth and on marketplace, which is as far as you get from seeing where on the new stuff kind of team and what I've seen happen a lot is organ rejection, that this thing looks so different to the rest of the body and the rest of the organization that you get some form of rejection of the ideas entirely. So I think what I've learned is a few things.

Adriel Frederick:
First is the rest of the company needs to see what you're doing as being core and critical to the mission. It can't seem like these guys are just playing off in a corner on something that isn't related to what we are doing every day. Because I think that leads to some of the resentment because you can imagine any team internally is fighting for resources and they look at this group as having resources that they can't get. They're like, Oh we got to get rid of that because they're not helping us do what we are here to do. So you have to be part of the core mission, otherwise you're going to have problems culturally with that. So I think that's one thing.

Adriel Frederick:
The second is it has to be everyone's success. So if you end up doing something on one of these R and D teams, it shouldn't just be the R and D team that wins. Everyone should feel like they win. And that is kind of relates to that first goal I was talking about. I think the third is you have to set up the work that these teams are doing such that people don't believe all innovation is going to happen on that team. It can like, okay, we're just stuck with the operational stuff and they're getting to have all the fun. Other teams are still going to innovate, but maybe we're taking on something that other teams don't have capacity for, that the organization needs and it's part of the core mission. And so I think that's been a lot of what I think about when working on and setting up these teams is to make sure that we are part of the organization and everyone wants to hug us as being, yes, you are one of us not, you kind of need to go off in your little corner and behave.

Lenny:
Amazing. That is really helpful. So just to kind of recap, you want it to feel like it's core and critical to the company. You want it to feel like it's everyone's success. It's not just, oh, Adriel over there is doing great, but we're stuck with these terrible hard problems. And then this idea of not all innovation's going to be just coming from that. We can all innovate but they're just working on this one specific innovation.

Adriel Frederick:
Yeah.

Lenny:
Awesome. Okay, great. Another question I definitely wanted to ask you. So you said you were born in Trinidad and Tobago, not something that you hear very often in tech. I'm curious your background and your journey to what you do now, how does that impact the way you lead, the way you build product, the way you just think about your career broadly?

Adriel Frederick:
Yeah, it's not something that I really think about consciously, but it affects me every day and it's tough not to see it in retrospect. I was the first Black product manager at Facebook.

Lenny:
Oh wow.

Adriel Frederick:
And so it's tough for me to not see that having some effect on what was built or how things were built or on me. So it's pretty meaningful. But I think one of the ways to see how it effects things is actually just to understand a little bit about Trinidad. It's kind of its own little unique animal. So Trinidad is an island in the southern Caribbean all the way up bottom next to Venezuela. It's a really diverse place. So ethnically it's 35% Indian, like from East India, 35% African, 25% mixed, and that last 5% is everything under the sun. European, Chinese, Arab, et cetera.

Adriel Frederick:
And then for religions it's about 60% Christian, but then that's a lot of different forms of Christianity in that 60%, 20% Hindu, 7% Islam. The media diet is a mix of British and American TV. You have a really broad range of incomes, but then schools are a melting pot, so you don't have as much of the kind of class and income segregation with schools that you get in most of the west. And so when you have that kind of a melting pot of ethnicities, religions, media consumption and kind of socioeconomic status in one place, you learn a lot of them because in school you're mixing up with everyone. One of the jokes we have is Trinidad probably has the most public holidays of any country because you have to celebrate everyone's holidays from Diwali for Hindus, Eid al-Fitr, to Christmas, I have friends who were fasting for Ramadan. I know a lot of the names of Hindu gods and I always love shocking my coworkers with my knowledge of this stuff. So that gives me this really different perspective that shows up at work.

Adriel Frederick:
So I'll give you an example. Something I've noticed in almost everybody I worked with in tech, as we work on mobile devices, people make an assumption that one phone number plus one device tied to one person. And growing up in Trinidad, I just knew that wasn't true. Someone who is using a prepaid phone could have their number change all the time, so that one person could have multiple phone numbers just because they were using prepaid. You have phones for two sim cards, that was pretty common. And a phone is and definitely was a really expensive digital device. It's a computer. So it was often shared and people couldn't just have one for themselves.

Adriel Frederick:
So when I was working on user acquisition and designing registration for Facebook, that knowledge was incorporated into the design of the product in ways that I think other companies not caught onto yet. And I know for a fact that a lot of that thinking that went into designing how you think about a phone number and a device and it's use among one, it's how to say pairing with an individual, has been helpful for Facebook's growth back then and even after I left, I know that's still been providing benefit. So that's a simple example of how just being in that environment and soaking up information could help product design in a way that I think wouldn't have happened if I and others like me weren't there.

Lenny:
You said you were the first Black PM at Facebook. I didn't realize that. How many PMs were there at that point when you joined?

Adriel Frederick:
Oh man. I remember we all fit into this conference room called Canada and that was probably my second week. It was probably about maybe 30 of us in there.

Lenny:
Wow. Yeah. Is there anything that you learned from that experience about just how to help with diversity at a company? Did Facebook do this well? Have you seen other companies do this better? Is there something you could share there for folks that are trying to work on this?

Adriel Frederick:
Man, that's a tricky one. So there's two parts of that, what was that like for me? I think it went quickly from being a little bit of imposter syndrome, like that day when I was sitting in that group was like, Dude, I'm one of 30 people working on Facebook. What am I doing? I'll belong in this group. This is crazy. And then I recognized after talking to a lot of the other PMs and the engineers, it's like no, no, no, they want me for what I know from my perspective because they're really trying to grow this product globally. And being this guy from Trinidad working on growth with the perspectives I just mentioned was appreciated. I think I was lucky enough to be on the growth team and having leaders on that team really valued diversity. I think about some of the teams I was on and they were awesome. I joke about them sometimes.

Adriel Frederick:
I remember being on a team where I was a Black Trinidadian product manager with a female Israeli engineering manager, a female Brazilian tech lead, then the rest of the engineering and design team was from all over the world. We had Russians, Chinese, some folks from Slavic countries and it made designing products fun because a lot of times when you're building a product and you want to think and get into your head of your customer, you have to go out and talk because you don't necessarily get them really well. Man, we didn't need to on that team. We would just argue with each other. We would think about how our friends would use it, how our cousins would use it, and we are covering a broad swath of the world when we were arguing about how to design a product. But I think the original leadership of the growth team, I think starting with Chima but then followed up with Javi.

Adriel Frederick:
[inaudible 00:16:51] that and kept bringing in that diversity of, again, ethnicities, religions, cultures from all over the world so that you could actually build a product that way. And it just makes you so efficient because an argument that might take two weeks to resolve because you have to go recruit a panel of users and talk to them and figure out what's going on. We kind of knock out in 15 minutes just throwing it back and forth with each other. And I can't stress how much that's important for building products that you want people across the world to use. You got to have your teams look like the world, it just makes you so much faster. It's not perfect. You still have to go out and talk to folks because we still have our own kind of monocultures that form that we need to get out of. But it helps a lot.

Adriel Frederick:
To your second point about diversity and how to foster it, man, from the beginning of my career at McKinsey to today at Reddit, I've been in rooms where everyone's asking the same questions about how to fix it and here's what I've seen work. When you recognize that you get business value from it, then it all of a sudden becomes something that you look out for and you take care of. That's it. And there's definitely a lot more to it, but I think when it goes from frankly something people feel they need to do to be PC or for cultural reasons or because they're getting social pressure to do it to something that you really recognize concretely, no, I get value from this and you are willing to take the other steps to have a culture at your company that utilizes it, then it becomes easy because when you bring folks in from diverse backgrounds, they retain and that's always the number one step to growth as you will know.

Lenny:
Retention.

Adriel Frederick:
You have to retain them, you have to retain diverse talent. And so you have to have an environment that values it, cares about it and uses it and rewards it because it's part of the core system of the company. Then once you have that working, it becomes a lot easier to recruit because people see you valuing it and bringing it in and wanting it. And it's not just lip service that you're paying. That's been what I've seen to be true in all the conversations I've had on the topic.

Lenny:
That first piece is interesting that it answers the second piece, which is the point you made about how having a large diverse global group of employees early on, especially for a company that's trying to go global and international is so powerful, you just save all this time. You don't have to necessarily interview people that you don't already have.

Adriel Frederick:
Yeah, there's something that feels like the approach to not doing it that way feels colonial. It almost feels like we're a group of people sitting down in this tower in this country, in this relatively sterile environment and don't worry, we know exactly what you need and these are the parts of the world. It just doesn't work well. So doesn't feel right to me also.

Lenny:
Yeah. Awesome. Thanks for sharing all that, that was really helpful. There's another topic I definitely wanted to spend a little time on, which is this interesting trend that I noticed when I was looking at your LinkedIn and your background. You worked at Facebook, Lyft, Reddit, and interestingly, they're all very in the news full of controversy type places. People like to tear them down and show all the reasons that they're doing bad things to the world. And I imagine as a PM that's just a challenging place to be and the fact that you've been at three different places. I imagine you've learned some stuff about how to operate as a product leader at companies full of chaos and fires and bad PR and things like that. So is there anything to share about what you've learned there?

Adriel Frederick:
I think the biggest thing is that as a PM you are a leader. You have to provide a buffering or damping effect on the team, and that goes two weeks. Sometimes we're doing stuff that everybody thought was amazing, this is the best thing we've ever seen, and you kind of got to bring people back down to earth and go, Look, that was cool, but we got a lot more stuff to do. We are really not there on providing the value that we want to provide to people in the real world, so slow your role and recognize that there's a lot more to do. And then when it's terrible and the press is telling you that you're the worst thing to ever happen in the world, you kind of have to also go back and say, Guys, slow down. We're not anywhere near as bad as what they think you see and know what we're doing and they're going to misunderstand us sometimes. And so pull your team up at this point in time and keep charging forward with the mission.

Adriel Frederick:
I think some controversy is necessary and so I may be at a different point on that one. I don't think you're going to have any meaningful influence on the world without changing some pattern of behavior. And if you're changing a pattern of behavior, there's somebody who's invested in that pattern of behavior and that's going to create some conflict. The most fun news stories to read involve conflict, so that's always going to make for a great story and put you in the press. For Facebook, it was traditional media and other social networks were one side of the fight and then Facebook was the other side of the fight and then it became other tech companies now and that always makes for a great story. With Lyft it was taxis and unions, and so you have to recognize that you're always going to have some bit of a challenge.

Adriel Frederick:
Now, the really hard part about dealing with this is understanding what criticism is valid and how much of it is just because the source of power is being changed. So I'll give you an example. Let's say with Lyft, rich medallion owners in New York, I had no sympathy for them when they were complaining about trying to ban Lyft because when I was in New York City putting my hand out to get a cab, they were tried right by my Black ass. So I'm sorry, I'm like, I do not feel that much empathy for them, but I think there were really legitimate complaints about the structure of driver pay that were coming up and that were behind I think some of the complaints and some of the big stories in the press and some of the big kind of legal action that was taken. Paying for pickup time when a driver's on their way to pick you up or when they drive somebody far out of town and they have a dead head to come back into a place where they can work, that's real.

Adriel Frederick:
That's a real problem that I think we got called out for that we weren't paying enough attention to and it got us off our ass to go fix it. I don't think we've, and I say we, but I'm not there, I don't think the problem has been fully solved, but I think as a PM listening to this, you kind of have to find the truth behind it and try to find a way to work on that and not get too lost in responding to the specific criticism. And so to walk this line between kind of going, yeah, some of this controversy is just part of the game, versus like, nah, this is really valid. Dude, to figure out where that is, you got to do what is so cliche, but you got to stay close to your users. And so to give you an example of how I did that, when a lot of the complaints were happening about driving on Lyft, I drove, I would just pick up the car and I would get out and I'd go drive and I'm like, let me me go feel this for myself. Let me go see what these guys are talking about.

Adriel Frederick:
But I can give you a story about Rick. I still remember this drive I did with Rick in Berkeley. So I'm at home, I just get in the car, I turn on the app, it's time to go driving. I get up ping 15 minutes away and I'm thinking do this, I go do this right now, this guy might cancel on me, I'm not really getting paid for this, but maybe the ride is worth it. So I drive on over, I'm dodging traffic, pedestrians, drunk college kids, stop signs, I make my way over to Rick, he's coming out Chez Panisse, and he's about 80 years old, jumps in the car and then I pushed the button to figure out the destination and it says the ETA to the destination is two minutes. So I was like, "Hey Rick, you get this right? What's going on?"He's like, "Hey, I had a little bit too much to drink. I'm worried about breaking my hip, so that's why I called a ride." And so I went from wanting to curse Rick out for making me drive 15 minutes to come pick him up to feeling like, all right, no, no, no, there's real value I'm providing you in driving him just two minutes. But I recognized that wasn't embedded in the structure of paying. Rick would've been happy to pee for my 15 minutes to come pick him up, but we weren't one, giving drivers compensation for that, nor were we finding a way to pass that through into pricing for Rick. It's a much more difficult problem than it seems from that simple example. But it clued me into why drivers were complaining. So then I went, got it. I understand what we need to do. So when there were all the PR was going on about AB5 and prop 22, I was out driving and I was out sitting with the team trying to figure out how we're going to design our product that helps pay a driver for this.

Adriel Frederick:
It still keeps prices reasonable for users, doesn't create bad incentives where you end up with riders not getting picked up when they really need a ride because I didn't want Rick to break his hip. He still needs a price that makes him feel like it's okay for him to take that ride, and finding a way to balance this out is actually more complex than you might think. And that's what I stayed focused on whether prop 22 passed or not, I was ready for either side with a solution that was going to work for rider and drivers. That was the job. And so I think for PMs it was so easy to get sucked into the press and it's like, Yo, plan the work, work the plan, go back to your job. That's what you're supposed to do. Solve for customers in the middle of this. And then you figure out how to communicate it well.

Lenny:
What I love about that strategy is it also helps you see that it's not everybody that is worried about something. I think of Airbnb, like all hosts are pissed off about this one feature, there's going to be a revolt. And then to your point, you talk to some, like nobody even knows about it. Nobody cares. Everyone's fine.

Adriel Frederick:
Yeah.

Lenny:
And so this, there's so many benefits to what you're talking about doing, which is talking to customers, not just paying attention to the loud voices.

Adriel Frederick:
Absolutely. I also have empathy for reporters too. The story that with the headline, some Airbnb hosts are annoyed by the-

Lenny:
Right.

Adriel Frederick:
I mean, come on, this is not a great headline. I recognize that they have a job to do and sometimes they hold people accountable and sometimes they're getting people to read a story that maybe has a bit of hyperbole in it. And so they have to do their job and I have to do mine too.

Lenny:
Yep. This episode is brought to you by Eppo. Eppo is a next generation AB testing platform built by Airbnb alums for modern growth teams. Companies like Netlify, Tenfold and Cameo rely on Eppo to power their experiments. Wherever you work, running experiments is increasingly essential, but there are no commercial tools that integrate with a modern growth team stack. This leads to waste of time building internal tools or trying to run your experiments through a clunky marketing tool. When I was at Airbnb, one of the things that I loved about our experimentation platform was being able to easily slice results by device, by country, and by user stage. Eppo does all that and more, delivering results quickly, avoiding annoying prolonged analytics cycles, and helping you easily get to the root cause of any issue you discover. Eppo lets go beyond basic click through metrics, and instead use your north star metrics like activation, retention, subscriptions, and payments. And Eppo supports test on the front end, the back end, email marketing, and even machine learning clients. Check out Eppo at geteppo.com, get E-P-P-O.com and 10x your experiment velocity.

Lenny:
Well you shared this really heartfelt story about Rick, what's your most stressful memory of working at Lyft?

Adriel Frederick:
I think the most stressful time was when I had to unwind a bad product I did and actually make a better version of it. It was really a pricing algorithm change, it was something behind the scenes that nobody would really see, but this was a fairly big initiative that we worked on. We had experts in revenue management to work like PhDs and the people who wrote the textbook on the subject helping advise us on this. We build this model, you launch it and you're expecting this big change. And it goes poof, just does a little bit. And then we work at it and we work at it and we work at it and eventually we get it to be good and it works really well in three cities. We start rolling it out to more cities and it's a pain in the butt to roll it out to more cities because it's super complex.

Adriel Frederick:
And eventually we get it rolled out to maybe a hundred cities and then someone says, "All right, cool, I want to change prices." And oh, we struggled for months to implement price changes and man, the sentiment around this product was just rough for a while. And I remember being on our walk after a particularly bad week of this and trying to figure out what I was going to do about this thing. Do we stay the course? After a while, the answer was kind of simple even though it was emotionally difficult. And the answer was like, Yo, we got to rebuild it. There was no answer where we couldn't have a product like this. We needed some ability to be able to influence prices so that we could actually run an effective marketplace. The current solution didn't work. It wasn't as operationally flexible as we needed it to be because we didn't consider that requirement when we were building it and we got caught up in the kind of algorithmic complexity and sweet sauce of it.

Adriel Frederick:
And so I recognized that we just needed to own up to it, tell everyone we didn't get it right and we needed to come at it in a different approach that was actually more flexible operationally. And we did. I think the big learning, at least in that business was you have to think about operational requirements and operational control as a first order requirement. And I think when a lot of us were building product at a lot of the other consumer internet companies, you didn't have to think about operational control. You gave the algorithms an objective, you feed them some data, you let it run, you observe it and make sure it's doing nothing crazy and you tweak it, but you didn't need to have day to day operational and strategic control over the product and we just needed to snap our brains into being able to put people in the loop with the algorithm.

Lenny:
For folks that haven't worked at a company with this kind of on the ground ops team, can you just unpack what that is? Like operational control, what does that actually mean in practical terms?

Adriel Frederick:
Okay, so I'll give you an example. So back in the days Lyft is in 300 cities, probably roughly across the US, and in every single one of those cities you don't have exactly the same pricing. It's a little bit different. And so sometimes you might need to make a change seasonally because traffic gets worse or because fuel prices were different or because there's a new tax or because your competitor did something that you need to respond to and your algorithm cannot see this. It has zero visibility into this. And so you need a person in the loop to not only give that visibility but also to make a decision about how you respond. Because I think also, let's say you're in Chicago and there is a snowstorm and you need to change the way, let's say you need to update pricing so that it handles the increases in driver pay that you need to create to get people out during a snowstorm. You don't know exactly how you want to respond, every snow storm's different and a person has to make that judgment call and provide the right information to the product to be able to get to utilize it. Now algorithms were handing a lot of that and they could generally respond, but to be a lot more precise and needed a person to help handle that, to make that call.

Lenny:
Got it. Cool. Thanks for sharing that. So you're making this point about when you're at a company that has a big operations component and obviously the core central product team, you were sharing some learnings about what you've learned to work in that environment. So yeah, I just wanted to come back to that.

Adriel Frederick:
For sure. For sure.

Lenny:
So the main thing you said is just ops as a first order component when you're designing the software. Is that the big learning?

Adriel Frederick:
I think it's not just treating ops as the kind of first order requirement. The bigger picture for me was when I look across my career is the algorithms need people to help make judgment calls. And so I saw it really, I got a heavy lesson in it at Lyft, but when I look back I recognized it was there at Facebook too. It just wasn't in my domain. There is always a judgment call that has to be made between how often are there going to be ads versus how often are we going to show organic stories from your friends and family? How often are we going to show content that you might be interested in that's not quite in that group? How often might be want to show you things that help you find your friends or help other people find their friends? And that is a judgment call that varies for different markets and different situations and there may be algorithms behind the scene that are making that call for every single person in real time, but there still have to be people applying some strategic judgment to that.

Adriel Frederick:
And I wasn't in the position of needing to do that at Facebook, but once I saw how much I needed to do it at Lyft and I kind of looked back at history, I saw that it was there too. But I think there are too many people who don't see this and believe that there's an algorithmic solution to everything. I think as a product manager and especially product managers working on systems that are heavy on machine learning or operations research and optimization, to think about where you want a person to make a decision and where you want the machine to be off to the races and to think about that as a product design problem because there actually is actually a computer interface that you have to think about there. You need information about what's going on, let's say at Lyft, what's going on with my market? How long does it take for somebody to get picked up? How expensive am I versus the competition? What are my goals in this market and how am I performing today with that? Give somebody information, but also give them the tools to execute the right decisions without creating trouble. And that's like a product design problem, that's a first order product design problem like anything else that you have to think about. And I'm not privy to it, but I would guarantee that there are people thinking about those same kinds of problems at other companies.

Lenny:
That reminds me, I was just listening to Zuck on Joe Rogan and he made this point that when you look at a post, you can add a little emoji reaction and you can have a little angry emoji reaction. And he made the call that we're not going to use the angry emoji reaction in our algorithm in any way, we're just going to ignore that because naturally you'd be like, okay, people are angry, that's interesting. Let's show that because it's interesting to people. But he specifically wants to avoid anger and facilitating anger probably because a lot of the feedback that they've gotten.

Adriel Frederick:
Exactly. And I think they're probably, I'd call them techno utopians who would say feed all data to the algorithm, give it an objective and it will do the right thing. And I was like, yeah, the reason that falls down is the algorithms don't understand long term effects often, nor do they understand how people might respond to it, nor do they understand your intent for the product. And I think it's really important for product managers to play that role. That is our job. When you are working on algorithmic heavy products, your job is figuring out what the algorithm should be responsible for, what people are responsible for and the framework for making decisions.

Lenny:
Is there an example that comes to mind where you did that or didn't do that well or someone on your team should have? Just something to make it a little more concrete even.

Adriel Frederick:
Let's assume that you are a person working on pricing and you say like, great, I have an objective that is I would like to win market share in a region. And you left that to an algorithm to say I need you to optimize prices such that you maximize market share, but what would the algorithm do? Drop your prices to the floor. All the way to the floor, and then you don't make any money. Okay great. So then you say, okay, what's the next step of that? Let's give it a constraint. Let's set some target that we might want to have for how little profit that you might be willing to take. Okay, go do it now.

Adriel Frederick:
What if the guy on the other side is doing the exact same thing? Both of you will hit your constraints and then the game will stop. Okay great. So now it then flips to, oh we have to choose where we want to win. And so I think one of the things we did that I'm particularly proud of is building products that help people see and understand that game a little bit more and decide where they want to. I think the first few pieces of that are not shockers, but that conclusion at the end where you get to, oh wait, I need to create a tool that gives people information to then decide how to play this game is actually what's critical.

Lenny:
Interesting. So kind of what I'm hearing is a lot of the work is giving humans more information versus giving machine learning algorithms more information and there's a lot more leverage potentially there, giving humans more ways to tweak and dial.

Adriel Frederick:
Let me refine that a little bit more. It's more about giving people the information that they can use for decisions that they alone are good at and giving machines the power to amplify a person's intent. So one of the ways I like to think about it is all software in any form including ML, is just a tool like a screwdriver and you could try to put a flat head into a Phillips and maybe it'll work a little bit but it's better to use a Phillips screwdriver. And we're tool designers generally and especially in part development function, you figure out how much do I put into the tool and how much do I leave it up to the person and I give the person the ability to choose what they want to do. I give them a screwdriver, a flathead, a Phillips, a torques and you let them decide how they want to use the tool for the application at hand.

Adriel Frederick:
And so going from that analogy to concretely with ML you say look, machine learning's going to be amazing at optimizing for a given objective, but it's not going to understand the constraints or strategic choices I need to make. The constraints and strategic choices that we need in the external world are always going to have to be decided by a person. You make that incredibly easy for people to do and intuitive for them to do and then you go that algorithm can then amplify their effect by making decisions on hundreds of thousands, potentially millions of individual decisions to take that person's intent and amplify it given all the information that they can learn in that single context. So I think about it as designing an interface and make it an extension of yourself rather than a black box on its own that you just need more information to. Is that helpful?

Lenny:
Yeah, it makes me think about a neural link and what Elon's trying to do, I don't know if this is how he thinks about it, but the [inaudible 00:39:56] guy described it as Elon's worried that AI will take over at some point and so he wants to build a tool that connects straights our brain that can access the power of AI to kind of have a chance against just a rogue computer in the future.

Adriel Frederick:
Even then you've got to make sure the person is still in control. I hear that thought and I go, okay, you build the interface but then who's in control? Is the person still in control or did they become a slave to the machine and you just made a better interface to make them a slave?

Lenny:
Oh shit, we're in trouble.

Adriel Frederick:
I am not yet as worried about these visions of them taking over. Thus far and maybe I haven't fathomed what they can do, they still seem like tools that need our guidance to be useful. Even the most amazing, we've been seeing the image generation and I've seen the cutting edge like text generation stuff. They can fool you into believing that they're like near human capability, but there is a lack of decision making and judgment that I see coming out of them. I see them as being again, extensions and useful like text generation algorithms. A lot of them can't write a paper for you and that's what I think people are scared of because it still requires your judgment to decide. Now when you decide what the salient topics are in something you've read, let's say you're doing a book report, you've decided what the topics are, it can help you write the paper faster for sure, but it can't write the paper for you. It can't choose the topics that your background and history and interest find useful or compelling to tease out.

Lenny:
This isn't where I was expecting our conversation to go, but I'll add another thought here because it's interesting, the way I think about it is there's nothing magical about our brain and so if that's true, why isn't there a world where we could just completely simulate it? Sam Harris talks about this a lot that it feels like once you get close then it could just accelerate so quickly beyond human potential. It'll start from 20% as good as a human to 40, 50, 60 and then it goes to a million times better. It can move so fast beyond us very quickly. So I think that's where a lot of the, not that I'm afraid of this, but I feel like that's where a lot of fear comes from. It could just dolly coming out and co-pilot just like holy shit.

Adriel Frederick:
Yeah, our brains are good with linear thinking, not exponential. So I've heard that argument that like, yes, this is increasing exponentially and you can't fathom it. I'm like, yes, that is definitely potentially true. Completely see that possibility and recognize that I have that cognitive defect in being able to understand it and even if it's a remote possibility, we should be paying attention to it. So I'm all for paying attention to it given the, let's just say the high cost of a low probability outcome is still a high cost and so it's still worth paying attention to.

Lenny:
Yep. Okay, good tangent, I wanted to chat about your learnings at Facebook. We've been chatting about all these other places and especially about growth, just stuff you've learned about growth and growth hacking and I was thinking about this interesting world that Facebook is in slash Meta where on the one hand when they started, and I'm talking about growth hacking, like Facebook did a lot of growth hacks, emailed all of Harvard, he had all these interesting dating thing happening and got a lot of controversy and it was all these interesting tactics to start Facebook, but now people use Facebook to growth hack and grow like Zenga famously, a few other places. So all that to say, I'm curious, what have you learned about growth slash growth hacking from your time at Facebook and other places?

Adriel Frederick:
I think growth hacking as traditionally assigned, finding those small changes you can make to a product to give you outsized impact, that is absolutely valuable. Where I've seen people get lost is they assume that if you do that alone, it will work. You can grow your way into something successful if you just find those few hacks and patch them together. And there's something about that that I find disrespectful to the people using the product. It's like you assume that they have no intelligence and they won't catch on to what you're doing eventually. The old saying fool me once, fool me twice, it kind of applies. So if you don't have a product that's providing real fundamental value to people, you can be a one hit wonder and have a flash in the pan and growth hack your way into something that might last for a few months but people will catch on it and then it'll disappear.

Adriel Frederick:
So I think that stuff is helpful, especially early on to get your initial traction. But you got to have something people and want to continue using. And when I think back over the products we did that really moved the needle, they were all things that just focus on the marginal user and figured out to make the product easier. It's easy to get seduced to thinking that there is a fast secret way to do it. And I'm like, no. The vast majority of it was just hard work and finding ways to solve the real problems. And what are those real problems? They were pretty damn simple but we just grinded on them for a long time it just stayed on it. One, make it easy to find the product. Number two, make it easy to get into the product. Three, stupid easy to find your friends. And then once you did that you were off the races and those were the things we were doing over and over again.

Adriel Frederick:
I think another big piece of it is reminding people that there's something interesting here and building the habit of coming back to the product and it was also part of it, but we just grinded on those few things over and over again. And some of the really big wins weren't hacks, they were just paying attention to little details. I'll give you an example. I remember sitting one day thinking about how to help people find their first few friends and we would do this thing where we'd have recommendations, if you could get one or two friends, you'd be off to the races and we could find you more people that were in that same friend group. So I thought about the way the people you may know algorithm worked, I get one or two friends, they would find your mutual friends and then would help find you more of those kinds of folks.

Adriel Frederick:
And I was like, you know what that does is it spirals you down one friend group but it doesn't get you all your other friends. I remember just looking at somebody using the product and recognizing that we were only taking them down this one path. So I was like, man, how do I see all your friend groups? And so we had this idea that we came up with that would do it. I'm not going to let that one out. And it was like game changer, like absolute game changer. Especially for users helping them find those first few friends in a few different friend groups, which then meant we could get you down one group and another and just continue building out that graph just by using recommendations. Because we had a great tool for seating it and that was not easy. That was not a hack. That was hard work.

Adriel Frederick:
I also remember one of my favorites is something Tom Allison did, Tom Allison I think now is responsible for the Facebook App, and when he was working on the engineering manager for one of those teams, there was a change we wanted to do to one of these algorithms and it was a bitch, it wasn't a hack and it was going to take a few months to pull off and Tom just hit it in a corner. He just let everybody know that we were really going to change the way this product worked. He had a really smart guy working on it, [inaudible 00:47:03], and they just hid off in a corner, rebuilt the product in the way it needed to be built to make it easier for us to operate it and scale it and then put it up there. I know of course they crushed it and they were incredibly modest about it, but it was not a hack. And it came from them looking at this deep problem of finding that thing that mattered and then saying, we need to make a fundamental change to make it easier to recommend friends to folks and just grinding on it.And so one of the things I recommend for people when they're thinking about growth for their product is figure out what the core actions are and then grind on them. Think about removing them, removing friction and some of them. But just keep staying at it and as you grind on it, you'll do little hacks. You got to figure out how to put the right text in the button and get it above the fold, create the right copy. All the things that we traditionally associate with growth marketing, you got to do those things. But to me that's stable stakes and just doing good product communication with your user, but then you got to think about this person who can't yet figure out your product and it's trying to take this action and making it stupid easy for them. I got a million more examples of that one, but that's the game. It's not just finding some trick to [inaudible 00:48:18] a site.

Lenny:
I love that. The way I think about this that I've heard well described is just there's no silver bullets, just many lead bullets.

Adriel Frederick:
Yes. And a few massive cannonballs every now and then. Every now and then there's some cannonballs.

Lenny:
What's an example of a cannonball as you think about that?

_[168 additional lines trimmed for context budget]_

---

### Building Lovable: $10M ARR in 60 days with 15 people | Anton Osika (CEO and co-founder)
**Guest:** Anton Osika | **Date:** 2025-03-09 | [YouTube](https://www.youtube.com/watch?v=DZtGxNs9AVg)  

# Building Lovable: $10M ARR in 60 days with 15 people | Anton Osika (CEO and co-founder)

## Transcript

Anton Osika (00:00:00):
... Lovable is your personal AI software engineer. You describe an idea and then you get a fully working product. The reason is to enable those who have had such a hard time finding people who are good at creating software that's been their absolute bottleneck and let them take their ideas and their dreams into reality.

Lenny Rachitsky (00:00:19):
You guys hit 4 million ARR in the first four weeks. You hit 10 million ARR in the first two months with just 15 people. You're the fastest growing startup in all of Europe. How did you decide on Lovable is the name. It's so sweet.

Anton Osika (00:00:31):
The best word for a great product is that it's lovable. A lot of jargon that I like to use to emphasize what we should be striving for is building a minimum lovable product and then building a lovable product and then building an absolutely lovable product. So I took that jargon with me in the company name.

Lenny Rachitsky (00:00:47):
People would wonder just what jobs will be more important, what skills will be less important?

Anton Osika (00:00:51):
Doing a bit of everything. Being a generalist, I think much more important than it used to be. If I'm putting together a product team today, I would really obsess about getting as many skill sets as possible for each person I hire.

Lenny Rachitsky (00:01:03):
What have you done that has allowed you to grow this fast with so few people?

Anton Osika (00:01:07):
People love the product. That's the driver of the growth.

Lenny Rachitsky (00:01:15):
Today, my guest is Anton O-C-K. Anton is co-founder and CEO of Lovable, which is essentially an AI engineer that takes an English prompt and codes a product for you in minutes. You can then talk to it, iterate on the product, and then launch it to the world. It's one of the fastest growing products in history. The fastest growing startup in Europe ever, and as Anton describes, their goal for Lovable is for it to be the last piece of software that anybody has to write because it'll be able to create all future products for us. They launched just a few months ago in the first four weeks, hit 4 million ARR in the first two months across 10 million ARR, all with just 15 people. Absurd. In our conversation, we covered a lot of ground, including a live demo of Lovable, how their team operates, how they hire, what has most enabled their team to scale this quickly with so few people, pro tips for using Lovable, how it all started, how he recommends you build product teams going forward with tools like this existing, what skills will matter more and less going forward?

(00:02:17):
Plus how to think about Lovable versus competitors and so much more. If you're trying to wrap your head around how product building will change with the rise of AI tools, this episode is a must watch. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. Also, if you become a yearly subscriber of my newsletter, you now get a year free of Perplexity and Notion and Superhuman and Linear and Granola. Check it out at Lenny'snewsletter.com. With that, I bring you Anton, O-C-K.

(00:02:49):
This episode is brought to you by Cinch the customer Communications Cloud. Here's the thing about digital customer communications. Whether you're sending marketing campaigns, verification codes or account alerts, you need them to reach users reliably. That's where Cinch comes in. Over 150,000 businesses, including eight of the top 10 largest tech companies globally use Cinch's API to build messaging, email and calling into their products. And there's something big happening in messaging that product teams need to know about. Rich Communication Services or RCS, think of RCS as SMS 2.0. Instead of getting texts from a random number, your users will see your verified company name and logo without needing to download anything new. It's a more secure and branded experience, plus you get features like interactive carousels and suggested replies, and here's why this matters. US carriers are starting to adopt RCS. Cinch is already helping Nature Brands send RCS messages around the world and they're helping Lenny's podcast listeners get registered first before the rush hits the US market. Learn more at get started at Cinch.com slash Lenny. That's S-I-N-C-H dot com slash Lenny.

(00:04:02):
This episode is brought to you by Persona, the adaptable identity platform that helps businesses fight fraud, meet compliance requirements, and build trust. While you're listening to this right now, how do you know that you're really listening to me, Lenny? These days, it's easier than ever for fraudsters to steal PII, faces and identities. That's where Persona comes in. Persona helps leading companies like LinkedIn, Etsy, and Twilio securely verify individuals and businesses across the world. What sets Persona apart is its configurability. Every company has different needs depending on its industry, use cases, risk tolerance and user demographics. That's why Persona offers flexible building blocks that allow you to build tailored collection and verification flows that maximize conversion while minimizing risks. Plus Persona's orchestration tools, automate your identity process so that you can fight rapidly shifting fraud and meet new waves of regulation. Whether you're a startup or an enterprise business, Persona has a plan for you. Learn more at withpersona.com slash Lenny. Again, that's with P-E-R-S-O-N-A dot com slash Lenny. Anton, thank you so much for being here and welcome to the podcast.

Anton Osika (00:05:19):
It's a pleasure to talk to you, Lenny, great to be here.

Lenny Rachitsky (00:05:22):
I don't know how you have time to do this podcast. Your life must be insane these days with the pace at which you guys are scaling, just how much is changing in AI every day. So I just extra appreciate you making time for this. I think you said it's 10:30, your time, is when we're doing this.

Anton Osika (00:05:39):
I'm a bit tired, yes. Mostly from the crazy pace of everything, but yes.

Lenny Rachitsky (00:05:45):
This is going to be an invigorating conversation and you're not going to be able to sleep.

Anton Osika (00:05:50):
Yes. I'm sure. I'm sure.

Lenny Rachitsky (00:05:51):
Okay, so for folks that are maybe a little bit familiar with Lovable or not at all familiar, what is Lovable? What's the simplest way to understand it?

Anton Osika (00:06:00):
I'd say Lovable is your personal AI software engineer. You describe an idea and then you get a fully working product from the AI. And what this means is that entrepreneurs actually today, they turn their ideas into real businesses. We have a lot of designers and product managers that create the first version of their product ideas to show to the teams, and some of them become founders because of the empowerment from this, but also developers themselves, they actually writing code or creating products much faster. The reason, it's pretty obvious for me, but I'll spell it out, the reason why we're doing Lovable is that I don't know about your mom, but my mom doesn't write code and-

Lenny Rachitsky (00:06:52):
Same.

Anton Osika (00:06:55):
... almost all my friends throughout my life reached out for help. Like, "Anton, I need to build something. How do I find a great software engineer?" And we are building for this 99% of the population who don't write code. Currently, if you're technically inclined, you get much further, but over time, naturally the way to build software is by just talking to an AI. And that's how we see it.

Lenny Rachitsky (00:07:21):
I love the way that you guys describe it and you didn't mention it, but I think it's building the last piece of software ever. How do you phrase that?

Anton Osika (00:07:28):
Yeah, we say we're building the last piece of software.

Lenny Rachitsky (00:07:31):
The last piece of software. Okay, we're going to do a live demo, but first of all, can you just share some stats on the scale of this business at this point because it's quite absurd.

Anton Osika (00:07:42):
Yeah. So we launched Lovable less than three months ago, and now we have 300,000 monthly active users and 30,000 of those are actually paying and it is growing at the same rates, just almost only through organic word of mouth.

Lenny Rachitsky (00:08:02):
Okay. And I'll share a couple stats in terms of revenue, just so folks know this, and we'll have this in the intro too. I think you guys hit 4 million ARR in the first four weeks. You hit 10 million ARR in the first two months with just 15 people. You're the fastest growing startup in all of Europe, and you guys had to rewrite your entire code base recently and you couldn't ship any new features for a while. Is that right?

Anton Osika (00:08:26):
That's right, yeah. People were saying like, "Oh, you're shipping so fast." And we were all quite frustrated because we wrote our service in this kind of scripting language and then as we started scaling, we were just, no, we have to throw everything away and rewrite it in a more performant way.

Lenny Rachitsky (00:08:43):
Okay, before we get to the demo, last question, you shared there's some companies that have started based on Lovable. I didn't even know that. So what are some examples of companies slash businesses that have launched off of Lovable and now are actually companies?

Anton Osika (00:08:56):
I mentioned designers using Lovable and one of our early users, Harry, he started shipping real web apps to his clients instead of just shipping designs. And then he went on to say, okay, wait, I'm going to start an AI startup. And his company, he launched on Product Hunt and everything and making money is just like, let's anyone upload their photo library and then the AI parses and categorizes it. And if you go to launched.lovable.app, this is an app built with Lovable is again a product Hunt version where you can see a lot of businesses or small SaaS featured there.

Lenny Rachitsky (00:09:38):
Okay, cool. So we're going to come back to some of this stuff, but let's get into demo. I rarely do demos on this podcast, but I'm finding that I think it's really important for people to see these products in action because in a large part, this is the future of product building and a lot of people hear about, "Oh yeah, AI's coming," and I don't think a lot of people actually see what the latest tools are capable of. And so I love showing these sorts of things on this podcast.

Anton Osika (00:10:05):
So Lenny, I was thinking, did you ever consider making a copy and build your own Airbnb?

Lenny Rachitsky (00:10:14):
I haven't, but go on.

Anton Osika (00:10:17):
How about you do that?

Lenny Rachitsky (00:10:18):
Let's do it. Let's do it. Okay, so we're going to make our own Airbnb.

Anton Osika (00:10:18):
Okay.

Lenny Rachitsky (00:10:21):
Okay, cool.

Anton Osika (00:10:22):
So I just put in the first prompt for an Airbnb clone.

Lenny Rachitsky (00:10:27):
Okay. And what is the prompt, just for folks that aren't watching?

Anton Osika (00:10:31):
Two words, Airbnb clones. That's the prompt.

Lenny Rachitsky (00:10:33):
Okay.

Anton Osika (00:10:34):
Just start simple and then what you get is that the AI says, okay, I can go through what does a beautiful Airbnb clone look like and it goes through a bit of design decisions and then I'll zoom out to see more of it. We have this just UI that is... I mean it has all the nice things you would expect from Airbnb clone where you see different categories and you can see two listings from Airbnb with login buttons and everything. So far it doesn't have the functionality of Airbnb, it just has the UI. I would now ask for an improvement on some of the functionality. Like if I'm switching category, I want to see different listings, let's say. But if you have any thoughts on what we should build next, let me know.

Lenny Rachitsky (00:11:25):
Okay, and so you had this preloaded, so you didn't see how long it would take, but how long would this normally take for it to just write all this code and have it for you?

Anton Osika (00:11:32):
The first prompt takes 30 seconds.

Lenny Rachitsky (00:11:34):
30 seconds? Okay. And it's like a very good copy of Airbnb. I love that you didn't have to show it a design, you just tell it Airbnb and it knows. Okay, so your question is would I want to add to my own version of Airbnb? I've always wanted to explore buying the place that I look at just like, Is this for sale? So what if we see what that would feel like if you're just a way to buy a listing.

Anton Osika (00:11:59):
Okay. Okay. So how about we add, I mean prompting is important here, so let's be specific, but we would ask, add a button on the listing which has purchased this Airbnb home. Is that it?

Lenny Rachitsky (00:12:16):
Perfect.

Anton Osika (00:12:19):
Okay, so, add, and [inaudible 00:12:19]. I'll be even more specific. It will pop up a model to purchase the listing.

Lenny Rachitsky (00:12:32):
Perfect. And I love... So I think something as you're typing, I'm just going to share thoughts as you're doing this. So the site that you asked this AI engineer to build, it's actually a functioning website that you can browse around. It's not just a design, obviously there's no actual listings here, there's no actual houses here. Say you were trying to actually build Airbnb and you wanted to start adding actual homes that plug into this, how does that sort of step work?

Anton Osika (00:13:02):
So as you say, this is just kind of the mockup UI, but it's also interactive. If I want to add login and add listing management, then we will connect something called the backend. So where data is stored, where user's log information is stored, and I can show you how to do that. First let's just try out where we got with this short prompt.

Lenny Rachitsky (00:13:29):
Let's do it.

Anton Osika (00:13:31):
Adding the purchase listing and it didn't do exactly what I wanted. I said, add a button... Or I didn't say what a button should say, but it says book now, and if I click book now I get a booking confirmation. So the AI was like, okay, it didn't... It was probably surprised by you wanting to buy the listing since it's Airbnb. So it still says book the listing, but it shows a pretty model where I can click confirm and pay. And then it's says booking confirmed.

Lenny Rachitsky (00:14:05):
I'll just say real quick, I love that this is actually a really good example of why being a good product manager is important. A lot of wasted time happens when you're not clear about the problem you're trying to solve and why you're trying to solve it and all that kind of stuff. So it's really cool that this is a use case where you have to be really good at explaining what it is you want. And it's interesting, you don't have to tell this AI-why. Humans want to understand, "Why is this important." Mostly you need to be very clear about what it is you're doing and I love that's a really strong PM skill. Your PM's really good at that. So we have to...

Anton Osika (00:14:39):
Hey. Explaining exactly what you expect and what you're not getting is even more important with AI than with the humans. So I'm going into hooking up more of the actual functionality, but first I'll actually show you something. What's the fastest way to change what went wrong, it's created buttons that say book now and I want them to say, "Buy now." And what I could do is select this item and say change it to buy now. But what we just realized is that you can actually edit this, this is a fully functioning product, but you can edit it visually like you do in Squarespace and Wix and so on. So I'll just change the text to buy now and then it instantly changes. It actually changes deep down in the code base, but it's very fast to do that.

Lenny Rachitsky (00:15:35):
So I think people listening to this and seeing this, if you're not aware this is the cutting edge of tools like this, no other tool out there lets you generate code from an AI engineer and then actually just change a small element of it of every other tool that I'm aware of. You have to ask the agent, do this for me, and then you hope that it does the right thing. So this is a huge deal which you just showed. Right?

Anton Osika (00:16:00):
Yeah. Now it says buy now.

Lenny Rachitsky (00:16:01):
Okay. Like that's amazing. Okay, and that's something you just launched?

Anton Osika (00:16:04):
Yeah. Great. We just launched this a few days ago, but I won't go into for building the full functionality, but what it looks like is that you connect an open source backend as a service and that's called SuperBase. And I have this instance to connect to that's completely empty, just like one click to set that up and now it's connected to the backend. It's just automatically generating some code and explaining what I can do next. And what I would do now is, say, let's add login, let's say let's add login.

Lenny Rachitsky (00:16:41):
And where is it actually hosted on the backend and everything in general?

Anton Osika (00:16:45):
So everything can be one click deployed and then it's running. It's hosted by a cloud vendor, which is hosting, I think a huge chunk of the internet, it's called Cloudflare, and the backend is hosted by also good cloud writer, which is called SuperBase.

Lenny Rachitsky (00:17:07):
Amazing. Okay, let's wrap up the demo, that was... Unless there's anything else, was there anything else really important that you wanted to show?

Anton Osika (00:17:14):
No I'll just explain what I would do next. I would say, okay, let's add login. Let's make the listings editable by the users so users can upload listings and then this is going to take a bit more time, but with patience and good prompting skills, you're going to get to a full working Airbnb.

Lenny Rachitsky (00:17:33):
That was a really good piece to add. So basically this is getting to a place where it actually is not so different from actual Airbnb. People can log in, they can add their home, you can add internal tools to add listings for your, say, sales team, ops team. Basically it just will allow you to build a marketplace that looks a lot like Airbnb. Amazing. Okay, thank you for the demo. I think for a lot of people they're like, "Yeah, yeah, I've seen this kind of stuff," for most people, like, "Holy shit." It's unreal what... It's almost like we're taking for granted now. You can ask an app to build you a whole website and that costs probably like a few pennies. It took like five minutes versus it would've been tens of thousands and weeks and weeks and months to even build just a prototype.

Anton Osika (00:18:23):
I mean, these tools as we see here, they're already very good, it looks really good as well, but mainly I would say they're getting better very, very fast. And I'd say one of the bigger bottlenecks is now they're not integrated into the current way that you have your existing products and so on. But since they're getting better so fast, I think the best thing for people who are interested in this or interested in just being a part of the future economies, get your hands very dirty with these tools because being in the top 10% in using them is going to absolutely set you apart in the coming months and years.

Lenny Rachitsky (00:19:05):
So let me follow that thread. So say you are magically able to sit next to everybody that is using Lovable for the first time and you could just whisper a tip in their ear to be successful with Lovable, what would that tip be?

Anton Osika (00:19:20):
It takes a lot to master using tools like Lovable and being very curious and patient and we have something called chat mode where you can just ask to understand like, "How does this work? I'm not getting what I want here, am I missing something? What should I do?" Is the best way to be productive is also one of the best ways to just learn about how software engineering works, which is you don't have to write the code anymore, but it is useful to understand how software engin- or how building products works. So I think that's the patience and curiosity is super useful. The second part that we spoke about is that being, if I would sit next to you, I would probably say like, "Hey, you are not being super clear here." For example, don't say it doesn't work. Just explain exactly what you're expecting and which parts are working and which parts are not working. And that's something that a lot of people don't do naturally.

Lenny Rachitsky (00:20:25):
I love that when you have an engineer you're working with that does a very expensive mistake to miscommunicate something, to just forget about a feature, to forget a better requirement, and here it's... You do that and then 30 seconds later you're like, "Oh okay, sorry, that was wrong." And then you could just try again.

Anton Osika (00:20:41):
That's true. It might be more costly with humans.

Lenny Rachitsky (00:20:45):
Okay, and so the first step is chat mode. So your advice is chat with the... What do you call it? Do you call it an agent? What's the term for the thing that you were talking with?

Anton Osika (00:20:57):
Yeah, Lovable is an agent.

Lenny Rachitsky (00:20:59):
Just Lovable?

Anton Osika (00:20:59):
Yeah.

Lenny Rachitsky (00:21:00):
Okay. So you're talking about Lovable by the way. How decide on Lovable as the name? It's so sweet.

Anton Osika (00:21:06):
I think it's all about building a great product. That's what I want more people to be able to do and the best word for a great product is that it's Lovable. A lot of jargon that I like to use to emphasize what we should be striving for is building a minimum Lovable product and then building a Lovable product and then building an absolutely Lovable product. So I took that jargon with me in the company name.

Lenny Rachitsky (00:21:36):
That is great. Absolute Lovable product. ALP is the new MVP. Okay, so we talked about this, the scale you guys have hit at this point, I imagine it's far beyond 10 million ARR. Do you share that at this point or are you keeping that private?

Anton Osika (00:21:51):
We don't anchor on the numbers, but I could probably do a two X tweet about this quite soon. Yes.

Lenny Rachitsky (00:21:57):
Okay, so it's far beyond 10 million ARR at this point. It's one of the fastest growing startups in history, the fastest growing startup in Europe. I want to zoom us back to the beginning. What is the origin story of Lovable? How did it all begin? What was the journey to today?

Anton Osika (00:22:14):
I think I was not impressed by what people were doing with the large language models [inaudible 00:22:21], especially after I was using them way back. But when ChatGPT came out, they were starting to get really good at taking a human instruction and spitting out code and then people in my team, I was the CTO at a YC startup, they felt like, "Oh, Anton, you're exaggerating. This is not going to change anything in the coming years." So I wanted to prove a point and I created an open source tool called GPT Engineer where you write something like create a snake game and then it spits out a lot of code, a little of different files and then opens the snake game. And then I tweeted a video about that and GPT Engineer is to date the most popular open source tool to showcase the ability for large language models to create applications and it's at like 50 something thousand GitHub stars and dozens of academic references.

Lenny Rachitsky (00:23:21):
And I know that I'll just add that it GitHub shut you down because they thought it was some kind of attack, like how many stars you're getting, how many people were using it,

Anton Osika (00:23:29):
Right. Yeah. So that came later. That's with Lovable. So this is Lovable. Lovable, earlier was always creating new projects on GitHub when someone used Lovable and we asked them, "Is it fine? How was the limits here?" They said, "Oh, there are no limits." But once we started creating 15,000 projects per day, so there were a lot of usage. Then some engineer when was on call, maybe they woke up in the night and they saw their servers were taking too much load because of us. So then they shut off down completely and we got this email that said, "Oh, you broke some kind of rules and we didn't know what was going on."

Lenny Rachitsky (00:24:13):
That's similar to a story I heard when ChatGPT was originally being trained, Microsoft servers blocked it because they thought it was some crawler and it was just actually the very first version ChatGPT being trained on data. Anyway, keep going.

Anton Osika (00:24:29):
So I built this tool called GPT Engineer and I was thinking about we're seeing the biggest change humanity will ever see, I think, where before you had the manual labor being taken over by machines, but now it's actually cognitive labor being done better than humans by machines and what's the best way to have some kind of positive impact here? It's not to make engineers more productive, which there's a lot of companies using AI to make engineers more productive, Microsoft did with co-pilot and so on. But it is to enable those who have such a hard time finding people who are good at creating software that's been their absolute bottleneck and let them take their ideas and their beliefs into reality. So enabling more entrepreneurship and innovation by building the AI software engineer for anyone. And then I grabbed a previous colleague of mine who has also been a founder, Fabian, and I said we should build something like GPT Engineer but it has to be for the people who don't write code and that's the story.

Lenny Rachitsky (00:25:43):
Okay. And then that became lovable? There's the shift from open source into a product that anyone can use but also pay for. Makes sense. Okay, so from that point I saw a stat that you started making a million dollars in ARR per week and once you launched lovable, is that true?

Anton Osika (00:26:00):
Yeah, so launched, we actually called the first version of the product like GPT Engineer app and it was very different in some ways and we launched that under a waitlist and said like, Oh yeah, we have this waitlist and we got a lot of feedback and iterated. Finally, when we thought the product was really good we said okay, now we have a Lovable product. And it was mainly on the AI that we did a lot of improvements, once we launched that, that was 21st of November, so that's almost three months ago. We just hit 1 million ARR in a week and then it kept growing at that pace. It still growing at even faster than that pace.

Lenny Rachitsky (00:26:43):
Faster than 1 million ARR per week. Holy shit.

Anton Osika (00:26:48):
Yeah.

Lenny Rachitsky (00:26:48):
Okay, that sounds like product market fit to me. You said that you did a lot of work on the backend. I saw you tweet about this that you guys figured out some kind of unlock on scalability, like a new scaling law that allowed you to build something like this. What can you talk about there that on the technical element allowed you to build something new and the successful?

Anton Osika (00:27:08):
There are many scaling laws I would say when you build AI systems and this one in particular is about when you put in more work, the product reliably gets better and better. And what you've seen generally when you have AI building something is that it can get stuck in some place. It is super good in the beginning and then it gets stuck. What we did was to painstakingly identify places where it got stuck and there is different approaches but address different ways how we do it but address the places where it gets stuck, tune the entire system quantitatively and having a very fast feedback loop to improve it in the areas where it got stuck. The most important areas, it still does get stuck sometimes, but that's the scaling law and we're still early in that scaling law, I would say.

Lenny Rachitsky (00:28:04):
And so when you talk about things getting stuck, it's like the AI agent just saying, I don't know what to do from this point or they introduce some kind of bug. Is that an example of getting stuck?

Anton Osika (00:28:13):
Yeah. It introduces some kind of bug and then it's not smart enough to figure out how to get out of that bug.

Lenny Rachitsky (00:28:20):
I see. And this is a common problem people have with tools like this is they get to a certain point and then it's like, "Well I don't know what to do. I'm not an engineer, here's a bug it's running into or the infrastructure's built the wrong way." And so it sounds like one of the paths to solving that is what you're describing is you make the AI smarter to avoid more and more of these places they get stuck. Another is people just learning how to get AI unstuck. This is something when we had Amjad on the podcast from Replit, he said that this is the main skill that he thinks people need to learn is how to unstuck AI when it runs into a problem. Just thoughts there, I don't know anything along those lines come up as I say that.

Anton Osika (00:29:04):
This is something that is a problem today and the frontier of where this is a problem is very rapidly receding back. So what we did was we identified the most important areas, so specifically adding login, creating data persistence, adding payment with Stripe. Those are the things that we made sure it doesn't get stuck on, for example. And the places where it gets stuck today is currently something that you can use being very good at understanding and getting unstuck, but in the future it won't be so important. This experience just going to not get stuck.

Lenny Rachitsky (00:29:48):
And I know you're not talking super in-depth about this because this is one of your unfair advantages, this kind of stuff you figured out. So I'm not going to push too far. I know you want not everyone's into exactly the same stuff. So I want to zoom back to the pace of growth that you guys have seen. One of the big stories, everyone's always looking at you guys of like 15 people, 10 million ARR in two months. That's absurd. I don't know if it's ever been done in history. If so, it's maybe a couple other AI startups recently. How have you been able to do this? What have you done that has allowed you to grow this fast with so few people?

Anton Osika (00:30:24):
I'd like to take credit of having done everything end to end in the product, but we are building on top of taking the oil here, which we have discovered oil, which is are the foundation models and then what we've done is that we're obsessed about what's the right way to present this to a user. What's the interface for the human to get as much out of this as possible? Packaging together, I showed you in the demo how you can add authentication and making this work seamlessly together as a whole. That's what we've done. And then people love the product. That's the driver of the growth. For getting awareness, we've mainly been posting what we've shipped on social media, that's how people know about us.

Lenny Rachitsky (00:31:17):
So building in public is how people usually describe that. So I think it's like you guys have the advantage of the demos are just like, "Holy shit, you can do that." And then you guys share the numbers that you guys are growing at. So it's innately interesting and shareable, but I imagine most people have something interesting to share. I guess is there anything that you think you did that other companies maybe haven't done that make the product so lovable?

Anton Osika (00:31:43):
I mean the team is everything in building a great product, so I just give a big shout-out to the team that has written the code. I haven't written much of the code recently, I would say. You want people who can ship really fast and have good taste for what this simple, what's the right abstractions and I think that's what we've done differently and have this obsession for us making it better and better and better.

Lenny Rachitsky (00:32:17):
This episode is brought to you by the Fundrise Flagship Fund. Full disclosure, real estate investing is boring. Prediction markets are exciting. Meme coins are a thrill ride. Even the stock market can swing wildly on a headline. Hello Deepseek. But with real estate and investing there's no drama or adrenaline or excuses to refresh your portfolio every few minutes. Just bland and boring stuff like diversification and dividends. So you won't be surprised to learn that the Fundrise Flagship real estate fund is a complete snoozefest. The fund holds 1.1 billion dollars worth of institutional caliber real estate managed by team of pros focused on steadily growing your net worth for decades to come, see? Boring.

(00:32:59):
That's the point. You can start investing in minutes and with as little as $10 by visiting Fundrise.com slash Lenny. Carefully consider the investment objectives, risks, charges and expenses of the Fundrise Flagship fund before investing. Find this information and more in the fund's prospectus at fundrise.com slash flagship. This is a paid ad.

(00:33:22):
Okay, I want to come back to the team. I know you have a lot of thoughts there in terms of writing code, how much do you guys actually use AI to write the code that is building Lovable? How does that work on your team?

Anton Osika (00:33:32):
We have set up lovable so that we can change lovable with itself. We have done that. There is a lot of hyper-specific things in terms of running a separate... We spin up a dedicated computer for each user. It doesn't do everything. Lovable doesn't do everything. So we use the tools that are for developers, not for the 99%, most of the time. And everyone uses AI all the time in writing code. It's also in great course for experimentations.

Lenny Rachitsky (00:34:10):
And are there tools like Cursor and stuff like that? Like any tools you can share right now?

_[285 additional lines trimmed for context budget]_

---

### How to speak more confidently and persuasively | Matt Abrahams (professor, speaker, author)
**Guest:** Archie Abrams | **Date:** 2024-03-31 | [YouTube](https://www.youtube.com/watch?v=LpbBzmXrzEY)  

# How to speak more confidently and persuasively | Matt Abrahams (professor, speaker, author)

## Transcript

Archie Abrams (00:00:00):
When you have teams naturally break up the world into different funnel stages or different points in the journey, it gets very seductive to look at my part of the funnel and what's my conversion rate through that part of the funnel, right? And then the team starts to optimize for that conversion rate as their north star. But in practice, it's actually almost always easier to just make it harder to do the thing right before your step in the funnel to increase your conversion rate. Instead of I'm trying to convert a bunch of people, I just want more people to get activated.

(00:00:32):
And then once you start thinking that way, you realize actually the best way to get more people to get to a step is just get more people in the door in the first place. That will always hurt your conversion rate, but it may actually give you more people on the outside.

Lenny Rachitsky (00:00:48):
Today my guest is Archie Abrams. Archie is VP of product and head of growth at Shopify, where he leads an org of over 600 people across product, design, engineering, data ops, and growth marketing. Shopify is both an incredibly unique and also an incredibly successful business, and they do things very differently. And as a result, there's a lot that we can learn from how they approach building product and driving growth.

(00:01:12):
Some examples include their priorities in product roadmap are driven by a 100-year vision that comes from Tobi, the CEO. And the core product teams don't have metrics or KPIs. They're essentially banned. And instead, decisions are made based on taste, and intuition, and building towards this long-term vision. Also, the growth team optimizes for churn, which is unlike any other company I've ever come across. And once you hear why, this will make a lot of sense.

(00:01:38):
Also, they keep long-term holdouts for every experiment they run, and they automatically look at the impact these experiments have had on the business a year later, two years later, and three years later, and then revisit these decisions down the road.

(00:01:52):
And in our conversation, we dig into all of this plus how Shopify organizes their growth team, how they run experiments, how the growth team collaborates with the product team, how they measure impact. Plus, Archie shares a bunch of very specific and interesting examples of changes that have driven growth for the business and so much more. This is such a fascinating conversation, and I know this will give you a lot to think about in terms of how you run and organize your own product and growth teams. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. It's the best way to avoid missing feature episodes and it helps the podcast tremendously. With that, I bring you Archie Abrams. 

(00:02:34):
Archie, thank you so much for being here and welcome to the podcast. 

Archie Abrams (00:02:38):
Thanks Lenny.

Lenny Rachitsky (00:02:38):
Excited to be here. Okay, so what I want to do with our time together is to basically do kind of a living archeology of how Shopify grows and what you specifically have learned about growing a company like Shopify into this just juggernaut of a business that it's turned into. To give people a little bit of a sense of just how large Shopify has gotten, so maybe surprising them about the scale of this company at this point. Could you share some stats about the scale of the business at this point?

Archie Abrams (00:03:09):
Yeah, absolutely. So overall, we're about 10% of e-commerce in the United States. So basically if you're not buying an Amazon or Walmart, you're probably buying on a Shopify-powered store. And behind the scenes globally, we did about 235 billion in GMV in 2023, which is roughly the size of the economy of Finland. So we've got a big economy and big impact happening from Shopify.

Lenny Rachitsky (00:03:37):
Wow. I think interestingly with Shopify, it's kind of this behind the scenes tool, and so I imagine many people have no idea they're using Shopify a lot of time when they're buying stuff online, and I think some of these numbers kind of creep up on people with just how large a company like Shopify has gotten.

Archie Abrams (00:03:53):
100%.

Lenny Rachitsky (00:03:56):
This episode is brought to you by Explo, a game changer for customer facing analytics and data reporting. Are your users craving more dashboards, reports, and analytics within your product? Are you tired of trying to build it yourself? As a product leader, you probably have these requests on your roadmap, but the struggle to prioritize them is real. Building analytics from scratch can be time-consuming, expensive, and a really challenging process. Enter Explo. Explo is a fully white labeled embedded analytics solution designed entirely with your user in mind.

(00:04:29):
Getting started is easy. Explo connects to any relational database or warehouse. And with its low-code functionality, you can build and style dashboards in minutes. Once you're ready, simply embed the dashboard or report into your application with a tiny code snippet. The best part, your end users can use Explo's AI features for their own report and dashboard generation, eliminating customer data requests for your support team. Build and embed a fully white labeled analytics experience in days. Try for free at explo.co/lenny. That's E-X-P-L-O dot C-O slash Lenny. 

(00:05:08):
This episode is brought to you by Dovetail, the AI first customer insights hub for all teams. Dovetail has always been the go-to tool for teams who want to find insights in customer calls, user interviews, or documents. Now they've stepped it up with the release of Dovetail 3.0. that's three new products and a ton of AI features that make it faster and easier than ever before to truly get at the heart of what your customers want. You can get a real-time pulse on what your customers are thinking with Dovetail's, automated feedback analysis platform, channels, or pull summaries and insights from every customer interaction your team has ever had with their AI chatbot Ask Dovetail. You can even recruit from over 3 million participants directly in Dovetail. All this is just the tip of the Iceberg. Dovetail wants to give everyone in their organization instant access to their customers at any time. From roadmaps, discovery, to strategy sessions and more, it's never been easier to make customer-centric decisions. The good news is Lenny's listeners can try Dovetail's Pro plan along with their newest products and features free for 30 days. Just go to dovetail.com/lenny. 

(00:06:18):
I want to start with something that I think is most unique from what I've heard, and I think there's going to be a lot of really unique approaches to how you all think about growth. One of the most interesting things I've heard is that how you think about churn and retention. To most companies, the most important thing is to increase retention, reduce churn. My sense or my understanding is you guys are kind of the opposite. You one, don't think tons about churn, you almost optimize for churn. Talk about that. How does that work?

Archie Abrams (00:06:48):
The way we think about churn is really going back to Shopify as a kind of our mission and what we want to do, which is to increase the amount of entrepreneurship on the internet. And so as a business, we want to make it as easy as possible to get started with your online store, with your business.

(00:07:06):
But most businesses do ultimately fail. And so the way we look at it is can we lower the barriers to getting started and get as many people in the door trying their hand at entrepreneurship? If we do that, again, many of those businesses, many of those folks will maybe on their first attempt not be as successful, but we're going to have a set of merchants who go on to become extremely big businesses, the Allbirds of the world, FIGS, etc.

(00:07:36):
And the way the Shopify business model works is we do charge a subscription, but most of our revenue comes from payments, which is tied to directly to a merchant's success. So in a given cohort of merchants, a lot of people will start. Some of those people on their first attempt that's entrepreneurship might not succeed, but the folks who do go on to be successful will make that entire cohort of merchants who started something that makes Shopify as a business extremely successful. And that's why we lower the barriers to get started and help folks grow, and those winners make the whole thing work.

Lenny Rachitsky (00:08:12):
I love that. So what I'm hearing is it's not that you don't want people to stick around, it's not that you don't want people to succeed. It's that you're not optimizing every new shop for sticking around long-term. It's basically make it as easy as possible for people to try it. And all you need is a few big wins for it to all work out.

Archie Abrams (00:08:33):
Correct. And that's really a different insight than most SaaS companies that they get a customer, they really never want that person to leave. And we want to lower that barriers to get started and be successful.

Lenny Rachitsky (00:08:44):
One of the main reasons companies focus so much on churn and retention is because it costs them a lot of money to drive new customers and users. I imagine there's almost an implied it's really cheap for you all to find new customers because of maybe the brand and word of mouth. Is that true?

Archie Abrams (00:08:59):
I think that definitely has some dynamics. I think the bigger factor is the monetization model. For most SaaS companies, they're making from a subscription, right? 29 bucks a month is the only way that they're going to really monetize. Whereas our business works, you have folks who are paying a subscription. But as folks get bigger, because we're monetizing on that GMV that that merchant is producing or the revenue the merchant is producing in the form of payments and other services, it allows us to grow with the merchant in those really successful merchants, make the whole system work well.

Lenny Rachitsky (00:09:34):
Got it. So basically, your net dollar retention or network revenue retention is just absurd for the winners and it makes up for all the losers slash not losers, people that have tried to build an online-

Archie Abrams (00:09:44):
Yes, tried and haven't been very successful. When you can think of the other parallel is in angel investing, right? Most of angel investments are not going to work out, but the couple that do make that entire investment portfolio successful.

Lenny Rachitsky (00:10:00):
With retention not being the primary goal and the metric you guys focus on optimizing, how do you know if you're doing well? Is it some number of these winners have to come out every quarter, every year? How do you think about progress and achieving, and success basically for growth?

Archie Abrams (00:10:18):
This way is thinking about a cohort of users we acquire in a given time period, say a quarter. And then over the next year, two years, three years, four years, five years, how much GMV have those merchants produced in total? Not about per merchant basis, but in total, did that cohort generate GMV? And if they generate GMV, that will translate into revenue and gross profit and all of those things that we can then use to reinvest in growing the business. So it's really looking at the total value, but on that GMV basis. And GMV is a power law based metric. And so it's really that power law that drives the success of each cohort.

(00:10:56):
Again, going back to investing, same thing there. Each vintage from a fund, how much did that return as a fund? And it's really driven by the few really successful outliers.

Lenny Rachitsky (00:11:09):
So this begs the question, that sounds like a very long feedback loop. And I don't know what I do with that information if five years from now, "Oh okay, that was a really good idea we did five years ago."

Archie Abrams (00:11:18):
Correct.

Lenny Rachitsky (00:11:19):
Comment on that. It touches on something you said about how metrics aren't actually a driver of how you all think at Shopify, so take that wherever you want to go.

Archie Abrams (00:11:26):
Yeah. So it's interesting. I think with Shopify, we very purposely set up different parts of the org to think on very different time horizons and with very different ways of thinking about how to build product and the like. Very different than a lot of companies that typically, have maybe one kind of unified, there's one north star that the entire company is rallying around. 

(00:11:49):
And so there's three major product groups at Shopify. There's core product which is basically building the 100 year, the right things for commerce 100 years from now. There's merchant services which is building things like payments, shipping, the tools that entrepreneurs need to be successful with a more shorter or medium term horizon. And then growth is really thinking about that end-to-end customer journey. How can we bring folks on and make sure they're successful?

(00:12:19):
And then from a metrics standpoint, we do have obviously some leading indicators in growth that we're looking at on a given experiment or what have you. But the key in what we try to instrument in our experimentation is the ability to really look at longterm effects of experiments.

(00:12:37):
So we constantly will relook at an experiment a year later, see that the way the GMV curve for the distribution was different than we might've originally thought. And that'll actually change what we do from that previous experiment. And so there's a lot of longterm monitoring of experiments over these very long time horizons to both inform what those input metrics are and more importantly hold ourselves accountable to, did we actually move what we cared about, which is that longterm GMV, in the right way?

Lenny Rachitsky (00:13:12):
Wow. Okay. I want to spend more time here. So the way you're describing it is the way the business operates is you think, what is our 100-year plan? How do we think, where does this need to be in 100 years? And with that, it allows you to run these long holdout experiments to see, is something we're doing impacting the business broadly? And because you think so longterm, you can take a year, or two, or three to see if there's an impact and then make adjustments versus I'm having to drive a certain metric every quarter, every year.

Archie Abrams (00:13:47):
Correct. And I mean on growth, we're definitely in the... We want to drive metrics on a short-term basis and we can do that obviously, but we have the luxury, and the way Tobi thinks about the world and the way we operate, to really think about these longterm effects and make sure that we're holding ourselves accountable with these longterm holdouts, and then constantly refining the input metrics that we're using and getting a lot smarter about that. But because we take that long horizon, it allows us to be better in the short term and just get a lot smarter.

(00:14:17):
And a lot of counterintuitive things. And I would encourage everyone, if you can, look at some of the experiments that you thought were your biggest winners. Look at the downstream metrics for a year, two years on that experiment. And I'll bet you'd be surprised how many times the metric is different than what you thought it would be after a year.

Lenny Rachitsky (00:14:36):
Because where people just make a call at a certain point in time, here's the list in it, here's the list experience. I love this, because very few people have experiences running a longterm experiment, and so this is a really interesting insight that you're sharing that, I guess how often do you find this to be true in your long-term holdouts, where things end up being very different downstream?

Archie Abrams (00:14:59):
I think there's probably two things that have been very common. And I would say in quite a few cases, you get a lift on a metric up front, a more short-term metric. Number of people who become a paying shopper, number of people who make their first sale in Shopify. And then you look a year later, and there's actually no incremental lift on GMV from that cohort.

(00:15:21):
And so I think it actually trains, a lot of us in growth are looking at these short-term metrics. A lot of the time it's actually more pull-forward effect, than you fully realize or an incremental user that's just really not worth that much. So that's one.

(00:15:35):
And then two, so this effect size goes away. There are cases where the experiment has flipped the other way. And then there are cases, and these are the most interesting ones, where you realize that you uncovered a pocket of merchants that are actually extremely valuable entrepreneurs who go on to be successful, that you missed in your normal short-term measurement techniques. And so all across the board we see that. But actually the most common is it actually isn't a long-term lift from a lot of things that you might think of the short-term are.

Lenny Rachitsky (00:16:16):
Is there an example in that second bucket of what you mean when you say there's a pocket of valuable merchants?

Archie Abrams (00:16:22):
Yeah, I think a lot of this has to do with, we call it monetary friction. So one of the hardest things to do with a business is when you're getting started, is you might not have any revenue coming in, and you are kind of bootstrapping, which in Shopify's case might be 39 bucks a month. But still, it's a real expense. 

(00:16:43):
And so typically when you can lower the barriers to monetary friction in some form, that could be all sorts of monetary friction early. The common belief is that we'll usually get lower quality folks coming in the door, because usually discounts are associated with lower quality. 

(00:17:03):
If you think about in a business case, if I give you a little monetary boost and reduce that monetary friction, I can actually causally change your ability to become successful, because I've given you a little bit more time to try that idea a little bit longer. I've given you that opportunity to move your business over to Shopify. And so often in those types of experiments you see that you've basically unlocked a class of people who might've given up without reducing that monetary friction

Lenny Rachitsky (00:17:35):
Interesting. And giving them time to actually make it work.

Archie Abrams (00:17:39):
To make it work.

Lenny Rachitsky (00:17:40):
Okay. So just roughly, do you have a sense of how often you find no effect after a year that you saw early impact? Just to ballpark that.

Archie Abrams (00:17:50):
Yeah, it's in the 30 to 40% range.

Lenny Rachitsky (00:17:51):
Okay. I think you're tearing the heart out of so many growth people right now, and nobody wants to hear this that works on growth where you're saying potentially a third of the experiments they're running today that are showing lift probably don't have that same... Don't have any impact down the road.

Archie Abrams (00:18:09):
Yes. Unfortunately, I think that's brutal. Probably more common than we like to believe.

Lenny Rachitsky (00:18:15):
Yes, and nobody wants to hear this, except people that you should want to hear this because if you want to build a business that grows and need to grow, it's better to know to learn that now. 

Archie Abrams (00:18:28):
Yeah.

Lenny Rachitsky (00:18:29):
Okay. So for people that can't run whole long hold that experiments, I guess is there anything that you find is a good early indicator that might be the case? Most people don't have time to sit around and wait a year or two or three. They're not thinking 100 years.

Archie Abrams (00:18:43):
I mean I think end of the day that is going to be the most effective and you actually learn the most. I think it is, though even in shorter term horizons, really being as specific as you can be about what are the early signs of success in your product, and making sure you instrument those. And then making sure, particularly up funnel experiments, you are actually looking at the further downstream metrics to make sure you have some understanding of what's moving down. 

(00:19:17):
So as deep as you can go in the funnel for as long as you can wait. Do that. And if you can't, you know what I would say? Still you should just bet on, if something is showing lift up funnel, still ship it and it's probably not going to hurt you, but don't overestimate the amount of impact that this is having.

(00:19:34):
So it's funny, two things here is, my recommendation to folks is don't think, "Oh my goodness, I have to wait all this time." Because if you didn't move the short-term impact, you're not going to have the long-term lift. So still ship if it's short-term lift. Just be reasonable that if you can measure it longer term, you'll get better about identifying what things are that are really impactful.

Lenny Rachitsky (00:19:57):
Got it. And so it may be positive initially, but often neutral. Rarely is it neutral initially and then positive down the road?

Archie Abrams (00:20:09):
There are some cases of that, but it's rarely... I've seen neutral be positive, but I haven't seen negative.

Lenny Rachitsky (00:20:15):
Got it. Okay-

Archie Abrams (00:20:16):
That resulted positive. 

Lenny Rachitsky (00:20:17):
Got it. Okay. So that's reassuring. You're not harming the business, but you're probably getting a lot more credit than you deserve as a growth team shipping things that are-

Archie Abrams (00:20:27):
Likely.

Lenny Rachitsky (00:20:28):
Likely, right?

Archie Abrams (00:20:29):
Likely.

Lenny Rachitsky (00:20:29):
And there's also just trade-offs to moving on and on balance, you're probably doing good things if you continue to ship things that are showing positive. Right?

Archie Abrams (00:20:39):
100%.

Lenny Rachitsky (00:20:40):
Okay. This is awesome. For people that want to run long-term holdout experiments, I imagine you've built your own experimentation system internally? Yeah, we have.

Archie Abrams (00:20:50):
Yeah.

Lenny Rachitsky (00:20:51):
And is it basically you hold out 10%, say it was some percentage of users from seeing the new change? Is that how you approach it or is there a different way of approach?

Archie Abrams (00:20:59):
Two things. We have two layers of holdouts. So one is more the holdouts of every change in a quarter, holdout 5% across the board. Second is for changes that only affect new merchants, what we'll do is we'll take that group of folks, let's call it 50/50 split, and then run that for a few weeks. And then what we're doing, we look at the long-term effects is actually ship the winner to 100%, but we're looking at the cohort of folks who was assigned to the experiment. We're going back and looking at those people who were assigned a year later.

(00:21:36):
So it allows us to still ship, get stuff out, but we've kind of held the experiment in a way that allows us to see those long-term effects just for the cohort that was exposed. That only works if you're doing it on new users. For existing, it's a little more complicated. That's okay. And then in our experimentation tools, all experimenters are paying that three months, six months, nine months, 12 months with here are the updated results. So you can't really get hide from, what did this really result in over a longer term horizon?

Lenny Rachitsky (00:22:10):
So your tool is email everyone that's involved with the experiment of here's what this cohort is doing now.

Archie Abrams (00:22:16):
Correct.

Lenny Rachitsky (00:22:16):
I love that. Okay, that's awesome. It's interesting that you use kind of these cohort curves for GMV, and is that the core metric you look at to see?

Archie Abrams (00:22:25):
There's a few GMV, obviously gross profit. But GMV is kind of like a key determinant of long-term success.

Lenny Rachitsky (00:22:35):
So it's interesting. Most people use cohort retention curves. You're using cohort because you don't look at retention. You're looking at for GMV over time. So that's really interesting. 

Archie Abrams (00:22:45):
GMV over time, which correlates better. And there's a retention in profit. And then really the absolute number of merchants who are on the platform and then reaching certain GMV.

Lenny Rachitsky (00:22:56):
Okay, I'm going to not keep falling this path. We can go on and on. While we're in the topic of experiments and what you've done, I'm curious if there's any examples of big wins that your team has shipped that might inspire people as they're thinking about launching experiments. I know there's probably some trade secret stuff you don't want competitors to know, and I know this is particular to Shopify and a platform in eCommerce. But I guess is there anything that would be worth sharing of like, "Here's a huge win that maybe we didn't expect."

Archie Abrams (00:23:25):
Going back, there's always a lot of value in thinking through monetary friction as I mentioned. That's always going to be something to export. Trial dynamics, different types of incentives, all of those things are very impactful.

(00:23:39):
I would say on things that are maybe more practical and for everyone, there's an enormous amount, and we do see these with long-term effects. But just the nuts and bolts of sign up, collecting the right information. And you usually want to collect more information than most people think you do in your sign up flow. If you can then leverage that to personalize the guidance. And this is for SaaS product, the guidance that someone can get when they onboard into Shopify. 

(00:24:09):
So whether you're coming on, Shopify is a very diverse product, in-person selling, online selling different channels. There's the nuts and bolts of get more information from folks, build trust in there, give them right amount of guidance when they come on in a personalized way.

(00:24:25):
And that may sound like, okay, that's kind of obvious. But the amount of impact by just nailing those flows has never ceased to amaze me and setting up that person for long-term success. So monetary friction. Then just really good onboarding, personalization, a well of opportunities there.

Lenny Rachitsky (00:24:49):
I love that onboarding comes up every time I ask anyone where they've seen ongoing success and opportunities, particularly in actually surprisingly driving retention. It's interesting that that's not what you look at, but it turns out that's one of the biggest levers for increasing retention. Interesting that even for a company that doesn't look at retention, that's a big opportunity.

Archie Abrams (00:25:07):
Yes. Yeah, it's really because it's setting people up, for Shopify's case, I think the big thing about all of our metrics is... What we get very nervous about is the easiest way to increase retention is always to constrict the funnel stage one above the retention metric you're trying to optimize for. 

(00:25:27):
The simplest way to increase my signup to activated thing is just make it harder to sign up. Nuts and bolts, that will always happen is when you have teams on that local conversion rates, you get all these weird team incentives, because they're optimizing to basically implicitly make it harder to do the step before them.

(00:25:49):
And because we focus on that long-term GMV, number of merchants who are successful, orienting every team to think about the total number of people, not the rate, but the total number of people who got to the end of their part of the journey is a very powerful way to incentivize people to do the right thing in terms of getting people set up versus do the, "I'm going to constrict the funnel step right before me to make my local conversion rate look better," which is the bane of my existence but something I see a lot of teams, implicitly or explicitly do when they get too focused on rates as a way to think about the world.

Lenny Rachitsky (00:26:32):
Incentives. What a power.

Archie Abrams (00:26:34):
Incentives, what a power, what a lever.

Lenny Rachitsky (00:26:36):
I definitely want to chat a little bit more about metrics. I know you have a really interesting take that's kind of built on what you're just talking about. But first of all, you mentioned this term monetary friction as one of the levers that you've seen success with. Can you just describe what that actually means?

Archie Abrams (00:26:48):
Totally. So things like trial, trial dynamics, trial length, trial amount. It means incentives. So what is in your product? What do people value and need in order to be successful? So in Shopify's case, that might be app score credits or things like that, but those are the two forms of monetary friction we talk about and then of course actual price point. But that's what the larger bucket of monetary friction is.

Lenny Rachitsky (00:27:16):
So let's follow this thread of metrics. You're big on absolute numbers and you've been talking about this already, versus percentages and ratios. Talk about that and how you encourage your teams to think about metrics.

Archie Abrams (00:27:29):
Yeah, I think one of the things that I think happens particularly in large, in Shopify's growth order, it's about 600 folks. When you have teams naturally break up the world into different funnel stages or different points in the journey, it gets very seductive to look at my part of the funnel, and what's my conversion rate through that part of the funnel? And then the team starts to optimize for that conversion rate as their north star over a longer time period. I'm going to try to move my conversion rate from 10 to 12% or what have you.

(00:28:04):
But in practice, I talked about it's actually almost always easier to just make it harder to do the thing right before your step in the funnel to increase your conversion rate. If I make it harder to sign up, it's going to be very easy to increase sign up to activated rate, because I just have fewer people and the people who made it through our higher intent.

(00:28:23):
And so I see teams get really stuck when they are trying to optimize conversion rate, but they just make it harder to do the previous thing. Versus everyone is thinking about absolute number of people who made it through their "stage" of the funnel. So instead of I'm trying to convert a bunch of people, a conversion rate, I just want more people to get activated.

(00:28:48):
And then once you start thinking that way, you realize actually the best way to get more people to get to a step sometimes, and often they just get more people in the door in the first place. So make it easier to sign up or reduce friction. It's the opposite. 

(00:29:05):
Because that will always hurt your conversion rate, but it may actually give you more people on the outside. And a lot of teams get very nervous, their retention rate went down, their LTV went down. Oh my goodness, is this this going to affect our ability to pay? No, your CAC also went down by probably more. And so now you have the ability to likely spend more and you have more people through the door, getting to each point in the activation or the immersion journeys.

Lenny Rachitsky (00:29:33):
What I'm hearing is essentially teams are gold not on increase, lift this conversion step by some percentage. It's drive some absolute number of new merchants, potentially.

_[498 additional lines trimmed for context budget]_

---

### The ultimate guide to Martech | Austin Hay (Reforge, Ramp, Runway)
**Guest:** Austin Hay | **Date:** 2023-08-13 | [YouTube](https://www.youtube.com/watch?v=B79p85DHLkU)  

# The ultimate guide to Martech | Austin Hay (Reforge, Ramp, Runway)

## Transcript

Austin Hay (00:00:00):
From 2010 to 2020, we had the golden years of deterministic matching where it was very easy to run an ad and understand with precision who installed the app. Maybe you didn't know their name, but you actually would know their IDFA and you could tie that to their PII. You can't do that anymore. So, what that means is these ad networks are becoming more complex, sophisticated, and interesting, right at the same time that it's harder for marketers to really understand how they're spending money. And so I am paying a lot of attention to how marketers make decisions with probabilistic data because most of the work that I'm doing now is actually saying, well, given that we don't have determinist data about a per certain audience or where somebody came from, how can I find other information that will create a model for 30% of the population and we can use that to extrapolate to a hundred.

Lenny (00:00:52):
Welcome to Lenny's Podcast, where I interview you world-class product leaders and growth experts to learn from their hardwood experiences building and growing today's most successful products. Today my guest is Austin Hay. Austin is one of the smartest people in the world on the field of MarTech, aka Marketing Technology. He's advised companies like Notion, Airbnb, Walmart, Postmates, Robinhood, even Pete's Coffee and Mars on their MarTech strategy and tactics. He's currently head of marketing technology at Ramp. Before that, he was VP of business operations at Runway. Before that, he was VP of growth at mParticle and the fourth employee at the Unicorn Branch Metrics. He's also a teacher at Reforge on this very topic of MarTech. In our conversation, Austin explains what exactly is MarTech, how it fits into your growth organization when you need to hire a MarTech person and what to look for plus his favorite interview questions.

(00:01:43):
Also, his favorite tools, frameworks, team structures, and emerging platforms that he's most excited about. This episode is for anyone who's responsible for growth and is curious about ways to optimize your approach and how marketing technology fits into that. Enjoy this episode with Austin Hay after a short word from our sponsors. Today's episode is brought to you by OneSchema, the embeddable CSV importer for SaaS. Customers always seem to want to give you their data in the messiest possible CSV file. And building a spreadsheet importer becomes a never ending sync for your engineering and support resources. You keep adding features to your spreadsheet importer, but customers keep running into issues. Six months later, you're fixing yet another date conversion edge case bug. Most tools aren't built for handling messy data, but OneSchema is.

(00:02:28):
Companies like Scale AI and PAVE are using OneSchema to make it fast and easy to launch delightful spreadsheet import experiences from embeddable CSV import to importing CSVs from an SFTP folder on a recurring basis. Spreadsheet import is such an awful experience in so many products. Customers get frustrated by useless messages like error on line 53 and never end up getting started with your product. OneSchema intelligently corrects messy data so that your customers don't have to spend hours in Excel just to get started with your product.

(00:02:59):
For listeners of this podcast, OneSchema is offering a $1,000 discount. Learn more at oneschema.co/lenny. This episode is brought to you by Mixpanel. Get deep insights into what your users are doing at every stage of the funnel at a fair price that scales as you grow. Mixpanel gives you quick answers about your users from awareness to acquisition through retention, and by capturing website activity, ad data, and multi-touch attribution, right in Mixpanel, you can improve every aspect of the full user funnel. Powered by first party behavioral data instead of third party cookies. Mixpanel is built to be more powerful and easier to use than Google Analytics. Explore plans for teams of every size and see what Mixpanel can do for you at mixpanel.com/friends/lenny. And while you're at it, they're also hiring. So, check it out at mixpanel.com/friends/lenny. Austin, thank you so much for being here. Welcome to the podcast.

Austin Hay (00:04:03):
Lenny. Thank you so much for having me.

Lenny (00:04:04):
We are going to get super nerdy today and we're going to dive deep into the very cool field of MarTech. How excited are you about us chatting about MarTech?

Austin Hay (00:04:15):
I'm so excited. Because it seems like you might be one of the first people in product and growth to talk about MarTech.

Lenny (00:04:21):
Wow, okay. That makes me even more excited. Yeah, it's something that I haven't fully understood and so I'm excited to dig real deep. So, let's start with just the basics. What exactly is MarTech and then what does someone who is in MarTech do?

Austin Hay (00:04:35):
Such a good question. Because marketing technology is like this very amorphous, cross-functional discipline that lives at the crossroads of product and growth and engineering and marketing. It brings together processes and systems from a wide range of disciplines. And I think really the way to think about marketing technology is it's a product manager whose specific role and focus is the system or the third party or first party platform because marketing technology can mean a collection of third party tools, which is a lot of people think, but as a company scales and grows actually it could include a collection of first party homegrown solutions that you build yourself with or in addition to third party. So, I like to think about marketing technology more as one piece is people and process and the other is the system and the platform. And that probably sounds pretty familiar to what a lot of product people think about their world as, and that's how I define MarTech.

(00:05:31):
And then you asked this other question around what exactly the role of somebody in MarTech, and maybe we'll talk about this a little later, but it's such a function of the size and the stage of the company that you're at. At Airbnb, I would say Dmitri who you might've worked with was the MarTech guide. He managed a lot of our Airbnb's, the first and third party tools. Airbnb at that size was, I don't know, maybe 800 people or so. And so it makes sense to have a function with product and engineering resources. A small startup for example, when I was working with Siqi, we were just talking about this at Runway, there was no such thing as MarTech. There was me and Tanner and Siqi standing up tools and using them because you just have to use the tools to get the job done. And so I would say on the spectrum of what is MarTech, you really have to look at the size and the stages of the company and as you grow you start to see it become more refined or pronounced.

Lenny (00:06:17):
So, if someone listening to this that has done growth or has a growth PM may be like, oh, but this is sort of what I do. What is the difference between someone that just runs growth or has a growth team versus someone that's specifically a MarTech person?

Austin Hay (00:06:30):
At some levels there's maybe no difference. There's a lot of startups I would say are 30 people or less where you have a growth team and your growth acquisition person is using a CDP to send data to their ad network to run their ads because that's part of their job and maybe they are the MarTech person. And actually you find a lot of people who consider themselves MarTech professionals now having started in growth or user acquisition roles because they had to just use tools in order to get their jobs done. But what I would say is as a company grows and scales, it moves from being a community or village driven aspect of your products to being something that's centrally owned. If you're a startup, again, like 30 to 40 people, everybody might chip in to manage your CDP or use Amplitude or build a first party solution on top of those.

(00:07:16):
It's a mixture of first and third party tools and engineering and product and marketing all work together on it. That doesn't scale though. As you cross a hundred to 200 people, somebody has to be responsible for knowing how data flows through tools, how it's worked, what's the schema. And that's not even considering procurement and legal stuff. You have infinite liability if you don't manage your contracts well. And so usually around I would call it a hundred to 150 people is the critical mass where you can't just have a village approach to systems and tools much like in the IT org, if it was a village approach to SSO businesses would be in a lot of danger. That's where you typically start to see the question of, all right, we need a systems and tools person. We need somebody to manage these systems and manage that platform.

(00:08:01):
And there's a variety of ways it can go. I've seen it go just into pure product that's with a product operations org and a product ops person actually will manage a lot of third and first party tools. I've seen it go into the IT org, Walmart for example, at a really big scale. They had a MarProd function which was marketing products. It was product within the marketing function or product that was designed to serve marketing. And then of course you can have more traditional routes like you can have marketing technology as a single standalone unit or business technology as a standalone unit. Some of this depends too on whether the business is B2C versus B2B. Classically in a B2B business you see it in rev ops or some types of systems role because you have to serve not only users coming into your funnel, but then the businesses that you're serving afterwards.

(00:08:46):
That's also where you typically see tools like Salesforce coming into play and more advanced CRMs. In a B2C business, your user funnel is actually really simple acquiring users and you're getting them into your product and then product is taking them over. There's no additional CRM, so usually your CDP is the source of truth and that's where you might actually see marketing technology fit in with growth a lot more. Just some examples like at Postmates, I worked for them for a long time as a consultant. Marketing technology was just part of growth. We had a director of growth even before that, Siqi Chen who's the CEO of runway, and I guess you were his first manager as I just learned, he was the first VP of growth and marketing technology was just part of growth and product owned that as a system.

(00:09:30):
As a different example though, at Ramp we're big enough and we're a B2B company, but we have a B2C top of funnel where we try to acquire users and get them to fill out our application to get a credit card. We have a distinct revenue operations team that's broken into business technology and marketing technology. So, there's lots of flavors of how it can exist. I think that's kind of the interesting and fun part of Marketing Tech is that it's not just one single version of the world that you apply to many companies, there's like a million variations that I've seen and they all kind of look to solve the same problem.

Lenny (00:10:00):
So, to make it even more specific and really simple for people to think about what someone in MarTech does, essentially it's using technology and tools to drive growth. Is that a simple way of thinking about this one specific roles?

Austin Hay (00:10:11):
Totally. That's exactly right. And I have this adage I always say, which is tools are just meant to solve problems. And the problem set for marketing technologists and business technologists is you focus on the tools.

Lenny (00:10:24):
And so when someone currently say listening doesn't have a MarTech person and they're thinking about, hey, is this a gap we have? What is that slice of work that a MarTech person would take if they currently have say a growth team or a growth PM that's leading growth and a growth team around them?

Austin Hay (00:10:40):
This comes up all the time, by the way, I talk to businesses every year that have this problem of we have a growth team, we're growing pretty fast. We have a guy that we hired, usually an engineer who stood up all these tools for us. Or it could be gal too just to be clear, but this person has been here for two years and knows all of our systems really well, but now they're becoming overwhelmed. They don't have enough time. The systems are too complex. This is the flavor of story that I hear so often around startups who have hired a great growth person and managed tools and systems, but at some point they reach that point in time where it's no longer manageable by one person or even a set of people. And that slice of works looks like setting up new tools, building new tools on top of them because a lot of times you'll take a third party tool, call it like a segment or an amplitude, and you'll build tooling in your own stack behind it to power something much more advanced.

(00:11:35):
And everybody thinks that marketing technology is just the third party tools, but actually it's designing, architecting and building that stuff on top of your third party tools. That's how you actually have a lot of velocity is thinking about not just build versus buy. It's build and buy now. So, you buy the tool to get 90% of the way there and then you build the cool thing on top with the other 10%. And so that architecting decision usually falls on this person. The one really unsexy part of it, which I tend to love because it's really high leverage is the contract part. When you start out as a business, you sign any contract you want with a third party because you're just trying to get going. You have much bigger problems, product market fit, staying alive, runway. But at some point as you scale and you're starting to make money, now you start to care more about not just how much money you're making but how much money you're losing usually from contrasting SaaS tools.

(00:12:24):
And so that's where you start to have more scrutiny around what types of deals are we signing, what are the terms? Do we have liability exposure? What's it going to cost us if we actually scale? And it's great that we have this cool rate at 500 MTUs, what happens when we have a million MPUs? So, I worked at mParticle, which was a CDP provider for a long time and I was their VP of growth and part of their SaaS vendor strategy is like, how can we design these cost structures in a way so that at the company scales we make more money? That's just part of the business. And so if you have that mindset of, well, I'm looking out for the business not just now, but two 30 years in the future, that's where you can also have a lot of value from a systems or marketing technologist.

Lenny (00:13:05):
Maybe a sign that you should start thinking about a MarTech person on a growth team is what I'm hearing is you're starting to accumulate all these different tools and maybe there's a sense that you could be a lot more efficient in connecting data and the backend infrastructure for how you think about growth and how you drive growth and measure growth.

Austin Hay (00:13:24):
Yeah, efficiency and pain. I would say pain drives people more. It's like, hey, we can't do something because nobody knows this thing. We can't do something because we don't know the best way to set up these tools or to change these tools or we can't even move forward where a business plan because we're worried that changing our tools might have an impact. And usually this is related to email marketing tools and data tools, so like CDPs and folks like Braze interval and just because a lot of times your email is the thing driving recurring customers to come back to your product and use it. So, you can't actually sometimes make the changes you want without understanding how something was set up in the first place.

Lenny (00:14:03):
You talked about where this person would live in the organization. There's all these different places. I talked about revenue team, maybe the ops team, maybe growth team, marketing team. What's your general advice for who should lead the hiring of this role and also just roughly who should they report to?

Austin Hay (00:14:21):
So, I have not to shamelessly plug my Reforge course in the fall, but I'm going to be shamelessly plug my Reforge course in the fall. We have this awesome matrix that we built that shows where this person should live, what they do, who they should report into, and it's all part of the fall course if you want like the deep dive into it. There's going to be a section on it, but just the gist of it is I first like to break it down into two dimensions. First is a B2C company or B2B company. And then the second dimension is how important is it to you that this person report into a specific function or not? So, first with B2C and really maybe a simpler version of that is centralized versus decentralized. So, we have B2C, B2B, centralized, decentralized. In a B2C organization I think actually thinks it's quite simple.

(00:15:08):
Most of the time your tools, your marketing tools are intended to help the growth team. The growth team has a job to be done, which is to spur user growth and tools are just meant to solve the problem. So, marketing technology's job is to serve the growth team. Now it obviously serves product and analytics and data, but its key stakeholder and customer is the marketing or growth function. And so I think it makes a lot of sense that if you're designing an org under a CMO or a marketing person, you put marketing technology alongside your head of growth or maybe reporting into your head of growth depending on the seniority of the person. And that works quite well. The key thing there is you just want to make sure that this marketing technology person is a really strong technical architect or some type of technical operator because they're going to be your representation to the product in engineering orgs.

(00:15:53):
Now, some people take a little bit of a slight twist on that. They say, hey, I have a product manager who manages growth that comes from the PM side. You could have a platform PM that serves the same thing in MarTech and they're responsible for all internal platform systems. And then you get into questions of does that belong in product ops or not? And I'm not going to go there. But for B2C, that's the centralized function. For B2C decentralized, what you do instead is you just say like, hey, we're going to have one of these systems, people in every org. Product is going to have a product ops person and growth is going to have a growth ops person, engineering will have engineering ops, and then we kind of divide the lines based on what tools they're managing. I generally don't see that working very well just because as you add more operational people, it just creates more systems.

(00:16:39):
And so unless you're a massive company where you need that type of scale, I think most startups should avoid that decentralized model. And then for B2B, I think B2B is really messy because not only do you have pure B2B where you're only selling to enterprises, but you have this concept of B2B2C, which is where you're actually selling to users and to businesses sometimes at the top of the funnel and the bottom, but also sometimes at the same time like notion. Notion sells to users so, they have a little growth acquisition funnel at the top, but then they also sell to businesses. And I find there's really, again, there's two ways decentralized or centralized actually at Ramp we've gone back and forth between the two models. We started centralized with the Rev ops group, we decentralized it and put marketing technology into the CMO org and now we're rolling it back into the revenue operations org Largely has to do with who is our customer?

(00:17:28):
Whose problems are we solving and where are resources allocated? Because if you have a decentralized model, then you run the risk of having to have lots of resources decentralized across the team. And the question is, can that function actually get work done or resources spread too thin and the priorities on align that it makes it challenging to get work done. And yeah, I would just say especially on B2B, for people out there listening, there is no right answer. And I even think that marketing technology could live in product, it could also live in engineering. Some of this has to do with who is the leader of this function. If it blends more towards ops, meaning managing processes and systems, then yeah, maybe you want to decentralize it and keep it in its representative function. If you have a really technical leader who was an architect or a PM that might indicate where that person should actually be leading their team. So, it's very case specific, which I know is a terrible answer, but it's the way it is.

Lenny (00:18:25):
Makes total sense. If someone were to hire someone like in Austin, are you doing the work yourself? Are you an IC for quite a while or do you end up building a team, say engineers that are building some of this infrastructure, how does that usually play out?

Austin Hay (00:18:38):
I think all marketing technologists at some level are ICs. I think it's a great job personally, because I get to be an IC and a manager. You have to be an IC in that, you are the most senior technical expert on all first party and third party systems. So, you have to know really well how third party tools work and you don't know that without doing the work yourself. So, I do find that some of the best marketing technologists have at least at some point in the last five years, been an operator and expert managing tools and systems. And then usually the teams are small and super cross-functional.

(00:19:10):
So, what I would say is more important to look for than how many people has this person managed is how well can they manage upward, laterally and downward because they're going to have to go talk to the head of rev ops if they want to change something in Salesforce, they're going to have to talk to the VP of product if they want to make a big platform change that touches something else. They're going to be relying constantly on data resources from their head of data. So, I think that this person, the secret sauce is more of how good of a cross-functional team player are they. I almost view them like a true quarterback every [inaudible 00:19:41] says people are quarterbacks. But really marketing technology because it lives between so many departments, it plays that role of having to call plays and pull on different departments.

Lenny (00:19:50):
And because it sounds like you don't have a team to do some of these things and you need to convince people to help you out.

Austin Hay (00:19:56):
Totally. Yeah. It's a game of persuasion and salesmanship. You have to convince people why the problems are big and especially as you get bigger, a lot of the decisions or problems of marketing technology are not about rapidly making a huge transformation. It's slow transformation that can have big implications. I'll just give you one example. Like lots of big companies I talked to have two CDPs or two attribution tools and it's like there's the cost problem. How do we get rid of this secondary tool to reduce the cost? Maybe it's a million dollars, but there's also the complexity and decision-making problem. How do we make people move and work faster by not having the complexity of asking, which tool do I use in such a simple decision?

(00:20:39):
And then you get to a really big scale at Walmart where your problem isn't even. How do we consolidate the stack and make it so tools that are helpful for people, but how do we prevent from getting back to that state? How do we put safeguards in place to make sure people actually have access to the tools that they want and can solve their problems? But we're not introducing duplicative tech into our organization because a really well-known, sorry to put SaaS vendors on the spot here, but well-known SaaS vendor plays the land and expand motion. You get in small and then you grow your business. Well, that's a distinct problem for businesses that are trying to control costs and simplify the way the world works.

Lenny (00:21:15):
I want to talk about tools that you recommend and use most often, but I'm thinking maybe we start with a different question, which is around just what does your day look like as a MarTech person? What are you doing day to day and from the lens of your growth PM listening or a leader listening and what could this person do for me and how much leverage can I get if I were to find a MarTech person?

Austin Hay (00:21:37):
There's half of marketing technology, which I would call somewhat administrative and high leverage. It's managing PI requests and PI technology, managing administrative stuff like contracts and admittance to tools and permissions. This is all at a big company scale. You probably don't do this when you're a small company, but that stuff matters because give you an example, you give edit access to somebody who wants HubSpot and they send a fake email test to a million people and now you're on Twitter being embarrassed as a company. It's like-

Lenny (00:22:12):
Does that happen to you?

Austin Hay (00:22:13):
It hasn't happen to me. But I've gotten the emails from certain companies where it's like, this is a test and it came from an intern.

Lenny (00:22:20):
Yeah, same.

Austin Hay (00:22:20):
You're like, that's just permissioning gone wrong. So, I think a big part of the role is designing systems that are automated to handle that stuff because ideally you don't want to be sitting around in your computer all day clicking one conductor request to approve permissions. You should look at the role, look at the experience of tenure and department and make a decision about which accesses you get. So, automating that is a big part of my job. The manual part of my job, which I feel like is actually really fun, is again the designing systems and contracts for the future. So, it's about how do we design a system and create a vision and persuade people about what our system technology can look like over the course of one to two years, the time span that I usually look at. And then how do you change state from then to now? Some of that has to bring in financials and contracts. That's where this plays a role. What are our contract terms today? What's the price we're paying? What is our growth going to be?

(00:23:12):
Can we build a financial model to show how much it's going to cost us both in terms of operational efficiency and actual real fixed and variable costs to end up in that state? And then how do I create a graceful argument to persuade people that we should spend engineering time and resources? And usually it nets out pretty clear. It's like if it's less than a certain amount, how do you justify spending any engineering time on it? You have to wait for the problem to become big enough. But then back to your other point around how do I give growth managers out there something useful. I would say the big thing that people forget in an early stage of a company's lifetime is that the company will outlast you, hopefully. You will not be the last growth manager unless the company fails. So, I tend to take a little bit of a different approach than most, which is like I think you should always be thinking about the future.

(00:24:02):
That doesn't necessarily mean you should make design choices that over index towards the future so much that you miss product market fit or you make poor product decisions. But when you set up tools and you pick tools and you implement them, you should be thinking, what's going to happen a year from now if I don't change anything? And is this going to be a catastrophic situation or not? And then try to take actions to mitigate that risk. Some examples are like if it's $2,000 to get SSO and two days to set it up and that prevents you from having a security problem where somebody downloads all your users, it seems like a great investment.

(00:24:37):
And guess what? Over time, if you don't do that, you're going to eventually have to hire an IT person to go and set up SSF for all your tools. So, some of this is more of just being a good steward about managing first and third party tools with an eye towards the future. It's always a trade-off, right? Because the more time you spend when you're building product early in a company's lifetime, that time could be spent on other things. So, if you waste it managing third party tools or setting up correctly, then maybe you miss out on a key product feature. So, I think it is a tough balance to strike.

Lenny (00:25:06):
Coming back to the different kind of roles within the growth umbrella, if someone has someone leading paid growth let's say, and they're just like a paid growth person, do you also find a MarTech person to work alongside this person? How connected would you be to someone that's just responsible for paid growth?

Austin Hay (00:25:24):
Maybe a key differentiator too. We didn't talk about this in the beginning, but there's marketing technology and marketing operations. So, in my mind, this is just my own kind of mental framework is marketing technology has tech in it. So, it's usually an engineer or somebody with an engineering background doing that function. Marketing operations is usually not always technical. Maybe a systems analyst or business analyst could be somebody really, really smart, but they may not have an engineering background. So, I think that's a key distinction too. And you typically see that in B2B where you'll have mar ops function, which is setting up campaigns, sending email blasts, debugging, doing analytics work, SQL queries, all semi-technical work but not engineering based. So, in my mind when we talk about marketing technology, I'm really thinking it as an engineering based role and even by background, I'm not a software engineer, but I was a civil engineer and I learned how to program and I went through a bunch of coding to get there.

(00:26:21):
So, that's my way into the engineering world. And you typically find that a lot with marketing technologists in particular is they either are software engineers or they've gotten enough experience to moonlight as software engineers. And so we get to this problem set of a user acquisition person. How would they rely on a marketing technologist? Well, I think the most superhuman user acquisition people out there are engineers and they don't need a marketing technologist because they set up the tool themself. They know how the paid campaign runs and they just do it all. And you'll typically find these super humans at small startups where the engineer is just told by the co-founder, hey, go figure out how Facebook ads work. And superhuman is born. More often though that doesn't happen. Or those people once they do it once, they never want to do it again. So, you'll typically find the role split and that's the natural thing that happens.

(00:27:13):
As you scale, you divide responsibility and you'll see you'll have the person who's responsible for bidding and acquiring users and paying down those campaign costs. Then you have the person who's in charge of how does it all work? How do we get this thing to actually run? And that's very similar to what we have at Ramp. We have an amazing user acquisition team. I know Sri Batchu was on here a while back. He hired a guy named Cody Morgan at Ramp who has a user acquisition team. And the way to think of it is, my job is to help support them in running all their campaign needs and when they have a directive from the CEO that says we need to improve CAC or change any of our metrics, it's my job to partner with them to help them do that. And actually one of the coolest and most fun projects that we worked on early when I joined Ramped is we were optimizing.

(00:27:55):
We're trying to get top of funnel data all the way down to the bottom of the funnel and tie it with opportunity data so we could send that back to the ad network so that rather than optimizing your campaign off of when a user clicks a button on the website, you're actually optimizing it off of did the opportunity occur and what was the kind of ideal value for that opportunity? And you're sending that data as a synthetic event back to Facebook and all those guys. So, it can be really cool and super advanced stuff depending how deep on the funnel you get and how complex your business is.

Lenny (00:28:25):
So, you're generally not running campaigns of your own unsafe Facebook or AdWords. You're mostly as a MarTech person supporting people who are doing that.

Austin Hay (00:28:34):
Yeah.

Lenny (00:28:35):
Awesome.

Austin Hay (00:28:35):
Helping them use tools and technologies to do it.

Lenny (00:28:38):
Great. Do people give you goals? Are you responsible for growth goals of your own? And in general, are MarTech people, should they have goals and growth goals on their plate or are they just there to support people who do?

Austin Hay (00:28:52):
Oh, that's a great question and I would like, maybe this is at the end of the podcast, we ask people about this because I would love to know what is a better version of goaling? So, there's two ways that I've thought of it. One is my goals are directly tied to the people I'm serving. So, if user acquisition has, I mean we do, we have a growth goal and we have a CAC goal at Ramp. So, my goals are tied to them, so I'm going to help make sure that that is achieved, but then there's also a cost and efficiency goal that I internally think is valuable. Whether or not the business thinks it is valuable, it doesn't really matter. I come from a sales background and I like to run lean and efficient teams, and so I'm always thinking to myself, how much were the tools when I came in, how much are they now?

(00:29:34):
Have I set us up for success so that as we grow, our cost per user or cost per seat comes down and how much more efficient are we because of that? The ideal world is that you actually are growing as a business making more money, hiring more people, acquiring more users, and your total cost of tooling per person goes down. That's like the dream. And there's lots of ways you can build that financial model, but I mean that's what I think most marketing technology leaders should strive for is to make sure that they're controlling costs over time because most businesses don't. There can be some goals that are discreet in nature that are not cost-efficient, but more like net capability related. So, it's like, hey, we want to design a first party system that's world-class that achieves these three goals, right? Maybe you want to incorporate artificial intelligence into some part of our product platform and incorporate third party tools.

(00:30:25):
And those are more like discrete product goals. In the same way that a business might launch an external product goal to launch a feature, they sometimes also might have internal product goals, clean up our revenue operations systems, make our email marketing system better. In particular, email marketing is one I see come often a lot with small businesses and even medium-sized businesses where they'll have picked a tool at the start of the company's lifecycle and as the company has grown, they've outgrown that tool. They need to move to a Braze or Marketo. And so there'll be a big six-month initiative to say, we just got to switch. That's the goal. We have to safely get off this small tool to a much bigger, more complex tool that's going to cost us more. It's a lot more complex, but we need to do it without losing money. That's usually the job of a MarTech person in some type of change transformation effort.

Lenny (00:31:14):
Perfect segue to where I wanted to go, which is tooling and your recommendations and favorite tools. And so maybe we start with just what do you find as a good starting tool stack for people starting to think about MarTech and basically growth, and then what does it end up being generally?

Austin Hay (00:31:32):
In terms of stack, again, we think about B2B and B2C. B2C I would say the stack was largely solved from 2017 to 2020. We've had like a renaissance of the data architecture, so what I'm going to do is I'm dig through B2C then and now and then we can go B2B then and now.

Lenny (00:31:52):
Great.

Austin Hay (00:31:52):
Okay. So, B2C, if you back up to 2016, 2017, you have segment and the rise of the CDP. Consumer based businesses have to collect a user and tie a bunch of data to them and then track their actions to send it out to performance ad networks and email marketing tools and product analytics tools. And so you would see this very commoditized stack. It would be like CDP in the middle bunch of tools connected. The promise of the CDP was you integrate one SDK, your engineers don't hate you send all the data to the other tools you can create audiences.

(00:32:26):
Great. Lasted for a long time. The thing about it though that I think really changed around 2020 is that the cost of ownership of warehousing became much cheaper. And so 2021, you start getting to the place where it actually makes a lot of sense and is really easy to store all your data in a warehouse model all your data in the warehouse, and to do it without needing a vast data team. I would say Airbnb was probably doing all this well before anybody else was, but they had the main advantage of a lot of money and a lot of resources. So, now come 2020, it's cost-efficient to have a data team with your own warehouse and to manage data centrally in something like Snowflake. So, now this question is like, okay, well we got to get data into the warehouse, but how do we move data around is totally different.

(00:33:11):
And that's what really led to the rise of reverse ETLs. So, now you can actually build your own CDP and lots of businesses already have, I'm consulting with a well known financial trading platform a couple of months back, and they have a CDP, they have all this internal data in their warehouse, but they have not been able to activate it because it's pretty old architecture. Everything's batch based end of the day. What they need is a reverse ETL. They don't need to take that data and just get it out into the world. So, they need the reverse ETL component or the transformation component of a CDP. And so I'd say now today when we think about B2C businesses, you can either go to the traditional route, buy CDP, hook up all your tools, third party.

(00:33:52):
I think that's a great move if you do not have a lot of engineering resources because you're not spending a ton of time and energy on a warehouse and all the modeling that comes with it, you're just spending time to implement one SDK. I think if simplicity is the name of the game for your business, CDP, Centralized Stack, great move. If you are an advanced engineering culture and you are cutting edge and you're going to do a bunch of modeling in DBT and you already have Snowflake, you should move towards a model of using a reverse ETL. What it means is that there's a way to get your data into the warehouse and then how you activate it is completely independent from the CDP. And so what that means is actually you can have lots of different variations of the stack.

(00:34:31):
You could use Amplitude as your CDP, collect all your data, stream it into Snowflake. They actually now have an integration with Snowflake that lets you feed data directly out of Snowflake, and then you could use a reverse ETL to just pipe that data wherever you want. There's a really good section though, again, sorry to self aggrandize, but there's a really good section in the Reforge module this fall that talks about what happens when you have multiple ways to move data. You buy amplitude for your CDP and you're moving data to your warehouse. Amplitude is a bunch of integrations, but you also have reverse ETL and you can move data out of your warehouse.

(00:35:05):
Where do you choose? And I would say a lot of businesses get in trouble when they don't have a methodology or a system for how and when to move data from one place to the other, so they just do it haphazardly, right? And the key in systems management is you want to design a process for doing it some type of waterfall or mental model for when it makes sense to move data directly from Amplitude, which is the ingestion point of your data stream or from the warehouse where you can model it and make it better. I think the key is just having a philosophy and approach. There's not really one answer, but that's all B2C. So, B2B I would say ... Yeah, go ahead.

Lenny (00:35:40):
Before we move on to that one, you mentioned reverse ETLs. What are some examples of products that are reverse ETLs so that people can look them up?

Austin Hay (00:35:47):
Yeah, I personally think the reverse ETL is a capability. It's the ability to move data from a warehouse to a tool. So, technically speaking, you'll find reverse ETLs in CDPs and as standalone products. Segment has a reverse ETL function they just launched, and Particle has a reverse ETL function they just launched. Rudder Stack, which is a CDP has always had a reverse ETL function where you can take warehouse data and move it to different cloud infrastructure. Then there are distinct standalone products. Census, which was back Bay 16Z and Hightouch are the two standalone reverse ETLs. And like I said, I'm an investor in Hightouch, love their work, we use them at Ramp. At the end of the day, you should pick tools because they help solve problems, not because of anything else. So, we can come back to that if you want.

Lenny (00:36:32):
Wonderful. Great, great. Yeah, that was perfect. Keep going.

Austin Hay (00:36:35):
Okay. Yeah, so we talked about B2B, or sorry, B2C. B2B, I probably don't have as much history as say people who survived the dot-com crash in 2008. I started really my career in B2B in 2014, so I'll share a little bit of my experience and I'm just hopefully just saying this because listeners may chime in and be like, oh man, this guy doesn't know what the hell he's talking about, which is totally fair game. So, 2014 though, I remember working at Branch, I was working for our COO Mike Molinet, who's now at this really cool company called Thena, but at the time I was working for Mike, and as we talked about before, oftentimes growth stacks just appear because you're given a challenge. And I remember sitting in this tiny room with Mike. We were over in Palo Alto, right off the fills in Palo Alto in this tiny room.

(00:37:27):
It was boiling in the room like so hot we were sweating and we were mapping out on a whiteboard how we would design our first version of our system, like how we capture leads, how we get them into Salesforce, how we would email them with a little tool called Outreach at the time, that was still a startup. And I'll send it to you after this if you want to show them to viewers, but it's so MVP, but it still models what a lot of people have today. There's some ingestion point for your data. There's Salesforce, there's some type of outbounding tool, there's an enrichment tool, and then a lot of other Jerry rig stuff hooked up to Salesforce. And for the most part, that's how B2B still exists today as you have Salesforce and then the whole world and the universe revolves around Salesforce. You just have more advanced tools, you have Gom and stuff like that.

(00:38:12):
I think the big change though, and what is really fascinating and has been fun to watch is in the last two, three years, you now have this whole rise of B2B2C, which takes all the complexity of the top of funnel user acquisition system and stuffs it right alongside your CRM and how you build an elegant system there in that space, I think is one of the most complicated and intricate pieces of being a MarTech person today. And some of it just has to do with the data language. Like all these B2C tools were designed with two objects, a user and an event. And so if you're not a technologist, it's like object orientation is how you kind of think about the world. There's only two concepts for the world in a user acquisition based system. A user who's a person either anonymous or known coming into your website and the things that they do on your website or application, and you use all that data to acquire them or model them.

(00:39:03):
In a B2B business you have all that complexity, but at the end of the day, you might not really need it if all the person is doing is it's just the company is signing the contract and then you don't really care what happens afterwards. You might track users and events inside your application, but it's not for the acquisition, it's for the retention of the user. B2B2C is fascinating because you have all the complexity at the top, but then how and when do you tie a user to a company or some type of entity object, and what tools do you need to do that and where do they live in the system? And do those tools actually have competing priorities? Let me give you the greatest example of this that happened at Notion when I was consulting to them at Chris when I was consulting to them and at Ramp is having both HubSpot and Salesforce.

(00:39:45):
Both are CRMs, both have the ability to track users and companies, neither are CDPs. And how you actually map the data from HubSpot to Salesforce kind of determines how much hell you're in, and there's really no good solution. It's just like you have to figure out for yourself, how do you want to acquire use at the top of the funnel? How do you merge them into the bottom of the funnel of the Salesforce? And again, there are lots of options or versions of the world. You could use Amplitude only and collect all your user and event data and then merge that into Salesforce directly. You could collect all your data in Amplitude or Segment and then post that to HubSpot, which then posts that to Salesforce. But of course, as you make these decisions, your systems becomes more complicated and more than one person can manage. So, there's this trade-off between complexity and resources that you always have to juggle.

Lenny (00:40:33):
Today's episode is brought to you by Brave Search and their newest product, the Brave Search API, an independent global search index you can use to power your search or AI apps. If your work involves AI, then you know how important new data is to train your LLMs and to power your AI applications. You might be building an incredible AI product, but if you're using the same data sets as your competitors to train your models, you don't have much of an advantage. Brave Search is the fastest growing search engine since Bing, and it's 100% independent from the big tech companies. Its index features billions of pages of high quality data from real humans, and it's constantly updated thanks to being the default search engine in the Brave browser. If you're building products with search capabilities, you're probably experiencing soaring API costs or lack of viable global alternatives to Bing or Google.

(00:41:23):
It's only going to become harder to afford these challenges. The Brave Search API gives you access to its novel web scale data with competitive features, intuitive structuring and affordable costs. AI devs will particularly benefit from data containing thorough coverage of recent events. Lenny's Podcast listeners can get started testing the API for free at brave.com/lenny. That's brave.com/lenny. There's this big question within B2B and B2C around how to do attribution. Well, it's a never ending struggle. I'm curious if you have any pro-tips or best practices or tools that you use to improve the way attribution happens at a company.

Austin Hay (00:42:09):
Actually, I listened to your pod on multi-touch attribution. I'm forgetting who you were with at this point, but it was like I was loving it because it talked about MMM and MTA specifically.

Lenny (00:42:19):
Yeah, that was a newsletter post actually, not even a podcast.

Austin Hay (00:42:22):
Yes. So, back to our conversation around division of responsibility. I'm not always the person you should talk to create an MMM model. I'm not a data scientist. I know how to make MMM models and I know what they are.

Lenny (00:42:36):
Can you explain MMM briefly?

Austin Hay (00:42:38):
Mixed Media Modeling. And MTA stands for Multi-touch Attribution and it's these two ways of measuring the world and marketing to understand how you should allocate resources to campaign spend. MTA and MMM though are both underpinned by how you collect data. They're both informed by the user object and the event objects that you collect on your website or your application that then lead to the data that data scientists use for MTA and MMM. That's the connection between data and MarTech is often the tools and systems that we build and stand up and manage are what are used for these very complicated growth, experimentation and attribution results at the end of it. And one of the most discreet things you can do for MTA, because I get this question all the time around, hey, do we need MTA?

(00:43:21):
What should I do first touch or last touch? Should I do both? And there's actually really, I can send you this guide, but there's six or seven things you can do to basically futureproof yourself from needing either one. Because most businesses either start with first touch or last touch and then eventually want to move to a multi-touch attribution model. And for those who don't know what that is, first touch is where you kind of collect the data about where somebody first came from. Last touch is where you collect the data about where the person last came from. So, an example, would this be like if I went to Lenny's Newsletter from a Google ad and that's all he has? That would be my first touch and my last touch. If I first came from a Google ad to Lenny's Podcast, but then later I came from a Facebook ad or I don't know direct, then that would be my last touch.

(00:44:06):
And so it's this question of does the Google original first Google Channel get credit or does the second one the Facebook or direct get credit? And the first touch attribution model, a hundred percent goes to the first channel and the last touch attribution model, a hundred percent credit goes to the last touch. And a mixed attribution model or multi-touch attribution model, you're trying to figure out how to split the difference. And usually the evolution for businesses is they start with first touch or last touch, then they go to splitting it literally 50/50. And then somebody gets angry because they're not getting enough credit and they say, we've got to go to MTA. And there are both first party solutions for that and third party solutions for MTA. But back to the main thing, the main point is if you think about what you're collecting, this is for website businesses, you're collecting the referrer, like in the URL where the person's coming from, and you need any UTMs associated with that person.

(00:44:58):
And you also need any parameters from the advertising networks that might give them the ability to counter a conversion. Every ad network out there has little things they stuff into your URL that tell you that you came from them. Facebook has FVP, FPID, they sometimes encode it. Google has this thing called Google Click ID, which is just a really long string of characters that don't matter unless you know how to decode it. But all advertisers, and for the longest time advertising worked by putting parameters in URLs, pushing somebody through to your website, collecting those parameters and then passing it back to the ad network so they could get credit for it. And so in my mind, the best practice that everybody should stand up from day one is to basically design the system for MTA and then use whatever makes sense as you grow.

(00:45:45):
And so the way that I typically recommend to people is like imagine when a user comes to your website, you collect the URL, collect the referring URL, collect all the additional marketing parameters that you might want, [inaudible 00:45:57], TikTok ID, Microsoft ID, you should just make a list of them. And if you don't have that list, I can give them to you. And then you should collect all UTMs. So, in the URL, you're going to have UTM campaign, UTM medium. Most marketers use this to note what the campaign type was. Now the thing is that UTM is only going to be specific to the moment in time that the person came to your website. So, back to example about Lenny's podcast. If I come to LE's podcast and I came from a Google ad, then my UTM is only for that Google ad.

(00:46:28):
So, I have a Google Click ID and I have a UTM. So, what you're got to do is you've got to store those parameters locally on the device. Either was a browser or whatever. You got to store it as UTM first campaign, UTM last campaign. And what you do is every single time that a person comes, you replace the last campaign or the last value with the one that's there. So, say the last one was Facebook and then I come later from a direct mailer ad you replace the UTM last medium with the new one. Now what's happening if you're using third party tools is that you're collecting this user information when the person's on the website, you're going to collect it both as a user attribute and as an event that way. What's going to happen on the backend for your data warehouse team is they're going to see a user profile that has both the first attribution information and the last attribution information.

(00:47:20):
And then for all the stuff in the middle, you're firing off a page view event with first and last, where the last might deviate if there were multiple steps in the middle. So, what they can do is they can just coalesce over all the last UTMs they've seen on all your events by user to get both their first one, all the ones in the middle and the last. And so this isn't actually that complicated to set up. Most people just don't do the work early on. And then when they want to go back later and have MTA results, they don't have the data to do it. So, one of the things I tell people who are debating this is let's just get the infrastructure right from the beginning.

(00:47:55):
Let's set up so that you have users, you have user attributes, you're collecting first and last UTM on users. You're firing events with all those. There's some other more complex things you can do too. You can set them in first party cookies and you can also set them in your third party cookies for your tooling vendors. At the end of the day though, what matters is you just are collecting this information from the beginning. That way when you actually want to progress your attribution model, you don't have to wait a really long time to start gathering that data.

Lenny (00:48:24):
Amazing. I love the details that you're sharing. I don't know where else people can find this sort of advice. It sounds like a core part of this is one, just having a data warehouse where you just throw all this data into, and two, having a taxonomy that you can rely on and do multiple things with down the road. Is that roughly right?

Austin Hay (00:48:42):
Yeah, I think that's right. The taxonomy though, I think what's interesting is it's very much guided by your third party tools. And again, that's the reason why I think companies often miss the mark here is because they're not thinking about what can my tool actually allow me to put into it in the first place.

Lenny (00:48:59):
Just to make sure I understand what you're saying there, you're saying generally maybe third party tools limit what you can do, which set you up for hardship later. And maybe what you're saying is do that yourself, that tracking piece, is that roughly what you're saying?

Austin Hay (00:49:14):
Yeah, I think that's right. The way to think of it is if you build your own data warehouse, your schema is unlimited. You can do whatever you want. You can design product schema, you can design user schema and event schema, but most third party B2C tools don't allow you to control the schema. There's only one CDP I know that does that, that's Snowplow. The rest are there's a user object and an event object. So, you can either stuff data as a user property onto the user object or you can stuff data into the event and fire it off as an event, but that's what you're working with. So, what I'm saying is most people just don't think about the object orientation of the third party tools they think about and they don't design their website traffic or their app traffic. We didn't talk about app, which is a whole different slew because doing attribution with Iowas 14 is much more difficult.

(00:50:07):
But even in the website version of the world, people will often just collect UTMs and think that their job is done and it's like actually it's more complex. You have to think about first and last, think about the steps in the middle, design it so that you're putting it on the user profile and in the event. And so this goes back to the main thing that we were talking about earlier, whereas the job of a marketing technologist is to think often one to two years down the road about what we're going to need to solve for and design systems in an elegant way, not to break the bank, but to at least be the minimum viable product to actually get there. And a lot of my job, and I think the job of marketing technologists is trying to preserve that future state in the most minimally invasive engineering and resource way possible.

Lenny (00:50:48):
You've talked a bit about thinking ahead and a bunch of tools and platforms, and I'm wondering are there any new and emerging tools, platforms or even growth channels that you're keeping an eye on or excited about or finding more and more useful?

Austin Hay (00:51:02):
I'd be remiss if we didn't talk about Threads, right? Threads is super interesting. The question will be how quickly can they stand up an API for advertising and what does that look like or do they just blind it in with the existing meta and Facebook architecture? One of the caveats that I'm sure a lot of performance marketers out there will agree with is Facebook has a conflict of interest in reporting, right? They want you to spend money, so obviously they want to report the best results. And that's the reason why attribution parties like Branch and AppsFlyer exist is to somewhat curtail that conflict of interest. And so I'll be really interested just to see how attribution works, especially when you're moving from Instagram to Threads, from Facebook to Threads. Will it be the same architecture, will be the same advertising platform? Will they try to do something new?

(00:51:52):
So, I'm keeping my eyes on that. Reddit is also a very interesting place to convert now. They're opening up their conversions API, and I'm seeing a lot more investment in Reddit just because you can have embedded ads now that almost look like they can be posts that you can comment on. I think it just speaks to the maturity of the advertising business. What's happening in the background of all this is ad attribution from apps has become a lot more difficult and mostly aggregate. From 2010 to 2020, we had the golden years of deterministic matching where it was very easy to run an ad and understand with precision who installed the app. Maybe you didn't know their name, but you actually would know their IDFA and you could tie that to their PI. You can't do that anymore. It's very challenging.

(00:52:35):
Even when you can do it, the results that you would get are pretty low because nobody's going to be opting into giving you their IDFA. So, what that means is these ad networks are becoming more complex, sophisticated, and interesting right at the same time that it's harder for marketers to really understand how they're spending money. And so I'm paying a lot of attention to how marketers make decisions with probabilistic data because most of the work that I'm doing now is actually saying, well, given that we don't have determinist data about a certain audience or where somebody came from, how can I find other information that will create a model for 30% of the population and we can use that to extrapolate to a hundred. So, probabilistic matching and probabilistic attribution I feel like is a skillset that more marketing technologists and marketers should just get familiar with the way that we make decisions today.

_[243 additional lines trimmed for context budget]_

---

### How Snyk built a product-led growth juggernaut | Ben Williams (VP of Product at Snyk)
**Guest:** Ben Williams | **Date:** 2022-11-06 | [YouTube](https://www.youtube.com/watch?v=21sFTZzIfUk)  

# How Snyk built a product-led growth juggernaut | Ben Williams (VP of Product at Snyk)

## Transcript

Ben Williams (00:00:00):
Being able to identify the various micro and macro loops, how they're all connected, being able to document them in a qualitative model to communicate a shared understanding of how you grow, it's really powerful. Augmenting that then with the quantitative side of things that helps guide quarter to quarter focus and ensure you can be intentional about where you're investing, that becomes a big enabler. You're never going to have a shortage of ideas in a high performing growth team. So, knowing where to focus amidst that kind of sea of ideas is a really important role of the strategy.
Lenny (00:00:40):
Welcome to Lenny's Podcast. I'm Lenny, and my goal here is to help you get better at the craft of building and growing products. I interview world-class product leaders and growth experts to learn from their hard-won experiences building and scaling today's most successful companies. Today my guest is Ben Williams. Ben is a VP of product at Snyk which is likely one of the biggest and most interesting companies that you've never heard of. Snyk makes it easy for developers to catch security issues in their code, and there's a lot to learn from how Snyk got started. It started through product-led growth, evolved into product-led sales, was very community driven, and it was also laser-focused on developers which has become one of the most lucrative markets to go after.
(00:01:19):
In our conversation, we cover how the founders have Snyk out their first a hundred users, what they got wrong when they tried to monetize early on, when they hired their first marketing and sales people, how they structured and grew their growth and product teams, what they figured out about what should go into freemium and what shouldn't, and so much more. As you'll soon hear, Ben is British, and so, the episode is automatically going to sound more sophisticated and I can't wait for you to hear it. With that, I bring you Ben Williams.
(00:01:48):
This episode is brought to you by Coda. Coda's an all-in-one doc that combines the best of documents, spreadsheets, and apps in one place. I actually use Coda every single day. It's my home base for organizing my newsletter writing. It's where I plan my content calendar, capture my research, and write the first drafts of each and every post. It's also where I curate my private knowledge repository for paid newsletter subscribers, and it's also how I manage the workflow for this very podcast. Over the years, I've seen Coda evolve from being a tool that makes teams more productive to one that also helps bring the best practices across the tech industry to life with an incredibly rich collection of templates and guides in the Coda Doc Gallery, including resources for many guests on this podcast, including Shreyas, Gokul, and Shishir, the CEO of Coda. Some of the best teams out there, like Pinterest, Spotify, Square and Uber use Coda to run effectively and have published their templates for anyone to use.
(00:02:47):
If you're ping-ponging between lots of documents and spreadsheets, make your life better and start using Coda. You can take advantage of a special limited time offer just for startups. Head over to coda.io/ lenny to sign up and get $1,000 credit on your first statement. That's C-O-D-A.io/lenny to sign up and get $1,000 in credit on your account.
(00:03:15):
This episode is brought to you by Athletic Greens. I've been hearing about AG1 on basically every podcast that I listened to, like Tim Ferris and Lex Fridman, and so, I finally gave it a shot earlier this year and it has quickly become a core part of my morning routine, especially on days that I need to go deep on writing or record a podcast like this. Here's three things that I love about AG1. One, with a small scoop that dissolved in water, you're absorbing 75 vitamins, minerals, probiotics, and adaptogens. I kind of like to think of it as a little safety net for my nutrition in case I've missed something in my diet. Two, they treat AG1 like a software product. Apparently they're on their 52nd iteration and they're constantly evolving it based on the latest science, research studies, and internal testing that they do. And three, it's just one easy thing that I can do every single day to take care of myself.
(00:04:09):
Right now it's time to reclaim your health and arm your immune system with convenient daily nutrition. It's just one scoop in a cup of water every day, and that's it. There's no need for a million different pills and supplements to look out for your health. To make it easy, athletic Greens is going to give you a free one-year supply of immune supporting vitamin D and five free travel packs with your first purchase. All you have to do is visit athleticgreens.com/lenny. Again, that's athletic greens.com/lenny to take ownership over your health and pick up the ultimate daily nutritional insurance.
(00:04:45):
Ben, welcome to the podcast.
Ben Williams (00:04:47):
Thank you very much, Lenny. Thanks first of all for inviting me. It's a pleasure to finally meet you. I've got to say that kind of what you're creating with the newsletter and now the podcast, just such awesome resources for the product growth and wider tech community, so it's real honor to be invited onto the show, and I hope there's a few useful things that people can take away.
Lenny (00:05:07):
Awesome, man. I really appreciate that. I have no doubt there will be many useful things people will be able to take away. I'm really excited to chat about Snyk and the things that you're building there. I feel like Snyk is this very under-talked about company and also super fascinating companies, especially in terms of how it got started, how it scaled, and it's also at the center of so many trends, product-led growth, community-led growth, focusing on developers to grow, and also just security in general is really interesting, and so, I'm really looking forward to our chat.
Ben Williams (00:05:36):
Me too.
Lenny (00:05:37):
Before we get into all of that, I'd love to spend just a minute on your background. So, you're currently VP product at Snyk, and I'm curious how you got to that role and just some of the other wonderful things you've done in your career along the way there.
Ben Williams (00:05:51):
I'll try to keep it reasonably short. My education is in computer science, graduated from the University of Manchester back in the late '90s. I'd already landed as a job as a developer, but ended up having a bunch of other interesting offers, one of which was to join a small startup building requirements management tooling for product and engineering folks. This was all pre-Agile, but that whole space of developer tooling, engineering tooling, it was something I just felt naturally drawn to and it's where I've really specialized through my whole career. I actually joined that company as a solutions engineer, so lots of demos and so on. I was really close to the product team, but also speaking with customers every day which as is quite common I think was my path into products there.
(00:06:34):
Several years and a few acquisitions later, I find myself in IBM with the Rational software developer tooling group. I was leading parts of the product strategy there and a bunch of initiatives. I actually, I learned a ton of useful stuff there, but also that I had a strong preference for working in smaller, fast-growing orgs verse 350,000 people [inaudible 00:06:55]. After an interesting unexpected interlude, leading a DevOps transformation at a fintech and some consulting and advising, I then joined CloudBees. They're a DevOps startup with an open-core model. I was leading product design and growth there. Stayed with them for three years through several raises and a period of really fast growth before finally joining Snyk to build out our growth organization and lead our developer experience initiatives. I have a broad remit at Snyk now than just the growth org, but yeah, that's how it started.
Lenny (00:07:26):
Awesome. To give folks a sense of just how successful and big Snyk has gotten, one is just what does Snyk do, we haven't even talked about that yet, and then two, just some stats about the scale of the company and the business at this point.
Ben Williams (00:07:40):
The developer security company, we make it ridiculously easy for developers and their teams to improve their security posture while still moving fast. So, Snyk can find and automatically fixed vulnerabilities in code, open source dependencies, containers, infrastructure and cloud configurations, and all underpinned by the best security intelligence data in the market with a laser focus on developer experiences, which is why we're, we are really different. It's also an amazingly fast-growing business with some stellar PLG-focused investors and board members from the likes of Ed Sim at boldstart to Tamar Yehoshua, Slack CPO. We were founded in 2015, last valuation after our Series F was at 8.6 billion. We're securing the software of millions of developers now, well over 2,000 paying customers, now around 1300 people of which are around 500 in R and D with nearly 70 folks in our product org. And the people here just create this amazing culture, and all in all, it's just a really exciting place to be.
Lenny (00:08:44):
Okay. Did you have any sense it would get to this scale when you joined early on?
Ben Williams (00:08:49):
Yes, I think because I wasn't looking for a new role when I ended up joining Snyk, when I was first approached by them, but everyone I spoke with along the interview process, just became more and more impressed with not only the caliber of people here, but the vision, the mission for the company, and all those things you mentioned in terms of PLG, community-led growth, focus on developers, the security space, these were all things that if you create a Venn diagram of all the things that I'm really interested in professionally, super interested in, super exciting to me, then kind of Snyk ended up in the middle of it. So, it's pretty cool.
Lenny (00:09:29):
Awesome. So, that's a good segue to where I wanted to start is how Snyk started and how Snyk got their first hundred users, and I know you weren't there necessarily for that, but I'm curious what you can share about how the founders found their first say a hundred users. How did they get to their initial developers and get people excited?
Ben Williams (00:09:47):
I think it's a really fun story. So, if you don't mind, I'll just take a moment because I think it's important to set the stage by looking back at-
Lenny (00:09:52):
Let's do this.
Ben Williams (00:09:53):
Yeah, just look back at the market in general. So, PLG or bottom up and security, these were never words that were known to have been spoken together in a single sentence, right? So, security has always been a centralized function. Security programs were historically more about audit and policing and enforcement versus developer enablement or empowerment. A sales motion you saw it was always top down. It was seen as immovable, CISOs, other AppSec leaders with the buyers. Security tooling that was out there at the time, they all catered to this dynamic and these were tools that slowed developers down. They created a lot of frustration. They were met with a lot of resistance, not the ideal recipe really for consistent adoption and strong engagement and retention, and ultimately, app security programs based around those kind of solutions just weren't effective as they really needed to be.
(00:10:46):
So, it was a realization around this, timed with adjacent market shifts happening with DevOps that sparked the ideas behind Snyks. So, the founders, Guy, Danny and Assaf, they saw a real opportunity just to do things differently. They believed that the most effective way to improve application security posture was a developer-first approach. They knew that the developers were increasingly caring about the security of their code in the same way that they cared about performance and functional quality of their code. But they also knew that to empower developers to own that security, they needed just much better tools with way less friction than they ever had before. And their approach was, I think looking back, super smart, focus on a community. It wasn't the full extent of what we'd think of as community-led growth now, but it was close.
(00:11:35):
They started with a really narrow, early focus. It was a single persona, single context, single use case, and what that meant for Snyk was developers building applications using Node.js who wanted to ensure that the open source dependencies they were pulling into their apps were secure. Now, open source software, that's a huge accelerant in building modern software. The average software application today is at least 75% of open source libraries and components. So, this was increasingly becoming a primary attack vector for malicious actors who could find a single vulnerability in an open source component and then find it and exploit it in every single application that was using that component. And at the same time, at least back then, open source software was much less tested for security vulnerabilities, and the maintainers of open source libraries were often less security aware. So, you get that context, and then at the same time, Node.js as a run time was gaining traction. So, there was this increasing adoption in the enterprise, more and more dedicated conferences and the like, but the community was still small enough that Snyk could meaningfully influence, and Guy and the others just went all out on being deeply involved in that community. They were presenting at dev conferences, meetups, they were building online content and so on. And the question that they repeatedly posed to the community was do you have known vulnerabilities in your apps, and Snyk was there to help them answer that question. And fun kind of fact on the side, if you search for Snyk in the Urban Dictionary, you'll see it's an acronym for so now you know. But all of this kind of I think really only worked because of the parallel product-led approach. So, while the answer to the question about how does your product monetize users was much less clear cut in the early days for Snyk, the answer to the questions, how does your product acquire and retain users has always been product led.
(00:13:35):
And the initial version of Snyk, it was a command line tool. It was a tool for developers, it could be run locally or easily integrated into CICD pipelines for early feedback. It allowed devs to assume more responsibility for the security of their apps, and that was just very different from the typical incumbent technologies that were run by security teams late in the dev process, long feedback loops, issues thrown over the walls, inevitably just frustrating developers. And all of this was just built on this fundamental belief that the only viable path, and by viable I really mean sustainably effective, the only sustainably effective path for software-centric organizations to meet the challenge of becoming and staying secure was for them to take this developer-led approach to that challenge. So, really kind of complete disruption of the industry and developer adoption for that reason was always a key priority for us.
(00:14:31):
So, with that in mind, Snyk has just been free to use in some capacity from day one, and the early strategy was always about creating something valuable that was readily available, something that solved a real problem in a uniquely differentiated way, and making it pervasive. So, with dev-led option, this core concern, a freemium go-to-market strategy was just the obvious approach. So, eventually, getting back to your original question, that's all of the context and where and when and how they did it, but the first hundred or so users really just came from the founders engaging with the Node.js community and the interest that drove. I think we probably had maybe around 5,000 free users before there are any attempts at monetization.
Lenny (00:15:13):
Awesome. There's a bunch I want to unpack there because what's interesting the way you describe it maps to the series that I recently wrote about consumer growth strategy and how the first three steps after you have an idea is to come up with your super specific who, kind of your target persona, come up with a hook that catches them and gets them excited, and then go find them where they are and pitch them your hook. So, the super specific who for Snyk was you said open source developers working on Node.js. Is that right?
Ben Williams (00:15:41):
Well, it was Node.js developers, and Node.js developers were building their applications using open source Node components.
Lenny (00:15:50):
Mm-hmm. Got it. Was there any other constraint to that, do you know, or those were the two to three attributes of a user?
Ben Williams (00:15:56):
That's really it. The community was growing for sure. It was big enough to have a decent opportunity there-
Lenny (00:16:03):
Makes sense.
Ben Williams (00:16:04):
... but narrow enough that technology wise, it meant that a product could be brought to market in a reasonable time.
Lenny (00:16:10):
Yeah, that's great. And then the hook was basically you have known vulnerabilities in your code base which if I were an engineer, like, "I don't know, shoot, I don't know. Get a find exactly. I'm scared now."
Ben Williams (00:16:20):
Exactly. And then so now you know. Right?
Lenny (00:16:22):
Yeah, exactly. Okay, cool. And then the where, so you said that they went to open source communities. Do you have any more specifics about what those were? Was it like a specific forum? Was it like GitHub somewhere? Was it Reddit? Do you know any idea where those communities lived?
Ben Williams (00:16:36):
Yeah, it was less about a particular place, but more about the community of developers themselves who focused on Node.js. So, a bunch of early evangelism was really at conferences. It was I think the Velocity Conference in Amsterdam where Guy and Assaf kind of first unveiled Snyk to the world, and yeah, it went from there.
Lenny (00:16:58):
I see. Interesting. So, it was in-person events, conferences, and meetups probably focused on Node.js developers.
Ben Williams (00:17:03):
Exactly. Yeah.
Lenny (00:17:05):
Okay, awesome. What happened after that? So, that was the first hundred. Was it just roughly the next stage of growth or did it focus on that for a long time? What was the next stage roughly?
Ben Williams (00:17:14):
Yeah. I think that focus was the really important kind of element there, if I can kind of latch on that. Starting with that narrow focus and building around community engagement, I think it's a well-proven playbook now, particularly in the developer tooling space like New Relic did it notably with Ruby community for example. But ultimately it was important because of this kind of depth verse breadth approach and that depth-first approach that Snyk took was important to be able to effectively validate the solution on the path to product market fit. A JavaScript developer just won't care if you support Golang or Rust, but will absolutely care if a key feature like automated package upgrades just isn't available for their ecosystem.
(00:18:04):
Of course, the bigger problem of vulnerable components in open source across all languages and all ecosystems, that's a very widespread problem. It affects the industry at large, but that just spoke to the potential opportunity that was there to be unlocked. But the key for Snyk I think was just not to go too wide, too early. So, it focused on nailing that initial use case for that specific community of Node.js devs, like I say, narrow enough to be able to really focus on quickly building a compelling solution to a real problem, but also wide enough to be something viable from a growth perspective. And even back then the NPM, the Node Package Manager hosted around 200,000 open source packages. They were downloaded something like two and a half billion times a month by over 2 million devs. And the typical node app would have hundreds of dependencies, mostly indirect and so hidden less immediately visible. But each of those dependencies brought with it some security risks. So, yeah, I think nailing that narrow and deep-use case before expanding wider was absolutely critical and generally just sound advice around finding product market fit and building solid momentum before casting a wider net. It's difficult to maintain that focus for sure as the lure of that bigger term can be really tempting, but ultimately you have to build a service and market well to capture it.
Lenny (00:19:23):
Do you have a sense of when that focus expanded to an adjacent group, how many years into the growth story that happened, or was there some kind of milestone there? Because I know everyone imagines, yeah, we'll expand, the question is when and when does it make sense and when is it too early. Do you have any insights into that phase?
Ben Williams (00:19:43):
Yeah, for sure. First, I think if we're talking about PLG and the story with Snyk, I actually like that definition of product-led acquisition from Julian Shapiro when you spoke with him, and beyond that maniacal focus on finding product market fit for your product, founders really should be thinking about how their product is going to grow, and that's important of course as you think about taking that next step. So, let's assume in a simplistic definition that you found product market fit as demonstrated by a strong retention, and then the real question is where are the new users for your product going to come from, and founders really should have, I think, strong hypothesis around this, your risk essentially, adopting an if we build it, they'll come approach.
(00:20:27):
So, if your acquisition strategy is product- led, then understanding and being intentional about your early acquisition growth loops I think is an essential founder's responsibility. Dedicating time there to design those loops into the product, it's key. And when I say product, I really mean the whole product experience considering every touchpoint in and out of the core application that your users and customers might have with you. Snyk, for example, believed very early that we could build out powerful content loops via fixed pull requests that we raise on GitHub. New users, they'll sign up for Snyk, they'll connect their GitHub accounts, Snyk will scan their code, will find vulnerabilities, will automatically create Snyk-branded pull requests to fix those vulnerabilities. Other devs in the repo will see and interact with those PRs, and some of them will follow links to Snyk, create accounts and some of them will connect their own repos, and so the loop continues. So, company generated, company distributed content loop, it's actually really powerful for us because it's both an acquisition loop and an engagement loop.
(00:21:28):
Over the course of time, we extended that loop by adding support for other source controlled systems beyond GitHub. We layered on a bunch of new loops, and I think if founders can be intentional about this as you're developing early product iterations, then you're going to have a bigger advantage when the product clicks with the market, and that was built into Snyk as we went along. So, that was kind of ready as we found product market fit. But I think to talk about specifically how Snyk took that next stage, it was a function of when we were chatting before this, we talked a little bit about some of the failed experiences spinning up a self-serve revenue channel, and-
Lenny (00:22:09):
Actually before we get there, which I definitely want to get into all that, I love this story you just shared. I hadn't heard of this growth tactic of basically they connect their GitHub account, you find all the vulnerabilities, push a fix, people see that Snyk did this for them and it just provides all this value, and you're saying that was really effective. It's an example of something that worked very well.
Ben Williams (00:22:29):
First of all, that integration in terms of connecting your code with security scanning like that was a first of a kind integration.
Lenny (00:22:38):
Yeah, magic.
Ben Williams (00:22:39):
No one had done that before. But the key was that we ultimately controlled the content. So, not only was the fixed pull request doing something useful in terms of the code, but all of the description of the pull request was explaining about the vulnerability, educating users, and it was all Snyk branded and saying, "If you find this useful, click here, come and learn more about the vulnerability. Sign up for an account if you don't have one." It kept existing users coming back.
PART 1 OF 4 ENDS [00:23:04]
Ben Williams (00:23:03):
You sign up for an account if you don't have one, it kept existing users coming back and it brings new users, a lot of new users, in fact.
Lenny (00:23:06):
You'd be in there all like, "Do you have known vulnerabilities in your code base? Click here to find out." Is that responsible for much of the early growth, that loop?
Ben Williams (00:23:15):
I think that was one of the loops. We also have a couple of, from fairly early on as well, other content loops that are more kind of programmatic SEO assets that have both been pretty instrumental in terms of new user growth, yeah.
Lenny (00:23:31):
It'd be cool to hear about those if they're relatively straightforward to explain, and then we can get to the thing that didn't work, the self-serve monetization piece you were going to get to.
Ben Williams (00:23:40):
We have a bunch of loops actually at this point to start off.
Lenny (00:23:42):
Lucky you.
Ben Williams (00:23:44):
Yeah, I'm a big loopist, funnily enough. But yeah, we have a bunch of loops. Company generated, company distributed content loops have actually worked really well for us. We have a side car product called Snyk Advisor. Snyk Advisor, it's basically a service that developers use to search and find open source packages when they're considering integrating some within their software applications. The unique thing about it is it indexes all of the package managers. It learns about those packages. It augments the data about them with a bunch of metadata, including of course Snyk security scans, but we also find out how actively maintained the software is on the source repo on GitHub or wherever.
(00:24:31):
We build this kind of package health score, so anyone searching on Google for a package that does X, Y, Z or a specific package by name, Snyk Advisor will be right up there in terms of the search results. They'll land on there, they'll get a good idea about that package, they can look at similar packages and it's all, of course, a Snyk website and we have CTAs to say, "If you want to secure your application on a perpetual basis, then just come and join us." That's a great loop. That's all kind of a programmatic asset. There are hundreds of thousands of these package pages, but they're just automatically being generated continuously.
Lenny (00:25:07):
Got it. It's programmatically generated better indexing of open source libraries that you can integrate with. That is so smart. It's programmatic because you can inform on the security vulnerabilities and then the maintenance and activity. Interesting. Yeah, that makes sense. That's all data you could just gather. That's awesome. Okay, so there's that. Is there anything else that's worked really well for you guys to help you grow self-serve?
Ben Williams (00:25:31):
One of the recent ones that's really interesting is security education. We think of Snyk as a change agent in helping DevSecOps transformations and it's fine kind of having this capability, but what we really want to get to is this position where developers truly understand and can be better placed to prevent security vulnerabilities being injected into their code. One of the things that is, again, something that's pretty different from the industry from an incumbent perspective is that we believe it's really important to democratize security education.
(00:26:06):
We have been building this bunch of really high quality but bite size lessons about developer security that focus on developers about security issues and vulnerabilities and we surface them. Again, they're out there in the public domain. There's no paywall to get access to those. All the traditional solutions you need to sign up, you need to pay to get access beyond more than a couple. But these were just, they're all out there in the public domain. That works really well for us from a company generated company distributed loop as well.
Lenny (00:26:36):
So cool. SEO and then integrating to GitHub in an interesting way. Imagine there's also a lot of intra-company virality when someone uses Snyk at a company and they spread it to their colleagues?
Ben Williams (00:26:47):
Yeah, I mean, I didn't talk about those. I think those are pretty well understood. We have both referral loops and invite loops as well.
Lenny (00:26:55):
Okay, awesome. Coming back to what didn't work, and I think you mentioned that there was a monetization attempt that was self-service oriented and that had some challenges. Can you talk about that?
Ben Williams (00:27:06):
At the time, a few things were in place. Valuable product, check, strong developer user growth, check, strong retention, check, but the first self-serve monetization efforts only really saw traction with individual developers paying a hundred dollars a month. Or purchases in larger companies, they just didn't happen as everyone had hoped. There was a really critical part of Snyk's history. At the time a bunch of investors didn't lean in, perhaps shy away from early conviction with the founders on building strong usage without a proven path to monetization at that point. Ed at BOLDStart who I mentioned previously, he was one of the first kind of true believers and was I think really key in helping with providing runway during that time. But it was clear that there was a lot of work still to do. The team dived in, they really figured out what the constraints were and through that process really learned about the importance of catering for the broader governance needs of the enterprise buyer.
(00:28:07):
And that meant a couple of things. First, there was a need to build out table stakes features around governance at scale. Just things that companies of a certain scale and size expected reporting, robust user management and so on. And second that it was time to move beyond that depth first approach, right? That depth first approach was absolutely critical in getting to that point, but it wasn't good enough to take the next step. If you think about it, there's a point in a company scale where you start to see diversification of tech stacks and all of those tech stacks need securing. It's obvious in retrospect that only supporting developers using a narrow slice of those tech stacks wasn't going to meet the needs of the security teams who were ultimately the people who were held accountable for the security of their entire application estate. The teams worked hard over the next few months starting to build support for additional languages and ecosystems and adding those table stakes features.
(00:29:04):
I think back then Snyk were simply ahead of this inevitable curve of developer first security. At the time, the only buyers were security teams and dev first Security for the most part wasn't something that CISOs and ApSec leaders were driving. But if you look at Snyk through that lens of, as I mentioned, being a change agent, being a key piece of the transformational journey of our customers' DevSecOps journeys, you realize how important it was for us to start to build relationships with those security leaders. It was that time also that it was the right time to bring in the first sales and engineering hires as well.
Lenny (00:29:48):
You basically found it couldn't work self-serve, independent of sales being involved in convincing the folks at the top, which makes sense. How do you trust a company with your security if the people at the top responsible for security aren't bought in? Makes sense.
Ben Williams (00:30:04):
Today it's less like that. There are organizations where the buying center is still very much ApSec, but there are also many organizations where kind of technical leaders on the buying decision around security investments. What was always true though even back then was the influencing power of developers, regardless of where the buying center was.
Lenny (00:30:28):
And I imagine as the brand has grown, it's gotten easier to convince people like, "Oh yeah, look at all these other logos using this. It's probably going to be okay."
Ben Williams (00:30:33):
For sure.
Lenny (00:30:36):
Just to understand in your experience with Snyk, it never really worked self-served monetization. It worked as a way to get into a company and then developers started using it in small scale, but you needed sales and marketing to really grow monetization. Is that what you found?
Ben Williams (00:30:51):
I think back then, yes. Now it's a very different story. We have a lot of self-serve only customers scaling pretty large, so.
Lenny (00:30:59):
Got it. That's interesting. I rarely hear that you start out with sales being important and it becomes less important or I imagine it's still very important, but there's like a segment that has emerged that can self-serve. Fascinating.
Ben Williams (00:31:14):
Yeah, I think it is important to acknowledge though, that the product has always played a really key part in the sales process for sure.
Lenny (00:31:21):
That touches on something I wanted to ask. [inaudible 00:31:24] you've mentioned him a couple times, he's got this awesome newsletter, he talks about you guys all the time. I think he's very proud of the progress of Snyk and he talks a lot about that for developers, you got to win hearts and minds of developers to build something that works. Any lessons or pieces of advice for folks that are targeting developers to win hearts and minds and get engineers, developers excited about what you're building?
Ben Williams (00:31:47):
I think there's two things, right? First of all, fundamentally for someone to get excited about using a product, they've got to care enough, right? They've got to have a problem that you're solving. I think there's two things. One, there is a shift that is happening and still happening. I think there's still a long way to go for developers to really care about security as an integral part of their job in the same way they think about functional quality or performance. I think that we're still, we're making strong progress there. It's changing all the time, but there's still a long way to go there. But the reality is that I think in most companies, developers have to care about security because their companies need to be secure. The key then is how do I make the job of being secure for these developers, as painless as it absolutely needs to be?
(00:32:44):
And that means really meeting them where they are, integrating with their tools, finding ways to take security to them instead of trying to pull them out of their workflows. Flow is just this incredibly important concept for developers and you want to strive to keep them in that flow for as long as possible. The GitHub kind of pool requests are a great example of that. Someone can sign up for Snyk and they could theoretically be the only user of Snyk and connect their repos. All of a sudden we're protecting, securing those repos, a hundred, a thousand developers could be working in GitHub with that code, all benefiting from Snyk without necessarily needing to sign up. That's that example of taking the product to users without pulling them out of their workflows. I think that's absolutely critical.
Lenny (00:33:38):
As an outsider hearing all this, it's a product that magically helps you avoid security issues, very little work, does a lot of the work for you. It's hard to imagine it not working looking at it now, and I'm curious what it was about the early days that just felt like maybe that people didn't believe in this working. Is it just there was doubt that it would be smart enough to find your security vulnerability issues? Was it the timing wasn't right, people weren't ready, weren't concerned about security enough? What do you think it was that created challenges early on? Because looking back, it's like, of course this is going to work. How could it not? It sounds just like a magical all win product.
Ben Williams (00:34:16):
First of all, don't think the challenges were there in terms of the developer adoption. Even when those first kind of forays into self-serve were struggling in terms of breaking into some of the larger customers. The developer adoption, the free user base was still growing at a really good pace. That momentum was just constantly building and it's that momentum that has ultimately fueled the sales led business as we've gone through the years. But it was just those few things I think that I mentioned earlier in terms of stumbling blocks that needed to be overcome because when those first sales and marketing hires did join us and we started having conversations and we also tweaked some of the things in the product to meet, had some breadth, had some additional languages, ecosystems, building those table stakes features, then it really unlocked and it was rocket ship time from then.
Lenny (00:35:11):
Got it. Sounds like the biggest issue is monetization. Can we make money doing this? Developers love it, they're using it like crazy, but will people be convinced to scale this an inside an organization and pay us a bunch of money for it?
Ben Williams (00:35:21):
Exactly, yep.
Lenny (00:35:22):
Okay, got it. I want to dive a little bit deeper into your growth team and product team and how you think about organizing teams like that in a product led growth sales org. The first question, just how did the growth team start at Snyk? What was kind of the early days and then what does it look like today?
Ben Williams (00:35:41):
There were some ad hoc efforts happening in various places. We had a small growth marketing function, we had [inaudible 00:35:49]. We also had some ownership of key growth services in R&D. There was a team that owned the new user onboarding flows, for example. But it wasn't until I joined that we really formalized the notion of a growth team. It was very kind of ad hoc before then. When I joined, we created what we call the developer growth group now. Before then there maybe wasn't strong an understanding about what a growth team needs to look like, how they might need to work differently to the core product teams. And I'd say overall it was much later than you'd typically expect to see. And at a bigger scale. You normally are going to start growth teams, one or two people, three or four maybe, and scale out from there. But we started much bigger than that. But at the same time, this bottom up developer first approach, it was baked into the company DNA in terms of how teams think and operate. Yeah, we were growing fast even before we spun up the growth group. I think the significant change that happened there, it was a transition from a simple freemium approach to a holistic and well-coordinated PLG strategy. It's much more common to start earlier, much more common to start at a smaller scale than we did at Snyk, but it worked for us because of this kind of perfect storm of where we had a product with that bottom up growth built in from the beginning. We had founders with a deep appreciation for how the product could grow and there was strongly exec alignment and sponsorship for scaling the motion. The problem when starting the growth group, it was really for the most part more oriented to how we can get the flywheel spinning faster as opposed to getting it moving in the first place.
Lenny (00:37:26):
Where did you initially focus that team? Which part of the flywheel?
Ben Williams (00:37:30):
Right now we have dedicated teams focused on acquisition, activation and monetization along with a supporting team who own our growth platform, including all of our data and experimentation stack. But the macro structure, it's changed over time to enable us to focus on the biggest constraints in our growth model. At the beginning we just focused on acquisition and activation, intentionally deferring any investment into specific monetization initiatives around the self-serve revenue channel until we felt confident that A, we'd built the necessary growth muscles to scale, and B, we'd figured out some of the more pressing issues that were present earlier in the user journey. It was important that we felt really confident about our ability to effectively connect developers to Snyk's value in such a way that introducing and optimizing a self-serve revenue channel would make sense. I also really wanted to avoid one of the common failure modes I've seen around cross-functional collaboration and growth.
(00:38:28):
When I joined, there was an inherent tension built into the system. It was particularly noticeable between R&D and the growth marketing team. We had amazing people in both teams, a ton of really great ideas, but many of them were just not being executed on and it was leading to a lot of friction, a lot of frustration, ultimately caused by misaligned incentives between the different functions. When creating the growth group, we resolved this by ensuring that each of the growth teams were truly cross-functional in nature with everyone in each team aligned around common objectives and KPIs. Every team has engineers, an engineering manager, a product manager, a designer, a growth marketer, decision science support, and a basic shape of the growth teams that'll be familiar to most, but I spoke to a bunch of people over the last couple of years and I've actually learned to my surprise that inclusion of growth marketers in the product teams is not all that common. And I personally think there's just a lot of opportunity being missed there and I expect that to start to become the norm rather than the exception over time.
Lenny (00:39:32):
Okay. I want to talk about that, but before we get there, you said there's a decision science person on the team. What is that about? That's cool.
Ben Williams (00:39:38):
That's right. We started off from a fundamental BI data analyst perspective, but over time we wanted to apply a much deeper level of analysis on the data such that we could start to build in predictive models that could help us make better decisions and can ultimately fuel and power some of the end product experiences. Yeah, we spun up a decision science function and those folks are very smart.
Lenny (00:40:13):
Is that similar to data science or is that a separate ... Okay. It's cool that you call them decision science people versus data science, because that's so much more actionable.
Ben Williams (00:40:23):
Yeah, I think so.
Lenny (00:40:24):
Wow, that's cool. All right. I haven't heard that before. Makes me think of Annie Duke and all the stuff about how to make better decisions and I love ... Is this something anyone else does or is this something you came up with calling [inaudible 00:40:38]-
Ben Williams (00:40:37):
I'm not sure. I don't necessarily think what we are doing is revolutionary there, but maybe the name, I'm not sure.
Lenny (00:40:46):
Yeah, the name is cool. I haven't heard that before. It implies bias towards action versus just we're going to do a bunch of cool stuff with data. Interesting. Okay. Then you said that there's a growth marketer embedded in each team, so maybe just broadly what makes up these teams? Which you touched on briefly, then what have you learned is the value of having a growth marketer embedded within each team?
Ben Williams (00:41:06):
It's important to have balanced teams with strong diversity across multiple vectors. Focusing on functional diversity at the moment, which is kind of what you're asking about with having growth marketers on the team, one of the big benefits you get is a broader pallet of ideas, but also a bigger toolbox when it comes to execution, which generally translates in an ability in a growth team for them to test and learn faster with more parallel, yet at the same time, aligned threats. Perhaps I can give a recent example there. Having a growth marketer in an acquisition focused team led us to some lightweight experimentation on the website in creating an SEO optimized page. It was something that was really high performing, both from the perspective of traffic and conversion, but it didn't require any engineering resources to create. The growth marketer and the team, and they decided together this was something worth pursuing.
(00:42:01):
But the growth marketer was able to kind of execute that independently while engineers were working on other things. But then based on the success of that, the team went on to build out a functional sidecar product that allowed users to basically try Snyk without needing to sign up by simply placing their code in for us to scan and giving them some results there and then. We saw really great results with that visitor traffic, saw a significant increase, sign up rate dropped a little bit as we'd expect it would, but overall new users had a big bump and those users had much higher intent, which we saw play out with increased activation rates.
Lenny (00:42:37):
Awesome. Okay. And so there's essentially four teams under the growth umbrella. There's acquisition, activation, monetization, and then this kind of experimentation platform team. Is that right?
Ben Williams (00:42:47):
Yeah, that's right. And that team is also responsible for making that data available elsewhere in the organization as well. Product led sales is a really important motion for us, and so taking the knowledge we have, the insight we have around behavior with the users and their teams and their companies within the product, and making that available to the GTM teams outside in smart ways, allowing them to focus on the things that are most important to focus on. That's a really important part of what that team does.
Lenny (00:43:20):
It's interesting, you guys are the epitome of product life sales. That's this new trend of from PLG to PLS for sales. It's obvious that they're a big part of this whole process. The fact that monetization happens almost all through sales is interesting. That's interesting. Cool. Okay. That's not a question, just a thought, talking out loud. One other thought I had is, so you talked about SEO being a really important part of your growth. What is the person team like to do the SEO piece, the right content? I imagine they're on the acquisition team, there's maybe a content person that lives within that team.
Ben Williams (00:43:55):
We have actually one of, the smartest SEO people I've ever met within [inaudible 00:44:02].
Lenny (00:44:02):
What's their name? Let's give them a shout out if you want.
Ben Williams (00:44:03):
Anna. Yeah, cool.
Lenny (00:44:05):
Joanna.
Ben Williams (00:44:05):
Well, she's part of growth marketing, but she works extremely closely with the growth teams and she's got a few people in her organization and we bring them into specific SEO focused initiatives when we're looking to build loops around that. Incredibly important to have someone like that who understands that at a far deeper level than I could ever hope to, how SEO works. And particularly in terms of keeping on top of some of the things that Google are constantly doing in terms of their algorithm changes.
Lenny (00:44:37):
And does she actually do the writing for editorially, for I guess even the programmatically made pages or there's someone she outsources-
Ben Williams (00:44:43):
No, but what she does do a great job of is providing the kind of continuously updated guidelines on how content should be structured to lead us to good results.
Lenny (00:44:55):
Then it's just engineers and PMs that end up writing the things? Wow. Cool.
Ben Williams (00:45:00):
Yeah, that's exactly right.
Lenny (00:45:04):
This episode is brought to you by Vanta, helping you streamline your security compliance to accelerate growth. If your business stores any data in the cloud, then you've likely been asked or you're going to be asked about your SOC 2 compliance. SOC 2 is a way to prove your company's taking proper security measures to protect customer data and builds trust with customers and partners, especially those with serious security requirements. Also, if you want to sell to the enterprise, proving security is essential. SOC 2 can either open the door for bigger and better deals or it can put your business on hold.
(00:45:39):
If you don't have a SOC 2, there's a good chance you won't even get a seat at the table. Getting a SOC 2 report can be a huge burden, especially for startups. It's time consuming, tedious and expensive. Enter Vanta. Over 3000 fast growing companies use Vanta to automate up to 90% of the work involved with SOC 2. Vanta can get you ready for security audits in weeks instead of months. Less than a-
PART 2 OF 4 ENDS [00:46:04]
Lenny (00:46:03):
Can get you ready for security audits in weeks instead of months, less than a third of the time that it usually takes. For a limited time. Lenny's podcast listeners, get $1,000 off Vanta. Just go to vanta.com/lenny, That's V-A-N-T-A.com/lenny to learn more and to claim your discount. Get started today. What advice do you have for folks building growth teams and maybe either similar space or just B2B, PLS oriented businesses in general? What have you learned about what is important to get right?
Ben Williams (00:46:34):
This is a big topic. I have a lot of thoughts here based on what I've seen work well and also not so well. I think I can broadly bucket things here into maybe three main topics. So the first would be people and process. The second would be strategy, and the third would be data. Now they're all related and they all have to be working well to be effective in growth. Starting with people maybe touch the first element there in terms of balance teams, you've got to have those balance teams with diversity and ability to create great ideas, but also ability to execute. So that's the first thing.
(00:47:14):
But still on the topic of people, I have this kind of mental model, that potential that at its core is unbounded, but that a bunch of things situationally prevent people from fulfilling their potential. It might be how they're thinking about something. It might be organizational. It might be in relationships with coworkers or in broader team dynamics. It might be in them not even being in the right role even.
(00:47:37):
So fundamentally I think it's the role of managers and leaders to help them identify those things and work with them to find ways to thrive and grow. And I've seen this have particular significance in a growth org where people are just naturally less good fit. Now that doesn't mean that they're not amazing talented humans. It just means they aren't going to do their best work in a growth context.
(00:47:59):
So when you're starting a growth team, you'll often be doing so with internal moves. So this can be something that's maybe a little bit easier to miss than with external candidates where you are likely testing for those things explicitly during the hiring process. I'll share an example with developers.
(00:48:17):
So the devs that really thrive in a growth context are the ones that are motivated by moving quickly, iterating to create measurable impact. They're not attached to their work. They embrace imperfection as part of the process. They happily discard their code, their ideas even. They're curious and they're always looking for ways to be closer to their users.
(00:48:38):
Now those are the folks that generally make great growth engineers and I've also known incredible engineers that are most motivated when they're working on really deep technical challenges and love the process as much as the outcome. And they've struggled in growth. Of course it's never that simple in reality. There's nobody who's really at either extremity of that spectrum. But it's really important to try to answer the question, can this person do their best work in this environment? So I think that's a really key part of it.
(00:49:10):
And yeah, you need to also make sure they're well equipped from a kind of skills and knowledge perspective as well. So they need the right skills and knowledge to be able to do their best work in the context of your growth process. So the ideal state is that every growth team member has common vocabulary. They're comfortable with the growth process. They can work well with data and experimentation platform. They understand the data. They have the right skills and mindset.
(00:49:36):
Education I think plays a big part here. So we're big fans of Reforge, but we've also developed a bunch of internal programs to align and uplevel the teams. Something we learned, I think as an example, is the importance of starting simple and going deeper as the teams build experience. So for example, when it comes to experimentation, don't try at the beginning to introduce multivariate testing or concepts like sequential samplings and alternative evaluation approach.
(00:50:04):
Teams are still trying to just dip their toes in that... This water, it's kind of a recipe for a lot of mistakes. So that would be some advice there.
(00:50:15):
But people also need to be well aligned. I've talked about this actually on another podcast that I did recently. But what I mean by that is their execution needs to be aligned with an evolving growth strategy. The growth strategy needs to be aligned with and at the same time influence where the company's going. The growth strategy needs hooks into the product strategy and ideally there's some overlap and alignment of KPIs so that the growth teams and the core product teams are swimming in the same direction. The skills and experience in the team need to be aligned with the strategy. If you've got to focus on activation and acquisition, then someone who's a plans and pricing expert probably isn't the right set of skills at that point in time.
(00:50:57):
But you also, leaders need to plan to ensure those skills are available as focus of the growth team inevitably shifts over time. But at the end of the day, I think everyone needs to be able to easily answer the question why they're there. Why the work they're doing is important.
(00:51:14):
I don't know if it's too far off track here, but I have a vision and mission framework that I like to use that leads to I think, great simple statements of an imagined better future state and your role in getting there. So I can talk about that a little bit if it's a-
Lenny (00:51:28):
Yeah, let's do it. That sounds too good to pass up.
Ben Williams (00:51:31):
-Cool. So the vision is the nirvana state that you aim to enable for your users and customers in five to 10 years. It's something that could equally be enabled by your competitors if you don't execute effectively or efficiently or quickly enough. You can always prefix a vision statement with in the future, dot, dot dot.
(00:51:52):
Now it's something that should be bound to your target market. So not too wide and not too narrow. And critically it should not mention your company, your product, or anything solution related at all. Completely agnostic of those things.
(00:52:05):
And then the mission, that's the thing that you are going to relentlessly iterate on to take you incrementally closer to the nirvana state described in the vision. It should answer how you'll realize the vision by describing what your fundamental approach will be. In other words, what you will do and how you'll do it. It should ideally aim to encode any unique differentiating advantage you have. So if I think about Snyk at large when it comes to advantage, we might mention our unequal security intelligence and knowledge of application context.
(00:52:36):
And one of the neat things about this framework is if you find utility in doing so, you can apply it at every level from the company level all the way down to individual team. It doesn't mean the process is not difficult and you need to spend a lot of time, but it gives you this set of kind of a framework, a set of bounds that help you really come out with world crafted statements that kind of stand the test of time.
Lenny (00:53:00):
Is there an example you could share of the mission vision, whether it's Snyk or something else?
Ben Williams (00:53:03):
Yeah, yeah. I'll give you one for the growth group of Snyk. So great. The vision, every developer securely unleashes their creativity and the mission is to connect every developer and their organizations to the value of the Snyk platform with frictionless self-serve, adoption and expansion.
Lenny (00:53:19):
Interesting how the vision is so big beyond Snyk's current focus. And to your point, this kind of trickle down, right? There's a company vision and mission and it's the growth team's mission vision.
Ben Williams (00:53:32):
Yep.
Lenny (00:53:32):
Awesome.
Ben Williams (00:53:32):
Exactly.
Lenny (00:53:34):
I want to shift a bit and talk about your product work. So we've talked a lot about the growth org. I'm curious what the broader product org looks like. How many teams do you have? How do you structure it? Is it like product focused, user focused, outcome focused? And then just how does that team work with the growth team?
Ben Williams (00:53:53):
Sure. Happy to go into a bunch of that stuff. I know I'd mentioned earlier kind of three areas of building a growth team. I don't know if you want me to cover those other two. 'Cause we talked about-
Lenny (00:54:02):
Oh yeah, okay, let's do that. Let's finish that thread.
Ben Williams (00:54:05):
-Cool. So people and process was the first and we'll cover process really quickly. I think on the process side, at a minimum here you need well understood, documented growth processes, practices, working cadences. Teams in growth need to work differently in some ways from R and D teams working on core product, assuming otherwise, and just giving growth responsibility to an existing team without working with them to implement appropriate ways of working. I think it's a common track.
(00:54:31):
Ideally you get to a point there where the growth process is something that's continually refined and iterated on trying to build in more predictability. But what I've found I think most singularly most important in a growth process is facilitating a rapid learning cadence and providing the means to socialize those learnings, surfacing them in the right place at the right time so they can be leveraged and at the context. And if you think about experimentation, it's not about delivering outcomes it's about generating learnings that the organization can leverage effectively to deliver outcomes.
(00:55:05):
Might not be now, might not be tomorrow or some point in the future. But the sad reality is that without good process learnings easily end up unused and gathering dust. And you have to ask then what was the point? So as people in process and you know when that's on the right track, when you start to see enthusiastic sharing of learnings, when you see regular contribution of ideas coming from everyone in the form of well crafted hypotheses that are based on data and learnings. And when you see a wide variety of folks, just assuming end to end ownership of managing and running experiments instead of delegating that to the product manager or an engineer and tech lead. So yeah, that's people in process and strategy is-
Lenny (00:55:48):
Let me throw in a question real quick before we get to the last piece.
Ben Williams (00:55:50):
Sure.
Lenny (00:55:51):
So learnings, just to kind of touch on that. I've heard more and more pushback on the idea of learnings being an outcome. Because a lot of... As a leader, you're not going to be like, Cool, we learned so many things but nothing really got done. How do you think about the tension between, yeah, learnings we want to learn, but we also want to move metrics, grow the business and learnings are a way to inform decisions more than even just learn. How do you think about that kind of balance?
Ben Williams (00:56:17):
Ultimately you're there to create impact, right? There's no getting away from that, but learnings is the means. It's the same as, there's a quote that I love from [inaudible 00:56:27] around focus on the user's path to value not on monetization. Because if you focus on the form of the latter will follow, and that's the same thing with learnings and impact here. If you try and focus on the impact itself might struggle. If you focus on the things you need in terms of learnings to take you step by step, that will pave the path to creating impact.
Lenny (00:56:47):
I imagine your OKRs and goals are still like move this metrics some percentage, but you think of that as an output and the input is let's learn a bunch of stuff about what works and doesn't work and use that to inform what we're going to double down on.
Ben Williams (00:57:00):
Exactly. Yeah.
Lenny (00:57:00):
Sweet. Okay.
Ben Williams (00:57:02):
You got to focus on when you build a strategic opportunity, you are thinking about the outcomes, but you don't just go right to the end state. You've got to think about what's the quickest way we can test this hypothesis? And from there, what we learn from that and what do we take into the next set of the next set of experiments and it... You're paving this path along the way. You kind of that rough destination. How you get there, you don't know at the start. And that's what the path that the learnings take you on.

_[182 additional lines trimmed for context budget]_

---

### Making Meta | Andrew ‘Boz’ Bosworth (CTO)
**Guest:** Boz | **Date:** 2024-03-03 | [YouTube](https://www.youtube.com/watch?v=_XqDB2Upr3s)  

# Making Meta | Andrew ‘Boz’ Bosworth (CTO)

## Transcript

Lenny (00:00:00):
You were basically the 10th engineer at Facebook. I imagine there was a lot of pain and suffering that people don't often hear about.

Andrew ‘Boz’ Bosworth (00:00:07):
I didn't sleep for more than four hours at a time. I'd wake up every four hours and check the report and see if anyone was attacking the site. They don't tell you about that stuff in the movies.

Lenny (00:00:14):
You worked 120 hours per week., you had no hobbies.

Andrew ‘Boz’ Bosworth (00:00:17):
I don't want to take away from the romanticism of it. It's just that most often, we hear those romantic stories from the successes. It's a healthy thing for people to want to throw themselves into something and take that risk, but it is not glamorous at the time.

Lenny (00:00:29):
The newsfeed. That was one of your early projects at Facebook. People did not want it. They were wrong, clearly.

Andrew ‘Boz’ Bosworth (00:00:33):
Now, newsfeed was an easier case than people suspect. Everyone was outraged at the same time as they immediately doubled their usage of the product.

Lenny (00:00:40):
In terms of the economic utility, the Venn diagram of Boz, of newsfeed and ads created $1 trillion of value.

(00:00:48):
Today, my guest is Andrew Bosworth, or Boz, as most people know him. Boz is the chief technology officer of Meta. He joined what was then called Facebook in early 2006 as one of the first engineers, and during his 18-year tenure at Meta, he created some of the most impactful and important products in internet history, including the Facebook newsfeed, which was the first ever algorithmically ranked content feed of any social network, and is basically what people think of as Facebook today.

(00:01:17):
He also built the original Facebook mobile ads platform, which he then ran for another four years. He also helped build and scale the Facebook messaging system, the profile, the timeline, Facebook groups, and even the internal engineering boot camp. Most recently, he served as VP of ads and business platform, where he led engineering product, research, analytics, and design. And in 2017, he created the company's AR/VR organization, now called Reality Labs.

(00:01:42):
These days, Andrew leads Meta's efforts in AR, VR and mixed reality, along with consumer hardware across Quest, Ray-Ban, Meta smart glasses, and more.

(00:01:52):
In our wide-ranging conversation, we touch on so many important lessons and stories, what it was really like in the early days of Facebook, why you should be asking your manager for help more often, why communication is the job. Lessons from Meta's turnaround over the past couple of years, Boz's thoughts on the Apple Vision Pro, a bunch of leadership and career advice, what it was like to build the very first newsfeed, and lessons from that experience, and stories of failure and stories of success, and so much more.

(00:02:22):
If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. It's the best way to avoid missing future episodes, and it helps the podcast tremendously.

(00:02:32):
With that, I bring you Andrew Bosworth, a.k.a. Boz, after a short word from our sponsors.

(00:02:39):
This episode is brought to you by Vanta. When it comes to ensuring your company has top-notch security practices, things get complicated fast. Now you can assess risk, secure the trust of your customers, and automate compliance for SOC 2, ISO-27001, HIPAA and more, with a single platform, Vanta. Vanta's market-leading trust management platform helps you continuously monitor compliance, alongside reporting and tracking risks. Plus, you can save hours by completing security questionnaires with Vanta AI. Join thousands of global companies that use Vanta to automate evidence collection, unify risk management, and streamline security reviews. Get $1,000 off Vanta when you go to vanta.com/lenny. That's Vanta.com/lenny. This episode is brought to you by Eppo. Eppo is a next-generation, A-B testing and feature management platform, built by alums of Airbnb and Snowflake for modern growth teams. Companies like Twitch, Miro, ClickUp and DraftKings rely on Eppo to power their experiments. Experimentation is increasingly essential for driving growth and for understanding the performance of new features, and Eppo helps you increase experimentation velocity while unlocking rigorous deep analysis in a way that no other commercial tool does. When I was at Airbnb, one of the things that I loved most was our experimentation platform where I could set up experiments easily, troubleshoot issues, and analyze performance, all on my own. Eppo does all that and more with advanced statistical methods that can help you shave weeks off experiment time, an accessible UI for diving deeper into performance, and out-of-the-box reporting that helps you avoid annoying prolonged analytic cycles. Eppo also makes it easy for you to share experiment insights with your team, sparking new ideas for the A-B testing flywheel. Eppo powers experimentation across every use case, including product, growth, machine learning, monetization, and email marketing. Check out Eppo at geteppo.com/lenny, and 10x your experiment velocity. That's geteppo.com/lenny.

(00:04:47):
Boz, thank you so much for being here. Welcome to the podcast.

Andrew ‘Boz’ Bosworth (00:04:55):
Thanks for having me. I've been a long-time fan of your program and all the things that you've been putting out, so I'm glad to finally get a chance to join.

Lenny (00:05:01):
Same. I'm really excited to have you here. I have at least a billion questions I want to ask you. But I want to start with a few fun facts that I've found about you, and what if I go through them and then just pick one that stands out, and then tell the story behind it? How does that sound?

Andrew ‘Boz’ Bosworth (00:05:17):
All right, sounds good.

Lenny (00:05:18):
Okay. You went to 14 proms.

Andrew ‘Boz’ Bosworth (00:05:22):
Yeah. It's true.

Lenny (00:05:22):
Okay, I'm going to keep going. Okay.

Andrew ‘Boz’ Bosworth (00:05:25):
Wow, that's a strong opener.

Lenny (00:05:27):
That might be the one. You were a national Taekwondo champion in college. You were Mark Zuckerberg's TA in college in a class on AI, which isn't actually how you landed at Facebook, from my understanding. Harvard was recruiting you to play football for them. You were very active in the 4-H Club, and you raised animals and showed them at county fairs when you were growing up. You once shared a stage with David Copperfield.

Andrew ‘Boz’ Bosworth (00:05:52):
That's true.

Lenny (00:05:52):
MC Hammer once told you that your outfit was stylish. And president George W. Bush complimented you on your shoes and the shine of your head.

Andrew ‘Boz’ Bosworth (00:06:03):
Yeah, these are all true. I want to say, wow. First of all, I got to make sure that people understand, I was a national collegiate champion, in as a green belt, which that's like being the JV champion. Just so everyone's clear on what that is.

Lenny (00:06:15):
W's a W.

Andrew ‘Boz’ Bosworth (00:06:16):
Heavyweight sparring. I'll tell... The prom story is a funny one. It's related to the 4-H story. I was a big-time 4-H'er, National 4-H Hall of Fame, did all this stuff there.

(00:06:29):
As a comeup to that, 4-H is a wonderful program, youth program, it's coed program, and I was all over the state, all over the country, doing leadership events and doing these conferences, and doing a lot of public speaking.

(00:06:39):
And almost every 4-H event has a dance. People don't know that. At the end of a conference, at the end of the, literally camp, you'd go camping for a week, at the end there's a dance.

(00:06:49):
And so, as a consequence, the most important thing, if wanted to go to a lot of proms, I was a good dancer. And it turns out, the high-level bit, at least in the 1990s, for girls selecting who they might want to go to prom with was, will he and can he dance? And the answer with me was yes. And combine that with the fact that I knew a bunch of girls who went to different schools, that's the recipe for success right there, if that's the goal that somebody has. Two my junior year and 12 my senior year. I once went to three in one weekend, a Friday, a Saturday, and a Sunday night.

Lenny (00:07:21):
Another fun fact about you is you were basically the 10th engineer at Facebook, initially, way before it was a clear success story. I imagine there was a lot of pain and suffering and struggle that people don't often hear about those early days. They see a movie like The Social Network. It looks like, "Oh, that was so much fun. I've got to start a company. It's going to become a trillion-dollar success story." I'm curious just what those early days were like. Are there memories that stand out to you?

Andrew ‘Boz’ Bosworth (00:07:47):
Yeah, there's a bit of a joke in the 10th thing, which is me and five other guys all joined at the same time, and there was nine engineers before us. We joined the same day, so we're all the 10th engineer. So, somewhere between 10 and 16, depending on how you want to do the numeration on that.

(00:07:59):
I've written about this in my blog, and I tell this story a lot, which is it was fun, and there was tremendous camaraderie and memories that were formed, but they were formed in a kind of forge of really intense times.

(00:08:13):
At that time, almost all of us lived within one mile of the office. We ate most of our meals together because we were working, not to say we weren't also friends, but because we were working, it's like, oh cool, you just roll into a meal and roll back into work.

(00:08:26):
And there's little things that you don't appreciate, which is like there was nobody to help you. There was no expert. And so, it wasn't like, "Hey, I'm struggling with this one tricky problem. Who should I talk to?" It's like, nobody. You should talk to yourself and figure this out. Or it's like, "Oh, man. My servers are out of capacity." It's like, "Cool. You should go to Fry's Electronics, you should buy a bunch of components, you should build a new server, and then you should run it. Maybe drive into the colo, rack it, and then get back and run it."

(00:08:52):
People really undervalue the fact that when you go to work, even a moderate mid-size corporation today, especially with the tremendous growth of startups supporting startups, things like payroll and finance and IT and HR, these things are professionally handled in many cases.

(00:09:10):
That was just not the case in the early 2000s. It was just you, and your personal car, and whatever you wanted to do with your time.

(00:09:18):
So, I don't want to take away from the romanticism of it, it's just that it's most often we hear those romantic stories from the successes. We so rarely hear somebody who went through really sacrificing a lot of my 20s from any kind of social or outgoing, fun environment.

(00:09:37):
It paid off for me, so no one feels bad for me, nor should they. But there are other people who do the exact same thing, maybe they worked harder, maybe they were smarter, maybe they did better, and it didn't play out for them. And it's a big sacrifice.

(00:09:48):
And so, I love the enthusiasm for startups, I love startup culture. I think it's a healthy thing for people to want to throw themselves into something and take that risk. But it is not glamorous at the time. In retrospect, it's like, "Oh, it can be..." We have a little halo around it. But at the time, it doesn't feel glamorous.

Lenny (00:10:06):
Yeah. In this post you mentioned, you said that you worked 120 hours per week.

Andrew ‘Boz’ Bosworth (00:10:07):
Yeah.

Lenny (00:10:10):
You had no hobbies, and you gained a lot of weight.

Andrew ‘Boz’ Bosworth (00:10:15):
Yeah. We drank a lot to make up for it, so I gained a lot of... And you weren't eating healthy. It was crazy.

(00:10:22):
I think I've told this before. There was a time where one of the first things I built was an anti-spam, kind of anti-scraping defense mechanism. But we didn't have any ops support. There was no 24/7 online support.

(00:10:35):
So, I built this tool. I had to wake up every four hours. For about two years, I didn't sleep for more than four hours at a time. I had to wake up every four hours and check the report, and to see if anyone was attacking the site. And if they were, I was up, and I had to go battle back. And if they weren't, cool, I'd go back to sleep. But that's the thing, they don't tell you about that stuff in the movies.

Lenny (00:10:55):
That's almost worse than having a kid, a newborn.

Andrew ‘Boz’ Bosworth (00:10:59):
And nobody asked me to do it. Nobody even asked me to do the anti-spam, anti-scraping stuff. I just thought it was a problem, and I went and did that, and that was the solution I come with. If I was a better engineer, maybe I'd have solved a better problem.

Lenny (00:11:11):
So, maybe just to close out that thread, when you talk to founders, what advice do you give them along these lines?

Andrew ‘Boz’ Bosworth (00:11:18):
I want to be cautious about this, because what I tell founders... The first thing I tell founders is that I've never been a founder, and I want to recognize the difference. I joined January 9th, 2006. That's almost two years after Mark started the company. I wasn't involved with fundraising, I didn't have to do any of that side of the things, and I didn't even have to deal with the board or the business side of things. I really was lucky, in a way, to have joined when I did.

(00:11:42):
But the first thing I tell founders is like, "You should take my advice with a grain of salt. I have not actually been in your shoes."

(00:11:47):
If I can compliment you, really, one of the things I like about your program is, there's a whole system of professionals in our industry. And when I grew up in technology in the valley, you always heard about the ACM, right? The Association of Computing Machinery. You heard of these legendary professional organizations that supported people in our fields.

(00:12:09):
And by the nature of the rapid pace of change in the technology, and the nature of the engagement of those institutions, even academics, even academia broadly, kind of are out of touch. The tools that you got from those places weren't useful in our field.

(00:12:23):
So, I do think the mentorship that we give each other has been a critical and sustaining resource. There is, today, now, resources like your podcasts and your newsletter that are actually really designed to help people who are professionals in our industry in a way that is almost kind of missing for 15, 20 years, and I love to see that. Because if you're an up-and-coming [inaudible 00:12:45], literally you used to have to know somebody and ask them a question.

(00:12:48):
And so, a lot of times what I'm helping founders with, I can help them with the strategy, I can help them think through the technology choices, I can help through business, I can think through the management, the organization structure. But I also try to be very clear, there's a bunch of stuff that I just was never exposed to.

(00:13:00):
So, even as we just talk about how tough it was for the average engineer joining Facebook in 2006, man, it was even tougher for Mark Zuckerberg in 2004, probably. And that's a story that's been told, I'm sure, but still. So, I think these are both... It's almost all scale and variant. No matter how far you dial back, the challenges are interesting and are worth talking about.

Lenny (00:13:22):
One of maybe your most popular posts is this quote that you share about the advice you often give. What you say is, "The advice I find I have to give more frequently than any other in my career, as a manager, a board member, an advisor and a friend, is for people to more directly leverage their leaders." Can you talk about that and what that means, and what that looks like?

Andrew ‘Boz’ Bosworth (00:13:40):
It's such a normal and natural healthy thing. And by the way, we do it in our personal relationships. Like I said in the post, we want to do it ourselves. We want to do it ourselves to prove to everyone that we can do it ourselves.

(00:13:52):
And we think in our heads, "If I ask for help, haven't I already given up that goal? Haven't I just admitted defeat on one of my top level goals, which is to demonstrate that I can do it myself?"

(00:14:04):
But what so often we forget is, more often than not, your job is not to do it yourself. Your job is to get it done, is to have the thing done, done well, done right, done competently. And a lot of times, the tools that you need to do that live with your manager, with your partner, with your advisor, with your mentor. That's where they live.

(00:14:25):
So, how many times as a manager have I gone through, and somebody's told them, "Here's the job." They're like, "I got it." They go off, they come back, it's done, it's wrong. And I'm not blaming them for it being wrong. They didn't check in with me. They misunderstood. We miscommunicated. I'll take the L on that. That's no problem.

(00:14:42):
But here we are, six months later, it's not done right because they misunderstood the brief. We miscommunicated with the brief.

(00:14:49):
Or they come back, and it took a year. And I'm like, "Why did this take a year instead of six months?" And they're like, "Oh, man. I had all these things I had to deal with." Where, if they had emailed me, I could have bulldozed that stuff. I could have cleared the path. I could have said, " Oh, no, no, no. Don't worry about that. This is the thing." And then we'd have been done six months sooner, and they would've been less frustrated. And so, light touches.

(00:15:09):
Now, I do think as a manager we also have a job to say, "Hey, that's kind of the work, so you got to kind of go figure that out." And one of my things I always tell my managers, one of the most powerful things we do is refuse to rule. Someone will bring me a thing. A lot of times we feel obligated to weigh in and help. I'll be like, "Nope, but look, I think you've got it. I think the challenges you're facing are the right challenges. I think you're approaching it in the right way. Just do your best there." And that's what it is. And so, there is a responsibility as well for those of us who are leaders, mentors, advisors, board members to do that.

(00:15:39):
But, by the way, we do this... Personal relationships. You're with your partner, and you're trying to do something the right way, but you're not talking to them about it. You're just taking a huge risk there, and for very little reward. They're not going to be mad if you ask them, like, "Hey, is this how you wanted it done? I don't know."

(00:15:56):
And so, I do think it's kind of funny how much we build these castles in our mind, these little silos that keep us from engaging the structures that are built around us, that are designed to help us succeed. I saw this great quote, actually just yesterday. I saw Patrick Stewart, who is one of my favorite actors of all time, and whose characters I love, and he talked about people going on casting calls. And this is a brutal thing for actors, right? You're going on 30, 40 things, you're getting rejected. It's tough. Everyone's kind of heard about this. And he said, "No one wants you to succeed more than the person you are auditioning for, because they want you to be awesome. Because as soon as you are awesome, they're done. They want you to be amazing."

(00:16:37):
That's like your manager. Nobody wants you to be more awesome than your manager does, because when you're amazing, your manager, his life gets easier, her life gets easier. So, I just think that's the mentality we get into is like, "No, no, no. They're testing me." They're not. They are rooting for you. I promise you that.

Lenny (00:16:53):
I love that advice. I imagine the reason people don't do this, as you said, is they don't want their managers to think they don't know what they're doing, or they can't solve it. Do you have any advice and guidance for when it makes sense to go reach out and ask?

Andrew ‘Boz’ Bosworth (00:17:06):
One of the things I think, for people who are timid about this especially, is I think you can put a framing around it that's really easy for your manager to engage with. You can say, "Hey, I'm making progress on this. This is what I'm blocked on, this is the current program." And I'll even say, "Hey, if this all looks good to you, no response required. If there is something here that you want me to do better, different, that you think you could help with, let me know."

(00:17:32):
I love a typed, five-, 10-sentence email, "No response required. Here's where things are." Even if everything is going really well, I'm like, cool, this person understands the urgency, they understand the assignment, and they're giving me a little heartbeat, a little ping back.

(00:17:53):
And then also, if two weeks later, let's say the blocking issue is bad, then you say, "Hey, I am sorry, but I do actually need your help now. I'm actually blocked on this thing." I have the context. I have a mental model of you toiling away on the right thing, on the thing I asked you to do over there. Even then, when you're blocked, you can make my life super easy. Like, "Hey, what I'd love for you to do, if you could send an email to this person, here's a draft with this thought, that would help."

(00:18:23):
Or it's like, here are specific questions framed up. "I think this is what you want. Is this right? Yes or no? If no, okay, we'll come back and we'll spend more time. If yes, we're all good." So now, not only am I up to speed, I have a mental model, I'm engaged. Also, you've made it super cheap for me to help you. And people are always surprised. People who work for me are always surprised when I tell them how big a part of my job is doing these little types of things.

(00:18:53):
It's a little spinning plates at my scale. I've got 10,000 or 15,000 employees, depending on how you want to count different things. And so, you're just like, every now and then I got to get a whole new plate, a whole new rod, and just really put the effort into it. But for the most part, I'm just trying to touch everything and keep the momentum going. And so, if something falls, and somebody didn't tell me that "Hey, we're losing rotational velocity here. We're losing momentum." Oh, I'm bummed. I'm like, "Ah, now that plate fell. I got to start a whole new thing over here now."

(00:19:22):
So, I think people underestimate. They think of my job differently than my job actually... My job is actually tons of little touches.

Lenny (00:19:29):
So, I think a key takeaway here is, one, index more towards asking your manager and leaders for help. And I love this way of framing it of, it doesn't always need to be like, "Here's what I need from you." It's, "Here's what's happening. Here's things that might be blocking me. Here's questions I have. Here's things that are going on."

(00:19:44):
This is actually similar to something I found really powerful that I'll share real quickly, this idea of a state of... I call it the State of Lenny email. And I sent this email to my manager every week. The State of Lenny. It's kind of like State of the Union. And it's, "Here's my current priorities, here's what's on my mind broadly, and then here's blockers that I need your help with.

Andrew ‘Boz’ Bosworth (00:20:02):
We actually used to have a format for that we called HPMs. Highlight, people, me. And every manager at Facebook from like 2008 to like 2014 would send to their manager, or even their leadership group. I mean, at one point when I was running what we called comm apps, I just sent it to Zuck and the whole leadership group.

(00:20:24):
It's like, what's the highlights include? And it highlights [inaudible 00:20:27] flow. What's the big ticket things you need to know? Where are people? Like is somebody in trouble? Is somebody at risk? Is somebody doing really amazing work that needs a shout-out? And then me, how are you personally doing? HPMs, we called them.

(00:20:39):
Actually, it's funny. I hadn't thought about that in a long time. But yeah, no, I think this kind of thing can work. And look, every manager is different, so even at the Meta level, by the way, is another success. I think what people do is they want to treat every manager the same, and that's not going to work because every manager is different.

(00:20:54):
But every manager, you can ask, "How do you like to get updates?" You can ask them when you first start working with them. Like, "Hey, what's your cadence? How do you like to stay informed?" And so, for me, I do regular one-on-ones. As the org's has gotten bigger, those have gotten more distant, so people have replaced those with more written things.

(00:21:11):
But no manager will get pissed at you if you're like, "How do you like to get information about me?" That's a totally reasonable thing to ask.

Lenny (00:21:18):
I love the specific idea you shared of just drafting the email to say the other team leader, "Here's what I need you to tell them. That would really unblock this thing." And that's such a cool idea.

Andrew ‘Boz’ Bosworth (00:21:27):
By the way, I always put my own... I don't take that copy paste it. I'm always looking at that and be like, "Okay, I understand." A lot of it is actually not about what you want the other person to hear, it's about the voice, the tone.

(00:21:41):
It includes a lot of history. I don't know. Have you been going back and forth with them for 12 rounds, and this is going to feel to them like I'm really coming over the top? Or is this like, "Hey, first time you're hearing about this, my bad. Here's what we're doing. Need your help."

(00:21:54):
So, a lot of that isn't even about making my life easy because I want to copy paste. A lot of it is, actually, there's a rich set of information in how you tone and how you draft that note that's going to help me land it correctly and not feel like I'm just out of band, heavy coming in.

Lenny (00:22:11):
This touches on something that I often hear is very core to the way Meta works, which is transparency. Anyone can ask Zuck questions at the Q&A's. People are encouraged to post constantly internally of what they're thinking, what they're working on. All the data is shared publicly. Which often leads to leaks, which I hear you hate, and that is a pet peeve of yours.

Andrew ‘Boz’ Bosworth (00:22:32):
Just feels like a violation of the team trust. Just feels like... I grew up with playing sports, right? I was football, soccer, track. And you just can't imagine one of your guys calling out the play to the other team. Can you imagine what you would do in that case? "You're off the team. I'm sorry, you can't be here." Anyways, sorry. Carry on.

Lenny (00:22:48):
Yeah, and there's so many more people, it's hard to find. Who is this? So, with this downside as an example, and I imagine there's other downsides also takes a lot of work, and it puts people on the spot a lot of times, what have you seen as benefits and why is that such a big part of Meta's way of working?

Andrew ‘Boz’ Bosworth (00:23:05):
Yeah. This kind of comes back to, I think, the principle that really good, talented people, you want to leverage them fully. You really want to make sure that they are fully leveraged. And so, anytime they have the wrong information, or they don't have the information, you've now blocked one of the economically most valuable things that your company possesses, which is this person's time, attention, talent. Not only that, you've also made them more frustrated, and now they are more likely to leave.

(00:23:35):
If the lifeblood of any company are the people inside of it who collectively commit to some kind of a goal and a mission and work together, then you want to maximize that potential. And creating this really open information ecosystem is one of the ways that we do that. So often, great, phenomenal work that has happened at our company has not come from this one top-down mandate, but has come from people understanding not just what we're trying to accomplish top down, but also having way more information at their disposal to be able to act on it.

(00:24:16):
People talk about top-down or bottoms-up culture, and it's a bit of a myth, in my opinion. If you've ever met Mark Zuckerberg, it's not a bottoms-up thing. The ideas that we're pursuing are Mark Zuckerberg's ideas, first and foremost. That's not to say that he's not open to new ones, and of course he is, and that's a form of bottom-up, people can bring ideas to him and he internalizes them and acts them or not. But when he brings things top-down, he's not micromanaging, he's in the details. I'll be careful on that.

(00:24:44):
But he does create the space for you to bring back three or four versions of the thing that he's talking about, and then he shapes it from there. And you can't do that if there's... If you don't have degrees of freedom, sure, but also if you don't have the information. Otherwise, if you don't have the information available, what we're trying to accomplish, why we're trying to do it, what the infrastructure is like, what the availability is like, what the performance is going to be like, well, you just are stuck. You're just going to have to follow the script. That's very boring for high-talent, high-creativity, high-engaged people.

(00:25:15):
Now, it does come at a tremendous price. You have to get really good at managing information on the incoming. Most people at most companies consume all the information that's given to them, but the information itself is carefully managed. They're getting all the information they're intended to get.

(00:25:32):
We've turned that on its head, and it sounds great, but it's not free. Even somebody senior coming from outside of the company to the company, one of the things I have to coach them on is, how do you find signal amongst all the noise?

(00:25:45):
You have to have a system for managing your information. You have to have a system for triaging the incoming, getting rid of a bunch of stuff that is on the wrong channel, or it doesn't matter to you, figuring out what's the... groups that you want to be a part of, but you consume only when you choose to and-

Andrew ‘Boz’ Bosworth (00:26:00):
... groups that you want to be a part of but you consume only when you choose to. And where are the things where you're getting push notice? Like that's the real time thing, and that takes some time.

Lenny (00:26:08):
This point you made about bottom up versus top down is really interesting, because, when I think of Meta, I think it's a very bottom up culture. I hear everyone comes up with their ideas, runs experiments, is very encouraged to just try stuff, and it's really interesting to hear that. And it makes a lot of sense that most of the big ideas actually do come from the top.

Andrew ‘Boz’ Bosworth (00:26:26):
It's of these mythology things. I don't think it's the wrong... As a contract, it's more bottoms up than many other companies, because you do have these degrees of freedom within the construct. But make no mistake, like Mark or me or Chris Cox or Javi, they have very strong opinions about what we should be doing as a company, and your bottoms up-ness works within that framework. But it is true that you can ask Mark any question, and he's going to answer it. Same with me, same with Chris, same with Javi and also that we certainly take inspiration from the discussion that we have with employees. So I don't know, it's just not as black and white as people tend to paint it.

_[612 additional lines trimmed for context budget]_

---

### Lessons from scaling Uber and Opendoor | Brian Tolkin (Head of Product at Opendoor, ex-Uber)
**Guest:** Brian Tolkin | **Date:** 2024-08-04 | [YouTube](https://www.youtube.com/watch?v=sRukk520Fds)  

# Lessons from scaling Uber and Opendoor | Brian Tolkin (Head of Product at Opendoor, ex-Uber)

## Transcript

Lenny Rachitsky (00:00:00):
You've worked at two businesses that have done incredibly well combining product in ops.

Brian Tolkin (00:00:03):
Uber always has this mentality and Opendoor does two of the product operations, twin turbine jet plane where you can fly the plane on one engine for a little bit if you need to, but it's operating most efficiently and effectively if both are working together.

Lenny Rachitsky (00:00:17):
What has having been in ops done to make you a better product leader?

Brian Tolkin (00:00:21):
Gave a really deep understanding of how the business actually works. It's a pretty good foundation for them going on to say, okay, what do we actually want to build in a more scalable technology way.

Lenny Rachitsky (00:00:31):
Something else I've heard that you're very good at is staying very calm under pressure.

Brian Tolkin (00:00:34):
I've slept on the floor in China before launching uberPOOL, and when you reflect the stress onto your teams, everybody tenses out. It counterintuitively doesn't produce better outcomes.

Lenny Rachitsky (00:00:51):
Today my guest is Brian Tolkin. Brian is currently head of product and design at Opendoor. Before that, he spent nearly five years at Uber where he joined as employee 100. Before Uber had UberX or uberPOOL or any shared rides, he actually started on the ops team at Uber, moved into product, ended up leading product and launch of uberPOOL, and then taking it global. He also started the product operations function at Uber. Before that function was really even a thing, which I didn't know until the chat that we had. In our conversation, Brian shares a ton of lessons about building products with a heavy operational component. Also, how to run great product reviews, how he implements the jobs to be done, framework and Opendoor's successfully.

(00:01:32):
The story behind Zillow trying to compete with Opendoor failing and then partnering instead. Plus a ton of great stories from the early days of Uber and Opendoor, and so much more. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. It's the best way to avoid missing feature episodes and it helps the podcast tremendously. With that, I bring you Brian Tolkin. Brian, thank you so much for being here and welcome to the podcast.

Brian Tolkin (00:02:00):
Thank you, appreciate it. Thanks for having me.

Lenny Rachitsky (00:02:02):
First of all, just a huge thank you to Kayvon Beykpour for connecting us, introducing us. He said all kinds of amazingly nice things about you. He also gave me some very hard questions to ask you. I hope you've come prepared.

Brian Tolkin (00:02:12):
Terrific. Put me in my hot seat.

Lenny Rachitsky (00:02:14):
Okay, I want to spend a bunch of time talking about product and ops. You started your career in operations. At Uber you actually started on the ops team and you moved into product. You've also worked at both Uber and at Opendoor, which have both huge operational components. I think it's really rare that people, one, see a company scale to the heights of Uber and Opendoor with such a heavy operational component that are still tech companies and also it's really where someone starts an ops and then moves into product and ends up where you are, where your chief product officer, really successful company. So I have a bunch of questions here. Maybe the first is just what has having been in ops done to make you a better product leader? How does that change the way that you operate as a product leader?

Brian Tolkin (00:02:58):
Starting on the operations side gave a really deep understanding of how the business actually works. You are truly operating it day in and day out and the success of the city is in large part driven by the inputs that you are putting into it every single day on the ground and whether or not there was rain that weekend, which was a nice driver of metrics, but talking to customers every single day like one-on-one onboarding drivers responding to support tickets, there's no centralized support team, there was no closer to the customer, right? And so I think that foundation actually for really understanding what moves the business and being super close to the customer actually is a pretty good foundation for them going on to say, okay, what do we actually want to build in a more scalable technology way?

Lenny Rachitsky (00:03:52):
This episode is brought to you by Pendo, the only all-in-one product experience platform for any type of application. Tired of bouncing around multiple tools to uncover what's really happening inside your product? With all the tools you need in one simple to use platform, Pendo makes it easy to answer critical questions about how users are engaging with your product and then turn those insights into action. Also, you can get your users to do what you actually want them to do. First, Pendo is built around product analytics, seeing what your users are actually doing in your apps so that you can optimize their experience. Next, Pendo lets you deploy in-app guides that lead users through the actions that matter most.

(00:04:31):
Then Pendo integrates user feedback so that you can capture and analyze what people actually want. And the new thing in Pendo, session replays. A very cool way to visualize user sessions. I'm not surprised at all that over 10,000 companies use it today. Visit pendo.io/lenny to create your free Pendo account today and start building better experiences across every corner of your product. PS, you want to take your product led knowhow a step further? Check out Pendo's lineup of free certification courses led by talk product experts and designed to help you grow and advance in your career. Learn more and experience the power of the Pendo platform today at pendo.io/lenny.

MUSIC (00:05:09):
Pendo.

Lenny Rachitsky (00:05:15):
This episode is brought to you by Explo, a game changer for customer facing analytics and data reporting. Are your users craving more dashboards, reports and analytics within your product? Are you tired of trying to build it yourself? As a product leader, you probably have these requests in your roadmap, but the struggle to prioritize them is real. Building analytics from scratch can be time-consuming, expensive, and a really challenging process. Enter Explo. Explo is a fully white labeled embedded analytics solution designed entirely with your user in mind. Getting started is easy. Explo connects to any relational database or warehouse and with its low-code functionality, you can build and style dashboards in. Once you're ready, simply embed the dashboard or report into your application with a tiny code snippet. The best part, your end users can use Explo's AI features for their own report and dashboard generation eliminating customer data requests for your support team. Build and embed a fully white labeled analytics experience in days.

(00:06:18):
Try it for free at explo.co/lenny. That's E-X-P-L-O/lenny. I've seen that a lot of companies, and this was definitely true to Airbnb, where the product team looks down a little bit on the ops team where they're like, "oh, we're doing things that are going to scale to millions of users. We're doing these things that are going to apply to everyone." There's this ops team over there doing a few things that are going to not scale. They keep asking us for things to build for their one-off ideas. What do you think that product teams often maybe miss or don't understand about the ops teams that would help them see them in a different light?

Brian Tolkin (00:06:56):
Yeah, it's a great question and I think Uber always had this mentality and OpenDoor does too of like a twin turbine jet plane where you can fly the plane on one engine for a little bit if you need to, but it's operating most efficiently and effectively if both are working together, and I think that's really true, right? The reality is operations teams, local teams, can iterate faster, can scale talking to customers really much more efficiently, have great qualitative insights, and so if it's seen more as a harmony instead of a competition, I think that's really, really helpful where it's like, okay, how do we get the insights that are happening day in and day out in the field, on the ground, whatever that may be, and help us build better products because of that, right?

(00:07:50):
Like a PM sitting in San Francisco can't be in Opendoor's case 50 markets, walking houses every single day in Uber's case, whatever, a thousand cities understanding the nuances of safety in South America and it's just not possible, but what you can do is foster a really good relationship and a really good feedback loop of how people who do deeply understand those things can help give insights. Now is actually the birth of product operations was that insight as well.

Lenny Rachitsky (00:08:22):
Can you say more on that?

Brian Tolkin (00:08:23):
Yeah, sure. So, sorry, I should probably define what product operations was. At Uber it was basically this notion that we had centralized, this was later in my career at Uber, but we had a centralized product team building stuff mostly in San Francisco, not strictly through the Ross, but at this point around the world, but mostly in San Francisco and then we had a very globally distributed operations team, and there was a bidirectional feedback loop that wasn't super strong and that feedback loop was basically when the EPD teams in San Francisco built new features, how do we effectively put it in global markets and then how do we effectively get input from global markets to better build features. And so one solution to that problem, our solution at the time was to start up a new function called product operations who had accountability and reported into operations but physically sat with and operated much like a member of the product team to help solve that.

Lenny Rachitsky (00:09:23):
Is that maybe the first time there's a... Did you invent product operations as a function?

Brian Tolkin (00:09:28):
I don't think so because at the time, I believe Google had a function, I can't remember what Google called it was something slightly different, but I met with a few folks who had been in similar type roles at Google and a couple other places, so I don't take credit for certainly for inventing IT and other people have actually dabbled in this model at Uber before me there was just a formalization of it and our actual building out of the organization, et cetera.

Lenny Rachitsky (00:09:54):
Did none of that. Sounds like you basically helped make it a thing. I know you're being very modest, I think. Coming back to your point about decentralized operations teams, something I've read is that search pricing came out of one GM and a market just testing, emailing all the drivers, hey, we're going to give you extra if you drive on Saturday night. Is that true?

Brian Tolkin (00:10:15):
That would've been probably a little bit before my time, but that being said, one thing that is true is that surge pricing for actually quite sometimes all of 2012, certainly 2013 probably, I don't know when we necessarily switched, was very much a human in the loop system or a very manual system where GMs in every city would control basically the parameters in which surge would operate and so much of the time that would need, for example, Monday through Friday, there would be no search, it couldn't flip on, and then Friday nights and Saturday nights it would flip on from whatever you set, 7:00 PM to 3:00 AM and the cap was X, whatever the cap was. And then within those parameters the algorithm would optimize for what the price was. But yeah, GMs controlled whether it was on or off and what geographies were surging.

Lenny Rachitsky (00:11:16):
Wow, I didn't know that. Was that out of we believe we are better than the algorithms or we just don't have time to make them amazing yet, so we're just going to help them along?

Brian Tolkin (00:11:25):
Yeah, I think it was probably a function of a bunch of stuff, one of which is like, hey, this is a fairly new concept and it's powerful and dangerous and so let's make sure we understand what's happening. The second is this belief that local city teams know their cities best and so you might know that an event is happening, a baseball game gets out and it's like, oh, I know that this baseball game's going to get out at 10:00 PM so I'm going to set surge at 9:45 and the algorithm may not be able to pick that up. And then the third is the technical constraint of nowadays clearly it's all automated, but it's really hard to build a fully dynamic, always on geospatially aware pricing system and not just a little bit of time.

Lenny Rachitsky (00:12:17):
That makes sense. I feel like you're full of wild stories from your time at Uber. Is there one that comes to mind of just, I think you helped scale in China, uberPOOL?

Brian Tolkin (00:12:17):
Yeah.

Lenny Rachitsky (00:12:29):
Maybe that's the one. I don't know. Can you share wild story from early Uber days?

Brian Tolkin (00:12:31):
Yeah, so in the early days of Uber, one fun story is obviously UberX is a random mainstream product but has a funny, silly name, UberX. This product in the early days was going to be all hybrid and had a bunch of different potential names. I was not personally driving this, this was someone else on the operations team, but they built the model for what this product could be and there's no name for it yet, so it was going to be a placeholder. So what do you put in some placeholder? X. So UberX and then the company was moving quickly enough, the product got the green light, it launched, and here we are, I don't know, 12 years later, 11 years later, whatever it is and UberX is the name that stuck.

Lenny Rachitsky (00:13:21):
That is hilarious. I love it. So it was a placeholder. It's like many products start that way where they're like, this is just the temporary name, and they're like, okay, I guess everyone just knows it this way now we're going to stick with it.

Brian Tolkin (00:13:31):
Exactly. It's too expensive to change and rebrand at this point.

Lenny Rachitsky (00:13:34):
That's an awesome story.

Brian Tolkin (00:13:36):
One that is good about scaling Uber uberPOOL in China is we were launching Uber pool in China and this was going to be, China at the time was pretty big for Uber, but uberPOOL was not there yet, and so we were going to launch. And myself and a few other folks were in Chengdu China, which is the first Chinese market that we were launching uberPOOL in and we were going to be on the ground took to launch. We wanted to go live at, I believe it was 6:00 AM for rush hour on, I don't remember the day, but whatever, Monday morning, and so we're there over the weekend getting ready to set up and at the same time we were doing some data center testing. And so we flipped on all the testing infrastructure and thought it was going to work and nothing works, and the matching algorithm just isn't working and we're like, oh my god, now it's whatever, 5:00 PM the day before we're supposed to go live, 6:00 PM, 7:00 PM okay, let's get on the phone with the US, try and figure out what's going on.

(00:14:43):
I remember I slept about 30 minutes that night between 2:00 and 3:00 AM being like, okay, well, we have to go live at 6:00 AM I think there was some press around it. We were planning on going live and I think we got everything finally working at probably about five 30 or six in the morning and launched just in the nick of time. And I'll never forget, we launched, it was great, we monitored, everything was good, and then we walked out for breakfast at 7:30 in the morning. Everyone sleep depressed, no one slept all night and we got these pancakes street food things and I have to imagine they were not that good, but in my mind it was the best meal I've ever had in my life.

Lenny Rachitsky (00:15:25):
It's like a meal after a marathon or a big hike.

Brian Tolkin (00:15:31):
Exactly. Yeah, exactly.

Lenny Rachitsky (00:15:32):
Everything's so delicious. This comes up a lot of just these moments that are so incredibly stressful and hard and leap deprived end up being the best memories and the best stories to tell and things you look back at fondly. It's so weird how human nature is like that.

Brian Tolkin (00:15:46):
Yeah, I mean another one more recent for Opendoor was when COVID hit, physically we buy and sell homes, and so we were physically going into people's homes and suddenly March 2020 going into people's homes was not something people were comfortable with. And you look at the real estate data coming out of China at the time and it looked like coming to a standstill, and so we actually turned off the core business and we stopped buying homes for a few months. hey, we can't go in and we don't know if anyone's going to be buying any homes, and so what do we do? And we took those few months and then came out the other side and had virtualized the whole process. Then it was pretty stressful, right, because looking at a business that relies on going into people's homes and suddenly you can't do that anymore, what do you do? So, again, a fond memory to look back on a very stressful time in the moment where it feels very, very difficult.

Lenny Rachitsky (00:16:51):
Just since you mentioned Opendoor, I think many people have heard of Opendoor. Maybe just give a quick explanation of what Opendoor does for people that aren't exactly sure.

Brian Tolkin (00:16:58):
So we're a digital platform to buy and sell real estate. The core product today is a seller focused product where people can go online, enter some information about their home, and we'll make an all cash offer to be able to sell simplicity and certainty. So the product really works for people who want something that is certain and simple and easy. I don't know if you've ever sold a home, but it can be a very, very, very successful difficult process with showings and open houses and how to price it and will it sell and all of that stuff. And so we offer basically a way to skip the whole process.

Lenny Rachitsky (00:17:41):
So you basically sell your house to Opendoor and it's just like, cool, done, move on.

Brian Tolkin (00:17:45):
You picked your closing date, you move out when you want. Yeah, there's no hassle.

Lenny Rachitsky (00:17:53):
Sounds amazing. I want that. Coming back to ops and product, just to close this thread again, you've worked at two businesses that have done incredibly well combining product and ops. Are there any just broad lessons you've taken away from how to make these two teams and functions work well together and to build a business that's very ops heavy but also offer driven?

Brian Tolkin (00:18:15):
The first one we touched on, which is a, there's just got to be mutual respect. Both functions have their time and their place and their skillsets, and you just don't build big businesses of this type without respecting the fact that that both need to exist. The second, particularly on the product and engineering side, is really understanding where and how the technology leverage comes from the business and then being really focused on making sure generally, especially in the earlier days, you are more limited on the technical resourcing side than you might be on the operational resourcing side. And so how do you be really focused on where to invest your time, effort, and energy technically, which is why most of the engineering effort for Uber was on the dispatching system and the pricing system. That's just where the leverage was at the time, given the scarcity of resources.

(00:19:11):
And so I think the second one is being really intentional about where those techs are and then being really forthcoming and saying, hey, that means all these other places where yes, it can make things easier, more efficient, et cetera, et cetera. We are okay not investing in right now, and that needs to be an explicit decision and very transparent. But then the last bit I would say is a deep understanding that the real world has entropy and it's hard and it's messy for us at Opendoor, we go into homes, someone may not be home, scheduling may be off, at Uber the driver may cancel the radio GPS. All these things happen, right? Computers are deterministic, but humans aren't, right? And so building products that have a little bit more flex or a little bit more fail safes in case those things happen becomes a little bit more of a paramount.

(00:20:08):
One other thing, the last thing I would say is I think that the companies evolve as well. So what I talked about at the beginning of Uber being very focused from an engineering and product side on the dispatching system and the pricing system, obviously over time not to evolve now it centralized all of these functions as the company got bigger and more mature and scale and optimization started to be more important and expansion and that Petri dish of trying new stuff and the tools got better and the tech got easier and there was more internal infrastructure. And so over time things can start one way and shift over time as the business needs.

Lenny Rachitsky (00:20:52):
Let's actually spend more time there. You keep saying things that make me want to dig deeper. So at Airbnb we went through the same thing where there was all these local ops teams driving supply, finding homes, bringing out the platform, and then there's this tipping point where the product in organic growth or word of mouth ended up driving more and then orders of magnitude more. So there was no need for these folks to spend time doing these things. Can you just maybe share an example, either we Opendoor, when you talk about there's a time and a place and a skillset for ops, how that evolved? What was the team doing initially and then what did they end up doing as things grew?

Brian Tolkin (00:21:25):
Yeah, I mean, maybe a very easy good example to pick just one part of the Uber process in the early days is at small scale, actually back when it was Uber black drivers, every driver was individually onboarded in a 90 minute to a two-hour in-person in the office onboarding with deep setting of expectations. The next version of that... So that's obviously very ops driven. The next version of that is a small classroom type setting of three or five or six drivers at a given time. Also, very ops driven. And then as we got into more mass market products like Uber Taxi or UberX, it was like, okay, maybe 20 or 30 at a time. So now it's a little bit bigger classroom setting. And we said, okay, let's make a video. Instead of giving verbally the same presentation, let's just make an onboarding video and that was the next set of scale, but now suddenly we have a different problem, which is okay, you have to validate all of these credentials.

(00:22:32):
So most driver's license who they are, all that stuff at one person, easy at three to four at a time, easy, 10 at a time, a little more challenging but fine. At 20 at a time, okay, you're starting to run up onto it now you fast-forward six months and you're doing a thousand a week or whatever, suddenly your system breaks and it's like, okay, we have reached the point where operational system improvements is no longer viable. So, you say, okay, we have gone from the iteration stage to the scale stage and technology is uniquely good at scaling. So now we say, okay, instead of having a bunch of folks around the world taking pictures of driver's licenses and validating and doing all that stuff, how do we integrate with some type of OCR technology or auto recognition of driver's licenses that feeds to a system that knows what a driver's license is or can do automatic validation and suddenly you've done two things.

(00:23:27):
One, you've scaled your system, and two, you've just created a ton of time for what at the time was probably dozens if not hundreds of people running these onboarding sessions all over the country, the world at the time to do other stuff. And so now you can level that up and say, okay, do we do more analytics? Do we do more figure out the next process that needs optimization or whatever the case may be in that virtuous cycle just continues.

Lenny Rachitsky (00:23:53):
The way I like to think about this is do things that don't scale and then scale the things that you're doing. That's the phrase I always come back to.

Brian Tolkin (00:23:58):
Exactly.

Lenny Rachitsky (00:24:00):
This reminds me of a hot take that previous podcast guest shared in a newsletter post Casey Winters. He talked about that operations is usually, and it's a hot take, that operations is a sign of inefficiency and over time your job is to squeeze that away and make it product software as much as possible. Doesn't mean you always get there. Thoughts?

Brian Tolkin (00:24:23):
Yeah, I actually don't. Fundamentally, it depends on what the operations is, but I don't fundamentally disagree, but I think that the right lens to think about it is... And then those folks can move on to the next challenge. And so there's always another hill to climb. And so I think that was one of the things at Uber and Opendoor where there's this culture of on the ground experimentation that's really helpful where we were just talking about driver onboarding may now be solved with technology so you have a few extra hours a day. How do we get better at optimizing the UberX system? How do you start tinkering with food delivery? How do you start thinking about higher capacity vehicles? How do you think about better feedback loop for those manual surge pricing toggles that we talked about? So I generally agree it just generally free across and solve more problems.

Lenny Rachitsky (00:25:21):
It feels like a big part of this is making sure the operations teams understand there's more opportunity, even if this ends up being automated, your job is not going to go away. We're going to find something new to try and experiment and do things that don't skip.

Brian Tolkin (00:25:34):
Yep.

Lenny Rachitsky (00:25:34):
Awesome. Okay. Going a completely different direction.

Brian Tolkin (00:25:37):
Great.

Lenny Rachitsky (00:25:38):
I hear you're very good at product reviews.

Brian Tolkin (00:25:40):
Okay.

Lenny Rachitsky (00:25:41):
A few people told me this. I'm curious how you set up a product review and any things you've learned, any tips for how to run an effective product review?

Brian Tolkin (00:25:48):
That's very whoever mentioned that. But yes, big fan of doing them actually in particular to maybe bridge the conversations in companies that have ops driven cadences or start out very ops driven because the cadences can sometimes be different. And so the operational cadences that you might have something like a WVRA weekly business review may not be conducive to always picking your head up and saying like, Hey, where's the product going on a slightly longer timeframe. And so I think product reviews in general for all companies are probably really helpful, but actually in particular for some of the product and operations led companies. In terms of things I've learned, I think being really intentional about what the goals are, I think it's okay to say that there are two goals, a goal of accountability and inform to an audience.

(00:26:43):
But also most importantly, I think this is the primary goal is to help make the product better, to help the teams think through a problem and to have that, again, back to our earliest conversation, be a very intellectual conversation about the work and how to make the product better and not super scary. Product reviews hopefully are not feeling like firing squads. That's a scary environment to be in and not necessarily one that's conducive to how do we make the product better. Obviously sometimes the conversations have to get a little intense, but in general that's what we're shooting for is something that helps the team go back and think through how to make the product better.

Lenny Rachitsky (00:27:24):
So the two goals you try to communicate for your product reviews, accountability slash informing people what's happening, but also just like we are here to make the product better and setting that context. Yep. Is there anything you'd do specifically to make it not feel like a firing squad? Like you're coming in here to be attacked and criticized? Do you set context at the beginning of the meeting? Is this just a part of the culture?

Brian Tolkin (00:27:43):
Yeah, I think definitely part of the culture, but also I am a firm believer in general that the people closest to the problems also have the best context to solve that problem. And so as a more senior voice in the room, often the job is probing, asking questions, throwing out ideas in a way that says like, hey, this is an idea. This is not a mandate, this is a thought. And if there's context missing that would inform the product direction, then providing that context in not a question asking sense, but hey, this is context that you might not be aware of. And so I think it's all in how you show up as a leader and what that looks like in terms of probing and pushing the team on dimensions that they may not be thinking about. And then understanding that the team is bringing a perspective that you don't have, which is they think about this problem 40, 50, 60 hours a week, and you might think about this problem three hours a week. So you bring them a breath, the team brings a depth in haven't been there yet.

Lenny Rachitsky (00:28:49):
I don't know if you heard Dharmesh Shah's episode or his thing on flash tags. Have you seen this?

Brian Tolkin (00:28:54):
I have not, no.

Lenny Rachitsky (00:28:55):
Okay. He has a whole system. So you talked about how as a leader you want people to not take everything you tell them as feedback as I need to do this. So he has a whole set of hashtags that communicate how important this is to him from hashtag FYI to suggestion, to a plea.

Brian Tolkin (00:29:13):
Yes.

Lenny Rachitsky (00:29:14):
A plea to you.

Brian Tolkin (00:29:17):
This was actually explained to me. I don't think I've seen the original source, so I'll go back and watch it, but this was explained to me as I'm actually a big fan. I think that's great.

Lenny Rachitsky (00:29:26):
Yeah, just get everyone on the same page. Okay. Maybe one last question here. Who do you try to invite to product reviews? Do you have any frameworks and ways of thinking of who to invite, who not to invite?

Brian Tolkin (00:29:36):
Yeah, good question. We, I would say have oscillated over time, but in general, big subscribers of the best conversations happen when they're relatively small, so try and keep it under 10. Could be wide distribution of the document. The artifacts created are actually really powerful and they're powerful for the whole team to understand. And secret power is they're very powerful for new people who are onboarding to be like, here are the last 20 product reviews, you'll get a pretty good idea of what's going on. But generally the conversation itself try and be relatively tight. We try to keep it under 10.

Lenny Rachitsky (00:30:15):
And these artifacts, you mean the recordings of the meeting that people can watch or?

Brian Tolkin (00:30:20):
Yeah. Or just the document depends on what the company culture is, whether you want to record it or just have the document either way.

Lenny Rachitsky (00:30:26):
And then is there some specific cadence you operate on? Is it like a weekly product review that people can sign up for? Does every team, how do you like to set this up the cadence?

Brian Tolkin (00:30:35):
Yeah, obviously it scales are with the size of the company. For us right now, what's working well is signup cadence. We have two slots a week that anyone can sign up for as their product area needs it. And then if there's something that we would love to see that we haven't seen in a bit, we do a little bit of all in telling to make sure that the work is generally cycling through on a quarterly basis.

Lenny Rachitsky (00:30:59):
This episode is brought to you by Attio. A radically new type of CRM. There's a world where your CRM is powerful, easily configured, and deeply intuitive. Attio makes that a reality. Attio is built specifically for the next era of companies. It syncs with your data sources, easily configures to their unique structures and works for any go-to-market motion from self-serve to sales led. Attio automatically enriches your contacts, syncs your email and calendar, gives you powerful reports and lets you quickly build Zapier style automations. The next era of companies deserves more than an inflexible one size fits all CRM. Join modal, replicate 11 labs, and more, and scale your startup to the next level. Head to attio.com/lenny and you'll get 15% off your first year. That's A-T-T-I-O.com/lenny.

(00:31:54):
Adjacent topic. I hear you're a big fan of drops to be done, which is okay, so it's a fun recurring topic on this podcast. We've had many people that love it, many people that hate it. I love seeing both sides of it. I love that you find it helpful and you implement it at Opendoor. I'd love to hear just how you actually apply it at Opendoor, what you've learned about how to apply jobs to be done effectively.

Brian Tolkin (00:32:17):
Yeah. I think like all frameworks, the right answer is to pick your set of frameworks, have more tools in your toolbox, and then actually understand when and how to apply them. So we try to avoid being a hammer and everything's a nail. We try to for course the framework if it's not working. But I think what I really like about it is it forces you to put yourself in the customer's shoes. I think in a slightly deeper way and be a little bit more empathetic when I think about building at Opendoor versus say building at Uber or when you are building at Airbnb is we are not... Most people at Opendoor, we don't have homes to sell every week or every month, nor do we buy homes every week or every month. On average in the US is something people do once every seven years.

(00:33:10):
I'm sure the average at Opendoor is something similar, and so it's a little bit harder to be a customer. I took Uber every day. You probably use Airbnb a number of times a year. And so in some sense for some of those companies, you can bill for yourself, you would intuit the job to be done because you're just doing it for yourself. We don't necessarily have that context. And so a framework that forces us to be really thoughtful and intentional about how a customer might perceive our product is really helpful. The other thing that I like about it is the canonical version of it encourages you to think about the context in which the user's operating or the other things outside of your product that they might be going through.

(00:33:59):
And in our case, the home buying or selling journey often is a certainly multi-week, if not multi-month or multi quarter journey with a lot of complexity and a lot of conversations outside of our product. You may be talking to an agent, you may be talking to a friend, you may be driving around the city trying to find a house, and the framework is very flexible and encouraging of saying what is actually the job to be done of this user when they're thinking about our product and what is the context in which they're operating.

Lenny Rachitsky (00:34:29):
I'd love to go one level deeper to talk about how you actually implement it. Do you have templates of, you have a startup project as a blank, I blank, blank, blank? How do you...

Brian Tolkin (00:34:40):
I would say we're medium rigorous on template standardization or adherence. So we do have a template, the standard product review template talks about jobs to be done and has a section for what is the problem statement and what are the jobs to be done.

Lenny Rachitsky (00:34:58):
And this is a doc that when you're coming to a product review, the person running it and coming is filling out this document?

Brian Tolkin (00:35:04):
Correct, pre-filling it up, sorry, pre-filling it out. And again, I think we are not sticklers about always using that template, but I think the beauty of a template is yes, it sets expectations of what you expect, but it's also just easier often for people to be able to work off something. And so yeah, it's part of our product review template and then part of our planning process as well. Because we've used it for a while. I think there's been an internalization of the culture where people will also just start commenting about it or writing about it and saying, hey, what is the job to be done here? Or what is the user trying to do? Which is maybe another colloquial phrase in it. And so, yeah, I think there's a cultural seeping that has happened.

Lenny Rachitsky (00:35:49):
From memory, just what is in this template. So what's the phrasing that you try to use for setting up a problem?

Brian Tolkin (00:35:55):
Yeah, yeah. I mean, the specific framing, I would have to go remind myself on the template itself, but generally it looks like context, problem, potential solution, risks, risks/premortal and measurement of success. And then we also try to bucket our product reviews by stage. So you could be in the ideation stage, which might look very different than at the very end of the process. Like, Hey, we're getting ready to ship speak now forever hold your piece. Those two artifacts will also be very different.

Lenny Rachitsky (00:36:35):
Okay. So it's not as a blank the standard jobs to be done language, it's not exactly how you implement it's more just make sure we're thinking of it what is the problem for the customer? What is the context of their problem?

Brian Tolkin (00:36:47):
Correct. Yeah. Yeah, we're not math living our template.

Lenny Rachitsky (00:36:52):
Okay, awesome. Any other tips or lessons about just working well with this concept of jobs to be done? Maybe when you come into Opendoor and like, hey everyone, we're going to be thinking this way. Is there anything there that would be useful to people if they're trying to operate this way?

Brian Tolkin (00:37:06):
Recognizing that correctly implementing a framework, any framework, but if you don't in particular, we can talk about takes a little bit of time and getting used to and understanding. And so I don't think you can just like, okay, we're going to make the template and then that makes the content better. That just takes people's content and they wedge it into the template. It's actually the cultural internalization of like, hey, this might be phrased as the job to be done, but is this actually the job to be done? Let's talk about why the customer might be in that situation or not be in that situation. Or I think the job to be done might actually be something else.

(00:37:43):
Or you might say, hey, the job to be done is maybe an early day version would be the job to be done is to get an offer from Opendoor. And it's like, well kind of, but the broader job to be done might be price discovery for the customer. And so you can have a rich conversation where it's like, well, one might be a little bit influenced by our business goals. I don't think you just run around and people are like, yeah, I'm going to sell my house, but my goal is to get an offer from Opendoor. And so that's like, okay, the template might be the same, but it's actually the content that takes a little bit of cultural instantiation.

Lenny Rachitsky (00:38:21):
Got it. And it sounds like people talk from what is the job to be done that feels like a core part of the way you think about it. What is the job to be done? Just that language alone feels really powerful. Is there a resource or a book that you point people to help your team learn about the jobs to be done work? Is there one thing you find useful?

Brian Tolkin (00:38:38):
Not about jobs to be done. I do a lot more pointing people towards internal examples of where I saw other PMs maybe do as well or blogs and stuff. But your blog is a column when we pass around, not about jobs to done, but just about many topics.

Lenny Rachitsky (00:38:56):
I'm flattered. Thank you.

_[294 additional lines trimmed for context budget]_

---

### How Notion leveraged community to build a $10B business | Camille Ricketts
**Guest:** Camille Ricketts | **Date:** 2022-12-11 | [YouTube](https://www.youtube.com/watch?v=bY5KC9Gguz8)  

# How Notion leveraged community to build a $10B business | Camille Ricketts

## Transcript

Camille Ricketts (00:00:00):
The way that you think about product market fit, you have to think about content market fit. So even though content feels like it's running adjacent to the actual product that you're putting out there, you still have to think about who is my audience? Who is the audience that I really want to have? Who is the audience that is going to be drawn to this most? Who are they? What is it that they really need in their lives? Even abstracting content from it at all. What is it that they need to get promoted? What is it that they need to avoid failure? What is it that causes them a great deal of anxiety in the day-to-day of their lives or their work? And can you create some type of content product that is going to address this for them?

Lenny (00:00:38):
Welcome to Lenny's podcast. I'm Lenny and my goal here is to help you get better at the craft of building and growing products. I interview world class product leaders and growth experts to learn from their hard won experiences building and growing today's most successful companies. Today my guest is Camille Ricketts. Camille was the first marketing hire at Notion and longtime head of marketing at Notion. Prior to that, she was head of content and marketing at First Round Capital, where amongst many other things, she launched the First Round Review, which holds a very special place in my heart because a guest post in the First Round Review essentially helped me launch my now career of newsletter and now podcast. Camille also did content marketing at Kiva and also comms and PR at early Tesla where she sat right next to Elon Musk for about a year and she shares some really fun stories about that.

(00:01:26):
In this episode, we focus on two areas that Camille was very early in and has tremendous insights around. One, community led growth. What it actually is, when it's something you should invest in, how to do it well. All based on her experience building Notion's early community, which was a huge part of Notion's early success. We also talk about content marketing. When it's worth investing in, how to do it well, and all kinds of tips for building a content marketing machine. It was a total blast chatting with Camille and I am really excited for you to learn from her. With that, I bring you Camille Rickets right after we hear a word from our wonderful sponsors.

(00:02:02):
This episode is brought to you by Eppo. Eppo is a next generation AB testing platform built by ar Airbnb alums for modern growth teams. Companies like Netlify, Contentful, and Cameo rely on Eppo to power their experiments. Wherever you work, running experiments is increasingly essential, but there are no commercial tools that integrate with a modern grow team stack. This leads to wasted time building internal tools or trying to run your experiments through a clunky marketing tool. When I was at Airbnb, one of the things that I loved about our experimentation platform was being able to easily slice results by device, by country, and by user stage. EPO does all that and more. Delivering results quickly, avoiding annoying prolonged analytics cycles, and helping you easily get to the root cause of any issue you discover. Eppo lets you go beyond basic clickthrough metrics, and instead you to North Star metrics like activation, retention, subscriptions and payments. And EPO supports tests on the front end, the back end, email marketing, and even machine learning clients. Check out Eppo, geteppo.com, get E-P-P-O.com and 10X your experiment velocity. Hey, Ashley, head of marketing at Flatfile. How many B2B SaaS companies would you estimate need to import CSV files from their customers?

Ashley (00:03:21):
At least 40%.

Lenny (00:03:23):
And how many of them screw that up and what happens when they do?

Ashley (00:03:26):
Well, based on our data, about a third of people will consider switching to another company after just one bad experience during onboarding. So if your CSV importer doesn't work right, which is super common considering customer files are chock full of unexpected data and formatting, they'll leave.

Lenny (00:03:45):
I am 0% surprised to hear that. I've consistently seen that improving onboarding is one of the highest leverage opportunities for both signup conversion and increasing long-term retention. Getting people to your aha moment more quickly and reliably is so incredibly important.

Ashley (00:04:00):
Totally. It's incredible to see how our customers like Square, Spotify and Zuora are able to grow their businesses on top of Flatfile. It's because flawless data onboarding acts like a catalyst to get them and their customers where they need to go faster.

Lenny (00:04:17):
If you'd like to learn more or get started, check out Flatfile and flatfile.com/lenny.

(00:04:27):
Camille, welcome to the podcast.

Camille Ricketts (00:04:29):
Hello there. Thank you so much for having me.

Lenny (00:04:32):
Absolutely, my pleasure. You have such a fascinating background working at so many world-class companies with so many fascinating people. Could you just take a minute to talk about some of the wonderful things you've done in your career just to set a little context for folks?

Camille Ricketts (00:04:47):
Yeah. Well thank you for characterizing them as wonderful.

Lenny (00:04:50):
It's true.

Camille Ricketts (00:04:51):
I feel like it's been a quite circuitous path, but definitely has taken me to some interesting places. I started off as a journalist at the Wall Street Journal and then found my way into communications and marketing at Tesla Motors where part of my responsibility there was to sit to Elon's right and make sure he had all the data he needed at his fingertips when talking to the press, which was deep end of the pool on the PR learning. And then after that, found my way to First Round Capital where I was really fortunate to be at the ground floor of First Round Review, if anyone out there watching this is familiar with those pieces. Was there for about five years. Loved that team. Really incredible folks. And then they had invested in Notion really early on, and so I was able to meet Ivan Zhao as a result of that and him and Simon, and they gave me the opportunity to join as the first marketing hire at Notion. And that's what I was doing up until recently.

Lenny (00:05:44):
I love that Elon tidbit. I like that it was on his right. His right hand person. What was that like? And is there something that you learned working alongside Elon, sitting next to Elon, about operating, working that maybe you've taken to other places you worked at?

Camille Ricketts (00:05:59):
I mean, it was a long time ago, so I'll caveat that. This was before Model S came out even. So a lot of my work was, and this was a great opportunity, but driving around in the Roadster and talking to journalists and letting reporters ride in the car, which was very seductive and I think maybe just a little unfair from a PR standpoint. But in terms of what I learned, that was really the first job that I had that was necessitating just being incredibly on point with all the information. So making sure that I knew everything that could possibly come up in a conversation, being incredibly well-versed in just the topics at hand, I think that served me really well. I just have to be really, really, really quick and on it. And then the other thing that Elon I think is very talented at or definitely at the time really made an impression on me was painting an emotional picture of the vision that he was really going after and being able to convey the emotional quality of the mission to the people he talked to. So definitely at the time about the electric vehicle revolution and then space travel, I think he just knew how to make people feel about it that really enlisted a lot of hearts and minds and that is something that I've taken with me for sure.

Lenny (00:07:09):
Would you say that was the most stressful place you've worked or have you found more stress post Elon?

Camille Ricketts (00:07:15):
I think that that was the place where you just needed to be so on your game. Game face every single day. Which is a wonderful skill to learn. And then I think there were other moments in my career where just the stakes might have been a little bit higher. Certainly at Notion every day felt like we're building this thing together and we're in this very special moment. So yeah, I think there was a mix there.

Lenny (00:07:39):
Speaking of Notion, I think you mentioned this and if not, you were the first marketing hire at Notion. Is that right?

Camille Ricketts (00:07:44):
Yes.

Lenny (00:07:45):
What employee number was that?

Camille Ricketts (00:07:47):
I was number 11.

Lenny (00:07:48):
Wow.

Camille Ricketts (00:07:49):
Yeah. So it was really a small squad of folks at the time.

Lenny (00:07:53):
And how big are they now, roughly would you say?

Camille Ricketts (00:07:55):
The last I heard, I think that they were around 400. Maybe a little over 400.

Lenny (00:07:59):
Amazing. And I think they're worth ... I don't know. Last valuation was like $10 billion. So there's been quite the journey. Must have been quite the adventure being at Notion during this time. What's maybe the most tangible memory of working at Notion in the early days? What was it like early day Notion?

Camille Ricketts (00:08:15):
I think a lot about just what the environment felt like. This was the first very small startup that I had worked for. When I left First Round, I really wanted that experience. And the first office that I worked in was really just like a home. It literally had an apartment on top of this loft space and it just felt like we were a group of people who lived there together during the day, but it had that kind of home spun really warm quality. So we all took our shoes off. There was beautiful furnishings and rugs and we would all just sit around and drink tea and work together on these couches. So it really had that feeling to it. And then there were little quirks. I like to reminisce with my colleagues who were there at the time that we didn't have a great HVAC system.

(00:08:58):
So during the summer it was really hot and then in the winter it was really cold and we would have these big industrial fans and at the time we were like, "Oh, this is really bizarre." But now it's one of our favorite memories to talk about. Or for a while we didn't have overhead lighting, so me and my colleagues who were there working really late at night, it would just get darker and darker and darker. And one of my favorite folks there actually had a headlamp that she would switch on at a certain point in the evening. So that's the stuff that really comes up for me. We were all working really hard and in this thing together, but it's that team familial quality that stands out to me.

Lenny (00:09:35):
I love how some of these early moments where it feels like, what the hell are we doing? We have to wear headlamps? It's super hot. When you're in it, you're like, this isn't maybe how our startup should be going. And it feels really painful and hard. But looking back, it's always the best memories, those hardships.

Camille Ricketts (00:09:52):
It truly is. And the moments that we were there late at night really trying to get something done before a big launch the next day, that's where our hearts lie, I think, to a large extent. That crew that was there.

Lenny (00:10:04):
On that note, and when you're talking about stress working with Elon, you talked about Notion had a different kind of stress. What's maybe the most stressful memory you have of working at Notion? Whatever you can share.

Camille Ricketts (00:10:14):
This is something that has long since been rectified, but the first day that we came back from break in 2021 ... We had all been sort of away for the holidays. We reassemble. I think it's January 3rd, 2021 perhaps. Had a massive outage that day that took down, not just us but also a lot of our peer companies. And so it was literally all hands on deck. We're suddenly seeing all of these people on Twitter pop up, on the Reddit pop up being like, "Oh my gosh. What am I going to do?" And it really reinforced for us how central Notion had become to so many people. So on one hand it was kind of this amazing moment of realization of how vital this thing we were building was all the time, which adds to the stress in the moment, but also your motivation overall.

(00:11:01):
And then we also saw on Twitter, and this is part of why community is such a core focus of mine, but people being like, "They're trying really hard to get it back up. Give them a break." Or like, "Sending hugs to the Notion team. We know you've got this." And we really appreciated that and that was just a very heartwarming aspect of it. But that day was definitely a scramble and we wanted to be as communicative as possible. So my team was really central to making sure that everybody knew what was going on, what the efforts were being made to fix it, time horizon, all of that. So they've long since hired the best infrastructure people I think in the industry and refactored the database and everything. So it's not an issue anymore, but certainly that was a moment of stress at the time.

Lenny (00:11:50):
It's interesting looking at those times. When you're in it, you're like, "We are going to die. We're down. People will stop using Notion. We're in big trouble." When really people always come back if it's an awesome product. I think of last things down for a week, JIRA or Confluent, and people come back if it's an awesome product.

Camille Ricketts (00:12:07):
I think that's a good tactical learning and hopefully a takeaway for folks who maybe will experience that moment is that truly there's more resilience built into the system than you might think.

Lenny (00:12:16):
So speaking of community, you talked about just how important that was during this time and then just in general. I was doing research on you and things that you've done over your career to prep for this podcast and I found there's two areas that you've led the charge on and we're ahead of the curve on and in part help innovate. One is community led growth and two is content marketing in a big way. And so I wanted to focus a lot of our chat on these two areas. Community led growth, it feels like a very buzzy topic on Twitter. Everyone's always talking about how the future of growth is community. You've got to build a community. You got to be community led and all these things. And so I want to try to make this concept concrete and help people understand should they invest in community. How can community help you? When does it make sense to you? When does it not make sense to invest? And so maybe just as a first question, just what is community led growth? What does that actually mean as a concept?

Camille Ricketts (00:13:09):
Yeah. I think it has become quite buzzy and it's certainly aspirational for a lot of product led growth companies and even those that are maybe a little bit outside of the product led growth orbit. And we're seeing all of these startups I think also come out that are about community and how to enhance the effects. In terms of how I think about what it actually is, it's when your community helps you achieve such ubiquity and such name recognition that it actually allows you to start moving upmarket into the enterprise. And I know that might be very specific to enterprise oriented companies, but that's how we defined it at Notion was the fact that so many people were talking about this, sharing what they had built about it, honestly starting businesses of their own around it to formalize the relationship with teams that I think it de-risked Notion as a choice for a lot of companies just because they had heard about it through so many channels. They had seen it on social media, they've heard about it on a podcast, their friend told them about it, they saw a billboard. All of that lended itself to larger and larger companies and teams buying more and more seats. So I think that's the power that the community had for us. And I see that also being analogous to what companies like Figma have been able to achieve.

Lenny (00:14:21):
It sounds like a lot of the way you're describing it is basically awareness. Brand awareness is what you found to be maybe the most useful element of this community that you built around Notion.

Camille Ricketts (00:14:31):
I love using the word discovery because I think that that is even a little bit like a step further than awareness where true discovery is when you have intent to find out more. You've heard about it so many times or you've been intrigued by something that someone has told you to the extent that you're actually going to take the step of now learning about it. And that's where we really wanted to play and to emphasize our work.

Lenny (00:14:59):
Got it. So it sounded like the KPI/OKR of your team was get more people aware and excited to explore Notion.

Camille Ricketts (00:15:08):
Yeah. And maybe this is a helpful tactical point. I think when people think about acquisition or discovery or brand awareness or brand in general, they're like what collection of metrics are actually going to give us insight into this? And the one that I found to be the most instructive was net new visitors to the Notion website. So month over month, how many new people who had never been there before were motivated enough to come and actually learn about the product. And that was really the responsibility of the brand team and the folks that worked with me on community and content and all of the awareness campaigns that we were putting out into the field was about getting more new people interested.

Lenny (00:15:49):
So that begs to the question, did you have any clever ways of attributing that new traffic to stuff your team did versus the SEO team or other teams?

Camille Ricketts (00:15:58):
In particular I'll call out the influencer marketing efforts that were really being run by this incredible woman, Lexi Barnhorn, where they were incredibly measurable. Where we were like, okay, well we're sponsoring people for this amount, these creators across these platforms and we know that people came from that content directly to the Notion website. So we were able to draw really tight connections. So I think that some types of content lend themselves to that. And then also with community, there's certain things you can do around helping your community members report on how many people are attending, et cetera, to give you that sense.

Lenny (00:16:36):
So you may be already answering this question, but I'm curious what efforts had the most impact to achieve these goals that you had of creating more awareness and discovery motivation and things like that. What actually worked?

Camille Ricketts (00:16:48):
So I'd say that the community efforts that were very big for us we're the ambassadors. Also making sure that people were hosting in-person events. This really took off in 2019. Obviously we paused for 2020, 2021, but now I just spent time with Notion's head of community, Ben Lang, who truly is the mastermind and genius behind so much of this and he says that they're back up to 30 in-person events a month around the world. So that really helped on the international scale of spreading ubiquity and ended up lending itself to relationships with Station F in France, which is the biggest startup campus in Paris. So really helping us work our way into those types of networks and then supporting those people to also start their own businesses and derive whatever reward they were looking for themselves. So we really wanted to align our goals with theirs.

(00:17:38):
A lot of those folks actually started revenue generating businesses as consultants or course makers or influencers. Some of them just wanted to build their own platforms online. So all of our efforts there are around building guides or counseling people one-on-one or making it easier for them to actually achieve those goals for themselves was also a big part of this growth. And then like I said, influencers. This was something that Ben started exploring in 2019 and we were so pleasantly overwhelmed with the amount of traction and traffic that was driven by working with some of these influencers. And now that program has exploded into a multi-channel effort that's huge for Notion.

Lenny (00:18:24):
Awesome. The influencers makes a lot of sense. I want to learn more about this ambassador program and what that was about with events and maybe just broadly, I imagine a lot of founders might be listening and they're like, "Yeah, this all sounds awesome, but how do you know if it's doing anything?" Events. That would be great, but how much is it worth investing? How much time and attention does it take? How do we know if this is actually ROI positive? Is there anything you learn there about just ... Is it a founder must believe in this as a thing that is probably going to work sort of thing? Or is there something you found to convince people like, yes, this is how you can know it's working?

Camille Ricketts (00:18:58):
That's a great question. I think that we were really fortunate that Ivan saw the inherent value in community from the very beginning and was deeply supportive. And actually one of my number one recommendations for anybody who suspects the community could be a big growth driver is to not make metrics the be all end all at the very beginning. So we didn't necessarily start measuring things very concretely until last year with community. Mostly because we had already seen so much organic scale that we saw being tied to our community efforts in some way in terms of where we were geographically expanding, how people were reporting that they had discovered us whenever we surveyed them. So that type of motion. And I think for any company that is seeing this type of just organic fervor, one of the worst things you can do is say, let's cut this off at the knees if it's not generating ROI.

Lenny (00:19:52):
I imagine internally there's just like obviously this is good. We may not be able to measure it, but it feels like this is very good for Notion. It feels like especially for a prosumer product like Notion, it makes a lot of sense because it's driven by people using it and then they bring it into the company, like you said. Maybe it's less ROI positive or just one enterprise product. Do you have any thoughts there? Is this a great strategy for prosumer enterprise products more so than more enterprise-y?

Camille Ricketts (00:20:19):
Definitely I think if you have a long sales cycle or a high price point where there has to be many, many, many touchpoints in order to get somebody to decide to buy, I'm not sure that community should be the number one thing that you invest in. Certainly for freemium products, I think for a lot of them, especially if they have what I'm going to call the atomic unit of sharing, which I will define out, it becomes a no-brainer. I think that community lends itself particularly well if you have something that your product creates that people want to share because it exhibits something about themselves. So at Notion it was templates or even people just creating their own workspaces and being really excited to show them off. So Notion really benefited from being a creative product, but the same is true of Figma or Canva or any of these where showing people what it is that you've created is an aspirational thing to do. Because you are showing that you are really well versed in how to use the products, extremely organized. You're self expressing in some way. So if your product does have that element to it, I think that community is a great investment.

Lenny (00:21:34):
You touched on this point, and I don't think people realize this, but you can make a lot of money creating templates on Notion, right? That's a whole ecosystem. Can you talk about that? Because I don't think a lot of people know this.

Camille Ricketts (00:21:45):
Yeah. This is one of the reasons that I would advise any of the companies that feel like they fall into this category start early. Because you need to nurture all of these different routes that people in your community can take. Certainly early on I think that the people that we initially recruited in the ambassadors didn't see themselves doing maybe even close to a million dollars in business around helping other teams succeed with the product or selling templates. I remember really early on, probably mid 2021 we heard of one creator who had made $35,000 in four months selling one template and that was a very common story then from that point forward. And helping them do that, actually creating the guide material and the networks and also the connections between the people who are running similar businesses who could help each other, that all became really fundamental. But to your point about, oh is this actually related to the enterprise motion for Notion? So many companies now of many sizes are relying on the consultants that first came up through our community and some of those consultants are now employing dozens of other people.

Lenny (00:22:53):
That's incredible. There's no better way to motivate someone to evangelize Notion than have their income rely on Notion.

Camille Ricketts (00:23:00):
And it's also just inspiring for us, honestly. There's so many people who started off with not very many followers and now they are celebrities within this ecosystem.

Lenny (00:23:12):
So maybe coming back to the ambassador program, that's separate from this selling Notion templates ecosystem. What is the ambassador program?

Camille Ricketts (00:23:19):
They're actually quite blended because the folks who are excited about Notion, it takes a lot of forms. Sometimes they want to host events, sometimes they want to build templates. So we would actually have channels inside of our Slack instance for the ambassadors that had these areas of focus based on what people really were passionate about or wanted to do and they were like a force multiplying flywheel for each other. Because a lot of folks would enter the ambassadors program and then I'm happy to talk about champions as well, which is a little bit different, and then discover what it would mean for them to build templates and it became motivating for that reason. So on the champions side of things, and this is maybe speaking a little bit more to the enterprise as well, we wondered if the same DNA that existed among consumers for the most part in the ambassadors could work for folks who were inside of our customer companies. And so we launched another community, another Slack instance for folks who were the most passionate or the most avid users of Notion inside of our customer companies, which has become just a wonderful channel for customer success to be more communicative with those companies, make sure that things are sticking or obstacles are being overcome. And that's been designed very specifically that way and it has been really, really valuable over time.

Lenny (00:24:35):
Okay. So let me try to understand this. Champions are basically the most active users of Notion. You put them in a Slack and help them become even more excited and make sure they're happy. Ambassador. I still don't totally understand what is an ambassador? Is that someone you're paying to help promote Notion? What does that actually mean when you're an ambassador?

Camille Ricketts (00:24:52):
They're people who are really just passionate about the product. So it's not transactional. They're people who love building with Notion. They love sharing what they've built in order to help others. And they really just want it to be a bigger part of their lives. And I think that one of the points about community is that it's not just a one-to-one conversation with us. The big draw over time, maybe people joined because they would get early access to features. We would get their feedback. That became really important for our product team or because we would offer AMAs with some of our folks internally. But over time it was really because they were forming these bonds with each other and learning so much from each other that most of the time someone would come in and say, I'm struggling with this or I don't quite know how to use this and it would be another member of the community that would help them more immediately. So it really allowed them to form these dense networks of friendships that I think became just a positive part of people's lives.

Lenny (00:25:51):
What I'm taking away from this partly is you identify a group of people that are interested in Notion, excited about Notion and then just lean in to support them. There's people that are buying Notion and that are power users, help them be better power users. Influencers that are kind of excited about Notion, pay them to promote Notion. Then the ambassadors that are people just passionate about Notion, help them be more passionate. And then the people making templates, help them be successful. Is that roughly how you think about it? Just identify something that's working and make it more effective?

Camille Ricketts (00:26:21):
I think if it doesn't sound too reductive, yes. I would also say that one of the things that I think Ben was best at is not putting a one size fits all experience on any of this. I think that some communities get built where people are like, okay, well we have this community and it's going to be this and this and this, or these are the types of programs we're going to offer or these are the types of interactions we're going to have. As opposed to I think a lot of listening of the people who are actually participating. Really early on one of the things that Ben did that I thought was really amazing was he'd spend a ton of time just on Zoom having conversations, one-on-one conversations, semi small group conversations just saying, "Why are you here? Why do you like participating in this? What is it that would make it better?" And really helping our entire team follow their lead. I would recommend highly not necessarily coming in with preconceived notions about what a community needs to look like.

Lenny (00:27:21):
You touched on this, that if the founder believes in the power of community, this becomes so much easier. A lot of founders are like, "Nah. That's a waste of time." Do you think founders are convincible that building community and investing in community is worth it? Have you seen that effective where a founder just comes into it being like, "Nah, I don't think this is worth our time," and then they get convinced later? Or is it just like, "Nah, forget it. Don't even try."?

Camille Ricketts (00:27:45):
I mean I've talked to a lot of different people who come at this with different impressions and everybody knows more about their company than I do, but I do think that if ubiquity or just the sheer word of mouth engine is something that is going to be valuable for your company over time, I would really urge people to sit down and really think carefully what is going to be more conducive to our long-term success? Is it going to be that ubiquity or is it going to be revenue now? And I think if we look at a lot of the companies that have been just wildly successful from the start, they're people who have pushed off maybe monetizing every little thing if it's going to really put a damper on that type of enthusiasm and momentum that people have to share it at what it is they're doing. Because there's always opportunity I think later once you have that big tide of people who are not just excited but also legitimizing what it is that you do every single day, that gets mobilized in a lot of different directions and you have a lot more options then.

Lenny (00:28:47):
What's interesting about Notion is you have high LTVs when you sell to larger companies, but the initial users are often just regular folks. And so I think it's a unique place where you have cash to spend on making it ubiquitous and getting the word out through all these community efforts because it'll pay off. And a lot of companies probably don't have that advantage. So would it feel right to say that this is really effective for product led, growthy, freemium products most? Is that a good way to think about it?

Camille Ricketts (00:29:20):
Yeah. Or I think if organic growth is something that you see being really beneficial or if organic growth happens to be something you really have to crack because you don't always have everything you need for paid growth from either a resourcing standpoint, team standpoint, really figuring out how to get that organic flywheel going can serve you well. It becomes this buttress for any paid growth you explore in the future.

Lenny (00:29:47):
This episode is brought to you by Vanta. Helping you streamline your security compliance to accelerate growth. If your business stores any data in the cloud, then you've likely been asked or you're going to be asked about your SOC 2 compliance. SOC 2 is a way to prove your company's taking proper security measures to protect customer data and builds trust with customers and partners, especially those with serious security requirements. Also, if you want to sell to the enterprise, proving security is essential, SOC 2 can either open the door for bigger and better deals or it can put your business on hold. If you don't have a SOC 2, there's a good chance you won't even get a seat at the table. Beginning a SOC 2 report can be a huge burden, especially for startups. It's time consuming, tedious and expensive. Enter Vanta. Over 3000 fast growing companies use Vanta to automate up to 90% of the work involved with SOC 2. Vanta can get you ready for security audits in weeks instead of months. Less than a third of the time that it usually takes. For a limited time Lenny's podcast listeners get $1,000 off Vanta. Just go to vanta.com/lenny. That's V-A-N-T-A.com/lenny to learn more and to claim your discount. Get started today.

(00:31:04):
What other companies come to mind when you think about companies that effectively did community led growth, did community well and grew in large part because of community?

Camille Ricketts (00:31:14):
I've mentioned Figma a couple times here so I don't want to beleaguer the point, but they're certainly a team that I've looked up to through my entire experience at Notion. We were kind of sibling companies in a way. Huge kudos to Claire Butler over there who I knew led all of those efforts and we would trade a lot of knowledge back and forth, which was so lovely to have that relationship. But they did an amazing job I think in a similar vein to Notion of saying, okay, people are really excited to create these things and then put them out there on the internet. So how can we just fuel that particular motion out there? The other example I'll give, which is a little bit of a different tack is Stripe. And when Stripe launched Stripe Atlas, not necessarily core to the initial product line that Stripe was known for and what had been foundational for them, but allowed them to build this community among probably their core demographic at the time, which was founders and startups that were growing through the stages to mid-market, they were able to cultivate this huge audience of founders around giving advice and providing them with resources to actually get started and do that zero to one journey.

(00:32:22):
So while it was adjacent to maybe what the company's core mission was, it allowed them to actually create community among their customer base because they were like, "We're knowledgeable. We can share these things with you that we know are core to your journey." So I would encourage anyone who's thinking about community that way to be like, "Oh, maybe it doesn't have to be around our product. So specifically. What other knowledge or resourcing can we offer to the people who we do want using our product that's going to be really instrumental for them and can we convene them around that idea?"

Lenny (00:32:54):
I'm noticing a strong correlation between legendary generational companies, Figma, Stripe, Notion and community efforts and building community. That's interesting.

Camille Ricketts (00:33:05):
Yes. I'm a big proponent. At the same time I don't think that community is right for every company. I think that there is definitely an analysis to run on that. But hopefully this is helpful for those who can identify that those are attributes they have.

Lenny (00:33:19):
To pull on a thread there, what are maybe thoughts for when it probably doesn't make sense to invest a lot of efforts into building a community around your product? We talked a little bit about high-end enterprise products. Is there anything else that just like, man, it's probably not worth your time?

Camille Ricketts (00:33:34):
Like I said, if it's more of a sales led culture that you have, which is definitely true of products that are a little bit pricier or that require longer contracts, so understanding that. But I do think the community takes on different forms and I think when you hear the word community, you think of a big forum of some type, whether it's a Slack instance or something else where people are chatting away all day long. And I don't think it has to be that. That's not the only representation of it. So if you think about what is going to be right for you at any given time, I actually created this two by two matrix, which maybe I'll share with you after this. And on the axis you have, whether you have hit product market fit or if you're still exploring product market set and then whether you're strongly enterprise or strongly consumer. And based on where you land in that two by two matrix, there's a form of community or a community related initiative that could be right for you.

(00:34:31):
So just to give you an example of maybe an extremely different form factor from Notion, let's say that you're still on your way to product market fit and you're a strongly enterprise oriented product. I think that you have the opportunity to do customer advisory boards, which is really convening even smaller circles of ideal fit users and making sure that they are connected to each other as well as you, and then incentivize to provide you with feedback. Understanding that they're really on the ground floor of this journey with you and that they're going to be able to have influence over whatever you do in the future. Those folks can end up growing into your biggest evangelists and I've seen that happen a number of times and I would still consider that community even though maybe that is not what comes to mind for folks.

Lenny (00:35:20):
Well I imagine that becomes the seed of a community that you eventually build. Let's definitely link to this in the show notes. Can you give maybe a couple more examples of this grid? So that was pre-product market fit and then what was the other?

Camille Ricketts (00:35:32):
Strongly enterprise.

Lenny (00:35:33):
Enterprise. Okay, cool. Yeah, what are a couple other of the elements of this grid?

Camille Ricketts (00:35:37):
So if you're strongly enterprise and you have product market fit, let's say, this is something that Notion has really benefited from, but really emphasizing the champions in the consultants communities. So the folks who, like I said, may be inside of your customers who really get it, really get your value, really are excited to help you land and expand perhaps inside of their companies, making sure that they have a place to gather and a place to feel like they are more connected with your team than the average person gets to be. That they are special and that they have access. And then on the consultant side, like I said, just making it really easy, removing friction, helping promote the folks who want to be out there, helping you succeed with more customers. Like Salesforce. I know that this is a golden oldie of an example, but if you talk to anybody who was really early at Salesforce, they really went into this where they saw people emerging who wanted to help other companies. This layer of people who didn't work at Salesforce but saw the opportunity to help other companies actually succeed with it, implement it, grow with it, and that's become a massive part of Salesforce's model. And so if you're in that quadrant, figuring out how to start moving people in your customer base into those categories.

Lenny (00:37:00):
This is awesome. Maybe let's do one more of this grid and then we'll leave one for people to click into and check it out.

Camille Ricketts (00:37:04):
I'll talk about Notion's quadrant, which is the one that I would put up and to the right, which is you have product market fit and you're maybe a little bit closer to the consumer side of the spectrum. Obviously Notion runs the full gamut, but I would say especially early on I think that that's where we saw things take root and that's where I think ambassadors and influencers really take off. Individuals who are going to be extremely vocal, extremely excited, and where you're going to see more of this wildfire spread, at least trying the product, using the product, understanding what the product is. So if you can try to fuel that type of motion if you're in that quadrant, that's helpful.

Lenny (00:37:43):
I want to come back to this ambassador program real quick because it feels like something that a lot of people talk about and can do and especially in this quadrant of product market fit and consumer. How does this work? Is it you select, here's 100 ambassadors we're going to pick because we think they're awesome and they're great examples of people using, say, Notion and then we're just going to provide them with all the help they need to be successful with Notion. How do you think about creating an ambassador program?

Camille Ricketts (00:38:10):
I actually think it's pretty analogous to when you're thinking about positioning your company because I think the best first step for any positioning exercise is to think who are our best fit customers? And it's not necessarily who we wish they would be, but it's actually the hard cold reality of who they actually are. Where it's like these are the people that seem to be really getting it. They're paying us more, they're talking about it just organically. So really figuring out everything about who they are and making sure that those are the people that you're actually inviting in early. So the initial base of the ambassadors program which started back in 2019 was just 20 people and they were the 20 people who we happened to see be the most vocal already across Twitter and a couple of other social media platforms because they had that shared quality of wanting to be really vocal and expressive about their experience with the product. So that would be my advice for how to get one of these rolling.

Lenny (00:39:13):
And then what do you do for them?

Camille Ricketts (00:39:13):
Definitely making sure that there's enough incentive built in, right? Because like we said, it's not meant to be a transactional relationship, but we want them to feel like they are having a special experience, that they are connected with the company in a unique way. And it was so interesting to us how giving them the preview of features was so motivating to them and being able to use them and then give us feedback and feel really heard by the product team. So that was a big area of focus and I know that that still is and it's become even more of a robust conversation between the community and the team at Notion itself.

(00:39:52):
And then also we would do these very special experiences where Ivan or Akshay or Simon or MLM who's the head of engineering there would be available for these conversations where they would answer questions and it would feel like a very proprietary space. I think that that was really interesting to people. And then of course the things that you would suspect around subsidizing events. Making sure that people felt that they were actually supported by us to throw these events. And then also promoting their work. So if you look back at the social media channels, so much of the focus is on putting the creations of the people we were working with front and center as opposed to talking about just what the company was up to.

Lenny (00:40:36):
Have you ever written about just how to design an ambassador program or has anyone written about how Notion did this? Because this is really interesting.

Camille Ricketts (00:40:42):
I don't know if anything has been written or went into all of this detail, but it was truly one of the more magical and I think still is one of the more magical parts of this entire endeavor. And now that team is three people. So Ben who's still there doing amazing things, Francisco who joined us in 2021. Or sorry at the end of 2020. And then Emma. And they are just all day every day talking to people around the whole world. The international component of this is also just completely wild to see.

Lenny (00:41:18):
This could be a future First Round Review post, which we'll talk a bit about.

Camille Ricketts (00:41:21):
Yes. Perhaps.

Lenny (00:41:24):
Last question about this segment. Say someone is convinced they want to start investing in community and we talked about this two by two, but maybe just broadly if you had to boil it down to two or three pieces of advice for founders, for teams thinking about investing in community led growth and community in general, what would be some of those pieces of advice?

Camille Ricketts (00:41:44):
I don't know if you want to link to this in the show notes as well, but I actually put together some commandments for community builders.

Lenny (00:41:50):
Ooh. Absolutely.

Camille Ricketts (00:41:51):
Some alliteration. So the thing that I think were very defining for us early on, I already mentioned something about this, but not trying to hit a number early on. So don't dilute the impact of what it is that you're trying to do in order to show growth. I think that that's very important to protect yourself early on. So making sure that you are learning what individuals really want out of this and making them feel like they're very seen and very heard. That was a big area of focus and I think it's what kept people really engaged and coming back and feeling like this was a secondary family for them. And then one of the things that was most interesting to us that once we started sharing what was going on in the community with folks at Notion. So we would do this during all Hands meetings or on Slack, Ben would post these really incredible updates of just all of the activities of people in the community and what they were up to every month.

(00:42:46):
And it was just so inspiring for everybody inside the company that I think it all rallied us to do even more, I guess, day to day and really understand who it was we were building for.

Lenny (00:43:00):
Is there any other commandments you would add for if you already have a community going? If you have something bubbling for things you should do to keep it healthy and consistently good and growing?

Camille Ricketts (00:43:12):
Yeah. I mean this is going to be a little contrarian perhaps, and I mean this is just one data point for me, but not growing it so big so fast. One thing that we actually thought about pretty carefully was what a rate of healthy growth would be. So there actually is an application process for joining the ambassadors. It's a very light application process and it really is just so that we know how many people are interested in this. And then they're inducted around ... I think at the time it was 20 people at a time every month. So that it wouldn't feel like all of a sudden this had changed in terms of how the interactions were feeling, but rather gave everybody time to welcome the new people in and get to know them. And one of Ben and I's favorite things ever about working at Notion I think was when we would induct new people into the ambassadors and they would introduce themselves and say, "Hey, I am from Venezuela and here's the ways in which notion has changed my life."

Lenny (00:43:12):
That's awesome.

_[315 additional lines trimmed for context budget]_

---

