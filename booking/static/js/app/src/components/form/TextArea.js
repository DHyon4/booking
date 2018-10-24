import React from 'react';
// import PropTypes from 'prop-types';
import { compose } from 'redux';
import { withStyles } from '@material-ui/core/styles';
import Input from '@material-ui/core/Input';
import ReduxFromField from '../HOComponents/ReduxFormField';
import classNames from 'classnames'

const styles = theme => ({
  textArea: {
    height: '100px',
    border: `2px solid ${theme.palette.grey[200]}`,
    padding: theme.spacing.unit,
  },
  underline: {
    '&:after': {
        borderBottom: `0px`,
    },
    '&:before': {
        borderBottom: `0px`,
    },
    '&:hover:not(disabled):not(focused):not(error):before': {
        borderBottom: `0px`,
    }
  },
  input: {
    height: '100%',
  }
});

let TextArea = (props) => {
  const {
    classes,
    className,
    touched,
    error,
    warning,
    ...rest,
  } = props;

  return (
      <div>
        <Input
            multiline
            fullWidth
            {...rest}
            rows={10}
            type="textArea"
            classes={{
              underline: classes.underline,
              input: classes.input
            }}
            className={classNames(classes.textArea, className)}
        />
        <div className="error">
          {touched && (error && <span>{error}</span>)}
        </div>
      </div>
    )
  }


export default compose(
  ReduxFromField,
   withStyles(styles)
)(TextArea);
