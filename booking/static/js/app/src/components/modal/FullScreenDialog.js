import React from 'react';
import DialogBase from './DialogBase';

const FullScreenDialog = WrappedComponent => props => {
        return (
            <DialogBase
                onMount={props.onMount}
                fullWidth
                maxWidth={false}
                fullScreen
            >
                <WrappedComponent {...props}/>
            </DialogBase>
        )
    }

export default FullScreenDialog;