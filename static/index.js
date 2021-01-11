



$(function () {
    // enable tooltips
    $('[data-toggle="tooltip"]').tooltip()

    // change upload icon to check on upload
    $("#image-upload").change(function () {
        $("#upload-icon").html("check")
    })

    $("#submit-image").click(function () {
        $("#conversion-progress").removeClass("hidden")
    })
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