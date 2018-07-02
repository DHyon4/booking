import React from 'react';
import Dialog from '@material-ui/core/Dialog';
import autoBind from 'auto-bind';

class DialogBase extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      open: true,
    }

    autoBind(this)
  };

  open() {
    this.setState({ open: true });
  };

  close() {
    this.setState({ open: false });
  };

  render() {
    const {
      children,
      classes,
      fullScreen,
      fullWidth,
      maxWidth
    } = this.props;

    const childrenWithProps = React.Children.map(children, child =>
      React.cloneElement(child, { openDialog: this.open, closeDialog: this.close }));

    return (
        <Dialog
          fullScreen={fullScreen}
          fullWidth={fullWidth}
          maxWidth={maxWidth}
          classes={classes}
          open={this.state.open}
          onClose={this.handleClose}
          aria-labelledby="alert-dialog-title"
          aria-describedby="alert-dialog-description"
        >
            {childrenWithProps}
        </Dialog>
    );
  }
}

DialogBase.defaultProps = {
  fullScreen: false
}

export default DialogBase;
