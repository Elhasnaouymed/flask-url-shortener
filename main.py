from flask_url_shortener.methods import create_custom_new_uid


ts = set()
for f in range(200000):
    t = create_custom_new_uid(ts, 'mine', True, None)
    print(f, t)
    ts.add(t)
