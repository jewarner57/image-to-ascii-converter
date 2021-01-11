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

    // disable height input when auto determine height checked
    $("#proportionalheight").change(function () {
        if ($("#image-height").prop('disabled') === false) {
            $("#image-height").prop('disabled', true);
            $("#height-slider-container").hide()
        }
        else {
            $("#image-height").prop('disabled', false);
            $("#height-slider-container").show()
        }
    })
})

function updateSizePreview() {

    let charactercount = $("#image-width").val()
    let linecount = $("#image-height").val()

    dimensionDisplay = `<p class="text-center">Width: ${charactercount} Height: ${linecount}</p><hr>`

    displayLine = "<p>" + ("* ").repeat(charactercount) + "</p>"
    displayAll = displayLine.repeat(linecount)

    $(".dimension-display").html(dimensionDisplay)

    $(".ascii-display").html(displayAll)
}

$(document).ready(() => {
    updateSizePreview()

    // disable height form on load
    $("#image-height").prop('disabled', true);
    $("#height-slider-container").hide()
    $('#proportionalheight').prop('checked', true);
})