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
    define(['ApiClient'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'));
  } else {
    // Browser globals (root is window)
    if (!root.ProductAdvertisingAPIv1) {
      root.ProductAdvertisingAPIv1 = {};
    }
    root.ProductAdvertisingAPIv1.PriceType = factory(root.ProductAdvertisingAPIv1.ApiClient);
  }
}(this, function(ApiClient) {
  'use strict';


  /**
   * Enum class PriceType.
   * @enum {}
   * @readonly
   */
  var exports = {
    /**
     * value: "LIST_PRICE"
     * @const
     */
    "LIST_PRICE": "LIST_PRICE",
    /**
     * value: "LOWEST_PRICE"
     * @const
     */
    "LOWEST_PRICE": "LOWEST_PRICE",
    /**
     * value: "LOWEST_PRICE_STRIKETHROUGH"
     * @const
     */
    "LOWEST_PRICE_STRIKETHROUGH": "LOWEST_PRICE_STRIKETHROUGH",
    /**
     * value: "WAS_PRICE"
     * @const
     */
    "WAS_PRICE": "WAS_PRICE"  };

  /**
   * Returns a <code>PriceType</code> enum value from a Javascript object name.
   * @param {Object} data The plain JavaScript object containing the name of the enum value.
   * @return {module:model/PriceType} The enum <code>PriceType</code> value.
   */
  exports.constructFromObject = function(object) {
    return object;
  }

  return exports;
}));


