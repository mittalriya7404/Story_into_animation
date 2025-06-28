document.getElementById("storyForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form submission

    // Get the story text from the textarea
    var storyText = document.getElementById("storyText").value;

    // Display the story text in a <div> (for demonstration purposes)
    document.getElementById("animation").innerText = "Story Text: " + storyText;

    // You can now process this text further for animation
});
