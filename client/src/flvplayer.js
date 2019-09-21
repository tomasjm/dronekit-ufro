import React, { Component } from 'react';
import flvjs from 'flv.js';

/**
 * react component wrap flv.js
 */
export default class Reflv extends Component {
  constructor(props) {
    super(props);
  }
  initFlv = ($video) => {
    const {url} = this.props;
    if ($video) {
      if (flvjs.isSupported()) {
        let flvPlayer = flvjs.createPlayer({
          type: "flv",
          url
        });
        flvPlayer.attachMediaElement($video);
        flvPlayer.load();
        flvPlayer.play();
        this.flvPlayer = flvPlayer;
      }
    }
  }

  componentWillUnmount() {
    if (this.flvPlayer) {
      this.flvPlayer.unload();
      this.flvPlayer.detachMediaElement();
    }
  }

  render() {
    return (
      <video
        controls={true}
        style={{width: "100%", height: "100%"}}
        ref={this.initFlv}
      />
    )
  }
}