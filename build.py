"""Builds every page of the GTA Shorts Studio website: python build.py (writes the .html files next to it).

The log-in itself is a Cloudflare Worker (gta-shorts-studio-login, source in the Studio's repo, site-login/).
"""
import pathlib

out = pathlib.Path(__file__).parent
LOGIN = "https://gta-shorts-studio-login.tradeskis26.workers.dev/login"
NAV = [("index.html", "Home"), ("features.html", "Features"), ("how-it-works.html", "How it works"),
       ("about.html", "About & contact"), ("privacy.html", "Privacy"), ("terms.html", "Terms")]
EMAIL = "dknapptravels@gmail.com"
UPDATED = "24 November 2026"


def page(file, title, desc, body):
    nav = "".join(f'<a href="{f}"{" aria-current=page" if f == file else ""}>{n}</a>' for f, n in NAV)
    nav += f'<a class="login" href="{LOGIN}">Log in</a>'
    foot = "".join(f'<a href="{f}">{n}</a>' for f, n in NAV[1:]) + f'<a href="{LOGIN}">Log in</a>'
    t = "GTA Shorts Studio" if file == "index.html" else f"{title} – GTA Shorts Studio"
    html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="assets/favicon-32.png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<meta property="og:title" content="{t}"><meta property="og:description" content="{desc}"><meta property="og:image" content="assets/icon-512.png">
