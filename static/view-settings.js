$(function () {

  let backgroundColor = $("#background-color").val()
  let fontFamilyNumber = $("#font-family").val()
  let textColor = $("#setting-toggle-color").val()

  // create ascii image file and download
  $("#image-download").click(async () => {
    // Hide the download button and show loading bar
    $("#image-download-prompt").removeClass("hidden")
    $("#image-download").addClass("hidden")
    $("#download-error").text("")

    let response = ''

    try {
      response = await fetch('/createImage', {
        method: "POST",
        headers: { "Content-type": "application/json" },
        body: JSON.stringify({ imageData, backgroundColor, fontFamilyNumber, textColor }),
      })
    }
    catch (err) {
      hideLoadingBar()
      $("#download-error").text('Something went wrong and your image could not be downloaded. Try again in a few moments.')
      return
    }

    hideLoadingBar()

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

  function hideLoadingBar() {
    // Hide loading bar and show download button
    $("#image-download-prompt").addClass("hidden")
    $("#image-download").removeClass("hidden")
  }

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
    textColor = $("#setting-toggle-color").val()

    if (textColor === "Black") {
      $("#ascii-text-wrapper").addClass("ascii-display-black")
    }
    else if (textColor === "Color") {
      $("#ascii-text-wrapper").removeClass("ascii-display-black")
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

// Fullscreen preview
let isFullscreen = false
let zoomFactor = 1
$("#fullscreenButton").on('click', function () {
  if (isFullscreen) {
    // $("#ascii-text-wrapper").css({ 'transform': 'scale(' + 1 + ')' });

    $(".ascii-display").removeClass("ascii-fullscreen-display")

    $("#fullscreenButton").removeClass("fullscreenButton-fullscreen")
    $("#fullscreenButton").addClass("fullscreenButton-closed")

    $("#fullscreen-zoom").removeClass("fullscreen-zoom-open")
    $("#fullscreen-zoom").addClass("fullscreen-zoom-closed")
    isFullscreen = false
  }
  else {
    // $("#ascii-text-wrapper").css({ 'transform': 'scale(' + zoomFactor + ')' });

    $(".ascii-display").addClass("ascii-fullscreen-display")

    $("#fullscreenButton").addClass("fullscreenButton-fullscreen")
    $("#fullscreenButton").removeClass("fullscreenButton-closed")

    $("#fullscreen-zoom").removeClass("fullscreen-zoom-closed")
    $("#fullscreen-zoom").addClass("fullscreen-zoom-open")
    isFullscreen = true
  }
})

// zoom fullscreen preview
$("#fullscreen-zoom-slider").on('input', function () {

  zoomFactor = $("#fullscreen-zoom-slider").val()

  $("#ascii-text-wrapper").css({ 'transform': 'scale(' + zoomFactor + ')' });
})