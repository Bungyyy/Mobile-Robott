// Auto-generated. Do not edit!

// (in-package ired_aruco.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class MPSPosition {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.number_found = null;
      this.id = null;
      this.x = null;
      this.y = null;
      this.theta = null;
    }
    else {
      if (initObj.hasOwnProperty('number_found')) {
        this.number_found = initObj.number_found
      }
      else {
        this.number_found = 0;
      }
      if (initObj.hasOwnProperty('id')) {
        this.id = initObj.id
      }
      else {
        this.id = [];
      }
      if (initObj.hasOwnProperty('x')) {
        this.x = initObj.x
      }
      else {
        this.x = [];
      }
      if (initObj.hasOwnProperty('y')) {
        this.y = initObj.y
      }
      else {
        this.y = [];
      }
      if (initObj.hasOwnProperty('theta')) {
        this.theta = initObj.theta
      }
      else {
        this.theta = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MPSPosition
    // Serialize message field [number_found]
    bufferOffset = _serializer.int16(obj.number_found, buffer, bufferOffset);
    // Serialize message field [id]
    bufferOffset = _arraySerializer.string(obj.id, buffer, bufferOffset, null);
    // Serialize message field [x]
    bufferOffset = _arraySerializer.float64(obj.x, buffer, bufferOffset, null);
    // Serialize message field [y]
    bufferOffset = _arraySerializer.float64(obj.y, buffer, bufferOffset, null);
    // Serialize message field [theta]
    bufferOffset = _arraySerializer.float64(obj.theta, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MPSPosition
    let len;
    let data = new MPSPosition(null);
    // Deserialize message field [number_found]
    data.number_found = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [id]
    data.id = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [x]
    data.x = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [y]
    data.y = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [theta]
    data.theta = _arrayDeserializer.float64(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    object.id.forEach((val) => {
      length += 4 + _getByteLength(val);
    });
    length += 8 * object.x.length;
    length += 8 * object.y.length;
    length += 8 * object.theta.length;
    return length + 18;
  }

  static datatype() {
    // Returns string type for a message object
    return 'ired_aruco/MPSPosition';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '769b8cad66706e9d423d19e4152250be';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int16 number_found
    string[] id
    float64[] x
    float64[] y
    float64[] theta
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new MPSPosition(null);
    if (msg.number_found !== undefined) {
      resolved.number_found = msg.number_found;
    }
    else {
      resolved.number_found = 0
    }

    if (msg.id !== undefined) {
      resolved.id = msg.id;
    }
    else {
      resolved.id = []
    }

    if (msg.x !== undefined) {
      resolved.x = msg.x;
    }
    else {
      resolved.x = []
    }

    if (msg.y !== undefined) {
      resolved.y = msg.y;
    }
    else {
      resolved.y = []
    }

    if (msg.theta !== undefined) {
      resolved.theta = msg.theta;
    }
    else {
      resolved.theta = []
    }

    return resolved;
    }
};

module.exports = MPSPosition;
