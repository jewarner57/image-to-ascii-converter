$(function () {
    // change upload icon to check on upload
    $("#image-upload").change(function () {
        $("#upload-icon").html("check")
    })

    // display loading bar when submit button is pressed
    $("#submit-image").click(function () {
        $("#conversion-progress").removeClass("hidden")
    })

    // modify symbol preview size when sliders are changed
    $(".slider").change(function () {
        updateSizePreview()
    })
})

function updateSizePreview() {

    let charactercount = $("#image-width").val()
    let linecount = $("#image-height").val()

    dimensionDisplay = `<p class="text-center">Width: ${charactercount} Height: ${linecount}</p><hr>`

    displayLine = "<p>" + ("* ").repeat(charactercount) + "</p>"
    displayAll = displayLine.repeat(linecount)

    $(".ascii-display").html(dimensionDisplay + displayAll)
}

$(document).ready(() => {
    updateSizePreview()
})