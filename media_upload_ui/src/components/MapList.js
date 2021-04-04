import React from 'react';
import API from '../api/axios';
import Preview from './MapComponents/MapPreview';


export default class MapList extends React.Component {
    state = {
        maps: []
    }
    
    componentDidMount() {
        API.get(`/api/map/?skip=0&limit=100`)
          .then(res => {
            const maps = res.data;
            console.log(maps);
            this.setState({ maps });
          })
      }

    render() {  
        return (
            <Preview previews={this.state.maps}/>
        )
    }
}
    
    
    