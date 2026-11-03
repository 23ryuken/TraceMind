-- 001_create_projects.sql
-- Records the state of the projects table as built so far.
--
-- The table itself was created in the Supabase dashboard with these columns:
--   id          uuid         primary key, default gen_random_uuid()
--   created_at  timestamptz  default now()
--   name        text         not null
--   user_id     uuid         not null, foreign key -> auth.users(id), on delete cascade
-- Row Level Security is enabled on the table.

-- Convert id from an integer identity column to a UUID.
alter table public.projects alter column id drop identity;
alter table public.projects alter column id type uuid using gen_random_uuid();
alter table public.projects alter column id set default gen_random_uuid();

-- Users can read only their own projects.
create policy "Users can read their own projects"
on public.projects
for select
to authenticated
using (auth.uid() = user_id);

-- Users can create projects only for themselves.
create policy "Users can create their own projects"
on public.projects
for insert
to authenticated
with check (auth.uid() = user_id);