<link rel="stylesheet" href="style.css">
</head><body>
<header class="site"><div class="wrap"><a class="brand" href="index.html"><img src="assets/icon-512.png" alt="">GTA Shorts Studio</a><nav class="main" aria-label="Main">{nav}</nav></div></header>
<main>
{body}
</main>
<footer class="site"><div class="wrap"><span>© 2026 GTA Shorts Studio · <a href="mailto:{EMAIL}">{EMAIL}</a></span><nav aria-label="Footer">{foot}</nav></div></footer>
</body></html>
"""
    (out / file).write_text(html, encoding="utf-8")


page("index.html", "Home", "GTA Shorts Studio turns long GTA gameplay streams into short vertical videos and publishes them to our own YouTube, Instagram and TikTok channels.", f"""
<section class="hero"><div class="wrap">
<div><h1>Long GTA streams in, finished Shorts out.</h1>
<p class="lead">GTA Shorts Studio is the editing and publishing studio behind our GTA gameplay channels. It finds the best moments in long streams, cuts them into vertical videos with captions, and posts them to our own YouTube, Instagram and TikTok accounts, with a person approving every clip.</p>
<a class="btn" href="{LOGIN}">Log in with TikTok</a><a class="btn ghost" href="how-it-works.html">See how it works</a></div>
<img class="mark" src="assets/icon-512.png" alt="GTA Shorts Studio icon">
</div></section>
<section class="block"><div class="wrap">
<h2>What the Studio does</h2>
<p class="sub">One place to go from a three-hour stream to a week of short videos, without losing track of what went where.</p>
<div class="grid">
<div class="card"><div class="num">1</div><h3>Finds the moments</h3><p>Reads a stream's transcript, chat and keyframes to find the funniest and most surprising stretches, and suggests where each clip should start and end.</p></div>
<div class="card"><div class="num">2</div><h3>Edits them for vertical</h3><p>Puts the streamer's webcam above the gameplay, adds readable captions and a short hook, and keeps every graphic inside each app's safe area.</p></div>
<div class="card"><div class="num">3</div><h3>Publishes on schedule</h3><p>Each approved Short is booked into a posting slot and goes to the matching channel on YouTube, Instagram and TikTok, the same clip at the same time.</p></div>
</div></div></section>
<section class="block alt"><div class="wrap">
<h2>Built around review</h2>
<p class="sub">Nothing posts until a person has watched it. The Studio rates, ranks and prepares clips; we decide which ones go out.</p>
<div class="grid">
<div class="card"><h3>Review queue</h3><p>Watch each Short, approve or reject it with a reason, fix the hook or the trim, and the Studio learns from every decision.</p></div>
<div class="card"><h3>Posting dashboard</h3><p>One view per platform shows every channel's last and next 24 hours: what posted, what is booked, what failed and how many views each post has.</p></div>
<div class="card"><h3>Credit and permission</h3><p>Every clip records the creator it came from and their clipping permission, and the creator is credited in the caption.</p></div>
</div></div></section>
""")

page("features.html", "Features", "Features of GTA Shorts Studio: moment finding, vertical editing, captions, review, scheduling and per-platform posting.", """
<section class="block"><div class="wrap">
<h1 style="font-size:40px;margin:0 0 12px">Features</h1>
<p class="sub">Everything the Studio does, from a long recording to a post on each platform.</p>
<h2>Finding clips</h2>
<div class="grid">
<div class="card"><h3>Stream scanning</h3><p>Long streams and VODs are scanned for their hottest stretches using the clips viewers made, live chat spikes and the transcript.</p></div>
<div class="card"><h3>Moment editor</h3><p>Each candidate is checked on keyframes and the timestamped transcript, then cut so it opens fast and ends on the payoff.</p></div>
<div class="card"><h3>Link clipping</h3><p>Paste a stream link with a time and the Studio clips just that moment.</p></div>
</div>
</div></section>
<section class="block alt"><div class="wrap">
<h2>Editing</h2>
<div class="grid">
<div class="card"><h3>Streamer and game stacked</h3><p>The webcam is found automatically and placed above the gameplay; a clip without the streamer's face in frame is flagged.</p></div>
<div class="card"><h3>Captions and hooks</h3><p>Word-timed captions from the speech, a short opening hook, and a highlight-first option that opens on the best second.</p></div>
<div class="card"><h3>Safety checks</h3><p>Burned-in captions from the source are hidden, slurs are bleeped, nudity is detected and blurred, and clips that are not GTA are held back.</p></div>
</div>
</div></section>
<section class="block"><div class="wrap">
<h2>Publishing</h2>
<div class="grid">
<div class="card"><h3>Posting schedule</h3><p>Approved Shorts are booked into fixed daily slots per channel, within each platform's posting limits.</p></div>
<div class="card"><h3>TikTok</h3><p>Posts through TikTok's Content Posting API after showing the account, the privacy choice, interaction settings and the commercial content disclosure.</p></div>
<div class="card"><h3>Performance</h3><p>View, like, comment and share counts of our own posts are read back so we can see which clips are working.</p></div>
</div>
</div></section>
""")

page("how-it-works.html", "How it works", "How GTA Shorts Studio connects to TikTok, YouTube and Instagram and publishes a Short, step by step.", f"""
<section class="block"><div class="wrap">
<h1 style="font-size:40px;margin:0 0 12px">How it works</h1>
<p class="sub">From a stream to a post, and exactly what the Studio does with each platform account.</p>
<ol class="steps">
<li><span class="num">1</span><div><h3>Log in with TikTok</h3><p>Press <a href="{LOGIN}">Log in</a> (or <strong>Connect with TikTok</strong> on a channel's page in the Studio). TikTok's own sign-in page opens; you sign in to the channel's account and approve the permissions. The Studio then shows which account is connected. <strong>Log out</strong> ends the session; <strong>Disconnect TikTok</strong> revokes the access at TikTok.</p></div></li>
<li><span class="num">2</span><div><h3>Clip and review</h3><p>The Studio clips a stream into candidate Shorts. Each one waits in Review, where a person watches it and approves or rejects it.</p></div></li>
<li><span class="num">3</span><div><h3>Choose how it posts</h3><p>Before a TikTok post the Studio reads the account's current settings and shows them: the account name, who can see the post (chosen by the user, never pre-selected), whether comments, duets and stitches are allowed (off until ticked), and the commercial content disclosure for branded or paid content.</p></div></li>
<li><span class="num">4</span><div><h3>Post now or on schedule</h3><p>The Short is posted straight away or at the channel's next posting slot. The post's link appears on the Posting dashboard as soon as the platform confirms it.</p></div></li>
<li><span class="num">5</span><div><h3>Track performance</h3><p>The Studio reads the view, like, comment and share counts of the videos it posted on the connected account, and shows them per channel and per platform.</p></div></li>
</ol>
</div></section>
<section class="block alt"><div class="wrap">
<h2>TikTok permissions we use</h2>
<div class="grid">
<div class="card"><h3><code>user.info.basic</code></h3><p>Shows which TikTok account is connected, by display name and profile picture.</p></div>
<div class="card"><h3><code>video.upload</code> and <code>video.publish</code></h3><p>Sends an approved Short to that account, as a draft or as a direct post with the settings chosen in step 3.</p></div>
<div class="card"><h3><code>video.list</code></h3><p>Reads the view, like, comment and share counts of the account's own videos for the Posting dashboard.</p></div>
</div>
<p style="margin-top:20px;color:var(--ink-2)">Access can be removed at any time with <strong>Disconnect TikTok</strong> (website) or <strong>Disconnect</strong> (Studio), or in TikTok under Settings and privacy › Security › Apps and services.</p>
</div></section>
""")

page("about.html", "About & contact", "About GTA Shorts Studio, who runs it, frequently asked questions and how to get in touch.", f"""
<div class="doc">
<h1>About &amp; contact</h1>
<p>GTA Shorts Studio is run by David Knapp. It is the tool behind our GTA gameplay channels, among them GTA 6 Secrets, GTA 6 NPC Moments, GTA 6 Lore, GTA 6 Chaos and GTA 6 Viral Moments, on YouTube, Instagram and TikTok.</p>
<p>The Studio is used by our team to run our channels. Team members log in with the TikTok account of the channel they manage.</p>
<h2>Contact</h2>
<p>Email <a href="mailto:{EMAIL}">{EMAIL}</a>. We answer within two working days.</p>
<p><strong>Creators:</strong> if a clip of your stream is on one of our channels and you would like it credited differently or removed, email us with the link and we will act on it promptly.</p>
<h2>Questions</h2>
<dl class="faq">
<dt>Where does the footage come from?</dt><dd>Our own gameplay, creators who run open clipping programs or gave us permission, and Rockstar Games' official material. Every clip credits its creator.</dd>
<dt>Does anything post without a person checking it?</dt><dd>No. Every Short is reviewed before it is booked to post.</dd>
<dt>What does the Studio do with TikTok, YouTube or Instagram data?</dt><dd>See the <a href="privacy.html">Privacy Policy</a> for exactly what is read, stored and for how long.</dd>
<dt>How do I log in or out?</dt><dd>Use <a href="{LOGIN}">Log in</a> at the top of every page. Log out ends your session; Disconnect TikTok on the account page revokes the Studio's access to your TikTok account.</dd>
</dl>
</div>
""")

page("privacy.html", "Privacy Policy", "How GTA Shorts Studio collects, uses, stores, shares and deletes data, including data from TikTok, YouTube and Instagram.", f"""
<div class="doc">
<h1>Privacy Policy</h1>
<p class="date">Effective and last updated: {UPDATED}</p>
<p>This Privacy Policy explains how GTA Shorts Studio ("the Studio", "we", "us") collects, uses, stores, shares and deletes information when you visit this website, log in with TikTok, or use the Studio to connect a TikTok, YouTube or Instagram account. By using the website or the Studio you agree to this policy. If you do not agree, please do not use them.</p>

<h2>1. Who we are</h2>
<p>GTA Shorts Studio is operated by David Knapp, an individual based in the United States, who is the data controller for the information described here. Contact: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

<h2>2. Information we collect</h2>
<p><strong>a. When you log in with TikTok.</strong> With your permission, TikTok gives us, under the scopes you approve:</p>
<ul>
<li><code>user.info.basic</code>: your TikTok open ID (an identifier unique to our app), display name and profile picture (avatar URL).</li>
<li><code>video.list</code> (only if you approve it in the Studio): the list of your public videos with their IDs, links and view, like, comment and share counts.</li>
<li><code>video.upload</code> and <code>video.publish</code> (only if you approve them in the Studio): permission to send videos you choose to your account. We receive the publish status and the resulting post ID.</li>
<li>An access token and a refresh token that let the Studio act on your behalf within those scopes.</li>
</ul>
<p>We never receive your TikTok password, phone number, email address, messages, followers list, or any data about other TikTok users.</p>
<p><strong>b. When you connect YouTube or Instagram in the Studio.</strong> Through Google OAuth (<code>youtube.upload</code>, <code>youtube.readonly</code>, <code>yt-analytics.readonly</code>) and Meta's Instagram API: the channel or account name and ID, access tokens, and statistics of the videos posted through the Studio (views, likes, comments, shares, retention).</p>
<p><strong>c. Content you create.</strong> Video files, transcripts of their audio, captions, titles and hashtags made in the Studio.</p>
<p><strong>d. Website visits.</strong> This website uses no analytics, advertising or tracking cookies. The log-in page sets two strictly necessary, HttpOnly cookies: a one-time security code during sign-in (deleted after 10 minutes) and an encrypted session cookie holding your access token (deleted when you log out, or after 24 hours). Our hosting providers (GitHub Pages and Cloudflare) may process your IP address and browser details in their server logs to deliver and protect the site.</p>

<h2>3. How we use information</h2>
<ul>
<li>To show which TikTok, YouTube or Instagram account is connected (display name and picture).</li>
<li>To publish the videos you approve to the account you choose, with the privacy level, interaction settings and disclosure you select for each post.</li>
<li>To show the performance of videos posted through the Studio on its dashboard.</li>
<li>To keep the service secure, prevent misuse and fix errors.</li>
<li>To answer your messages and handle removal requests.</li>
</ul>
<p>We do not use your information for advertising, we do not sell or rent it, we do not build profiles of you, and we do not use TikTok data to train artificial-intelligence models.</p>

<h2>4. Legal bases (EEA, UK and Switzerland)</h2>
<p>Where these laws apply, we process your information to perform our service at your request (contract), on the basis of your consent given on TikTok's, Google's or Meta's permission screen (which you can withdraw at any time), and for our legitimate interests in keeping the service secure.</p>

<h2>5. How we share information</h2>
<p>We share information only as follows:</p>
<ul>
<li><strong>TikTok, Google (YouTube) and Meta (Instagram)</strong>: the videos and captions you choose to publish are sent to the platform you choose, under that platform's own privacy policy.</li>
<li><strong>Service providers</strong> that process data for us under their terms: Cloudflare (log-in page hosting), GitHub (website hosting), Buffer (scheduling some posts), and Anthropic (short transcript excerpts and a few low-resolution video frames, to judge clips and write captions; never your TikTok account data).</li>
<li><strong>Legal reasons</strong>: if required by law, a court order, or to protect the rights, safety or property of anyone.</li>
</ul>
<p>We never sell or share personal information for cross-context behavioral advertising.</p>

<h2>6. Storage and security</h2>
<p>Access tokens are encrypted in transit (HTTPS) and at rest: on the website, in an AES-GCM encrypted HttpOnly cookie; in the Studio, in the operating system's credential store or an encrypted file on our own computers. Client secrets stay on the server and never reach your browser. Access is limited to the operator. No method of storage is completely secure, but we take reasonable measures to protect your information and will notify affected users of a breach as the law requires.</p>

<h2>7. How long we keep information</h2>
<ul>
<li>Website session cookie: until you log out, or 24 hours at most.</li>
<li>Studio access tokens: until you disconnect the account or revoke access; TikTok refresh tokens expire after 365 days.</li>
<li>Video statistics and post links: for as long as the post is live, and deleted within 30 days after you ask.</li>
<li>Working video files: deleted automatically after 14 days.</li>
</ul>

<h2>8. Your choices and rights</h2>
<ul>
<li><strong>Revoke access</strong> at any time: Disconnect TikTok on this website's account page, Disconnect in the Studio, or in TikTok under Settings and privacy › Security › Apps and services (Google: myaccount.google.com/permissions; Meta: Settings › Apps and websites).</li>
<li><strong>Access, correction, deletion and portability</strong>: email <a href="mailto:{EMAIL}">{EMAIL}</a> and we will respond within 30 days (45 days where California law allows). We may need to verify that the request comes from the account holder.</li>
<li><strong>California residents</strong> (CCPA/CPRA): you have the right to know what personal information we collect, use and disclose, to delete it, to correct it, and not to be discriminated against for exercising these rights. We do not sell or share personal information, and we do not use or disclose sensitive personal information.</li>
<li><strong>EEA/UK residents</strong> (GDPR): you also have the right to object to or restrict processing, and to complain to your local data protection authority.</li>
</ul>

<h2>9. Children</h2>
<p>The website and the Studio are not directed at children under 13 (or the minimum age in your country), and we do not knowingly collect their information. If you believe a child has given us information, email us and we will delete it.</p>

<h2>10. International transfers</h2>
<p>We are based in the United States and our providers may process data in other countries. Where required, transfers rely on the providers' standard contractual clauses or equivalent safeguards.</p>

<h2>11. Third-party services</h2>
<p>Your use of TikTok, YouTube, Google and Instagram is governed by their own terms and privacy policies, which we encourage you to read: TikTok Privacy Policy (tiktok.com/legal/privacy-policy), Google Privacy Policy (policies.google.com/privacy) and Meta Privacy Policy (facebook.com/privacy/policy). The Studio's use of YouTube data follows the YouTube API Services Terms of Service.</p>

<h2>12. Changes to this policy</h2>
<p>We will post any change on this page with a new date above. If a change is material, we will say so on the log-in page before it takes effect.</p>

<h2>13. Contact</h2>
<p>Questions, requests or complaints: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
</div>
""")

page("terms.html", "Terms of Service", "The terms that apply to the GTA Shorts Studio website, its TikTok log-in and the Studio.", f"""
<div class="doc">
<h1>Terms of Service</h1>
<p class="date">Effective and last updated: {UPDATED}</p>
<p>These Terms of Service ("Terms") are an agreement between you and David Knapp, operator of GTA Shorts Studio ("we", "us"), and govern your use of this website, its TikTok log-in, and the GTA Shorts Studio software (together, "the Service"). By using the Service you accept these Terms and our <a href="privacy.html">Privacy Policy</a>. If you do not accept them, do not use the Service.</p>

<h2>1. Eligibility</h2>
<p>You must be at least 18 years old, or the age of majority where you live, and able to form a binding contract. You must also meet the minimum age and other requirements of every platform you connect. If you use the Service for an organisation, you confirm you may bind it to these Terms.</p>

<h2>2. The Service</h2>
<p>The Service edits gameplay footage into short videos and publishes them, at your direction, to TikTok, YouTube and Instagram accounts you connect. It is provided to our team for the channels we run. We may change, suspend or stop any part of it at any time.</p>

<h2>3. Your accounts and log-in</h2>
<p>You log in with your TikTok account through TikTok Login Kit and connect other platforms through their official sign-in. You may connect only accounts you own or are authorised to manage. You are responsible for activity under your connected accounts and for keeping your own platform credentials secure; we never ask for or receive your platform passwords. You can log out and revoke access at any time.</p>

<h2>4. Publishing and platform rules</h2>
<p>Every post is made at your direction. Before each TikTok post the Service shows the destination account, lets you choose the privacy level (never pre-selected), whether comments, duets and stitches are allowed (off unless you turn them on), and the commercial content disclosure. You must follow the terms, community guidelines and policies of each platform, including TikTok's Terms of Service, Community Guidelines and Branded Content Policy, YouTube's Terms of Service, and Meta's Terms of Use, and must disclose paid or branded content where required.</p>

<h2>5. Your content</h2>
<p>You keep all rights to the content you create and publish. You grant us a limited licence to host, process, edit and transmit that content solely to provide the Service to you. You confirm you have the rights and permissions needed for any footage, music or other material you publish, including any creator's permission, and that your content does not infringe anyone's rights or break any law.</p>

<h2>6. Acceptable use</h2>
<p>You must not use the Service to: post content that is illegal, hateful, harassing, sexually explicit, violent or misleading; infringe intellectual property or privacy rights; send spam or artificially inflate engagement; impersonate anyone; access accounts you are not authorised to manage; interfere with or reverse-engineer the Service or any platform's API; or exceed or evade any platform's rate limits or rules.</p>

<h2>7. Copyright complaints</h2>
<p>If you believe content published through the Service infringes your copyright, email <a href="mailto:{EMAIL}">{EMAIL}</a> with the work, the link to the post, your contact details, and a statement that you are the owner or authorised to act for them. We will act promptly, which may include removing the post.</p>

<h2>8. Third-party services</h2>
<p>The Service relies on TikTok, Google, Meta, Buffer, Cloudflare and others. Their services are governed by their own terms, and we are not responsible for their availability, changes or actions, including any decision they make about your account or content.</p>

<h2>9. Termination</h2>
<p>You may stop using the Service and revoke its access at any time. We may suspend or end your access if you break these Terms, if a platform requires it, or if we stop the Service. Sections 5 (licence ends when your content is deleted), 10, 11, 12 and 13 survive termination.</p>

<h2>10. Disclaimers</h2>
<p>THE SERVICE IS PROVIDED "AS IS" AND "AS AVAILABLE", WITHOUT WARRANTIES OF ANY KIND, WHETHER EXPRESS OR IMPLIED, INCLUDING MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE AND NON-INFRINGEMENT. WE DO NOT PROMISE THAT THE SERVICE WILL BE UNINTERRUPTED, ERROR-FREE OR SECURE, OR THAT ANY POST WILL BE PUBLISHED OR REACH ANY AUDIENCE.</p>

<h2>11. Limitation of liability</h2>
<p>TO THE FULLEST EXTENT PERMITTED BY LAW, WE WILL NOT BE LIABLE FOR ANY INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL OR PUNITIVE DAMAGES, OR ANY LOSS OF PROFITS, REVENUE, DATA, FOLLOWERS OR GOODWILL, ARISING FROM YOUR USE OF THE SERVICE. OUR TOTAL LIABILITY FOR ANY CLAIM RELATING TO THE SERVICE IS LIMITED TO ONE HUNDRED US DOLLARS (US$100). SOME JURISDICTIONS DO NOT ALLOW THESE LIMITS, SO THEY MAY NOT APPLY TO YOU.</p>

<h2>12. Indemnity</h2>
<p>You agree to defend and indemnify us against any claim, loss or expense (including reasonable legal fees) arising from your content, your use of the Service, or your breach of these Terms or of any platform's rules.</p>

<h2>13. Governing law and disputes</h2>
<p>These Terms are governed by the laws of the United States and of the state in which the operator resides, without regard to conflict-of-law rules. Before filing any claim, you agree to contact us at <a href="mailto:{EMAIL}">{EMAIL}</a> and try to resolve it informally for 30 days. Any claim that is not resolved will be brought in the state or federal courts located where the operator resides, and you and we consent to their jurisdiction. Either party may bring a qualifying claim in small-claims court.</p>

<h2>14. Changes</h2>
<p>We may update these Terms. We will post the new version on this page with a new date, and, for material changes, say so on the log-in page before they take effect. Continuing to use the Service after that means you accept them.</p>

<h2>15. General</h2>
<p>These Terms and the Privacy Policy are the whole agreement between you and us about the Service. If any part is unenforceable, the rest remains in effect. Our failure to enforce a right is not a waiver. You may not transfer these Terms without our consent; we may transfer them with the Service.</p>

<h2>16. Contact</h2>
<p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
</div>
""")
