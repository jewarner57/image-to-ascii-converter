let autoSetHeight = true

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
        checkAutoSetBox()
    })
})

function checkAutoSetBox() {
    if ($("#image-height").prop('disabled') === false) {
        $("#image-height").prop('disabled', true);
        $("#height-slider-container").hide()
        autoSetHeight = true
    }
    else {
        $("#image-height").prop('disabled', false);
        $("#height-slider-container").show()
        autoSetHeight = false
    }

    updateSizePreview()
}

function updateSizePreview() {

    let charactercount = $("#image-width").val()
    let linecount = $("#image-height").val()

    let dimensionDisplay = `<p class="text-center">Width: ${charactercount} Height: ${linecount}</p><hr>`

    // if the height is auto determined then make the height preview 1 tall
    if (autoSetHeight === true) {
        linecount = 1
        dimensionDisplay = `<p class="text-center">Width: ${charactercount}</p><hr>`
    }

    let displayLine = "<p>" + ("*").repeat(charactercount) + "</p>"
    let displayAll = displayLine.repeat(linecount)

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