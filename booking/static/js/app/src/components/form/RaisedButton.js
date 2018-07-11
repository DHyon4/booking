import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';
import classNames from 'classnames'
import Grid from '@material-ui/core/Grid';

const styles = theme => ({
  //TODO share these styles
  button: {
    margin: theme.spacing.unit,
    borderRadius: '22px',
    minWidth: '137px',
    height: '44px',
    outlineColor: 'none',
    outline: 'none',
  },
});

function RaisedButtons(props) {
  const {
    classes,
    children,
    onClick,
    type,
    className,
  } = props;

  return (
    <Button
      type={type}
      variant="contained"
      color="secondary"
      onClick={onClick}

      // for some reason outline will not go away unless its an inline style
      style={{outline: 'none'}}
      {...props}
      className={classNames(classes.button, className)}
    >

        { children }

    </Button>
  );
}

RaisedButtons.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(RaisedButtons);