Summary
Looking for an experienced Next.js / Full Stack Developer to finish the remaining integration and sync tasks for my SaaS platform, Surfa - an AI-powered Local SEO tool that connects with Google Business Profile (GBP) and DataForSEO APIs.

The core app is already functional and deployed (GBP-allowlisted + DataForSEO verified). I now need help completing the last 10% so it’s fully production-ready and stable for all users.

What’s Working Now:

- Full Google OAuth + multi-GBP connection flow (Dashboard, Listings, Reports)
- Dynamic insights via GBP API
- Keyword tracking + suggestions via DataForSEO
- Deployed on Vercel with working environment variables
- Reviews and metrics load correctly on the developer’s side


Remaining Tasks:

1️⃣ Review Response Center

- Ensure reviews sync and display correctly for all user GBPs, not just mine.
- Make sure review replies posted inside Surfa are synced to the actual GBP profile.
- Fix edge cases where reviews take too long to fetch or time out.

2️⃣ Rankings (DataForSEO)

- Improve suggested keywords relevance (use GBP categories + location context).
- Ensure tracked keywords are isolated to each GBP - not shared across profiles.
- Confirm all data (rank, change, volume, status) is dynamic and accurate.

3️⃣ Stripe Integration

- Implement Stripe checkout/subscriptions (plans already set up in env).
- Add webhook handling for successful payments + user access levels.

4️⃣ Performance Improvements

- Make Dashboard and pages load instantly after login (reduce API latency).
- Optimize review sync time and general API call speed.

Tech Stack:

- Next.js / React / TypeScript
- Supabase (Auth + DB)
- Google Business Profile API (allowlisted)
- DataForSEO API
- Stripe API (already configured in .env)
- Vercel Hosting

Ideal Candidate:
- 3-5+ years with Next.js/Supabase/Stripe/Google APIs
- Proven experience debugging API sync issues
- Able to start immediately and deliver results fast
- Communicates clearly with short, frequent updates

If you’re confident you can wrap this up cleanly and make Surfa fully production-ready, apply and mention how soon you can start.

Deliverables
- Fully dynamic, production-ready build on Vercel
- Reviews + Rankings sync correctly across all GBPs
- Stripe billing flow tested in both test & live mode
- Fast loading (no need to refresh Dashboard/Reports)