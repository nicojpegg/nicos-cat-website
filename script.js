// button = catgenerator
// image = catmeme
// text = catmemeid

const MAX_MEMES = 1490; // Maximum number of cat memes

let crandomcat = 0;

function ImageExists(url)
{
    var http = new XMLHttpRequest();
    http.open('HEAD', url, false);
    http.send();
    return http.status!=404;
}

function generateCat() {
    const randomCat = Math.floor(Math.random() * MAX_MEMES) + 1;
    crandomcat = randomCat
    const catImageUrl = `/cats/cat${randomCat}.webp`;
    if (ImageExists(catImageUrl)) {
        const catImage = document.getElementById('catmeme');
        catImage.src = catImageUrl;
        const catText = document.getElementById('catmemeid');
        catText.textContent = `Cat ID: ${randomCat}`;
    } else {
        generateCat();
    }
}

const button = document.getElementById('catgenerator');
button.addEventListener('click', () => {
    generateCat();
});

function downloadMeme() {
    const catjpg = "/catjpg/cat" + crandomcat + ".jpeg";
    let link=document.getElementById('download');
    link.href=catjpg ;
    link.click();
}

const downloadbutton = document.getElementById('catdownload');
downloadbutton.addEventListener('click', () => {
    downloadMeme();
});