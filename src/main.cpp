#include <iostream>
#include <string>
#include <vector>

#include "range/v3/view/filter.hpp"
#include "range/v3/view/transform.hpp"

int main()
{
    std::vector<int> const vi{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    using namespace ranges;
    auto rng = vi | views::filter([](int i) { return i % 2 == 0; }) |
               views::transform([](int i) { return std::to_string(i); });
    std::cout << rng << std::endl;
}
