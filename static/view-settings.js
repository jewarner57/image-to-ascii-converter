$(function () {

  // download ascii characters as image
  $("#image-download").click(function () {
    $("#image-download-prompt").removeClass("hidden")

    // Turn the ascii div into a canvas
    html2canvas(document.querySelector(".ascii-display")).then(canvas => {
      // Convert the canvas to an image and download it
      download(canvas, "converted-image.png")
    });


    //$("#image-download-prompt").addClass("hidden")
  })

  // copy element's inner text to clipboard
  $('#clipboard-copy').click(function () {
    elm = document.querySelector(".ascii-display")

    let selection = window.getSelection();
    let range = document.createRange();
    range.selectNodeContents(elm);
    selection.removeAllRanges();
    selection.addRange(range);
    document.execCommand("Copy");

    $('#clipboard-copy').html("Copied!")

    window.setTimeout(function () {
      $("#clipboard-copy").html("<i class='material-icons mr-2' id = 'upload-icon' > content_copy </i> Copy Text To Clipboard");
    }, 3000);
  })

  // change font weight
  $("#font-weight").on('input', function () {

    fontWeight = $("#font-weight").val()

    $(".ascii-display").css({ "font-weight": fontWeight })
  })

  // change the text color
  $("#setting-toggle-color").on('input', function () {
    select = $("#setting-toggle-color")

    if (select.val() === "Black") {
      $(".ascii-display").addClass("ascii-display-black")
    }
    else if (select.val() === "Color") {
      $(".ascii-display").removeClass("ascii-display-black")
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

/* Canvas Donwload */
/* Convert a canvas into an image and download it */
/* By Jose Quintana - https://codepen.io/joseluisq/pen/mnkLu */
function download(canvas, filename) {
  // create an "off-screen" anchor tag
  var lnk = document.createElement('a'), e;

  // the key here is to set the download attribute of the a tag
  lnk.download = filename;

  // convert canvas content to data-uri for link. When download
  // attribute is set the content pointed to by link will be
  // pushed as "download" in HTML5 capable browsers
  lnk.href = canvas.toDataURL("image/png;base64");

  // create a "fake" click-event to trigger the download
  if (document.createEvent) {
    e = document.createEvent("MouseEvents");
    e.initMouseEvent("click", true, true, window,
      0, 0, 0, 0, 0, false, false, false,
      false, 0, null);

    lnk.dispatchEvent(e);
  } else if (lnk.fireEvent) {
    lnk.fireEvent("onclick");
  }
}