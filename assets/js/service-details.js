(function () {
    "use strict"; // Enforce strict mode for better coding practices

    // Wait for the DOM content to fully load
    document.addEventListener('DOMContentLoaded', function () {

        // Get all the service list links
        const serviceLinks = document.querySelectorAll('.services-list a');

        // Function to handle clicks on service links
        const handleServiceClick = function (event) {
            event.preventDefault(); // Prevent the default anchor behavior

            // Remove 'active' class from all links
            serviceLinks.forEach(function (link) {
                link.classList.remove('active');
            });

            // Add 'active' class to the clicked link
            this.classList.add('active');

            // Get the service number from the clicked link's class (e.g., 'service_two' -> 'serviceDetail-two')
            const serviceClass = this.className.split(' ')[0].replace('service-', 'serviceDetail-');

            // Hide all serviceDetail divs by explicitly selecting elements whose class includes "serviceDetail-"
            const allServiceDetails = document.querySelectorAll('[class*="serviceDetail-"]');
            allServiceDetails.forEach(function (detail) {
                detail.style.display = 'none'; // Hide all serviceDetail sections
            });

            // Show the specific serviceDetail divs for the clicked service
            const selectedServiceDetails = document.querySelectorAll(`.${serviceClass}`);
            selectedServiceDetails.forEach(function (detail) {
                detail.style.display = 'block'; // Show the selected serviceDetail sections
            });
        };

        // Add click event listeners to all service links
        serviceLinks.forEach(function (link) {
            link.addEventListener('click', handleServiceClick);
        });

        // Trigger click on the first link to make it active by default when the page loads
        serviceLinks[0].click();
    });
})();
