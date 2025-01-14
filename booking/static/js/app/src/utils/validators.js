import _ from 'lodash';

// TODO: could def be DRYed up a bit, but fine for now.

export const validate_video_embeds = (videos) => {

  const noEmbedCodeErrorMessage = 'Please paste an embed code from Youtube.'
  const whitelist = ['youtube.com']

  var validation_results = _.map(videos, (item) => {

    if(item.code === undefined) { return {} };

    var result = validate_embed(item.code, whitelist, noEmbedCodeErrorMessage);

    if(result === true) {
      return {}
    } else {
      return {code: result}
    }

  });

  return validation_results;

}


export const validate_audio_embeds = (videos) => {

  const noEmbedCodeErrorMessage = 'Please paste an embed code from SoundCloud or Spotify.'
  const whitelist = ['soundcloud.com', 'spotify.com']

  var validation_results = _.map(videos, (item) => {

    if(item.code === undefined) { return {} };

    var result = validate_embed(item.code, whitelist, noEmbedCodeErrorMessage);

    if(result === true) {
      return {}
    } else {
      return {code: result}
    }

  });

  return validation_results;

}


export const validate_embed = (code, whitelist, noEmbedCodeErrorMessage) => {

  var parser = new DOMParser();
  var doc = parser.parseFromString(code, "text/html");
  var iframe = doc.body.childNodes[0]

  if (!iframe) {
    return noEmbedCodeErrorMessage;
  }

  // Make sure code is an iframe.
  //  Will need to change if we encounter a valid embed
  //  code that's not an iframe
  if( iframe.tagName !== 'IFRAME' ) {
    return noEmbedCodeErrorMessage;
  }

  // Very basically, iframe needs to have a src
  if( !iframe.hasAttribute('src') ) {
    return noEmbedCodeErrorMessage;
  }

  // Check the src against our whitelist
  const src = new URL(iframe.src);
  const src_results = _.map(whitelist, (host) =>{
    return (src.toString().indexOf(host) !== -1);
  });
  const has_valid_src = src_results.some((element, index, array) => {
    return element === true;
  })

  if( has_valid_src ) {
    return true;
  } else {
    return noEmbedCodeErrorMessage
  }

}

export const required = (val) => {
  return val ? undefined : 'This field is required.';
}

export const requiredArray = (arrayVal) => {
  return _.get(arrayVal, 'length', 0) ? undefined : 'This field is required.';
}

// TODO: Probably want a different validation function for each social
// URL, to validate e.g. `https://facebook.com/[username]` specifically
export const validateURL = (val) => {
  if(!val) return undefined;
  // Regex credit: https://www.regextester.com/94502 (modified to require protocol)
  const URL_REGEX = /^(http(s)?:\/\/)[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:\/?#[\]@!\$&'\(\)\*\+,;=.]+$/;
  return URL_REGEX.test(val) ? undefined : 'A valid URL starting with http or https is required.';
}

export const validateEmail = (val) => {
  if(!val) return undefined;
  // Regex credit: https://www.regular-expressions.info/email.html
  const EMAIL_REGEX = new RegExp('^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$', 'i');
  return EMAIL_REGEX.test(val) ? undefined : 'This email address is not valid.';
}

export const validateMaxLength = (maxLength) => (val) => {
  if(!val) return undefined;
  return val.length <= maxLength ? undefined : `This value should not exceed ${maxLength} characters.`;
}
