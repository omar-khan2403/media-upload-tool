import React from 'react';
import API from '../api/axios';
import Preview from './MapComponents/MapPreview';


export default class MapList extends React.Component {
    state = {
        maps: []
    }
    
    componentDidMount() {
        API.get(`/maps`)
          .then(res => {
            const maps = res.data;
            this.setState({ maps });
          })
      }

    render() {  
        return (
            <Preview previews={this.state.maps}/>
        )
    }
}
    
    
    