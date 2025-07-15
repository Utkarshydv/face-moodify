def get_songs_by_emotion(emotion):
    LIB = {
        "happy": [
            {"title":"Happy","artist":"Pharrell Williams","cover":"https://i.ytimg.com/vi/ZbZSe6N_BXs/hqdefault.jpg","link":"https://youtu.be/ZbZSe6N_BXs"},
            {"title":"Good Vibes","artist":"Sunshine Beats","cover":"https://i.ytimg.com/vi/rC7m1iT6RPQ/hqdefault.jpg","link":"https://youtu.be/rC7m1iT6RPQ"},
            {"title":"Uptown Funk","artist":"Bruno Mars","cover":"https://i.ytimg.com/vi/OPf0YbXqDm0/hqdefault.jpg","link":"https://youtu.be/OPf0YbXqDm0"},
            {"title":"Can’t Stop the Feeling","artist":"Justin Timberlake","cover":"https://i.ytimg.com/vi/ru0K8uYEZWw/hqdefault.jpg","link":"https://youtu.be/ru0K8uYEZWw"},
            {"title":"Shake It Off","artist":"Taylor Swift","cover":"https://i.ytimg.com/vi/nfWlot6h_JM/hqdefault.jpg","link":"https://youtu.be/nfWlot6h_JM"}
        ],
        "sad": [
            {"title":"Someone Like You","artist":"Adele","cover":"https://i.ytimg.com/vi/hLQl3WQQoQ0/hqdefault.jpg","link":"https://youtu.be/hLQl3WQQoQ0"},
            {"title":"Let Her Go","artist":"Passenger","cover":"https://i.ytimg.com/vi/RBumgq5yVrA/hqdefault.jpg","link":"https://youtu.be/RBumgq5yVrA"},
            {"title":"All of Me","artist":"John Legend","cover":"https://i.ytimg.com/vi/450p7goxZqg/hqdefault.jpg","link":"https://youtu.be/450p7goxZqg"},
            {"title":"When I Was Your Man","artist":"Bruno Mars","cover":"https://i.ytimg.com/vi/ekyRHPEfYFk/hqdefault.jpg","link":"https://youtu.be/ekyRHPEfYFk"},
            {"title":"Say You Won’t Let Go","artist":"James Arthur","cover":"https://i.ytimg.com/vi/0yW7w8F2TVA/hqdefault.jpg","link":"https://youtu.be/0yW7w8F2TVA"}
        ],
        "angry": [
            {"title":"Numb","artist":"Linkin Park","cover":"https://i.ytimg.com/vi/kXYiU_JCYtU/hqdefault.jpg","link":"https://youtu.be/kXYiU_JCYtU"},
            {"title":"In the End","artist":"Linkin Park","cover":"https://i.ytimg.com/vi/eVTXPUF4Oz4/hqdefault.jpg","link":"https://youtu.be/eVTXPUF4Oz4"},
            {"title":"Break Stuff","artist":"Limp Bizkit","cover":"https://i.ytimg.com/vi/ZprXBr-01Ma/hqdefault.jpg","link":"https://youtu.be/ZprXBr-01Ma"},
            {"title":"Smells Like Teen Spirit","artist":"Nirvana","cover":"https://i.ytimg.com/vi/hTWKbfoikeg/hqdefault.jpg","link":"https://youtu.be/hTWKbfoikeg"},
            {"title":"Killing In The Name","artist":"Rage Against The Machine","cover":"https://i.ytimg.com/vi/bWXazVhlyxQ/hqdefault.jpg","link":"https://youtu.be/bWXazVhlyxQ"}
        ],
        "neutral": [
            {"title":"Lofi Chill Beats","artist":"Chillhop Music","cover":"https://i.ytimg.com/vi/jfKfPfyJRdk/hqdefault.jpg","link":"https://youtu.be/jfKfPfyJRdk"},
            {"title":"lofi hip hop radio","artist":"Lofi Girl","cover":"https://i.ytimg.com/vi/5qap5aO4i9A/hqdefault.jpg","link":"https://youtu.be/5qap5aO4i9A"},
            {"title":"relax lofi","artist":"Chill lofi","cover":"https://i.ytimg.com/vi/1eV1tKVl7rk/hqdefault.jpg","link":"https://youtu.be/1eV1tKVl7rk"},
            {"title":"Peaceful Piano","artist":"Peder B. Helland","cover":"https://i.ytimg.com/vi/Snx8AECGivM/hqdefault.jpg","link":"https://youtu.be/Snx8AECGivM"},
            {"title":"Calm Vibes","artist":"Ambient Chill","cover":"https://i.ytimg.com/vi/2OEL4P1Rz04/hqdefault.jpg","link":"https://youtu.be/2OEL4P1Rz04"}
        ]
    }
    return LIB.get(emotion, LIB["neutral"])
