$(function () {

  let backgroundColor = $("#background-color").val()
  let fontFamilyNumber = $("#font-family").val()

  // create ascii image file and download
  $("#image-download").click(async () => {
    // Hide the download button and show loading bar
    $("#image-download-prompt").removeClass("hidden")
    $("#image-download").addClass("hidden")

    const response = await fetch('/createImage', {
      method: "POST",
      headers: { "Content-type": "application/json" },
      body: JSON.stringify({ imageData, backgroundColor, fontFamilyNumber }),
    })

    // Hide loading bar and show download button
    $("#image-download-prompt").addClass("hidden")
    $("#image-download").removeClass("hidden")

    // Get the image response and create a blob
    const imageBlob = await response.blob()
    // Turn the blob into a downloadable image url
    const imageURL = URL.createObjectURL(imageBlob)

    // Create a download link
    const link = document.createElement('a')
    link.href = imageURL
    // Set the download filename to something unique
    link.download = `img-to-ascii-${Date.now() % 1000}`
    // Click the link and then remove it
    document.body.appendChild(link)
    link.click()
    document.body.removeChild(link)
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

    backgroundColor = $("#background-color").val()

    $(".ascii-display").css({ "background-color": backgroundColor })

  })

  // change the font family
  $("#font-family").change(function () {
    fontFamilyNumber = $("#font-family").val()
    font = ""

    console.log(fontFamilyNumber)

    switch (fontFamilyNumber) {
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
      case "5":
        font = "'Roboto Mono', monospace"
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