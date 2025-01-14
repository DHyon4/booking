import ActionCreators from './actionCreators';
import * as requests from '../request/requests';

// TODO: error handling

export function createArtistVideo({artistId, code, order}) {
    return (dispatch, getState) => {
        return requests.createVideo({artistId, code, order}).then(res => {
            dispatch(ActionCreators.videosCreateOrUpdate(res.data));
        });
    }
}

export function updateArtistVideo({id, artistId, code, order}) {
    return (dispatch, getState) => {
        return requests.updateVideo({artistId, videoId: id, code, order}).then(res => {
            dispatch(ActionCreators.videosCreateOrUpdate(res.data));
        })
    }
}

export function getArtistVideos({artistId}) {
    return (dispatch, getState) => {
        return requests.getVideos({artistId}).then(res => {
            dispatch(ActionCreators.videosCreateOrUpdate(res.data.results));
        });
    }
}

export function destroyArtistVideo({id, artistId}) {
    return (dispatch, getState) => {
        return requests.destroyVideo({artistId, videoId: id}).then(res => {
            dispatch(ActionCreators.videosDelete(id));
        });
    }
}
