async function isbnAssist(isbn) {
    
    // Define book data colleted from API call (default values)
    let title = ''
    let pubYear = ''
    let publisher = ''
    let coverURL = ''
    let summary = ''
    let authorFirstName = ''
    let authorSurname = ''
    let authorBirthYear = ''
    let authorDeathYear = ''

    // Fetch ISBN JSON
    const url = `https://openlibrary.org/isbn/${isbn}.json`
    const response = await fetch(url);
    const isbnJSON = await response.json()
    
    // Title
    if (isbnJSON['full_title']) {
        title = isbnJSON['full_title']
    } else {title = isbnJSON['title']}
    
    // Publication year
    if (isbnJSON['publish_date']) {pubYear = isbnJSON['publish_date'].slice(-4)}
    
    //Publisher
    if (isbnJSON['publishers'][0]) {publisher = isbnJSON['publishers'][0]}

    // Cover
    if (isbnJSON['covers']) {
        let coverID = isbnJSON['covers']
        coverURL = `https://covers.openlibrary.org/b/id/${coverID}-L.jpg`
    } else {}
    
    // Summary
    if (isbnJSON['works'][0]['key']) {
        const workKey = isbnJSON['works'][0]['key']
        const workURL = `https://openlibrary.org${workKey}.json`
        const workResponse = await fetch(workURL);
        const workJSON = await workResponse.json()
        if (workJSON['description']) {summary = workJSON['description']['value']} else{}

    } else {}

    // Author
    //From ISBN JSON
    if (isbnJSON['authors'][0]['key']) {
        let authorKey = isbnJSON['authors'][0]['key']
        let authorURL = `https://openlibrary.org${authorKey}.json`
        let authorResponse = await fetch(authorURL);
        let authorJSON = await authorResponse.json()
        
        //Author birth and death years
        if (authorJSON['birth_date']) {authorBirthYear = authorJSON['birth_date'].slice(-4)} else{}
        if (authorJSON['death_date']) {authorDeathYear = authorJSON['death_date'].slice(-4)} else{}

        // Author first name and surname
        if (authorJSON['personal_name']) {
            let authorNameSplit = authorJSON['personal_name'].split(' ')
            authorFirstName = authorNameSplit[0]
            authorSurname = authorNameSplit.slice(1, authorNameSplit.length)

        } else if (authorJSON['name']) {
            let authorNameSplit = authorJSON['name'].split(' ')
            authorFirstName = authorNameSplit[0]
            authorSurname = authorNameSplit.slice(1, authorNameSplit.length)

        } else {}
    
    // from WORK JSON
    } else if (isbnJSON['works'][0]['key']) {
        const workKey = isbnJSON['works'][0]['key']
        const workURL = `https://openlibrary.org${workKey}.json`
        const workResponse = await fetch(workURL);
        const workJSON = await workResponse.json()

        if (workJSON['authors'][0]['author']['key']) {
            let authorKey = workJSON['authors'][0]['author']['key']
            let authorURL = `https://openlibrary.org${authorKey}.json`
            let authorResponse = await fetch(authorURL);
            let authorJSON = await authorResponse.json()
            
            // Author birth and death years
            if (authorJSON['birth_date']) {authorBirthYear = authorJSON['birth_date'].slice(-4)} else{}
            if (authorJSON['death_date']) {authorDeathYear = authorJSON['death_date'].slice(-4)} else{}

            //Author first name and surname
            if (authorJSON['personal_name']) {
                let authorNameSplit = authorJSON['personal_name'].split(' ')
                authorFirstName = authorNameSplit[0]
                authorSurname = authorNameSplit.slice(1, authorNameSplit.length)
    
            } else if (authorJSON['name']) {
                let authorNameSplit = authorJSON['name'].split(' ')
                authorFirstName = authorNameSplit[0]
                authorSurname = authorNameSplit.slice(1, authorNameSplit.length)
    
            } else {}
        } else {}
    } else {}

    //Wrap up values to print to DOM
    let values = [document.getElementById("id_title").value = title, 
                    document.getElementById("id_pub_year").value = pubYear, 
                    document.getElementById("id_publisher").value = publisher,
                    document.getElementById("id_isbn").value = isbn,
                    document.getElementById("id_cover_url").value = coverURL,
                    document.getElementById("id_summary").value = summary,
                    document.getElementById("id_first_name").value = authorFirstName,
                    document.getElementById("id_surname").value = authorSurname,
                    document.getElementById("id_birth_year").value = authorBirthYear,
                    document.getElementById("id_death_year").value = authorDeathYear,
                ]
    
    return values }