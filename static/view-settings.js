$(function () {
    // change font weight
    $("#font-weight").on('input', function () {

        fontWeight = $("#font-weight").val()

        $(".ascii-display").css({ "font-weight": fontWeight })
    })

    let textColorToggle = 0
    // change the text color
    $("#font-color-toggle").click(function () {
        toggle = $("#font-color-toggle")

        if (textColorToggle === 0) {

            toggle.addClass("setting-toggle-button-deselect")
            toggle.removeClass("setting-toggle-button-select")

            toggle.html("Black")

            // $("#text-color").removeClass("hidden")

            $(".ascii-display").addClass("ascii-display-black")

            textColorToggle = 1

        }
        else {

            toggle.removeClass("setting-toggle-button-deselect")
            toggle.addClass("setting-toggle-button-select")

            toggle.html("Color")

            //$("#text-color").addClass("hidden")

            $(".ascii-display").removeClass("ascii-display-black")

            textColorToggle = 0

        }
    })

    // change background color
    $("#background-color").on('input', function () {

        color = $("#background-color").val()

        $(".ascii-display").css({ "background-color": color })

    })

    // change the font family
    $("#font-family").change(function () {
        fontFamilyNum = $("#font-family").val()
        font = ""

        console.log(fontFamilyNum)

        switch (fontFamilyNum) {
            case "1":
                font = "'Source Code Pro', monospace"
                break;

            case "2":
                font = "'Courier New', Courier, monospace"
                break;

            case "3":
                font = "'DM Mono', monospace"
                break;

            case "4":
                font = "'Space Mono', monospace"
                break;

            default:
                font = "'Courier New', Courier, monospace"

        }

        $(".ascii-display").css({ "font-family": font })
    })
})