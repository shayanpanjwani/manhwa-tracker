# Manhwa Tracker - Project Specification

## Executive Summary

**Problem:** When reading manhwas across multiple browser tabs on mobile, I lose track of which series I'm reading, where I left off, and how long it's been since I last read. Checking progress across multiple series requires opening each tab sequentially, which is tedious and leads to abandoning series.

**Solution:** A mobile-first web app that allows quick logging of reading progress and provides an at-a-glance view of all series, last chapter read, and when I last read each one.

**Target User:** Myself (primary), then potentially other manhwa readers who aggregate-read on mobile.

---

## Current Reading Workflow

1. I read on my iPhone using Brave or Safari (private browsing) to access aggregator sites, primarily MangaRead.org
2. For new series discovery, I browse recently updated series and filter by preferred tropes (reincarnation, action, etc.)
3. For existing series, I have chapter pages open in browser tabs
4. **Pain point:** I must check each tab sequentially to see if new chapters exist or remember where I left off
5. I often don't remember which chapter I stopped on or what day I last read
6. This friction causes me to abandon series or forget about them entirely

---

## User Stories & Acceptance Criteria

### Core MVP User Stories

**Story 1: View All Series**

- As a reader, I want to see a list of all series I'm tracking so that I can easily access the series I want to read
- Acceptance Criteria:
  - Display shows at least 20 series
  - Each series shows: title, current chapter, total chapters available, last read date
  - List is sorted by "last read date" (most recent first) by default
  - Mobile-optimized layout (works well on 6-inch screen)

**Story 2: Add a New Series**
- As a reader, I want to add a new series to my tracker so that I can keep track of it
- Acceptance Criteria:
  - Form includes: title, current chapter, total chapters available, link to aggregator page
  - Takes <30 seconds to complete
  - Form validation (title required, chapter numbers are numeric)
  - Success message or redirect to series detail after adding

**Story 3: Track Reading Progress**
- As a reader, I want to update my current chapter when I finish reading so that I don't forget where I left off
- Acceptance Criteria:
  - "Update Progress" button on series detail page
  - Can increment chapter number or enter manually
  - Last read date is automatically set to today
  - Confirmation message shows new chapter number

**Story 4: Know When I Last Read & How Many New Chapters Exist**
- As a reader, I want to see when I last read a series and how many new chapters are available so that I can prioritize which series to read
- Acceptance Criteria:
  - Series list shows "Last read: X days ago"
  - Series list shows "X new chapters available" (total chapters - current chapter)
  - Highlight series with new chapters (visual indicator)

**Story 5: Rate Series (Nice-to-Have for MVP)**
- As a reader, I want to rate how much I liked a series so that I can prioritize returning to ones I enjoyed
- Acceptance Criteria:
  - Add 1-5 star rating option on series detail
  - Rating displays on series list
  - Can edit rating anytime

---

## Out of Scope (Phase 2+)

- Browser extension for one-tap logging from MangaRead
- Series discovery/recommendations
- Genre, trope, and tag filtering
- Social features (comparing with friends, sharing lists)
- Import from existing trackers (MyAnimeList, etc.)
- Native mobile app
- Advanced analytics

---

## Success Metrics

- MVP deployed and accessible from iPhone browser within 6 weeks
- Can add a series in <30 seconds
- Can update progress in <15 seconds
- Personal use: Track my own reading for 4 weeks and actually use the app weekly
- GitHub: 20+ commits with clear, descriptive messages showing progression

---

## Data Model

```
Series {
  id (UUID)
  title (string, required)
  current_chapter (integer, required)
  total_chapters_available (integer, required)
  last_read_date (datetime, auto-set on progress update)
  date_added (datetime, auto-set on creation)
  rating (integer 1-5, optional)
  aggregator_url (string, optional)
  notes (text, optional - for later use)
}
```

---

## Technical Architecture

### Tech Stack
- **Backend:** Python + FastAPI (lightweight, fast, great for APIs)
- **Frontend:** React + Tailwind CSS (mobile-first, responsive)
- **Database:** PostgreSQL (local SQLite for development, Postgres for production)
- **Deployment:** Render or Railway (simple, free tier available)
- **Version Control:** GitHub with feature branches and meaningful commits

