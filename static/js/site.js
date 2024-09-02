const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        console.log(entry)
        if(entry.isIntersecting) {
            entry.target.classList.add('show');
        }
    });
});
const hiddenObjects = document.querySelectorAll('.hidden');
hiddenObjects.forEach((el) => observer.observe(el));


function scrollToSectionOne() {
    document.querySelector('#sectionOne').scrollIntoView({behavior: 'smooth'});
}

let headerBackgrounds = document.querySelectorAll(".background");

let imageIndex = 0;

function changeBackground()
{
    // remove .showing class from current bg
    headerBackgrounds[imageIndex].classList.remove("showing");

    // increment the image index by one
    imageIndex++;

    // if the image index is more than number of elements, set it to 0
    if (imageIndex >= headerBackgrounds.length)
    {
        imageIndex = 0;
    }

    // Add the .showing class to the next bg
    headerBackgrounds[imageIndex].classList.add("showing");
}

setInterval(changeBackground, 6000);

function confirmRedirect(url, region)
{
	var proceed = window.confirm("This will redirect you to the " + region + " Passtime Discord. Are you sure you want to proceed?");
	if (proceed) {
		window.location.href=url
	}
}
