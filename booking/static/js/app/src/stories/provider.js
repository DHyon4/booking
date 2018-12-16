import React from 'react';
import { Provider as ReduxProvider } from 'react-redux';

import { combineReducers } from 'redux';
import { reducer as form } from 'redux-form';
import { createStore } from 'redux';

import { MuiThemeProvider, createMuiTheme } from '@material-ui/core/styles';

// import theme from '../theme';

const storybookTheme = createMuiTheme({
  typography: {
      useNextVariants: true,
      htmlFontSize: 16,
      fontSize: 16,
      body1: {
        fontFamily: "'GT Zirkon','Gill Sans', GillSans, serif",
        fontWeight: 300,
        fontSize: "1rem",
        lineHeight: 1.4285,
        letterSpacing: "0em",
        textRendering: "optimizeLegibility",
        webkitFontSmoothing: "subpixel-antialiased",
      },
      body2: {
        fontFamily: "'GT Zirkon','Gill Sans', GillSans, serif",
        fontWeight: 300,
        fontSize: "0.875rem",
        lineHeight: 1.375,
        letterSpacing: "0",
        textRendering: "optimizeLegibility",
        webkitFontSmoothing: "subpixel-antialiased",
      },
      subtitle1: {
        fontFamily: "'Modern Era','Roboto', 'Helvetica', 'Arial', sans-serif",
        fontWeight: 400,
        fontSize: "1rem",
        lineHeight: 1.375,
        letterSpacing: "0em",
        textRendering: "optimizeLegibility",
        webkitFontSmoothing: "subpixel-antialiased",
      },
      subtitle2: {
        fontFamily: "'Modern Era','Roboto', 'Helvetica', 'Arial', sans-serif",
        fontWeight: 300,
        fontSize: "0.875rem",
        lineHeight: 1.4285,
        letterSpacing: "0",
        textRendering: "optimizeLegibility",
        webkitFontSmoothing: "subpixel-antialiased",
      },
      overline: {
        fontFamily: "'GT Zirkon','Gill Sans', GillSans, serif",
        fontWeight: 500,
        fontSize: "0.75rem",
        lineHeight: 1.66,
        letterSpacing: "0.06em",
        textTransform: "uppercase",
      },
      caption: {
        fontFamily: "'GT Zirkon','Gill Sans', GillSans, serif",
        fontWeight: 400,
        fontSize: "0.75rem",
        lineHeight: 1.66,
        letterSpacing: "0.0133em",
        textTransform: "none",
      },
      h6: {
        fontFamily: "'Modern Era','Roboto', 'Helvetica', 'Arial', sans-serif",
        fontWeight: 500,
        fontSize: "1.25rem",
        lineHeight: 1.25,
        letterSpacing: "0.0075em",
      },
      h5: {
        fontFamily: "'Modern Era','Roboto', 'Helvetica', 'Arial', sans-serif",
        fontWeight: 500,
        fontSize: "1.5rem",
        lineHeight: 1.33,
        letterSpacing: "0em",
      },
      h4: {
        fontFamily: "'Modern Era','Roboto', 'Helvetica', 'Arial', sans-serif",
        fontWeight: 400,
        fontSize: "2rem",
        lineHeight: 1.25,
        letterSpacing: "0.00735em",
      },
      h3: {
        fontFamily: "'Modern Era','Roboto', 'Helvetica', 'Arial', sans-serif",
        fontWeight: 600,
        fontSize: "2.25rem",
        lineHeight: 1.222,
        letterSpacing: "0em",
      },
      h2: {
        fontFamily: "'Modern Era','Roboto', 'Helvetica', 'Arial', sans-serif",
        fontWeight: 600,
        fontSize: "3rem",
        lineHeight: 1.229,
        letterSpacing: "-0.00833em",
      },
      h1: {
        fontFamily: "'Modern Era','Roboto', 'Helvetica', 'Arial', sans-serif",
        fontWeight: 600,
        fontSize: "4rem",
        lineHeight: 1.21875,
        letterSpacing: "-0.01562em",
      },
      button: {
        fontFamily: "'Modern Era','Roboto', 'Helvetica', 'Arial', sans-serif",
        fontWeight: 600,
        fontSize: "1rem",
        lineHeight: 1.18,
        letterSpacing: "0",
        textTransform: "none",
      },
  },
  palette: {
      primary: {
          main:"#2B4BD1",
          light:"#7280E3",
          dark:"#0025B2",
          contrastText: "#FFFFFF",
      },
      secondary: {
          main:"#2BD1B3",
          light:"#AEEBDE",
          dark:"#00B890",
          contrastText: "rgba(0,0,0,0.87)",
      },
      grey: {
          50:"#F5F9FA", // can be used in place of background.paper for a light grey bg.
          100:"#E9F2F5",
          200:"#DDEAED",
          300:"#CEDDE0",
          400:"#A2B7BD",
          500:"#83989E",
          600:"#607175",
          700:"#4D5C61",
          800:"#333F42",
          900:"#031B21",
          A100:"#C7D3D6",
          A200:"#96A6AB",
          A400:"#152A30",
          A700:"#4D5C61"
      },
      background: {
          paper: "#FFFFFF"
      },
  },
});

const initialState = {};

const store = createStore(
  combineReducers({
    form
  }),
  initialState
);

const Provider = ({ story }) => (
  <MuiThemeProvider theme={storybookTheme}>
    <ReduxProvider store={store}>
      {story}
    </ReduxProvider>
  </MuiThemeProvider>
);

export {
  Provider
}