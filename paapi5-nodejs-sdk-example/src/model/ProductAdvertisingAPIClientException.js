/**
 * Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License").
 * You may not use this file except in compliance with the License.
 * A copy of the License is located at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * or in the "license" file accompanying this file. This file is distributed
 * on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
 * express or implied. See the License for the specific language governing
 * permissions and limitations under the License.
 */

 /**
 * ProductAdvertisingAPI
 * https://webservices.amazon.com/paapi5/documentation/index.html
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD. Register as an anonymous module.
    define(['ApiClient', 'model/ErrorData'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'), require('./ErrorData'));
  } else {
    // Browser globals (root is window)
    if (!root.ProductAdvertisingAPIv1) {
      root.ProductAdvertisingAPIv1 = {};
    }
    root.ProductAdvertisingAPIv1.ProductAdvertisingAPIClientException = factory(root.ProductAdvertisingAPIv1.ApiClient, root.ProductAdvertisingAPIv1.ErrorData);
  }
}(this, function(ApiClient, ErrorData) {
  'use strict';




  /**
   * The ProductAdvertisingAPIClientException model module.
   * @module model/ProductAdvertisingAPIClientException
   * @version 1.0.0
   */

  /**
   * Constructs a new <code>ProductAdvertisingAPIClientException</code>.
   * @alias module:model/ProductAdvertisingAPIClientException
   * @class
   */
  var exports = function() {
    var _this = this;


  };

  /**
   * Constructs a <code>ProductAdvertisingAPIClientException</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/ProductAdvertisingAPIClientException} obj Optional instance to populate.
   * @return {module:model/ProductAdvertisingAPIClientException} The populated <code>ProductAdvertisingAPIClientException</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();

      if (data.hasOwnProperty('Errors')) {
        obj['Errors'] = ApiClient.convertToType(data['Errors'], [ErrorData]);
      }
    }
    return obj;
  }

  /**
   * @member {Array.<module:model/ErrorData>} Errors
   */
  exports.prototype['Errors'] = undefined;



  return exports;
}));


