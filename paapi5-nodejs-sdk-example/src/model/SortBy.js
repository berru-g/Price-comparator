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
    root.ProductAdvertisingAPIv1.SortBy = factory(root.ProductAdvertisingAPIv1.ApiClient);
  }
}(this, function(ApiClient) {
  'use strict';


  /**
   * Enum class SortBy.
   * @enum {}
   * @readonly
   */
  var exports = {
    /**
     * value: "AvgCustomerReviews"
     * @const
     */
    "AvgCustomerReviews": "AvgCustomerReviews",
    /**
     * value: "Featured"
     * @const
     */
    "Featured": "Featured",
    /**
     * value: "NewestArrivals"
     * @const
     */
    "NewestArrivals": "NewestArrivals",
    /**
     * value: "Price:HighToLow"
     * @const
     */
    "Price:HighToLow": "Price:HighToLow",
    /**
     * value: "Price:LowToHigh"
     * @const
     */
    "Price:LowToHigh": "Price:LowToHigh",
    /**
     * value: "Relevance"
     * @const
     */
    "Relevance": "Relevance"  };

  /**
   * Returns a <code>SortBy</code> enum value from a Javascript object name.
   * @param {Object} data The plain JavaScript object containing the name of the enum value.
   * @return {module:model/SortBy} The enum <code>SortBy</code> value.
   */
  exports.constructFromObject = function(object) {
    return object;
  }

  return exports;
}));


