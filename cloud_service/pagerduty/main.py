from pdpyras import EventsAPISession

key = ''
cl = EventsAPISession(key)
pgd_summary='takatest'
pgd_source='API Alert from Airflow'

data = {
    "summary": pgd_summary,
    "source": pgd_source,
    "dedup_key": None,
    "severity": "warning",
}
res = cl.trigger(**data)

print(res)

