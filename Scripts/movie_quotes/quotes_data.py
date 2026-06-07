# -*- coding: utf-8 -*-
"""
250 famous movie quotes from well-rated, acclaimed films.

Each entry: (quote, movie, year, character, actor)

The first 100 are AFI's "100 Years...100 Movie Quotes" (2005), the definitive
ranked list, with the performing actor added. The remaining 150 are widely
celebrated quotes from highly rated films spanning the 1930s to the 2020s.
"""

QUOTES = [
    # ── AFI's 100 Years...100 Movie Quotes (ranked 1-100) ────────────────────
    ("Frankly, my dear, I don't give a damn.", "Gone with the Wind", 1939, "Rhett Butler", "Clark Gable"),
    ("I'm gonna make him an offer he can't refuse.", "The Godfather", 1972, "Vito Corleone", "Marlon Brando"),
    ("You don't understand! I coulda had class. I coulda been a contender. I could've been somebody, instead of a bum, which is what I am.", "On the Waterfront", 1954, "Terry Malloy", "Marlon Brando"),
    ("Toto, I've a feeling we're not in Kansas anymore.", "The Wizard of Oz", 1939, "Dorothy Gale", "Judy Garland"),
    ("Here's looking at you, kid.", "Casablanca", 1942, "Rick Blaine", "Humphrey Bogart"),
    ("Go ahead, make my day.", "Sudden Impact", 1983, "Harry Callahan", "Clint Eastwood"),
    ("All right, Mr. DeMille, I'm ready for my close-up.", "Sunset Boulevard", 1950, "Norma Desmond", "Gloria Swanson"),
    ("May the Force be with you.", "Star Wars", 1977, "Han Solo", "Harrison Ford"),
    ("Fasten your seatbelts. It's going to be a bumpy night.", "All About Eve", 1950, "Margo Channing", "Bette Davis"),
    ("You talkin' to me?", "Taxi Driver", 1976, "Travis Bickle", "Robert De Niro"),
    ("What we've got here is failure to communicate.", "Cool Hand Luke", 1967, "Captain", "Strother Martin"),
    ("I love the smell of napalm in the morning.", "Apocalypse Now", 1979, "Lt. Col. Bill Kilgore", "Robert Duvall"),
    ("Love means never having to say you're sorry.", "Love Story", 1970, "Jennifer Cavalleri", "Ali MacGraw"),
    ("The stuff that dreams are made of.", "The Maltese Falcon", 1941, "Sam Spade", "Humphrey Bogart"),
    ("E.T. phone home.", "E.T. the Extra-Terrestrial", 1982, "E.T.", "Pat Welsh (voice)"),
    ("They call me Mister Tibbs!", "In the Heat of the Night", 1967, "Virgil Tibbs", "Sidney Poitier"),
    ("Rosebud.", "Citizen Kane", 1941, "Charles Foster Kane", "Orson Welles"),
    ("Made it, Ma! Top of the world!", "White Heat", 1949, "Arthur 'Cody' Jarrett", "James Cagney"),
    ("I'm as mad as hell, and I'm not going to take this anymore!", "Network", 1976, "Howard Beale", "Peter Finch"),
    ("Louis, I think this is the beginning of a beautiful friendship.", "Casablanca", 1942, "Rick Blaine", "Humphrey Bogart"),
    ("A census taker once tried to test me. I ate his liver with some fava beans and a nice Chianti.", "The Silence of the Lambs", 1991, "Hannibal Lecter", "Anthony Hopkins"),
    ("Bond. James Bond.", "Dr. No", 1962, "James Bond", "Sean Connery"),
    ("There's no place like home.", "The Wizard of Oz", 1939, "Dorothy Gale", "Judy Garland"),
    ("I am big! It's the pictures that got small.", "Sunset Boulevard", 1950, "Norma Desmond", "Gloria Swanson"),
    ("Show me the money!", "Jerry Maguire", 1996, "Rod Tidwell", "Cuba Gooding Jr."),
    ("Why don't you come up sometime and see me?", "She Done Him Wrong", 1933, "Lady Lou", "Mae West"),
    ("I'm walkin' here! I'm walkin' here!", "Midnight Cowboy", 1969, "'Ratso' Rizzo", "Dustin Hoffman"),
    ("Play it, Sam. Play 'As Time Goes By.'", "Casablanca", 1942, "Ilsa Lund", "Ingrid Bergman"),
    ("You can't handle the truth!", "A Few Good Men", 1992, "Col. Nathan R. Jessup", "Jack Nicholson"),
    ("I want to be alone.", "Grand Hotel", 1932, "Grusinskaya", "Greta Garbo"),
    ("After all, tomorrow is another day!", "Gone with the Wind", 1939, "Scarlett O'Hara", "Vivien Leigh"),
    ("Round up the usual suspects.", "Casablanca", 1942, "Capt. Louis Renault", "Claude Rains"),
    ("I'll have what she's having.", "When Harry Met Sally...", 1989, "Customer", "Estelle Reiner"),
    ("You know how to whistle, don't you, Steve? You just put your lips together and blow.", "To Have and Have Not", 1944, "Marie 'Slim' Browning", "Lauren Bacall"),
    ("You're gonna need a bigger boat.", "Jaws", 1975, "Martin Brody", "Roy Scheider"),
    ("Badges? We ain't got no badges! We don't need no badges! I don't have to show you any stinking badges!", "The Treasure of the Sierra Madre", 1948, "Gold Hat", "Alfonso Bedoya"),
    ("I'll be back.", "The Terminator", 1984, "The Terminator", "Arnold Schwarzenegger"),
    ("Today, I consider myself the luckiest man on the face of the earth.", "The Pride of the Yankees", 1942, "Lou Gehrig", "Gary Cooper"),
    ("If you build it, he will come.", "Field of Dreams", 1989, "Shoeless Joe Jackson (voice)", "Ray Liotta"),
    ("My mama always said life was like a box of chocolates. You never know what you're gonna get.", "Forrest Gump", 1994, "Forrest Gump", "Tom Hanks"),
    ("We rob banks.", "Bonnie and Clyde", 1967, "Clyde Barrow", "Warren Beatty"),
    ("Plastics.", "The Graduate", 1967, "Mr. Maguire", "Walter Brooke"),
    ("We'll always have Paris.", "Casablanca", 1942, "Rick Blaine", "Humphrey Bogart"),
    ("I see dead people.", "The Sixth Sense", 1999, "Cole Sear", "Haley Joel Osment"),
    ("Stella! Hey, Stella!", "A Streetcar Named Desire", 1951, "Stanley Kowalski", "Marlon Brando"),
    ("Oh, Jerry, don't let's ask for the moon. We have the stars.", "Now, Voyager", 1942, "Charlotte Vale", "Bette Davis"),
    ("Shane. Shane. Come back!", "Shane", 1953, "Joey Starrett", "Brandon De Wilde"),
    ("Well, nobody's perfect.", "Some Like It Hot", 1959, "Osgood Fielding III", "Joe E. Brown"),
    ("It's alive! It's alive!", "Frankenstein", 1931, "Henry Frankenstein", "Colin Clive"),
    ("Houston, we have a problem.", "Apollo 13", 1995, "Jim Lovell", "Tom Hanks"),
    ("You've got to ask yourself one question: 'Do I feel lucky?' Well, do ya, punk?", "Dirty Harry", 1971, "Harry Callahan", "Clint Eastwood"),
    ("You had me at 'hello.'", "Jerry Maguire", 1996, "Dorothy Boyd", "Renée Zellweger"),
    ("One morning I shot an elephant in my pajamas. How he got in my pajamas, I don't know.", "Animal Crackers", 1930, "Capt. Geoffrey T. Spaulding", "Groucho Marx"),
    ("There's no crying in baseball!", "A League of Their Own", 1992, "Jimmy Dugan", "Tom Hanks"),
    ("La-dee-da, la-dee-da.", "Annie Hall", 1977, "Annie Hall", "Diane Keaton"),
    ("A boy's best friend is his mother.", "Psycho", 1960, "Norman Bates", "Anthony Perkins"),
    ("Greed, for lack of a better word, is good.", "Wall Street", 1987, "Gordon Gekko", "Michael Douglas"),
    ("Keep your friends close, but your enemies closer.", "The Godfather Part II", 1974, "Michael Corleone", "Al Pacino"),
    ("As God is my witness, I'll never be hungry again.", "Gone with the Wind", 1939, "Scarlett O'Hara", "Vivien Leigh"),
    ("Well, here's another nice mess you've gotten me into!", "Sons of the Desert", 1933, "Oliver", "Oliver Hardy"),
    ("Say 'hello' to my little friend!", "Scarface", 1983, "Tony Montana", "Al Pacino"),
    ("What a dump.", "Beyond the Forest", 1949, "Rosa Moline", "Bette Davis"),
    ("Mrs. Robinson, you're trying to seduce me. Aren't you?", "The Graduate", 1967, "Benjamin Braddock", "Dustin Hoffman"),
    ("Gentlemen, you can't fight in here! This is the War Room!", "Dr. Strangelove", 1964, "President Merkin Muffley", "Peter Sellers"),
    ("Elementary, my dear Watson.", "The Adventures of Sherlock Holmes", 1939, "Sherlock Holmes", "Basil Rathbone"),
    ("Take your stinking paws off me, you damned dirty ape.", "Planet of the Apes", 1968, "George Taylor", "Charlton Heston"),
    ("Of all the gin joints in all the towns in all the world, she walks into mine.", "Casablanca", 1942, "Rick Blaine", "Humphrey Bogart"),
    ("Here's Johnny!", "The Shining", 1980, "Jack Torrance", "Jack Nicholson"),
    ("They're here!", "Poltergeist", 1982, "Carol Anne Freeling", "Heather O'Rourke"),
    ("Is it safe?", "Marathon Man", 1976, "Dr. Christian Szell", "Laurence Olivier"),
    ("Wait a minute, wait a minute. You ain't heard nothin' yet!", "The Jazz Singer", 1927, "Jakie Rabinowitz", "Al Jolson"),
    ("No wire hangers, ever!", "Mommie Dearest", 1981, "Joan Crawford", "Faye Dunaway"),
    ("Mother of mercy, is this the end of Rico?", "Little Caesar", 1931, "Rico Bandello", "Edward G. Robinson"),
    ("Forget it, Jake, it's Chinatown.", "Chinatown", 1974, "Lawrence Walsh", "Joe Mantell"),
    ("I have always depended on the kindness of strangers.", "A Streetcar Named Desire", 1951, "Blanche DuBois", "Vivien Leigh"),
    ("Hasta la vista, baby.", "Terminator 2: Judgment Day", 1991, "The Terminator", "Arnold Schwarzenegger"),
    ("Soylent Green is people!", "Soylent Green", 1973, "Det. Robert Thorn", "Charlton Heston"),
    ("Open the pod bay doors, HAL.", "2001: A Space Odyssey", 1968, "Dave Bowman", "Keir Dullea"),
    ("Surely you can't be serious. I am serious. And don't call me Shirley.", "Airplane!", 1980, "Dr. Rumack", "Leslie Nielsen"),
    ("Yo, Adrian!", "Rocky", 1976, "Rocky Balboa", "Sylvester Stallone"),
    ("Hello, gorgeous.", "Funny Girl", 1968, "Fanny Brice", "Barbra Streisand"),
    ("Toga! Toga!", "National Lampoon's Animal House", 1978, "John 'Bluto' Blutarsky", "John Belushi"),
    ("Listen to them. Children of the night. What music they make.", "Dracula", 1931, "Count Dracula", "Bela Lugosi"),
    ("Oh, no, it wasn't the airplanes. It was Beauty killed the Beast.", "King Kong", 1933, "Carl Denham", "Robert Armstrong"),
    ("My precious.", "The Lord of the Rings: The Two Towers", 2002, "Gollum", "Andy Serkis"),
    ("Attica! Attica!", "Dog Day Afternoon", 1975, "Sonny Wortzik", "Al Pacino"),
    ("Sawyer, you're going out a youngster, but you've got to come back a star!", "42nd Street", 1933, "Julian Marsh", "Warner Baxter"),
    ("Listen to me, mister. You're my knight in shining armor.", "On Golden Pond", 1981, "Ethel Thayer", "Katharine Hepburn"),
    ("Tell 'em to go out there with all they got and win just one for the Gipper.", "Knute Rockne, All American", 1940, "George Gipp", "Ronald Reagan"),
    ("A martini. Shaken, not stirred.", "Goldfinger", 1964, "James Bond", "Sean Connery"),
    ("Who's on first.", "The Naughty Nineties", 1945, "Dexter", "Bud Abbott"),
    ("Cinderella story. Outta nowhere. A former greenskeeper, now, about to become the Masters champion.", "Caddyshack", 1980, "Carl Spackler", "Bill Murray"),
    ("Life is a banquet, and most poor suckers are starving to death!", "Auntie Mame", 1958, "Mame Dennis", "Rosalind Russell"),
    ("I feel the need—the need for speed!", "Top Gun", 1986, "Pete 'Maverick' Mitchell", "Tom Cruise"),
    ("Carpe diem. Seize the day, boys. Make your lives extraordinary.", "Dead Poets Society", 1989, "John Keating", "Robin Williams"),
    ("Snap out of it!", "Moonstruck", 1987, "Loretta Castorini", "Cher"),
    ("My mother thanks you. My father thanks you. My sister thanks you. And I thank you.", "Yankee Doodle Dandy", 1942, "George M. Cohan", "James Cagney"),
    ("Nobody puts Baby in a corner.", "Dirty Dancing", 1987, "Johnny Castle", "Patrick Swayze"),
    ("I'll get you, my pretty, and your little dog too!", "The Wizard of Oz", 1939, "Wicked Witch of the West", "Margaret Hamilton"),
    ("I'm the king of the world!", "Titanic", 1997, "Jack Dawson", "Leonardo DiCaprio"),

    # ── 150 more famous quotes from acclaimed films ──────────────────────────
    # Star Wars saga
    ("No. I am your father.", "The Empire Strikes Back", 1980, "Darth Vader", "James Earl Jones (voice)"),
    ("Do. Or do not. There is no try.", "The Empire Strikes Back", 1980, "Yoda", "Frank Oz (voice)"),
    ("These aren't the droids you're looking for.", "Star Wars", 1977, "Obi-Wan Kenobi", "Alec Guinness"),
    ("I find your lack of faith disturbing.", "Star Wars", 1977, "Darth Vader", "James Earl Jones (voice)"),
    ("I've got a bad feeling about this.", "Star Wars", 1977, "Han Solo", "Harrison Ford"),
    ("It's a trap!", "Return of the Jedi", 1983, "Admiral Ackbar", "Erik Bauersfeld (voice)"),
    ("Help me, Obi-Wan Kenobi. You're my only hope.", "Star Wars", 1977, "Princess Leia", "Carrie Fisher"),
    # Terminator
    ("Come with me if you want to live.", "The Terminator", 1984, "Kyle Reese", "Michael Biehn"),
    # The Dark Knight trilogy
    ("Why so serious?", "The Dark Knight", 2008, "The Joker", "Heath Ledger"),
    ("You either die a hero, or you live long enough to see yourself become the villain.", "The Dark Knight", 2008, "Harvey Dent", "Aaron Eckhart"),
    ("Some men just want to watch the world burn.", "The Dark Knight", 2008, "Alfred Pennyworth", "Michael Caine"),
    ("When Gotham is ashes, then you have my permission to die.", "The Dark Knight Rises", 2012, "Bane", "Tom Hardy"),
    # The Godfather extras
    ("Leave the gun. Take the cannoli.", "The Godfather", 1972, "Peter Clemenza", "Richard S. Castellano"),
    ("It's not personal, Sonny. It's strictly business.", "The Godfather", 1972, "Michael Corleone", "Al Pacino"),
    ("Just when I thought I was out, they pull me back in.", "The Godfather Part III", 1990, "Michael Corleone", "Al Pacino"),
    # Pulp Fiction
    ("Say 'what' again. I dare you, I double dare you.", "Pulp Fiction", 1994, "Jules Winnfield", "Samuel L. Jackson"),
    ("The path of the righteous man is beset on all sides by the iniquities of the selfish and the tyranny of evil men.", "Pulp Fiction", 1994, "Jules Winnfield", "Samuel L. Jackson"),
    ("They call it a Royale with Cheese.", "Pulp Fiction", 1994, "Vincent Vega", "John Travolta"),
    # The Lord of the Rings
    ("One does not simply walk into Mordor.", "The Lord of the Rings: The Fellowship of the Ring", 2001, "Boromir", "Sean Bean"),
    ("You shall not pass!", "The Lord of the Rings: The Fellowship of the Ring", 2001, "Gandalf", "Ian McKellen"),
    ("A wizard is never late, Frodo Baggins. Nor is he early. He arrives precisely when he means to.", "The Lord of the Rings: The Fellowship of the Ring", 2001, "Gandalf", "Ian McKellen"),
    # Gladiator
    ("Are you not entertained?", "Gladiator", 2000, "Maximus", "Russell Crowe"),
    ("What we do in life echoes in eternity.", "Gladiator", 2000, "Maximus", "Russell Crowe"),
    ("My name is Maximus Decimus Meridius, and I will have my vengeance, in this life or the next.", "Gladiator", 2000, "Maximus", "Russell Crowe"),
    # Braveheart
    ("They may take our lives, but they'll never take our freedom!", "Braveheart", 1995, "William Wallace", "Mel Gibson"),
    # Titanic
    ("I'll never let go, Jack. I'll never let go.", "Titanic", 1997, "Rose DeWitt Bukater", "Kate Winslet"),
    # Jurassic Park
    ("Life finds a way.", "Jurassic Park", 1993, "Dr. Ian Malcolm", "Jeff Goldblum"),
    ("Welcome to Jurassic Park.", "Jurassic Park", 1993, "John Hammond", "Richard Attenborough"),
    ("Clever girl.", "Jurassic Park", 1993, "Robert Muldoon", "Bob Peck"),
    # Back to the Future
    ("Roads? Where we're going, we don't need roads.", "Back to the Future", 1985, "Dr. Emmett Brown", "Christopher Lloyd"),
    ("Great Scott!", "Back to the Future", 1985, "Dr. Emmett Brown", "Christopher Lloyd"),
    # Raiders of the Lost Ark
    ("Snakes. Why'd it have to be snakes?", "Raiders of the Lost Ark", 1981, "Indiana Jones", "Harrison Ford"),
    ("It's not the years, honey, it's the mileage.", "Raiders of the Lost Ark", 1981, "Indiana Jones", "Harrison Ford"),
    # The Matrix
    ("You take the red pill, you stay in Wonderland, and I show you how deep the rabbit hole goes.", "The Matrix", 1999, "Morpheus", "Laurence Fishburne"),
    ("I know kung fu.", "The Matrix", 1999, "Neo", "Keanu Reeves"),
    ("Welcome to the real world.", "The Matrix", 1999, "Morpheus", "Laurence Fishburne"),
    # Blade Runner
    ("All those moments will be lost in time, like tears in rain.", "Blade Runner", 1982, "Roy Batty", "Rutger Hauer"),
    # Aliens
    ("Get away from her, you bitch!", "Aliens", 1986, "Ellen Ripley", "Sigourney Weaver"),
    # The Princess Bride
    ("Hello. My name is Inigo Montoya. You killed my father. Prepare to die.", "The Princess Bride", 1987, "Inigo Montoya", "Mandy Patinkin"),
    ("As you wish.", "The Princess Bride", 1987, "Westley", "Cary Elwes"),
    ("Inconceivable!", "The Princess Bride", 1987, "Vizzini", "Wallace Shawn"),
    # Goodfellas
    ("As far back as I can remember, I always wanted to be a gangster.", "Goodfellas", 1990, "Henry Hill", "Ray Liotta"),
    ("Funny how? I mean, funny like I'm a clown? I amuse you?", "Goodfellas", 1990, "Tommy DeVito", "Joe Pesci"),
    # There Will Be Blood
    ("I drink your milkshake!", "There Will Be Blood", 2007, "Daniel Plainview", "Daniel Day-Lewis"),
    # No Country for Old Men
    ("What's the most you ever lost on a coin toss?", "No Country for Old Men", 2007, "Anton Chigurh", "Javier Bardem"),
    # Fight Club
    ("The first rule of Fight Club is: you do not talk about Fight Club.", "Fight Club", 1999, "Tyler Durden", "Brad Pitt"),
    # The Usual Suspects
    ("The greatest trick the devil ever pulled was convincing the world he didn't exist.", "The Usual Suspects", 1995, "Roger 'Verbal' Kint", "Kevin Spacey"),
    # The Shawshank Redemption
    ("Get busy living, or get busy dying.", "The Shawshank Redemption", 1994, "Andy Dufresne", "Tim Robbins"),
    ("Hope is a good thing, maybe the best of things, and no good thing ever dies.", "The Shawshank Redemption", 1994, "Andy Dufresne", "Tim Robbins"),
    # The Green Mile
    ("I'm tired, boss.", "The Green Mile", 1999, "John Coffey", "Michael Clarke Duncan"),
    # Schindler's List
    ("Whoever saves one life, saves the world entire.", "Schindler's List", 1993, "Itzhak Stern", "Ben Kingsley"),
    # Saving Private Ryan
    ("Earn this.", "Saving Private Ryan", 1998, "Captain John Miller", "Tom Hanks"),
    # Good Will Hunting
    ("It's not your fault.", "Good Will Hunting", 1997, "Sean Maguire", "Robin Williams"),
    ("How do you like them apples?", "Good Will Hunting", 1997, "Will Hunting", "Matt Damon"),
    # Dead Poets Society
    ("O Captain! My Captain!", "Dead Poets Society", 1989, "Todd Anderson", "Ethan Hawke"),
    # The Silence of the Lambs
    ("It rubs the lotion on its skin or else it gets the hose again.", "The Silence of the Lambs", 1991, "Jame 'Buffalo Bill' Gumb", "Ted Levine"),
    # Full Metal Jacket
    ("What is your major malfunction, numbnuts?", "Full Metal Jacket", 1987, "Gunnery Sgt. Hartman", "R. Lee Ermey"),
    # The Good, the Bad and the Ugly
    ("When you have to shoot, shoot. Don't talk.", "The Good, the Bad and the Ugly", 1966, "Tuco", "Eli Wallach"),
    ("There are two kinds of people in the world, my friend: those with loaded guns and those who dig. You dig.", "The Good, the Bad and the Ugly", 1966, "Blondie", "Clint Eastwood"),
    # Unforgiven
    ("Deserve's got nothin' to do with it.", "Unforgiven", 1992, "William Munny", "Clint Eastwood"),
    # A Clockwork Orange
    ("Viddy well, little brother. Viddy well.", "A Clockwork Orange", 1971, "Alex DeLarge", "Malcolm McDowell"),
    # One Flew Over the Cuckoo's Nest
    ("But I tried, didn't I? Goddamnit, at least I did that.", "One Flew Over the Cuckoo's Nest", 1975, "R.P. McMurphy", "Jack Nicholson"),
    # The Big Lebowski
    ("The Dude abides.", "The Big Lebowski", 1998, "The Dude", "Jeff Bridges"),
    ("Yeah, well, you know, that's just, like, your opinion, man.", "The Big Lebowski", 1998, "The Dude", "Jeff Bridges"),
    # Mary Poppins
    ("Supercalifragilisticexpialidocious!", "Mary Poppins", 1964, "Mary Poppins", "Julie Andrews"),
    ("A spoonful of sugar helps the medicine go down.", "Mary Poppins", 1964, "Mary Poppins", "Julie Andrews"),
    # The Sound of Music
    ("The hills are alive with the sound of music.", "The Sound of Music", 1965, "Maria von Trapp", "Julie Andrews"),
    # Willy Wonka
    ("We are the music makers, and we are the dreamers of dreams.", "Willy Wonka & the Chocolate Factory", 1971, "Willy Wonka", "Gene Wilder"),
    ("So shines a good deed in a weary world.", "Willy Wonka & the Chocolate Factory", 1971, "Willy Wonka", "Gene Wilder"),
    # Toy Story
    ("To infinity and beyond!", "Toy Story", 1995, "Buzz Lightyear", "Tim Allen"),
    ("Reach for the sky!", "Toy Story", 1995, "Woody", "Tom Hanks"),
    # The Lion King
    ("Hakuna Matata. It means no worries for the rest of your days.", "The Lion King", 1994, "Timon", "Nathan Lane"),
    ("Remember who you are.", "The Lion King", 1994, "Mufasa", "James Earl Jones"),
    ("Long live the king.", "The Lion King", 1994, "Scar", "Jeremy Irons"),
    # Finding Nemo
    ("Just keep swimming.", "Finding Nemo", 2003, "Dory", "Ellen DeGeneres"),
    # Frozen
    ("Let it go!", "Frozen", 2013, "Elsa", "Idina Menzel"),
    # Snow White
    ("Magic mirror on the wall, who is the fairest one of all?", "Snow White and the Seven Dwarfs", 1937, "The Evil Queen", "Lucille La Verne"),
    # Harry Potter
    ("You're a wizard, Harry.", "Harry Potter and the Sorcerer's Stone", 2001, "Rubeus Hagrid", "Robbie Coltrane"),
    ("It does not do to dwell on dreams and forget to live.", "Harry Potter and the Sorcerer's Stone", 2001, "Albus Dumbledore", "Richard Harris"),
    ("It is our choices, Harry, that show what we truly are, far more than our abilities.", "Harry Potter and the Chamber of Secrets", 2002, "Albus Dumbledore", "Richard Harris"),
    ("After all this time? Always.", "Harry Potter and the Deathly Hallows – Part 2", 2011, "Severus Snape", "Alan Rickman"),
    ("Not my daughter, you bitch!", "Harry Potter and the Deathly Hallows – Part 2", 2011, "Molly Weasley", "Julie Walters"),
    # Pirates of the Caribbean
    ("But why is the rum gone?", "Pirates of the Caribbean: The Curse of the Black Pearl", 2003, "Captain Jack Sparrow", "Johnny Depp"),
    ("You will always remember this as the day you almost caught Captain Jack Sparrow.", "Pirates of the Caribbean: The Curse of the Black Pearl", 2003, "Captain Jack Sparrow", "Johnny Depp"),
    # Marvel Cinematic Universe
    ("I am Iron Man.", "Iron Man", 2008, "Tony Stark", "Robert Downey Jr."),
    ("Avengers, assemble.", "Avengers: Endgame", 2019, "Steve Rogers", "Chris Evans"),
    ("I can do this all day.", "Captain America: The First Avenger", 2011, "Steve Rogers", "Chris Evans"),
    ("Wakanda forever!", "Black Panther", 2018, "T'Challa", "Chadwick Boseman"),
    ("With great power comes great responsibility.", "Spider-Man", 2002, "Uncle Ben", "Cliff Robertson"),
    ("I love you 3000.", "Avengers: Endgame", 2019, "Morgan Stark", "Lexi Rabe"),
    # 300
    ("This is Sparta!", "300", 2006, "King Leonidas", "Gerard Butler"),
    ("Tonight, we dine in hell!", "300", 2006, "King Leonidas", "Gerard Butler"),
    # Glengarry Glen Ross
    ("Put that coffee down. Coffee's for closers only.", "Glengarry Glen Ross", 1992, "Blake", "Alec Baldwin"),
    ("A-B-C. A-Always, B-Be, C-Closing. Always be closing.", "Glengarry Glen Ross", 1992, "Blake", "Alec Baldwin"),
    # Heat
    ("Don't let yourself get attached to anything you are not willing to walk out on in thirty seconds flat.", "Heat", 1995, "Neil McCauley", "Robert De Niro"),
    # Se7en
    ("What's in the box?", "Se7en", 1995, "Detective David Mills", "Brad Pitt"),
    # Django Unchained
    ("The D is silent.", "Django Unchained", 2012, "Django", "Jamie Foxx"),
    # Inglourious Basterds
    ("That's a bingo!", "Inglourious Basterds", 2009, "Colonel Hans Landa", "Christoph Waltz"),
    # Cast Away
    ("Wilson! I'm sorry!", "Cast Away", 2000, "Chuck Noland", "Tom Hanks"),
    # Ferris Bueller's Day Off
    ("Life moves pretty fast. If you don't stop and look around once in a while, you could miss it.", "Ferris Bueller's Day Off", 1986, "Ferris Bueller", "Matthew Broderick"),
    # The Breakfast Club
    ("Sincerely yours, the Breakfast Club.", "The Breakfast Club", 1985, "Brian Johnson", "Anthony Michael Hall"),
    # Monty Python and the Holy Grail
    ("It's just a flesh wound.", "Monty Python and the Holy Grail", 1975, "The Black Knight", "John Cleese"),
    ("We are the Knights Who Say... Ni!", "Monty Python and the Holy Grail", 1975, "Head Knight of Ni", "Michael Palin"),
    # Anchorman
    ("Stay classy, San Diego.", "Anchorman: The Legend of Ron Burgundy", 2004, "Ron Burgundy", "Will Ferrell"),
    ("I love lamp.", "Anchorman: The Legend of Ron Burgundy", 2004, "Brick Tamland", "Steve Carell"),
    # A Christmas Story
    ("You'll shoot your eye out.", "A Christmas Story", 1983, "Mrs. Parker", "Melinda Dillon"),
    # It's a Wonderful Life
    ("Every time a bell rings, an angel gets his wings.", "It's a Wonderful Life", 1946, "Zuzu Bailey", "Karolyn Grimes"),
    ("No man is a failure who has friends.", "It's a Wonderful Life", 1946, "Clarence Odbody", "Henry Travers"),
    # The Sandlot
    ("You're killing me, Smalls!", "The Sandlot", 1993, "Ham Porter", "Patrick Renna"),
    # Moneyball
    ("How can you not be romantic about baseball?", "Moneyball", 2011, "Billy Beane", "Brad Pitt"),
    # The Wolf of Wall Street
    ("Sell me this pen.", "The Wolf of Wall Street", 2013, "Jordan Belfort", "Leonardo DiCaprio"),
    # Inception
    ("You mustn't be afraid to dream a little bigger, darling.", "Inception", 2010, "Eames", "Tom Hardy"),
    # Interstellar
    ("Do not go gentle into that good night.", "Interstellar", 2014, "Professor Brand", "Michael Caine"),
    ("We used to look up at the sky and wonder at our place in the stars.", "Interstellar", 2014, "Cooper", "Matthew McConaughey"),
    # V for Vendetta
    ("People should not be afraid of their governments. Governments should be afraid of their people.", "V for Vendetta", 2005, "V", "Hugo Weaving"),
    # Joker
    ("I used to think that my life was a tragedy, but now I realize, it's a comedy.", "Joker", 2019, "Arthur Fleck", "Joaquin Phoenix"),
    # Dr. Strangelove
    ("Mein Führer! I can walk!", "Dr. Strangelove", 1964, "Dr. Strangelove", "Peter Sellers"),
    # Lawrence of Arabia
    ("The trick, William Potter, is not minding that it hurts.", "Lawrence of Arabia", 1962, "T.E. Lawrence", "Peter O'Toole"),
    # Psycho
    ("We all go a little mad sometimes.", "Psycho", 1960, "Norman Bates", "Anthony Perkins"),
    # Reservoir Dogs
    ("Are you gonna bark all day, little doggy, or are you gonna bite?", "Reservoir Dogs", 1992, "Mr. Blonde", "Michael Madsen"),
    # Scarface
    ("Say hello to the bad guy!", "Scarface", 1983, "Tony Montana", "Al Pacino"),
    # Forrest Gump
    ("Run, Forrest, run!", "Forrest Gump", 1994, "Jenny Curran", "Robin Wright"),
    ("Stupid is as stupid does.", "Forrest Gump", 1994, "Forrest Gump", "Tom Hanks"),
    # The Departed
    ("I don't want to be a product of my environment. I want my environment to be a product of me.", "The Departed", 2006, "Frank Costello", "Jack Nicholson"),
    # Trainspotting
    ("Choose life. Choose a job. Choose a career. Choose a family.", "Trainspotting", 1996, "Mark Renton", "Ewan McGregor"),
    # Whiplash
    ("There are no two words in the English language more harmful than 'good job.'", "Whiplash", 2014, "Terence Fletcher", "J.K. Simmons"),
    ("Not quite my tempo.", "Whiplash", 2014, "Terence Fletcher", "J.K. Simmons"),
    # La La Land
    ("Here's to the ones who dream, foolish as they may seem.", "La La Land", 2016, "Mia", "Emma Stone"),
    # Parasite
    ("You know what kind of plan never fails? No plan at all.", "Parasite", 2019, "Ki-taek", "Song Kang-ho"),
    # The Grand Budapest Hotel
    ("There are still faint glimmers of civilization left in this barbaric slaughterhouse that was once known as humanity.", "The Grand Budapest Hotel", 2014, "M. Gustave", "Ralph Fiennes"),
    # Apocalypse Now
    ("The horror... the horror.", "Apocalypse Now", 1979, "Colonel Kurtz", "Marlon Brando"),
    # Rocky Balboa
    ("It ain't about how hard you hit. It's about how hard you can get hit and keep moving forward.", "Rocky Balboa", 2006, "Rocky Balboa", "Sylvester Stallone"),
    # Misery
    ("I'm your number one fan.", "Misery", 1990, "Annie Wilkes", "Kathy Bates"),
    # Beetlejuice
    ("It's showtime.", "Beetlejuice", 1988, "Betelgeuse", "Michael Keaton"),
    # Ghostbusters
    ("We came, we saw, we kicked its ass!", "Ghostbusters", 1984, "Dr. Peter Venkman", "Bill Murray"),
    # The Exorcist
    ("The power of Christ compels you!", "The Exorcist", 1973, "Father Merrin", "Max von Sydow"),
    # Scream
    ("What's your favorite scary movie?", "Scream", 1996, "Ghostface", "Roger L. Jackson (voice)"),
    # Wayne's World
    ("Party on, Wayne. Party on, Garth.", "Wayne's World", 1992, "Garth Algar", "Dana Carvey"),
    # Dumb and Dumber
    ("So you're telling me there's a chance.", "Dumb and Dumber", 1994, "Lloyd Christmas", "Jim Carrey"),
    # Napoleon Dynamite
    ("Vote for Pedro.", "Napoleon Dynamite", 2004, "Napoleon Dynamite", "Jon Heder"),
    # Mean Girls
    ("On Wednesdays we wear pink.", "Mean Girls", 2004, "Karen Smith", "Amanda Seyfried"),
    # Clueless
    ("Ugh, as if!", "Clueless", 1995, "Cher Horowitz", "Alicia Silverstone"),
    # Legally Blonde
    ("What, like it's hard?", "Legally Blonde", 2001, "Elle Woods", "Reese Witherspoon"),
    # The Devil Wears Prada
    ("Florals? For spring? Groundbreaking.", "The Devil Wears Prada", 2006, "Miranda Priestly", "Meryl Streep"),
    # Pretty Woman
    ("Big mistake. Big. Huge.", "Pretty Woman", 1990, "Vivian Ward", "Julia Roberts"),
    # Notting Hill
    ("I'm just a girl, standing in front of a boy, asking him to love her.", "Notting Hill", 1999, "Anna Scott", "Julia Roberts"),
    # Jerry Maguire
    ("You complete me.", "Jerry Maguire", 1996, "Jerry Maguire", "Tom Cruise"),
    # Top Gun
    ("Talk to me, Goose.", "Top Gun", 1986, "Pete 'Maverick' Mitchell", "Tom Cruise"),
    # Jaws
    ("Smile, you son of a bitch!", "Jaws", 1975, "Martin Brody", "Roy Scheider"),
    # Goldfinger
    ("No, Mr. Bond, I expect you to die!", "Goldfinger", 1964, "Auric Goldfinger", "Gert Fröbe"),
]