### Architecture Diagram (High-Level)

```
iPhone Browser
      ↓
[React Frontend] → REST API Calls
      ↓
[FastAPI Backend] → Database Queries
      ↓
[PostgreSQL Database]
```

### API Endpoints (MVP)

```
GET    /api/series              → Fetch all series (sorted by last_read_date)
POST   /api/series              → Create new series
GET    /api/series/{id}         → Fetch one series detail
PUT    /api/series/{id}         → Update series (progress, rating, notes)
DELETE /api/series/{id}         → Delete series (optional for MVP)
```

---

## Wireframes & Key Screens

### Screen 1: Dashboard / Series List
```
┌─────────────────────┐
│  📚 Manhwa Tracker  │
│  [+ Add Series]     │
├─────────────────────┤
│ Solo Leveling       │
│ Ch. 127 / 200       │
│ Last read: 2 days   │
│ ⭐⭐⭐⭐⭐        │
├─────────────────────┤
│ The Beginning After │
│ Ch. 45 / 75         │
│ Last read: 5 days   │
│ 🆕 5 new chapters   │
├─────────────────────┤
│ [more series...]    │
└─────────────────────┘
```

### Screen 2: Add Series Form
```
┌─────────────────────┐
│  Add New Series     │
├─────────────────────┤
│ Title               │
│ [____________]      │
│ Current Chapter     │
│ [___]               │
│ Total Chapters      │
│ [___]               │
│ Aggregator URL      │
│ [____________]      │
│ [Cancel] [Save]     │
└─────────────────────┘
```

### Screen 3: Series Detail
```
┌─────────────────────┐
│ Solo Leveling       │
├─────────────────────┤
│ Current: Ch. 127    │
│ Total: 200          │
│ Last read: Oct 15   │
│ Rating: ⭐⭐⭐⭐⭐│
│                     │
│ [← Update Progress] │
│ [Edit Series]       │
│ [View on MangaRead] │
│ [Delete]            │
└─────────────────────┘
```

---

## Development Phases

### Phase 1: Discovery & Design ✅ (This Week)

- [x] Document current workflow
- [x] Write user stories with acceptance criteria
- [x] Define data model
- [x] Create wireframes
- [x] Choose tech stack
- [ ] Set up GitHub repo and initial project board

### Phase 2: MVP Development (Weeks 3-6)

- Backend: Data models, API endpoints, database setup
- Frontend: Build screens, connect to API
- Testing: Manual end-to-end testing
- Deployment: Deploy to Render/Railway

### Phase 3: Validation (Weeks 7-8)

- Use the app for 4 weeks of real reading
- Document what works and what doesn't
- Create Phase 2 roadmap

### Phase 4: Polish & Portfolio (Ongoing)

- Code cleanup and documentation
- Write case study
- Record demo video

---

## Next Steps (End of Week 1)

1. **Create GitHub repository** and add this spec as a README
2. **Set up project board** with user stories as issues
3. **Begin Phase 2 development** next weekend:
   - Python/FastAPI tutorial (2-3 hours)
   - React tutorial or refresher (2-3 hours)
   - Set up local development environment
4. **Document GitHub workflow:** Feature branches, commit message style, PR template

---

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Scope creep (adding features too early) | MVP never ships | Stick to core 4 user stories; cut story 5 if needed |
| Tech stack unfamiliarity | Slow progress, frustration | Dedicate first 2 days of Phase 2 to tutorials only |
| Database setup complexity | Blocks development | Use SQLite in development, switch to Postgres only for deployment |
| Mobile browser responsiveness issues | App doesn't work on iPhone | Test on actual iPhone weekly; design mobile-first from start |
| Losing motivation | Project stalls | Use the app yourself; celebrate small wins; track GitHub commits |

---

## How This Demonstrates PM Skills

**To future employers, this project shows:**
- Problem definition rooted in personal pain point (relatability)
- Detailed user research (workflow documentation)
- Clear scope management (MVP vs. Phase 2)
- Acceptance criteria thinking (how to measure "done")
- Data model design (technical literacy)
- Prioritization (core stories vs. nice-to-have)
- Risk awareness (documented mitigations)
- Execution mindset (detailed next steps)