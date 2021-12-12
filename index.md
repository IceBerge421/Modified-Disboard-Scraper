![Discord Research Toolkit](https://psberge.com/wp-content/uploads/2021/11/toolkit-banner-scaled.jpg)

# A Discord Research Toolkit

### By PS Berge <!-- omit in toc -->

:bird: [@theiceberge](https://twitter.com/theiceberge) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:envelope: [hello@psberge.com](mailto:hello@psberge.com)

## <a name='TableofContents'></a>Table of Contents <!-- omit in toc -->

- [A Discord Research Toolkit](#a-discord-research-toolkit)
  - [Introduction](#introduction)
  - [Google Colab Scraper](#google-colab-scraper)
  - [Zotero Library](#zotero-library)
  - [Discord Critical Research Network](#discord-critical-research-network)
  - [Additional Resources](#additional-resources)
    - [Discord's Developer Server](#discords-developer-server)
    - [Archival Repository Tracking Discord Updates](#archival-repository-tracking-discord-updates)
    - [Official Discord Links](#official-discord-links)
  - [Breaking Ground: The Obstacles of Studying Discord](#breaking-ground-the-obstacles-of-studying-discord)
    - [Novelty](#novelty)
    - [Few Extant Tools](#few-extant-tools)
    - [Closed Systems](#closed-systems)
  - [Scraping Disboard: A Methodology](#scraping-disboard-a-methodology)
  - [Working With Disboard Data](#working-with-disboard-data)
    - [Python](#python)
    - [Orange Data Mining Tools](#orange-data-mining-tools)
    - [AntConc Concordance Tools](#antconc-concordance-tools)
  - [Other Approaches](#other-approaches)
    - [Discord-Scraper by Dracovian](#discord-scraper-by-dracovian)
  - [Get Involved!](#get-involved)
  - [Updates and Disclaimer](#updates-and-disclaimer)

## Introduction

Over the past year, I’ve been lucky enough to connect with a handful of Discord researchers. Each time, without fail, we have the same exchange—one of us shakes our head and says “yeah… Discord is *critically* understudied.”

What an understatement.

As of this writing, Discord is arguably one of the most rapidly expanding social media platforms. It’s increasingly becoming a go-to tool for remote teaching and academic spaces (hell, I’ve had to join almost 10 different conference and academic servers in this last year alone!). While some studies have come forward evaluating Discord’s pedagogical success as a classroom management tool (e.g. Arifianto & Izzudin, 2021), relatively little scholarship has tackled the networked implications of Discord’s ecosystem, the platform's culture, or the practices of users.

It's in response to this urgent gap in knowledge that we're sharing this toolkit. Specifically, I’m writing this to accompany an article I have coming out with my friend and colleague, Daniel Heslep, in *New Media and Society* [*link once we have one*] that examines the metadata of 2,741 Discord communities as hosted on server bulletin site Disboard.  We are especially glad to finally be sharing this work because this study is, to our knowledge, one of the first longitudinal studies of hate networks on Discord.

But while our study is, we hope, a useful model for discussing hate networks on the platform—it is only a small glimpse at the larger breadth of Discord communities. There remains so much work to be done in examining Discord through the lens of technology and culture. But we can’t do much without established methods, tools, or community. That’s why I’m happy to say that, alongside the publication of Dan and my article at *NMS*, we are releasing this makeshift toolkit for our fellow Discord researchers that includes:

- A public GitHub repository, which contains the [**modified scraper code**](https://github.com/IceBerge421/Modified-Disboard-Scraper/tree/master) (with some improvements) that we used to collect Discord server data in our *NMS* study. I have also made a [**Google Colab version of the scraper**](https://colab.research.google.com/gist/IceBerge421/2918ea145c5385b82e0e1de56fcfcf20/disboard-scraper.ipynb) which ***requires no coding knowledge whatsoever to use!*** Start collecting data in less than five minutes-- simply copy and run the notebook out of your own Google Drive folder.
-	A shared [**Zotero library**](#zotero-library) of all extant research we have gathered on Discord as well as a comprehensive [**list of resources**](#additional-resources) (links to important blogs, videos, historical wikis, and more).
-	A public invite to a [**Discord community for Discord researchers**](#discord-critical-research-network) (which we’re calling the Discord Critical Research Network—or DisCRN). Please, join us if you're interested!
- This blog post, which contains an overview of [**current obstacles for Discord researchers**](#breaking-ground-the-obstacles-of-studying-discord) and some reflections on [**our methodology and using Disboard to examine Discord's ecology**](#scraping-disboard-a-methodology).

**We are sharing these as a starting place for aspiring Discord researchers in the hope that people will take, adapt, and improve our methods-and ultimately begin to close the research gap on Discord as a platform. We encourage you to use, share, teach, and remix our tools and resources.**

All we ask is for two things:

1. The project of our study has been to systematically expose hate networks on Discord. Specifically, identifying patterns of recruitment and networking by fascist, racist and white-supremacist, transphobic and homophobic, sexist, and ableist networks. We do this for the purpose of holding Discord accountable and dismantling the hegemonic systems of oppression embedded into cultural technologies. <br><br>*If you are using our tools, we expect that your work, likewise, will not reinforce hegemonic systems of oppression but expose those systems and help hold platforms accountable*. Additional information on the important work of cyberfeminist and digital humanist scholars dismanteling hegemonic structures through  platform studies can be found in the resources section.

2. Please credit myself and Dan appropriately by citing our study and/or this toolkit. 😊 [TK - citation once we have it].

## Google Colab Scraper

[<img height="100" width="100" src="https://unpkg.com/simple-icons@v5/icons/googlecolab.svg" />](https://colab.research.google.com/gist/IceBerge421/2918ea145c5385b82e0e1de56fcfcf20/disboard-scraper.ipynb)

If you're looking to quickly collect your own data from Disboard, check out the Google Colab version of the scraper here!

## Zotero Library

[<img src="zotero-square.svg" width="100" height="100">](https://www.zotero.org/groups/4518959/discord_literature) 

Join our Zotero group and view our library of Discord literature here!

## Discord Critical Research Network

<iframe src="https://discord.com/widget?id=912414026988937246&theme=dark" width="100%" height="250" allowtransparency="true" frameborder="0" sandbox="allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts"></iframe>

Are you currently researching Discord? Come join our Discord (yes, we understand the irony!). We're looking to connect Discord scholars, circulate resources and new literature, and help keep the pulse on a rapidly-shifting social media platform.

*Graduate students and early-career folks are especially welcome!*

## Additional Resources

### [Discord's Developer Server](https://discord.gg/discord-developers)

Most of Discord's discussions about new features, community events, etc., are advertised in its semi-public server for Discord developers.

### [Archival Repository Tracking Discord Updates](https://github.com/Discord-Datamining/Discord-Datamining/commits/master)

In addition to the official changelog, this repository tracks literally every change to Discord's sourcecode alongside small comments that explain what has been changed. This is an incredible code archive for how Discord is changing.

### Official Discord Links
Important links to Discord's official policies, pages, and marketing.

- [Discord's Community Guidelines](https://discord.com/guidelines)
- [Discord's YouTube Channel](https://www.youtube.com/channel/UCZ5XnGb-3t7jCkXdawN2tkA)
- [Discord's Safety Center](https://discord.com/safety) <br>

![Discord: Imagine a Place. From Discord: The Movie. Awkwafina and Danny DeVito ](https://i.ytimg.com/vi/3xOkZ0_Rocs/maxresdefault.jpg)
*Awkwafina and Danny DeVito featured in Discord's newest marketing push ("Discord: The Movie").*

## Breaking Ground: The Obstacles of Studying Discord

There are no shortage of answers as to *why* Discord remains an understudied platform.  It is undoubtedly a combination of factors, some unique to the platform and some shared by other social networks. Below, I characterize a few of these most signficiant obstacles for those interested in studying Discord. As important as it is to share tools and resources, we also require wary attention to the challenges ahead:

### Novelty

Discord is a relatively nascent platform (founded in 2015)—and very quickly pivoted from being a niche, gaming-centric service to a widespread tool used by educators, artists, public figures, and companies. Much of the earliest research on Discord (such as Brown Jr. & Hennis, 2019) identifies Discord as a platform exclusively for gamers. Yet, as Discord's marketing shows: the platform is in the midst of an enormous rebranding to broaden its userbase. This undertaking has won them a lot of attention—[interviews on NPR](https://www.npr.org/2021/04/01/983159051/why-does-discord-not-use-ads-and-why-is-microsoft-interested-we-asked-discords-c), numerous headlines, and a several-billion-dollar valuation from Microsoft (in an offer which Discord turned down). For many, Discord has only recently emerged as worthy of examination as a mainstream social media platform. While this means that more eyes are on Discord and new attention is being placed on the platform, we have also noted that Discord's legacy as a gaming-centric space has alienated some researchers.

Along with this comes the difficulty of studying a still-emerging platform: in the time it took our study to finish peer review and editing, several of Discord's services that we note had already changed significantly: the 7000 member requirement for Discovery had been lowered to 1000, and the Live Stage feature had been launched and quickly sunsetted! As Discord shuffles its public rhetoric, its audience, and adapts its features, it's going to be important that researchers are equipped to keep up with the rapid changes of Discord's evolutions.  

### Few Extant Tools

Discord researchers face another problem that’s always been persistent in internet scholarship: *the better the tools to study for a platform, the more that platform will be researched.* It’s a sentiment often used to point out how sites like Twitter are comparatively ‘over-researched’ compared to other internet platforms. While social science and digital humanist tools integrate easily with Twitter, Instagram, YouTube, and other mainstream social networks—chat-based applications are less often supported. Discord, as a strange blend between social platform and chat application, has few publicly known tools and few established methods or approaches.

It’s our hope that this toolkit can begin to alleviate this—building, modifying, and circulating new tools for analysis.

### Closed Systems

Perhaps the most significant obstacle to Discord research is the closed nature of servers themselves. According to Discord’s usage statistics, there are over 19 million active communities, yet a vast majority of these are not public facing. Most are private, ‘invite only’ servers that can only be accessed via a direct link. Although Discord servers can designate themselves as ‘community servers’ with a permanent, public invite link—there are some additional complications:

- An invite link is still required, even to join ‘public’ community servers (blurring the line between public and private spaces).
- Community servers must have, as of November 2021, at least 1000 members in order to qualify for Discord’s 'Discovery' feature (which makes them searchable within the platform).

This creates a number of difficulties for internet scholars. Because these communities require the user to be logged in to Discord and receive an ‘invite link’ (even if that invite is publicly available), many researchers will need to get approval from a research board to conduct studies within any Discord server. For broader studies, this often means getting IRB approval for *every community* that the researcher intends to investigate. Public servers (such as those in the Discovery menu) and community servers with links online remain a grey area in academic study, and I’ve heard from colleagues at several institutions who received entirely different guidance on whether to treat such Discord servers as private or public for the purposes of collecting data. Arguably, this is a space where we need more specific clarification from the academy, internet studies, and review boards in how we approach 'closed-system' networks like Discord.

Discord also creates immense precarity for researchers investigating hostile networks, predatory behavior, and hate groups: not only must the researcher join a server as a public member to view its content and activity but—as we note in our study—hate-oriented servers often set up security features including ID-checks, raid-requirements, and  skin-tone verification (Yep. That really happens.) before allowing participants to view certain channels. This means that researchers must expose and potentially implicate themselves to gain access to these communities. Although there are a handful of scrapers that allow for gathering of text/image data from Discord text channels (a full breakdown of which are available in the **Resources** section [TK]), in many cases, getting access to the text in the first place requires the researcher to expose themselves or engage the community directly.

Our study circumnavigates many of these difficulties by examining the irrefutably public metadata of Discord servers. But while this is a useful angle (and one we hope more scholars will make use of) it is not a solution. We must find a way to approach Discord both from a longitudinal, networked perspective—and through embedded and ethnographic approaches that can recognize the nuance of activity within communities.

Yet this assumes that researchers can even *find* these communities in the first place. The 1000 member minimum to qualify for Discord’s discovery feature (which must be applied for) means that what Discord provides is, at best, a cursory glimpse of only the most popular servers on the platform. Dan and I note this ‘iceberg effect’ in our study—Discord is able to curate an illusory public of partnered and verified servers while obscuring the activity of less-popular communities.

Our solution to this is imperfect, but it is a step forward. We rely on third-party bulletin site Disboard (which is not technically affiliated with, though sure loves to imitate, Discord). By scraping public server listings on Dis*board*, we are able to get a glimpse into the ‘darkside’ of Discord communities (those not made visible by search).

Below, I break down how to replicate our methods by using my fork of the Disboard scraper (provided on GitHub). I’ve specifically set up the instructions to be friendly to newcomers with little Python experience. We hope that giving scholars a way to quickly examine networks of servers through Disboard will empower further research into Discord communities.

## Scraping Disboard: A Methodology
*Note: This is not a technical guide for installing my fork of the Disboard scraper. For that, please see the [repository here]( https://github.com/IceBerge421/Modified-Disboard-Scraper/tree/master)!*

I want to share some of our reasoning for  *how* and *why* one might scrape Disboard in the first place, how we have gone about it, and what further interests this tool might serve for aspiring Discord scholars.

I’ll begin with the basics: Disboard is a public bulletin site for Discord servers. It gets listings from servers which have installed Disboard’s bot (a third-party program) and shares the following data about each community:

- The server name.
- A description.
- The number of members currently online.
- An invite link to the server.
- (Up to) five descriptive tags, chosen by the lister.

The scraper we use for Disboard is a fork of a repository originally coded by *DiscordFederation* (specifically, daegontaven) on GitHub. Our iteration on this is largely reliant on the original code; I'm immensely grateful to daegontaven for providing this repository with the generous MIT 3.0 license. That said, our scraper varies in a few key ways, namely by 1) collecting descriptions 2) using a sleep-timer to allow large-scale scraping without becoming rate limited and 3) some basic HTML cleanup features. When you run the scraper, you simply input a search term, and the scraper will collect every server that includes that token as one of its five tags on Disboard (note that this process is *tag-based* not name-based). Finding tags to scrape can be done simply by searching Disboard, and exploring what tags you might ultimately want to scrape. In designing your study, you should leave the opportunity for adding additional tags later, as you will almost certainly encounter co-occurring tags that you will want to add to your sample.<br><br>

![Toxic Server Network](https://psberge.com/wp-content/uploads/2021/11/toxic-server-plot-scaled.jpg)
*A visualization of tags linked to 'toxic' Discord servers, scraped from Disboard.*

Scraping Disboard provides brief previews of how Discord communities are publicly marketing themselves. Note that this method **does not scrape any information from these servers!** However, by looking at these public names, descriptions, and tags, one is able to:

-	Break through the ‘iceberg effect’ of Discord, by examining servers not otherwise searchable (smaller servers, servers that don’t *want* to be listed on Discord, and servers that failed the safety requirements of Discovery).

-	See how servers are attracting new users. These descriptions generally focus on recruiting new members to the community—and, as we show in our study, there is much to examine about how these spaces are marketing themselves to new users.

-	View Discord as a networked system. By examining these tags, we can quickly get a sense of how Discord’s broader ecology is networked. Because users select the tags for their networks, they are choosing to present their community under certain search terms. (See above for an example of a network visualization of co-occurring tags from >4000 “toxic” servers).

Again, this isn’t perfect: Disboard lists just over 1 million Discord servers (of 19 million on the platform). Yet scraping Disboard provides a more robust sampling of communities than anything within Discord’s own systems. Notably, Disboard is not the only bulletin site worth examining for such inquiries into Discord, [Top.gg](https://top.gg/), [discordservers.com](https://discordservers.com/), and even Discord's own Discovery all provide partial-but-useful glimpses into the broader practices of communities.<br><br>

![Tag Search Example](https://psberge.com/wp-content/uploads/2021/11/disboard.jpg)
*An example tag-search on Disboard.*

## Working With Disboard Data

Once you've collected data from a number of tags on Disboard, you'll have anywhere between one and several dozen CSV files with server data. Making use of such data will depend on the object of your study. If you are a social scientist, digital humanist, or internet researcher interested in exploring relationships between servers, the discourse of certain communities, or activity levels over time, you will likely want to borrow from some of our methods directly. Using your data, you can:

- Track relationships between different tag-clusters using Python.
- Code and analyze server descriptions using close and distant reading.
- Quantitiatively explore the popularity of tags and terms, and examine how they are being used in context.

Such approaches allow us to assess relationships between the discursive elements of these communities. Such work opens multiple considerations for how power (in the cyberfeminist sense) is being distributed across the network. As our study has shown, despite the alleged privacy of Discord communities, hate groups readily mobilize against marginalized communities on these networks. Bringing in the additional, networked context of Disboard data should be done with careful consideration for how technology and discourse shape and are shaped by power dynamics. If you're looking to develop such research, here are a few key recommendations for crucial literature in this area:

- Dr. André Brock, Jr.'s award-winning book [*Distributed Blackness: African American Cybercultures*](https://nyupress.org/9781479829965/distributed-blackness/) and his important article on [Critical Technoculture Discourse Analysis](https://journals.sagepub.com/doi/10.1177/1461444816677532). Brock's framework for approaching cyberculture focuses on bringing both technology and contextualizing discourse in conversation with one another. While Disboard data may provide useful *context* for research, it is important that we qualify that data with other cultural and technological forces.

- [*Data Feminism*](https://mitpress.mit.edu/books/data-feminism) by Catherine D'Ignazio & Lauren Klein (2020). *Data Feminism* clarifies not only important practices for researchers, but clarifies the dyanmics of power and hegemony in social media networks. Understanding cyberfeminist approaches to technology are important in thinking about the complexity of Discord communities and networks.

In addition to theoretical tools, there are a few technical tools that I highly recommend to support your analysis of Discord data, especially in high volumes. (A planet-sized thank-you to Dr. Anastasia Salter and the UCF Texts & Technology faculty for teaching me everything I know about these tools!):

### Python

Python is going to be the most effective tool for quickly examining your Disboard data. If you're unfamiliar with Python, or want a few quick tools to get started, **I've made a jupyter notebook with some of my go-to functions for looking at data from Disboard CSV files** [TK - Link once I have it].

### [Orange Data Mining Tools](https://orangedatamining.com/)

Orange is a robust toolset for examining data, including text. You'll want to install the 'text tools' plugin, which provides many of the same functionalities as Python, but with no coding experience required. There are many tutorials on Orange, but I recommend starting with this [wonderful guide from an NEH course on Understanding Digital Culture](https://understandingdigitalculture.hcommons.org/lesson/module-4-2-intro-to-orange/) put together by some of the rockstar faculty at UCF's T&T program.

### [AntConc Concordance Tools](https://www.laurenceanthony.net/software/antconc/)

AntConc is like CTRL+F with a nuclear jetpack. It allows you to quickly search through your dataset and find co-occurring words and tokens, and works with high volumes of data (even dozens of different files, so you can keep your tag-based data seperate).

You can watch my (very goofy) tutorial on using AntConc for digital humanist work here:

<iframe width="100%" height="315" src="https://www.youtube.com/embed/c3KUqUnOY_E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Other Approaches

Although the tools described above are great for examining the discourse, rhetoric, and networks of Discord communities, I hope these tools can bolster other approaches as well. I'm aware, for example, that this work has significant implications for scholars focusing on extremism, hate, and predatory behavior online (I was surprised to find several dozen criminology scholars in my Twitter follows after the announcement of our work in *NMS*).

For those interested in behavior and activity within Discord communities, these methods can be useful for providing important context and helping internet scholars identify ideal spaces for research. For **digital ethnographers**, Disboard provides a way to quickly scout communities for potential study. Using this data, one can quickly find:

- The most popular communities using a certain tag (sorting by active member count).
- Commonly co-occurring tags, allowing one to easily snowball and find other relevant samples.
- A way to easily identify public-facing communities, which may be more receptive to interviews or other kinds of study.
- Whether or not a community is a part of a network of same-name or associated servers (such as the white-supremacist recruitment networks we identified in our study).

We hope these tools will bolster more qualitative, ethnographic, and deep-dive approaches to Discord communities. Although there remains far too little ethnographic study of Discord and Discord users, there are two important studies which are worth spotlighting:

- Nicholas-Brie Guarriello's article ["Not Going Viral: Amateur Livestreamers, Volunteerism, and Privacy on Discord"](https://mpcaaca.org/wp-content/uploads/2021/10/SI10_Guarriello.pdf) (2019) examines, through embedded study, gaming livestream communities on Discord, and the precarity of copyright, privacy for Discord gaming communities. She also highlights the impact of COVID-19 on Discord spaces as well as intersections between gaming and Discord culture.
  
- Jiang et. al's study ["Moderation Challenges in Voice-based Online Communities on Discord"](https://dl.acm.org/doi/10.1145/3359157) (2019) remains one of the most exhaustive interview-based studies of user activity and behavior within Discord communities. The authors interviewed 25 different moderators, and write extensively about the challenges of moderation, and Discord's technical affordances (bots, roles, etc.).

There are also several additional technical tools that can support community or user-specific research:
### [Discord-Scraper by Dracovian](https://github.com/Dracovian/Discord-Scraper)

This scraper allows you to pull messages from Discord text channels (and even direct messages) and store them. Note that such scraping will usually require approval from a Review Board, but for ethnographic and even interview-based studies this can be enormously helpful.

Note that technically performing automized tasks from a personal Discord account violates Discord's terms and conditions. Ideally, this is best done by setting up a bot and collecting messages that way.

[Full annotation TK]. [More resources TK].

## Get Involved!

A big part of changing the landscape of Discord research is through community. If you or your research team need additional support in setting up tools for studying Discord, please don't hesitate to **contact me** ([@theiceberge](https://twitter.com/theiceberge) or [hello@psberge.com](mailto:hello@psberge.com)). Likewise, if you want to network with other researchers or have resources to contribute to this toolkit, please **join the DisCRN server** [link TK!] or message me!

![Join our Discord!](https://psberge.com/wp-content/uploads/2021/11/DisCRN-Banner-scaled.jpg)

## Updates and Disclaimer

*This toolkit was last updated on 11.23.2021 by PS Berge.*

Note that I am providing these tools to empower Discord researchers in the academic community. I am in no way taking responsibility for the things you do with these tools! As stated above, I expect that if you will not use our tools or methods to harass others, reentrench hegemonic systems, or perform unethical research practices. Although these methods help circumnavigate deprecated limitations by research boards **that does not mean your research should not be rigorously guided by an ethical framework**. If you are unfamiliar with designing ethical study design for internet research, a good place to start is the [Association of Internet Researchers Ethics Guidelines](https://aoir.org/ethics/).