import { AudioCarousel, PhotoCarousel, VideoCarousel } from './components/Carousels';
import EditBioForm from './components/EditBioForm';
import ShowsEditForm from './components/ShowsEditForm';
import UserEditForm from './components/UserEditForm';
import { AudioEditForm, VideoEditForm } from './components/DraggableCodeForms';
import PhotoCountIndicator from './components/PhotoCountIndicator';
import RenderFromDomNode from './renderFromDomNode';

// console.log('ShowsEditForm', ShowsEditForm)
console.log("here")

RenderFromDomNode({
    Component: UserEditForm,
    node: 'user-edit-form',
});

RenderFromDomNode({
    Component: EditBioForm,
    node: 'edit-bio-form',
})

RenderFromDomNode({
    Component: AudioEditForm,
    node: 'audio-edit-form',
})

RenderFromDomNode({
    Component: VideoEditForm,
    node: 'video-edit-form',
})

RenderFromDomNode({
    Component: VideoCarousel,
    node: 'video-carousel',
    className: 'carousel',
});

RenderFromDomNode({
    Component: AudioCarousel,
    node: 'audio-carousel',
    className: 'carousel',
});

RenderFromDomNode({
    Component: PhotoCarousel,
    node: 'photo-carousel',
    className: 'carousel',
});

RenderFromDomNode({
    Component: PhotoCountIndicator,
    node: 'photo-count-indicator',
});

RenderFromDomNode({
    Component: ShowsEditForm,
    node: 'show-edit-modal',
});
