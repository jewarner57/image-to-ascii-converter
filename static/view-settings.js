$(function () {
    // change font weight
    $("#font-weight").on('input', function () {

        fontWeight = $("#font-weight").val()

        $(".ascii-display").css({ "font-weight": fontWeight })
    })

    $("#background-color").on('input', function () {

        color = $("#background-color").val()

        $(".ascii-display").css({ "background-color": color })

    })

    // change the font weight
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