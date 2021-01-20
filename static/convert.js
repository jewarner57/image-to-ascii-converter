let autoSetHeight = true

$(function () {

    var uploadField = document.getElementById("image-upload");
    uploadField.onchange = function() {
        if(this.files[0].size > 10485760){
            alert("Your image must be smaller than 10 megabytes. Please use a smaller image.");
            this.value = "";
        };
    };

    // change upload icon to check on upload
    $("#image-upload").on('input', function () {
        $("#upload-icon").html("check")
    })

    // display loading bar when submit button is pressed
    $("#submit-image").click(function () {
        $("#conversion-progress").removeClass("hidden")
    })

    // modify symbol preview size when sliders are changed
    $(".slider").on('input', function () {
        updateSizePreview()
    })

    // disable height input when auto determine height checked
    $("#proportionalheight").on('input', function () {
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

    let dimensionDisplay = `<p class="text-center">Width: ${charactercount} Height: ${linecount}</p>`

    // if the height is auto determined then make the height preview 1 tall
    if (autoSetHeight === true) {
        linecount = 1
        dimensionDisplay = `<p class="text-center">Width: ${charactercount}</p>`
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

// convert.html
togglebutton = document.getElementById("charkey-toggle")
settingInput1 = document.getElementById("charkeydropdown")
settingInput2 = document.getElementById("charkeycustom")

createSettingToggle(togglebutton, settingInput1, settingInput2)

function createSettingToggle(button, input1, input2) {
    let toggleMode = 0

    button.addEventListener("click", function () {
        settingInput1 = input1
        settingInput2 = input2

        if (toggleMode === 0) {

            togglebutton.innerHTML = "Custom"

            togglebutton.classList.add("setting-toggle-button-deselect")
            togglebutton.classList.remove("setting-toggle-button-select")

            settingInput1.classList.add("hidden")
            settingInput1.setAttribute("name", "-");

            settingInput2.classList.remove("hidden")
            settingInput2.setAttribute("name", "charkey");

            toggleMode = 1
        }
        else {

            togglebutton.innerHTML = "Default"

            togglebutton.classList.add("setting-toggle-button-select")
            togglebutton.classList.remove("setting-toggle-button-deselect")

            settingInput2.classList.add("hidden")
            settingInput2.setAttribute("name", "-");

            settingInput1.classList.remove("hidden")
            settingInput1.setAttribute("name", "charkey");

            toggleMode = 0
        }


    })
}